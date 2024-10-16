#4.1
install.packages("lubridate")
library(lubridate)

fecha_hoy <- today()
fecha_hoy

fecha_cumple <- ymd("2002-06-26")
fecha_cumple

diferencia_dias <- as.numeric(fecha_hoy - fecha_cumple)
diferencia_dias

#4.2
año_bisiesto <- leap_year(fecha_cumple)
año_bisiesto

nueva_fecha_1 <- fecha_cumple + weeks(1)
nueva_fecha_2 <- fecha_cumple + weeks(2)
nueva_fecha_3 <- fecha_cumple + weeks(3)
nueva_fecha_4 <- fecha_cumple + weeks(4)
nueva_fecha_5 <- fecha_cumple + weeks(5)

nueva_fecha_1
nueva_fecha_2
nueva_fecha_3
nueva_fecha_4
nueva_fecha_5

#4.3
mes <- month(fecha_cumple)
año <- year(fecha_cumple)
dia_semana <- wday(fecha_cumple, label = TRUE, abbr = FALSE)
dia_semana <- as.character(dia_semana)

mes
año
dia_semana

#4.4
dias_transcurridos <- as.numeric(fecha_hoy - fecha_cumple)
dias_transcurridos
