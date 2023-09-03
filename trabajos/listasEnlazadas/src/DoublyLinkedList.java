public class DoublyLinkedList<T> {
    public static void main(String[] args) {

        /*Insertar elementos a una lista*/
        System.out.println("¿Que actividaes vas a realizar el dia de hoy?");
        String ingreso = "Sacar a pasear a los perros,";
        insert(ingreso);

        String ingreso2 = "Estudiar programacion,";
        insert(ingreso2);

        String ingreso3 = "Estudiar ingles,";
        insert(ingreso3);

        String ingreso4 = "Hacer ejercicio";
        insert(ingreso4);
        System.out.println("------------------------------------------------------------------");


        /*Imprimir los elementos que contiene una lista*/
        System.out.println("Imprimir los elementos que contiene una lista");
        print();
        System.out.println("------------------------------------------------------------------");

        /*Contar el número de elementos que tiene la lista.*/
        int tam = sizeList();
        System.out.println("Tamaño lista es de " + tam + "elementos");
        System.out.println("------------------------------------------------------------------");

        /*Mostrar el elemento que hay en una posición concreta de la lista*/
        System.out.println("Mostramos el elemento especifico de la lista en la posicion 3");
        System.out.println(get(3));
        System.out.println("------------------------------------------------------------------");

        /* Sacar un elemento concreto de la lista.*/
        System.out.println("Sacamos un elemento concreto de la lista que en este caso es 2 ");
        removeAt(2);
        print();
        System.out.println("------------------------------------------------------------------");
        //Sacar el elemento que ocupa una posición en la lista.
        System.out.println("Sacar el elemento que ocupa una posición en la lista que en este caso va a ser estudiar ingles");
        remove("Estudiar ingles");
        print();
        System.out.println("------------------------------------------------------------------");

        //Reemplazar un elemento de la lista
        System.out.println("Vamos a reemplazar la actidad en la posicion 1 por Leer in libro");
        replace(1, "Leer un libro");
        print();
        System.out.println("------------------------------------------------------------------");
        System.out.println();
        System.out.println("Vamos a comprobar si leer un libro se encuentra en la lista");
        //Comprobar si un elemento está en la lista
        contains("Leer un libro");
        System.out.println("------------------------------------------------------------------");
        System.out.println();


        System.out.println("Vamos a agregar otra actividad en la lista ");
        DoublyLinkedList<String> otherList = new DoublyLinkedList<>();
        otherList.otherlist2(", descansar");
        concatenate(otherList);
        print();

    }

    private static Node head;
    private static Node tail;
    private static int size;
    private static Node head2;
    private static Node tail2;
    private static int size2;



    private static class Node {
        private String data;
        private Node prev;
        private Node next;

        public Node(String data) {
            this.data = data;
            this.prev = null;
            this.next = null;
        }
    }
    //En esta funcion lo que vamos a hacer es definir el tamaño de la lista para
    //luego invocarlo en el main y que esta nos imprima de cuento es este tamaño
    public static int sizeList() {
        return size;
    }

    //En esta funcion lo que vamos a hacer es mostrar un elemento especifico de la lista
    public static String get(int index)     {
        //En el siguiente if lo que vamos a hacer es manejar un error por lo cual si
        //introducimos un numero menor a 0 o mayor al tamaño de la lista vamos a imprimir
        // que este numero esta fuera de nuestro rango
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of range");
        }
        //En las siguientes lineas de codigo lo que vamos a hacer es recorrer la lista
        //hasta encontrar el numero que le indicamos en el parametro para de esta manera
        //el nos va a retornar el elemento que se encuentra en el index
        Node current = head;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }

        return current.data;
    }

    //La siguiente funcion lo que va a hacer es evaluar si el elemento que nosotros le indicamos se
    // encuentra dentro de la lista o no
    public static boolean contains(String data) {
        //En las siguientes lineas de codigo vamos a recorrer la lista y mirar si el elemento
        //que le pasamos por parametro en el main se encuentra en la lista o no y para informar
        //esto devolvemos como resultado un true o un false
        Node current = head;
        while (current != null) {
            if (current.data.equals(data)) {
                System.out.println(true);
                return true;
            }
            current = current.next;
        }
        System.out.println(false);
        return false;
    }

    //En las siguientes lìneas de codigo en la funcion print lo que vamos a hacer es imprimir
    //los elementos de la lista siempre y cuando esta no este vacia
    public static void print() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    //En la siguiente funcion lo que vamos a hacer es insertar un nuevo elemento de
    //tipo String a la lista y al mismo tiempo vamos a dejar preparadoes el siguiente nodo y el nodo anterior
    static void insert(String data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        size++;
    }

    public void otherlist2(String data) {
        Node newNode2 = new Node(data);

        if (head2 == null) {
            head2 = newNode2;
            tail2 = newNode2;
        } else {
            tail2.next = newNode2;
            newNode2.prev = tail2;
            tail2 = newNode2;
        }
        size2++;
    }


    //En la siguiente funcion lo que vamos a hacer es eliminar un elemento de la lista el cual vamos
    //a indicar este elemento de forma String
    public static void remove(String data) {
        //Lo que vamos a hacer dentro de la funcion es tomar el String que se recibe por parametro
        //y empezar a buscarlo en los nodos que tenemos en nuestra lista por esta manera tenemos
        //que evaluar el nodo anterior y el nodo siguiente
        Node current = head;
        while (current != null) {
            if (current.data.equals(data)) {
                if (current.prev == null) {
                    head = current.next;
                    if (head != null) {
                        head.prev = null;
                    }
                } else if (current.next == null) {
                    tail = current.prev;
                    tail.next = null;
                } else {
                    current.prev.next = current.next;
                    current.next.prev = current.prev;
                }

                size--;
                return;
            }
            current = current.next;
        }
    }

    //Esta funcion es parecida a la anterior con la unica variacion que el elemento que vamos a eliminar
    //se va a hacer por medio de la posicion en la que se encuentra el elemeto a eliminar por esta razon
    //se recibe como parametro in entero
    public static void removeAt(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of range");
        }
        // En las siguientes lineas de codigo lo que vamos a hacer es tomar el numero que recibimos por
        // parametro y buscamos el elemento que tenemos en esa posicion para luego de esta manera poderlo eliminar
        Node current = head;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }

        if (current.prev == null) {
            head = current.next;
            if (head != null) {
                head.prev = null;
            }
        } else if (current.next == null) {
            tail = current.prev;
            tail.next = null;
        } else {
            current.prev.next = current.next;
            current.next.prev = current.prev;
        }

        size--;
    }

    //En la funcion concatenate lo que vamos a hacer es agregar otra lista con otros valores a la cadena inicial
    public static void concatenate(DoublyLinkedList<String> otherList) {
        if (otherList.head2 == null) {
            return;
        }

        if (head == null) {
            head = otherList.head2;
            tail = otherList.tail2;
        } else {
            tail.next = otherList.head2;
            otherList.head.prev = tail2;
            tail = otherList.tail2;
        }

        size += otherList.size2;
    }

    //En la siguiente funcion lo que vamos a hacer es reemplazar elemetos de la lista por lo cual vamos a indicar
    //la posicion en la que se encuentra el objeto y despues de esto le vamos a pasar un String el con el elemento
    //por el cual queremos que este sea reemplazado
    public static void replace(int index, String data) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of range");
        }

        Node current = head;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }

        current.data = data;
    }
}




