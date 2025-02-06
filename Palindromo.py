def palindromo(texto):
    # Convertir a minúsculas y eliminar espacios
    texto= texto.lower().replace(" ", "")

    # Comparar caracteres desde ambos extremos con un bucle for
    longitud = len(texto)
    for i in range(longitud // 2):  # Solo necesitamos revisar la mitad de la palabra ya que es un reflejo
    # Ejemplo reconocer
    #r  e  c  o  n  o  c  e  r
    #0  1  2  3  4  5  6  7  8   (Índices)
    #longitud=9
    #texto[0]=r es distinto de texto[9-1-0]=texto[8]=r
    #texto[1]=e es distinto de texto[9-1-1]=texto[7]=e
    #texto[2]=c es distinto de texto[9-1-2]=texto[6]=c
    #texto[3]=o es distinto de texto[9-1-3]=texto[5]=o

        if texto[i] != texto[longitud - 1 - i]:
            print("No es un palíndromo")
            return False  # Si un par de caracteres no coincide, no es palíndromo
    print("SI es un palíndromo")
    return True  # Si todos coinciden, es palíndromo

while True:
  texto1=str(input("Ingresa tu frase o palabra : "))
  palindromo(texto1)
  # Preguntar si el usuario quiere repetir
  # Metodo strip elimina los espacion en blanco al inicio y final de la cadena
  repetir = input("¿Quieres probar otra palabra? (s/n): ").strip().lower()
  if repetir != 's':
      print("Programa finalizado.")
      break  # Salir del bucle si el usuario no quiere continuar

# Ingresa tu frase o palabra : Anilina 
# SI es un palíndromo
# ¿Quieres probar otra palabra? (s/n): s
# Ingresa tu frase o palabra : olo
# SI es un palíndromo
# ¿Quieres probar otra palabra? (s/n): n
# Programa finalizado.

