import random
 
# Lista de palabras posibles
 
words = [
    "python", "programación", "computadora", "código", "desarrollo",
    "inteligencia"
]
 
# Elegir una palabra al azar
secret_word = random.choice(words)
#Contador de intentos
cont_attempts = 0
# Número máximo de errores permitidos
max_errors = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []
word_displayed = ""
 
 
#Funciones de dificultad dependiendo su caso
def nivel_Facil(secret_word):
  word_displayed = ""
  for letter in secret_word:
    if letter in 'aeiouáéíóú':
      word_displayed += letter
    else:
      word_displayed += "_"
  return word_displayed
 
 
def nivel_Medio(secret_word):
  word_displayed = secret_word[0] + "_" * (len(secret_word) -
                                           2) + secret_word[-1]
  if secret_word.count(secret_word[0]) == 1:
    guessed_letters.append(secret_word[0])
  if secret_word.count(secret_word[-1]) == 1:
    guessed_letters.append(secret_word[-1])
  return word_displayed
 
 
def nivel_Dificil(secret_word):
  word_displayed = "_" * len(secret_word)
  return word_displayed
 
 
salir = False
while (salir == False):
  print("¡Bienvenido al juego de adivinanzas!")
  #Elegir nivel de difcultad del juego
  print("""Elija nivel de difcultad:
  1. Facil
  2. Medio
  3. Dificil
  """)
  option = input("Ingrese opcion: ")
  match option:
    case "1":
      word_displayed = nivel_Facil(secret_word)
      salir = True
    case "2":
      word_displayed = nivel_Medio(secret_word)
      salir = True
    case "3":
      word_displayed = nivel_Dificil(secret_word)
      salir = True
    case _:
      print("Opcion invalida")
 
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
 
#Si no llego a la maxima cantidad de errores se ingresa letra y evalua
while cont_attempts != max_errors:
  # Pedir al jugador que ingrese una letra
  letter = input("Ingresa una letra: ").lower()
 
  # Verificar si la letra ya ha sido adivinada
  if letter in guessed_letters:
    print("Ya has intentado con esa letra. Intenta con otra.")
    continue
  # Agregar letra a la lista de letras adivinadas si es un valor valido
  if letter != '':
    #Verificar si la letra está en la palabra secreta
    if letter in secret_word:
      print("¡Bien hecho! La letra está en la palabra.")
      guessed_letters.append(letter)
    else:
      print("Lo siento, la letra no está en la palabra.")
      cont_attempts += 1
 
  #Si se ingresa un valor vacio muestra que es invalido y no suma intentos
  else:
    print('Valor invalido. Intentelo otra vez')
    continue
 
  #Convertir cadena actual a lista e iterar sobre cada letra para mostrar palabra parcialmente adivinada
  letters = list(word_displayed)
  for i in range(len(secret_word)):
    if (secret_word[i] == letter) and (word_displayed[i] == "_"):
      letters[i] = letter
 
  word_displayed = "".join(letters)
  print(f"Palabra: {word_displayed}")
  # Verificar si se ha adivinado la palabra completa
  if word_displayed == secret_word:
    print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
    break
else:
  print(
      f"¡Oh no! Has alcanzdo la maxima cantidad de erorres: {max_errors} errores. "
  )
  print(f"La palabra secreta era: {secret_word}")