# Prueba2
def leerTexto():
    archivo=open('datos.txt','w')
    linea=archivo.readline()

    def grabartxt():
        archi = open('datoss.txt', 'w')
        archi.write('hola 1\n')
        archi.write('hola 2\n')
        archi.write('como 3\n')
        lista = []
        lista_final = []

        for numero in contenido:
            lista += numero.split()
        lista.sort()
        set_lista = set(lista)
        set_lista = list(set_lista)
        set_lista.sort()
        print("Valor:Ocurrencias")
        for numero in set_lista:
            lista_final.append((lista.count(numero), numero))

        lista_final.sort(reverse=True)
        print(lista_final)

        archi.close()


def cabecera():
    print("Escuela Politecnica Nacional")
    print("Prueba 2")
    print("Integrantes: Bryan Corrales")
    print("             Sergio Sigcha")
    print("             Cristian Mainato")
cabecera()
leerTexto()
grabartxt()
