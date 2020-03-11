import arcade
import random

done = True

millasrecorridas = 0
sediento = 0
cansanciocamel = 0
distancianativos = -20
bebidas = 3
millastotales = 200
distancia1 = (millasrecorridas - distancianativos)
distancia2 = (millastotales - millasrecorridas)

def introduccion():
    print("Bienvenido a Camel," 
          "\nEste juego trata de que has robado un camello y tienes que cruzar con el todo el desierto de Mobi "
          "\n¡Los nativos te estan persiguiendo!, intenta escapar del desierto con el camello")

def menu(done, millasrecorridas, sediento, distancianativos, bebidas, distancia1, millastotales, distancia2):
    while(done):
        print("1. Beber de tu cantimplora.\n"
            "2. Moderar la velocidad.\n"
            "3. Ir a toda velocidad.\n"
            "4. Parar por la noche para acampar.\n"
            "5. Ver tu estado y tus provisiones.\n"
            "0. Quitar el juego.\n")
        opcion = int(input("¿Que quieres hacer? "))
        print(opcion)
        if(opcion == 1):
            print("Bebes de la cantimplora\n")
            bebidas = bebidas - 1
            sediento = sediento - 10
            millasrecorridas = millasrecorridas + 3
            distancianativos = distancianativos + 3
            if(bebidas <= 0):
                print("No te quedan bebidas")
        elif(opcion == 2):
            print("Has bajado la velocidad\n")
            sediento = sediento + 1
            millasrecorridas = millasrecorridas + 2
            distancianativos = distancianativos + 3
        elif(opcion == 3):
            print("Subes la velocidad\n")
            sediento = sediento + 7
            millasrecorridas = millasrecorridas + random.randint(10, 21)
            distancianativos = distancianativos + 3
        elif(opcion == 4):
            print("Has decidido parar y preparar una fogata\n")
            distancianativos = distancianativos + 3
        elif(opcion == 5):
            print("Te dispones a ver como te encuentras y ver cuantas provisiones te quedan\n")
            interfaz(millastotales, millasrecorridas, sediento, distancianativos, bebidas)
        elif(opcion == 0):
            done = False
            print("Has salido del juego")
        lose(distancia1, done)
        win(distancia2, done)

def interfaz(millastotales, millasrecorridas, sediento, distancianativos, bebidas):
    print("\nMillas que faltan: ", (millastotales - millasrecorridas), "\nMillas recorridas" , millasrecorridas , "\nBebidas: " , bebidas, "\nSediento: ", sediento, "\nLos nativos estan a " , (millasrecorridas - distancianativos), "millas de distancia.\n")

def lose(distancia1, done):
    if (distancia1 <= 0):
        print("\nHAS PERDIDO, LOS NATIVOS TE HAN CAPTURADO")
        done = False
    return distancianativos, done

def win(distancia2, done):
    if (distancia2 <= 0):
        print("\nHAS GANADO, HAS CONSEGUIDO HUIR DE LOS NATIVOS")
        done = False
    return distancia2, done

print(introduccion())
print(menu(done, millasrecorridas, sediento, distancianativos, bebidas, distancia1, millastotales, distancia2))