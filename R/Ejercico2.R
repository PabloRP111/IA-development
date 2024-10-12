#2.1
vector_num <- c(1, 5, -7)
vector_num

#2.2
vector_num <- c(1, 10, -1, 2)
vector_num

#2.3
longitud_vector <- length(vector_num)
longitud_vector

#2.4
vector_texto <- c("Hola", "me", "llamo", "Pablo", "R", "P")
frase <- paste(vector_texto, collapse = " ")
frase_completa <- paste(frase, "y tengo 30 años")
frase_completa

#2.5
secuencia <- seq(-1, 32, by = 3)
secuencia

#2.6
secuencia2 <- seq(-1, 32, length.out = 12)
secuencia2

#2.7
secuencia3 <- 1:10
secuencia3
secuencia4 <- rep(3, 7)
secuencia4

#2.8
secuencia5 <- rep(c(1, 2, 3), times = 5)
secuencia5

#2.9
x <- c("oso pardo", "oso polar", "ballena", "grillo", "oso panda", "perro")
lens = str_length(x)
lens
es_oso <- str_detect(x, "oso")
es_oso
