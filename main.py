

nombres_clientes= []
direcciones= []
ruta = ["centro","norte","sur"]
detalle_pedido = ["grande","pequeño","mediano"]



def menu():
    print("1. Registrar pedido")
    print("2. Listar pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir")

def registrarPedido():
    nombre_y_apellido= input("Ingrese nombre y apellido: ")
    nombres_clientes.append(nombre_y_apellido)
    
    direccion= input("Direccion: ")
    direcciones.append(direccion)
    
    sector= input("Sector: ")
    ruta.append(sector)
    
    detalle= input("Detalle del pedido: ").lower()
    if detalle not in detalle_pedido:
            print("El detalle debe especificar tamaño del paquete. Pequeño/Mediano/Grande")
            detalle= input("Detalle del pedido: ").lower()
    
    detalle_pedido.append(detalle)
    print("Registro del pedido")
    for nombre in nombres_clientes:
         for direccion in direcciones:
              for sector in ruta:
                   for detalleTamaño in detalle_pedido:
                    print(f"{nombre} {direccion} {sector} {detalleTamaño}")

def listar_pedido():
    for nombres_clientes, direcciones, ruta, detalle_pedido in list(nombres_clientes, direcciones, ruta, detalle_pedido):
         print(list)


def hojaDeRuta():
     with open("archivo.txt","w") as archivo:
          escritor.csv= txt.writer

def main():
     
    menu()

while True:
    try:
          
        opcion= int(input("Ingrese opcion que desa realizar: "))

        if opcion== 1:
            registrarPedido()
        elif opcion ==2:
            listar_pedido()
        elif opcion== 3:
            hojaDeRuta()
        elif opcion== 4:
            break
        else:
            print("Operacion incorrecta")

    except ValueError:
        print("Opcion no vàlida")

main()
     