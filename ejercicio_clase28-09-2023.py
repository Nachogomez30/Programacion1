fecha = input("Ingrese la fecha en formato 'día,DD/MM': ").strip().lower()

partes = fecha.split(',')
if len(partes) != 2:
    print("Error: Formato de fecha incorrecto")
else:
    dia, fecha = partes[0].strip(), partes[1].strip()

    niveles = {
        "lunes": "inicial",
        "martes": "intermedio",
        "miércoles": "avanzado",
        "jueves": "práctica hablada",
        "viernes": "inglés para viajeros"
    }

    if dia in niveles:
        nivel = niveles[dia]

        if nivel in ("inicial", "intermedio", "avanzado"):
            examanes = input("¿Hubo exámenes? (Sí/No): ").strip().lower()
            if examanes == "sí":
                aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
                reprobados = int(input("Ingrese la cantidad de alumnos reprobados: "))
                total_alumnos = aprobados + reprobados
                porcentaje_aprobados = (aprobados / total_alumnos) * 100
                print("Porcentaje de aprobados:", porcentaje_aprobados, "%")
            else:
                print("No se tomaron exámenes.")
        elif nivel == "práctica hablada":
            asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
            if asistencia > 50:
                print("Asistió la mayoría")
            else:
                print("No asistió la mayoría")
        elif nivel == "inglés para viajeros" and fecha == "1/10":
            print("Comienzo de nuevo ciclo")
            alumnos_nuevo_ciclo = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel_por_alumno = float(input("Ingrese el arancel en $ por cada alumno: "))
            ingreso_total = alumnos_nuevo_ciclo * arancel_por_alumno
            print("Ingreso total en $:", ingreso_total)
    else:
        print("Error: Día de la semana no válido o formato de fecha incorrecto.")
