#3.1
x <- c(1, 10, -1, 2)
suma_x <- sum(x)
suma_x

#3.2
y <- c(5, -7, 8, -3)
suma_xy <- x + y
suma_xy

#3.3
mayores_cero <- sum(suma_xy > 0)
mayores_cero

#3.4
x_ordenado <- sort(x)
x_ordenado

#3.5
in_min <- which.min(x)
in_min
in_max <- which.max(x)
in_max

#3.6
elementos_filtrados <- x[x > 1 & x < 7]
elementos_filtrados

todos_positivos <- all(x > 0)
todos_positivos

#3.7
vector_numeros <- c(-1, 0, 4, 5, -2)
raiz_cuadrada <- sqrt(vector_numeros)
lugares_nan <- which(is.nan(raiz_cuadrada))

raiz_cuadrada
lugares_nan

#3.8
impares <- seq(1, 21, by = 2)
elementos_extraidos <- impares[c(1, 4, 5, 8)]
impares <- impares[-2]

elementos_extraidos
impares

#3.9
install.packages("stringr")
library(stringr)

texto <- c("oso polar", "oso pardo", "salamandra", "buho", "lechuza", "oso malayo")
cantidad_osos <- str_count(texto, "oso")
inicia_con_oso <- str_starts(texto, "oso")
longitudes_texto <- str_length(texto)
texto_modificado <- str_replace_all(texto, "o", "*")

cantidad_osos
inicia_con_oso
longitudes_texto
texto_modificado

