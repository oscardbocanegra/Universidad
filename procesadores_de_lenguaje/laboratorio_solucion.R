# Cargar las librerías necesarias
library(gutenbergr)  # Para descargar textos desde Project Gutenberg
library(tidytext)    # Para procesamiento de texto ordenado
library(dplyr)       # Para manipulación de datos
library(ggplot2)     # Para visualización de datos
require(tm)          # Para la creación y manipulación de corpus de texto y matrices de términos

# Descargar los textos desde Project Gutenberg
# 17192 - The Raven by Edgar Allan Poe
# 62246 - Colossus of Chaos by Nelson S. Bond
# 46992 - Three Plays by Brieux by Eugène Brieux
# 69211 - The angry house by Richard Rein Smith
libros <- gutenberg_download(c(17192, 62246, 46992, 69211), meta_fields = "author")

# Filtrar el libro con ID 69211 ('The angry house')
libro <- libros[libros$gutenberg_id == "69211",]

# Crear un corpus a partir del texto filtrado
corpus <- Corpus(VectorSource(libro))

# Crear una matriz de términos del documento (TermDocumentMatrix)
tdm <- TermDocumentMatrix(corpus)

# Encontrar las 15 palabras más frecuentes en el texto sin ningún filtro
top <- findMostFreqTerms(tdm, n=15)

# Crear un gráfico de barras con las 15 palabras más frecuentes
barplot(top[[2]], main="15 palabras sin filtro", las=2)

# Filtrar el corpus para remover las palabras vacías en inglés
corpus_filtered <- tm_map(corpus, removeWords, stopwords('english'))

# Crear una nueva matriz de términos del documento con el corpus filtrado
tdm_filtered <- TermDocumentMatrix(corpus_filtered)

# Encontrar las 15 palabras más frecuentes en el texto filtrado
top_filtered <- findMostFreqTerms(tdm_filtered, n=15)

# Crear un gráfico de barras con las 15 palabras más frecuentes en el texto filtrado
barplot(top_filtered[[1]], main="Libro02", las=2)
barplot(top_filtered[[2]], main="libro 69211", las=2)

# Generar una nube de palabras con las 15 palabras más frecuentes en el texto filtrado
require(wordcloud)
wordcloud(corpus_filtered, max.words = 15)

# Procesamiento de texto con tidytext
words <- libros %>%
  unnest_tokens(word, text) %>%
  count(author, word, sort = TRUE)

# Calcular el TF-IDF (Term Frequency-Inverse Document Frequency) para cada palabra por autor
rated_words <- words %>%
  bind_tf_idf(word, author, n) %>%
  arrange(desc(tf_idf))

# Seleccionar las 15 palabras más características por autor según el TF-IDF
top_words <- rated_words %>%
  group_by(author) %>%
  top_n(15, tf_idf) %>%
  ungroup() %>%
  arrange(author, desc(tf_idf))

# Visualizar las palabras más características por autor en un gráfico de barras
top_words %>%
  mutate(word = reorder(word, tf_idf)) %>%
  ggplot(aes(word, tf_idf, fill="author")) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~author, ncol=2, scales="free") +
  coord_flip()