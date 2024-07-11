import statistics
import random
import csv
trabajadores =["juan Pérez", "María garcía", "Carlos López", 
    "Ana Martínez" , "Pedro Rodríguez",
    "LauraHernández", "ISabel Gómez", "Miguel Sánchez",
    "Francisco Díaz", "Elena Hernández"
  ]

sueldosTrabajadores = {}


def asignarSueldos():
    for trabajador in trabajadores:
        sueldo= random.randint(300000,2500000)
        sueldosTrabajadores[trabajador]=sueldo
    print("A continuación los sueldos de los trabajadores: ")
    print(sueldosTrabajadores)


def clasificarSueldos():
    if not sueldosTrabajadores:
        print("ERROR. No existen sueldos asignados.")
    menores800= {}
    entre800_2m= {}
    superiora2m = {}
    for trabajador, sueldo in sueldosTrabajadores:
        if sueldo < 800000:
            menores800[trabajador]=sueldo
        elif sueldo >= 800000 and sueldo < 2000000:
            entre800_2m[trabajador]=sueldo
        elif sueldo > 2000000:
            superiora2m[trabajador]=sueldo
    print ("Sueldos menores a $800000: ",len(menores800))
    for trabajador, sueldo in menores800.items():
        print(trabajador, ": $", sueldo)
        return trabajador, sueldo

    print("Sueldos entre $800000 y $2000000: ",len(entre800_2m))
    for trabajador, sueldo in entre800_2m.items():
        print(trabajador, ": $", sueldo)
        print()

    print("Sueldos mayores a $2000000: ",len(superiora2m))
    for trabajador, sueldo in superiora2m.items():
        print(trabajador, ": $", sueldo)
        print()
    return 

def estadisticas():
    sueldos = list(sueldos.value())
    max_sueldos= max(sueldos)
    min_sueldos= min(sueldos)
    prom_sueldos= sum(sueldos)/len(sueldos)
    media_geo = statistics.median(sueldos)
    

    print("El máximo sueldo es: ",max_sueldos)
    print("El mínimo sueldo es: ",min_sueldos)
    print("La media de los sueldos es: ",prom_sueldos)
    return sueldos

def reporteSueldos():
    for sueldos in sueldosTrabajadores:
        descuentoAFP = sueldos - (sueldos*0.12)
    for sueldos in sueldosTrabajadores:
        descuentoSalud= sueldos - (sueldos*0.07)
    for sueldos in sueldosTrabajadores:
        sueldoLiquido= sueldos - descuentoAFP- descuentoSalud

    reporte = {

        "Nombre": trabajadores,
        "Sueldo Base": sueldosTrabajadores,
        "Descuento AFP": descuentoAFP,
        "Descuento Salud": descuentoSalud,
        "Sueldo Líquido": sueldoLiquido
    }
    with open("reporteSueldos.csv","w") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow[("Nombre Empleado", "Sueldo base", "Descuento AFP", "Descuento Salud", "Sueldo Líquido")]
        escritor.writerows[(trabajadores, sueldosTrabajadores, descuentoAFP, descuentoSalud, sueldoLiquido)]

def main():
    while True:
        try:
            print("--Bienvenido al gestor de sueldos de su empresa--")
            print("---MENÚ PRINCIPAL---")
            print("1. Asignar sueldos aleatorios")
            print("2. Clasificar sueldos")
            print("3. Ver estadísticas")
            print("4. Reporte de sueldos")
            print("5. Salir")
            opc=int(input("Ingrese opción: "))

            if opc == 1:
                asignarSueldos()
            elif opc == 2:
                clasificarSueldos()
            elif opc == 3:
                estadisticas()
            elif opc == 4:
                reporteSueldos()
            elif opc == 5:
                print("Finalizando programa...")
                print("Desarrollado por Joaquín Reyes (El Da Vinci del código)")
                print("Viña del Mar, Julio 2024")
                break
            else:
                print("Solo se aceptan valores del 1 al 5")
        except:
            print("operación incorrecta")


main()