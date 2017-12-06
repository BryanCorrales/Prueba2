# Prueba2
def leerTexto():
    archivo=open('datos.txt','r')
    linea=archivo.readline()
    print(linea)
    lista=linea.split(' ')
    pa=len(lista)
    print("El numero de letras que existen en el archivo txt es",pa)
    while linea!="":
        linea=archivo.readline()
    archivo.close()
def cabecera():
    print("Escuela Politecnica Nacional")
    print("Prueba 2")
    print("Integrantes: Bryan Corrales")
    print("             Sergio Sigcha")
    print("             Cristian Mainato")
cabecera()
leerTexto()