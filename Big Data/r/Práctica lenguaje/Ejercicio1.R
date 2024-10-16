#EJERCICIO1
data("iris")
#6 primeras filas
head(iris)
#Resultado estadístico
summary(iris)
str(iris)
#Media
mean(iris$Sepal.Length)
mean(iris$Petal.Length)
#Mediana
median(iris$Sepal.Length)
median(iris$Petal.Length)
#Desviación típica
sd(iris$Sepal.Length)
sd(iris$Petal.Length)
#table
table(iris)

#EJERCICIO2
#Filtrar por condición
iris_grandes <- iris[iris$Sepal.Length > 6,]
iris_grandes
# Crear una nueva columna
Sepal.Area <- iris$Sepal.Area <- iris$Sepal.Length * iris$Sepal.Width
iris

#EJERCICO3
#historigrama
hist(iris$Sepal.Length)

#boxplot, (velas japonesas)
# Crear el boxplot para comparar Petal.Length entre las especies
boxplot(Petal.Length ~ Species, data = iris,
        main = "Comparación de la longitud del pétalo entre especies",
        xlab = "Especie", ylab = "Largo del Pétalo", col = c("lightblue", "lightgreen", "lightpink"))

#gráfico de dispersión
plot(iris$Petal.Length, iris$Petal.Width,
     xlab = "Largo del pétalo",
     ylab = "Ancho del pétalo",
     main = "Scatterplot de Largo vs Ancho del Pétalo",
     col = iris$Species,  # Colorea por especie
     pch = 19)  # Cambia el tipo de punto
legend("topright", legend=levels(iris$Species), col=1:3, pch=19)

#correlación
cor(iris$Sepal.Length, iris$Petal.Length)

#Modelado simple
# Ajustar el modelo lineal simple
modelo <- lm(Petal.Length ~ Sepal.Length, data = iris)
# Ver el resumen del modelo
summary(modelo)

# Realizar predicciones con nuevos valores de Sepal.Length
nuevos_valores <- data.frame(Sepal.Length = c(5.0, 6.5, 7.0))
predicciones <- predict(modelo, nuevos_valores)
# Ver las predicciones
predicciones
# Añadir las predicciones al dataset iris
iris$Prediccion_Petal.Length <- predict(modelo)

head(iris)

# Exportar el dataset modificado a un archivo CSV
write.csv(iris, file = "iris_modificado.csv", row.names = FALSE)
getwd()
