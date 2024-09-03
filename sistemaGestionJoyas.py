productos = [
    {"nombre": "Anillo de Oro", "precio": 500, "cantidad": 10},
    {"nombre": "Pulsera de Diamantes", "precio": 7000, "cantidad": 10},
    {"nombre": "Reloj de Oro.", "precio": 1500, "cantidad": 10},
    {"nombre": "Cadena de Plata.", "precio": 100, "cantidad": 10}
]

#Lista para almacenar los productos que el usuario agrega al carrito. 
carrito = []

#Función para mostrar los productos disponibles.
def MostrarProductos():
    print("\n------Lista de Productos disponibles-------")
    for item, producto in enumerate(productos):
        print(f"{item}. {producto["nombre"]}: ${producto["precio"]} - Disponibles: {producto["cantidad"]}")
        print("-------------------------------------------")
        
def agregarCarrito():
    MostrarProductos()
    try:
        opcion = int(input("\nSeleccionar el número del producto que deseas agregar al carrito: "))
    #Verificar si la opción es válida. 
        if opcion > 0 and opcion <= len(productos):
            cantidad = int(input("\nIngresar la cantidad que deseas comprar: "))
            producto = productos[opcion -1]
            #Verificar si hay Stock disponible.
            if cantidad > producto["cantidad"]:
                print("\nNo hay suficiente Stock disponible.")
            else:
                producto["cantidad"] -= cantidad
                
                carrito.append({"nombre": producto["nombre"], "precio": producto["precio"], "cantidad": cantidad})
                
                print(f"\nSe agrego {cantidad} {producto["nombre"]} al carrito.")
        else:
            print("\nOpción no valida.")
    except ValueError: 
        print("\nEntrada invalida por favor ingresar un número: ")
    except Exception as e:
        #Captura cualquier error que pueda ocurrir.
        print(f"Ocurrio un error {e}")

def MostrarCarrito():
    if carrito:
        print("\nCarrito de compras:")
        print("-------------------------------------------")
        #Recorre la lista del carrito y muestra casa producto con su nombre, precio y cantidad.
        for i, item in enumerate(carrito, 1):
            print(f"{i}. {item["nombre"]} - ${item["precio"]} (cantidad: {item["cantidad"]})")
            print("-------------------------------------------")
    else:
        print("\nEl carrito está vacío.")
        
#Función para calcular el total a pagar por los productos en el carrito.
def calcularTotal():
    total = sum(item["precio"] * item["cantidad"] for item in carrito)
    print(f"\nEl total a pagar es: ${total}")

#Función para finalizar la compra. 
def finalizarCompra():
    MostrarCarrito()
    if carrito: 
        calcularTotal()
        #Preguntar al usuario si desea finalizar la compra.
        confirmacion = input("¿Desea finalizar la compra? (s/n): ")
        if confirmacion.lower() == "s":
            #Si el usuario confirma, se vacía el carrito y se finaliza la compra.
            carrito.clear()
            print("Compra finalizada. Gracias por su compra.")
        else:
            print("Compra cancelada.")
    else:
        print("No hay productos en el carrito para finalizar la compra.")
        
#Función principal del menú del programa.

def menu():
    while True:
        print("\n  ------ MENÚ ------ ")
        print("\n1. Mostrar productos")
        print("2. Agregar producto al carrito.")
        print("3. Mostrar carrito.")
        print("4. Finalizar compra.")
        print("5. Salir.")
        
        try:
            opcion = int(input("\nIngresar la opcion: "))
            
            if opcion == 1:
                MostrarProductos()
            elif opcion == 2:
                agregarCarrito()
            elif opcion == 3:
                MostrarCarrito()
            elif opcion == 4:
                finalizarCompra()
            elif opcion == 5:
                print("Gracias por comprar.")
                break
            else:
                print("Opción no valida.")
        except ValueError:
            print("Entrada invalida. Ingresar un número: ")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        
#Invocar Menú.
menu()
            
    
    

