
  Calcula el tiempo en días, entre dos fechas, regresando un arreglo donde
  se separan los días que pertenecen a años bisiestsos y los días que pertenecen a años regulares.

  Ejemplo 1:
  start = '2020-01-01'
  end = '2021-05-30'

  entre estas dos fechas existen 515 días, 366 pertenecen a ser días de un año bisiesto (2020)
  y 149 pertenecen a un año regular (2021)

  Ejemplo 2:
  start = '2020-01-01'
  end = '2024-05-30'

  entre estas dos fechas existen 1611 días, 516 pertenecen a ser días de un año bisiesto (2020,2024)
  y 1095 pertenecen a un año regular (2021,2022,2023)


  Parámetros: Recibe dos cadenas en formato Y-m-d, la fecha de inicio y la fecha de fin en ese orden,
  la fecha de inicio debe ser mayor que la fecha de fin.

  Retorna:
      En caso de éxito: Un arreglo con dos números, el primer elemento son los días que pertenecen a años bisiestos
                      y el segundo elemento son los días que pertenecen a años regulares

      En caso de fracaso: Regresa 0
