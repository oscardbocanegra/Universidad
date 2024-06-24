import { auth, db, storage } from './firebase-config.js';
import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged } from 'https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js';
import { doc, setDoc, getDocs, collection, query, where, deleteDoc, updateDoc, getDoc } from 'https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js';
import { ref, uploadBytes, getDownloadURL } from 'https://www.gstatic.com/firebasejs/9.6.1/firebase-storage.js';

document.addEventListener('DOMContentLoaded', () => {
    // Form switching
    document.getElementById('show-login').addEventListener('click', showLoginForm);
    document.getElementById('show-register').addEventListener('click', showRegisterForm);

    // Menu navigation
    document.getElementById('all-posts').addEventListener('click', showAllPosts);
    document.getElementById('my-posts').addEventListener('click', showMyPosts);
    document.getElementById('create-post').addEventListener('click', showCreatePost);
    document.getElementById('contact-us').addEventListener('click', showContactUs);

    // Authentication
    document.getElementById('register-btn').addEventListener('click', registerUser);
    document.getElementById('login-btn').addEventListener('click', loginUser);
    document.getElementById('header-login-btn').addEventListener('click', showLoginForm);
    document.getElementById('logout-btn').addEventListener('click', logoutUser);

    // Post creation
    document.getElementById('post-form').addEventListener('submit', createPost);

    // Contact form
    document.getElementById('contact-form').addEventListener('submit', submitContactForm);

    // Check auth state
    onAuthStateChanged(auth, (user) => {
        if (user) {
            document.getElementById('auth').style.display = 'none';
            document.getElementById('logout-btn').style.display = 'block';
            document.querySelector('.user-container img').src = user.photoURL || 'assets/avatar.png';
            document.querySelector('.user-container').style.display = 'flex';
            document.getElementById('login-btn').style.display = 'none';
            fetchAllPosts();
        } else {
            document.getElementById('auth').style.display = 'block';
            document.getElementById('logout-btn').style.display = 'none';
            document.querySelector('.user-container').style.display = 'none';
            document.getElementById('login-btn').style.display = 'block';
        }
    });
});

const showLoginForm = () => {
    document.getElementById('register-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
    hideAllSections();
};

const showRegisterForm = () => {
    document.getElementById('register-form').style.display = 'block';
    document.getElementById('login-form').style.display = 'none';
    hideAllSections();
};

const showAllPosts = () => {
    hideAllSections();
    document.getElementById('posts-section').style.display = 'block';
};

const showMyPosts = async () => {
    hideAllSections();
    document.getElementById('my-posts-section').style.display = 'block';
    await fetchUserPosts();
};

const showCreatePost = () => {
    hideAllSections();
    document.getElementById('create-post-section').style.display = 'block';
};

const showContactUs = () => {
    hideAllSections();
    document.getElementById('contact-section').style.display = 'block';
    document.getElementById('auth').style.display = 'none';
};

const hideAllSections = () => {
    document.getElementById('posts-section').style.display = 'none';
    document.getElementById('my-posts-section').style.display = 'none';
    document.getElementById('create-post-section').style.display = 'none';
    document.getElementById('contact-section').style.display = 'none';
};

const showNotification = (message, isError = false) => {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = 'notification';
    if (isError) {
        notification.classList.add('error');
    }
    notification.style.display = 'block';
    setTimeout(() => {
        notification.style.display = 'none';
    }, 3000);
};

const registerUser = async () => {
    const firstName = document.getElementById('first-name').value;
    const lastName = document.getElementById('last-name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
    const phone = document.getElementById('phone').value;

    if (password !== confirmPassword) {
        showNotification('Passwords do not match', true);
        return;
    }

    try {
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;

        await setDoc(doc(db, 'users', user.uid), {
            firstName,
            lastName,
            email,
            phone
        });

        showNotification('User registered successfully');
        showLoginForm();
    } catch (error) {
        showNotification('Error registering user: ' + error.message, true);
    }
};

const loginUser = async () => {
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    if (!validateEmail(email)) {
        showNotification('Please enter a valid email address.', true);
        return;
    }

    try {
        await signInWithEmailAndPassword(auth, email, password);
        showNotification('User logged in successfully');
        document.getElementById('auth').style.display = 'none';
        document.getElementById('logout-btn').style.display = 'block';
        document.getElementById('login-btn').style.display = 'none';
    } catch (error) {
        showNotification('Error logging in user: ' + error.message, true);
    }
};

const logoutUser = async () => {
    try {
        await signOut(auth);
        showNotification('User logged out successfully');
        document.getElementById('auth').style.display = 'block';
        document.getElementById('logout-btn').style.display = 'none';
        document.getElementById('login-btn').style.display = 'block';
    } catch (error) {
        showNotification('Error logging out user: ' + error.message, true);
    }
};

const validateEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
};

const createPost = async (event) => {
    event.preventDefault();

    const title = document.getElementById('post-title').value;
    const description = document.getElementById('post-description').value;
    const videoUrl = document.getElementById('post-video-url').value;
    const imageFile = document.getElementById('post-image').files[0];

    if (!imageFile) {
        showNotification('Please select an image file.', true);
        return;
    }

    try {
        // Upload image to Firebase Storage
        const imageRef = ref(storage, `posts/${imageFile.name}`);
        await uploadBytes(imageRef, imageFile);
        const imageUrl = await getDownloadURL(imageRef);

        // Add post to Firestore
        const user = auth.currentUser;
        await setDoc(doc(db, 'posts', title), {
            title,
            description,
            videoUrl,
            imageUrl,
            userId: user.uid,
            createdAt: new Date()
        });

        showNotification('Post created successfully');
        showAllPosts();
    } catch (error) {
        showNotification('Error creating post: ' + error.message, true);
    }
};

const fetchAllPosts = async () => {
    const allPostsContainer = document.getElementById('all-posts-container');
    allPostsContainer.innerHTML = '';

    const querySnapshot = await getDocs(collection(db, 'posts'));
    querySnapshot.forEach((doc) => {
        const post = doc.data();
        allPostsContainer.innerHTML += `
            <div class="post">
                <h3>${post.title}</h3>
                <p>${post.description}</p>
                <img src="${post.imageUrl}" alt="${post.title}">
                <a href="${post.videoUrl}" target="_blank">Ver video</a>
            </div>
        `;
    });
};

const fetchUserPosts = async () => {
    const userPostsContainer = document.getElementById('my-posts-container');
    userPostsContainer.innerHTML = '';

    const user = auth.currentUser;
    console.log('Fetching posts for user:', user.uid);  // Debugging
    const q = query(collection(db, 'posts'), where('userId', '==', user.uid));
    const querySnapshot = await getDocs(q);
    console.log('Number of posts:', querySnapshot.size);  // Debugging
    querySnapshot.forEach((doc) => {
        const post = doc.data();
        userPostsContainer.innerHTML += `
            <div class="post">
                <h3>${post.title}</h3>
                <p>${post.description}</p>
                <img src="${post.imageUrl}" alt="${post.title}">
                <a href="${post.videoUrl}" target="_blank">Ver video</a>
                <div class="actions">
                    <button onclick="editPost('${doc.id}')">Edit</button>
                    <button class="delete" onclick="deletePost('${doc.id}')">Delete</button>
                </div>
            </div>
        `;
    });
};

// Asegurarse de definir las funciones globalmente
window.deletePost = async (postId) => {
    try {
        await deleteDoc(doc(db, 'posts', postId));
        showNotification('Post deleted successfully');
        fetchUserPosts();
    } catch (error) {
        showNotification('Error deleting post: ' + error.message, true);
    }
};

window.editPost = async (postId) => {
    // Obtener datos del post para editar
    const postRef = doc(db, 'posts', postId);
    const postSnap = await getDoc(postRef);

    if (postSnap.exists()) {
        const post = postSnap.data();
        // Rellenar el formulario con los datos del post para editarlos
        document.getElementById('post-title').value = post.title;
        document.getElementById('post-description').value = post.description;
        document.getElementById('post-video-url').value = post.videoUrl;

        // Mostrar formulario de edición
        showCreatePost();

        // Añadir event listener para actualizar el post
        document.getElementById('post-form').removeEventListener('submit', createPost);
        document.getElementById('post-form').addEventListener('submit', async (event) => {
            event.preventDefault();

            const title = document.getElementById('post-title').value;
            const description = document.getElementById('post-description').value;
            const videoUrl = document.getElementById('post-video-url').value;
            const imageFile = document.getElementById('post-image').files[0];

            let imageUrl = post.imageUrl;
            if (imageFile) {
                // Upload new image to Firebase Storage
                const imageRef = ref(storage, `posts/${imageFile.name}`);
                await uploadBytes(imageRef, imageFile);
                imageUrl = await getDownloadURL(imageRef);
            }

            try {
                // Update post in Firestore
                await updateDoc(postRef, {
                    title,
                    description,
                    videoUrl,
                    imageUrl,
                    updatedAt: new Date()
                });

                showNotification('Post updated successfully');
                showAllPosts();
            } catch (error) {
                showNotification('Error updating post: ' + error.message, true);
            }
        });
    } else {
        showNotification('No such post!', true);
    }
};

const submitContactForm = async (event) => {
    event.preventDefault();

    const name = document.getElementById('contact-name').value;
    const email = document.getElementById('contact-email').value;
    const subject = document.getElementById('contact-subject').value;
    const message = document.getElementById('contact-message').value;

    try {
        await setDoc(doc(collection(db, 'contacts')), {
            name,
            email,
            subject,
            message,
            createdAt: new Date()
        });

        showNotification('Message sent successfully');
        document.getElementById('contact-form').reset();
    } catch (error) {
        showNotification('Error sending message: ' + error.message, true);
    }
};
