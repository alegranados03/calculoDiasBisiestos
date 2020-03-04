from datetime import datetime, date, timedelta


def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def calcular_tiempo(start, end):
    dias_bisiesto = 0  # contador de dias de años bisiestos
    dias_normal = 0  # contador de dias de años regulares
    dates = []  # arreglo de fechas, en caso que la diferencia entre fechas sea mayor a 366
    inicio = datetime.strptime(start, '%Y-%m-%d')

    # se genera (base) la primera fecha del año de la fecha de inicio, sirve para generar los intervalos
    base = datetime.strptime(inicio.strftime('%Y')+'-01-01', '%Y-%m-%d')

    fin = datetime.strptime(end, '%Y-%m-%d')

    if(inicio >= fin):
        return 0

    anio_1 = int(inicio.strftime('%Y'))
    anio_2 = int(fin.strftime('%Y'))

    diferencia_inicial = (fin-inicio).days

    if(diferencia_inicial <= 366):
        if anio_1 == anio_2:
            if(es_bisiesto(anio_1)):
                dias = [diferencia_inicial, 0]
            else:
                dias = [0, diferencia_inicial]
        return dias
    else:
        dates.append(base)  # se incluye la fecha base
        f = base  # pivote para generar todas las fechas en el arreglo
        for year in range(anio_1, anio_2):
            if(es_bisiesto(year)):
                time = timedelta(days=366)
            else:
                time = timedelta(days=365)
            f = f+time
            dates.append(f)
        dates.append(fin)

        for i in range(len(dates)-1):
            fecha_alta = dates[i+1]
            fecha_baja = dates[i]

            anio_fecha_baja = fecha_baja.strftime("%Y")
            anio_fecha_alta = fecha_alta.strftime("%Y")

            dif_baja = (datetime.strptime(
                str(int(anio_fecha_baja)+1) + '-01-01', '%Y-%m-%d')-fecha_baja).days

            dif_alta = (
                fecha_alta - datetime.strptime(anio_fecha_alta+'-01-01', '%Y-%m-%d')).days

            if(i == len(dates)-2):
                if(anio_fecha_baja == anio_fecha_alta):
                    if(es_bisiesto(int(anio_fecha_alta))):
                        dias_bisiesto += min(dif_alta, dif_baja)
                    else:
                        dias_normal += min(dif_alta, dif_baja)
                    continue

            if(es_bisiesto(int(anio_fecha_baja))):
                dias_bisiesto += (dif_baja)
            else:
                dias_normal += (dif_baja)

            if(es_bisiesto(int(anio_fecha_alta))):
                dias_bisiesto += (dif_alta)
            else:
                dias_normal += (dif_alta)

        # correccion de desfase de fecha
        dif_correccion = (inicio-base).days
        if(es_bisiesto(int(anio_1))):
            dias_bisiesto -= (dif_correccion)
        else:
            dias_normal -= (dif_correccion)

    dias = [dias_bisiesto, dias_normal]

    return dias


start = '2021-09-20'
end = '2021-10-30'
print(calcular_tiempo(start, end))
