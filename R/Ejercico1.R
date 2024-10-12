#1.1
edad <- 22
nombre <- "Pablo"

#1.2
apellidos <- "R P"
nombre_completo <- paste(nombre, apellidos)
nombre_completo

#1.3
num1 <- 10
num2 <- 5

suma <- num1 + num2
suma
class(suma)

#1.4
frase <- paste("Hola me llamo ", nombre_completo)
frase <- paste(frase, "y tengo ")
frase <- paste(frase, edad)
frase <- paste(frase, " años.")
frase

#1.5
install.packages("stringr")
library(stringr)

cadena <- "mi código postal es 28045"
len <- nchar(cadena)
substr <- str_sub(cadena, 3, 17)

len
substr

#1.6
substr2 <- str_trim(substr, side = "left")
substr2 <- toupper(substr2)
substr2

#1.7
cadena_modificada <- str_replace(cadena, "código postal", "cp")
cadena_modificada
