library(stringr)

edad = 22
altura = 176
nombre = "Pablo"
apellidos = "Rosas Plaza"
complete_name = paste(nombre, apellidos)

sum = edad + altura
class(sum)

direc =  "mi código postal es 28045"
x = direc
y = substr(direc, 3, 17)
toupper(sub(" ", "", y))
sub("código postal","cp", x)
