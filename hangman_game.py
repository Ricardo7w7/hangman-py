from itertools import count
import random
import os
from hangman_pics import HANGMANPICS

def texthangman():
    print("""
    88                                                          
    88                                                                       
    88                                                                            
    88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,     
    88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'   `"8a  
    88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88 
    88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88       88 
    88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88       88 
                                        aa,    ,88                                
                                        "Y8bbdP"                          
                                                """)


def winner():
    print("""
8b        d8                        I8,        8        ,8I 88              
 Y8,    ,8P                         `8b       d8b       d8' ""              
  Y8,  ,8P                           "8,     ,8"8,     ,8"                  
   "8aa8" ,adPPYba,  88       88      Y8     8P Y8     8P   88 8b,dPPYba,   
    `88' a8"     "8a 88       88      `8b   d8' `8b   d8'   88 88P'   `"8a  
     88  8b       d8 88       88       `8a a8'   `8a a8'    88 88       88  
     88  "8a,   ,a8" "8a,   ,a88        `8a8'     `8a8'     88 88       88  
     88   `"YbbdP"'   `"YbbdP'Y8         `8'       `8'      88 88       88                                                                                                                                                                                         
    """)


def losser():
    print("""  
8b        d8                           88                                           
 Y8,    ,8P                            88                                             +---+
  Y8,  ,8P                             88                                             |   |
   "8aa8" ,adPPYba,  88       88       88          ,adPPYba,  ,adPPYba,  ,adPPYba,    O   |
    `88' a8"     "8a 88       88       88         a8"     "8a I8l    "" a8P_____88   /|\  |
     88  8b       d8 88       88       88         8b       d8  `"Y8ba,  8PP"""""""         / \  |
     88  "8a,   ,a8" "8a,   ,a88       88         "8a,   ,a8" aa    l8I "8b,   ,aa        |
     88   `"YbbdP"'   `"YbbdP'Y8       88888888888 `"YbbdP"'  `"YbbdP"'  `"Ybbd8"'  =========   
     """)


#La funcion read_data es la que busca el archivo que contiene las frases y 
#regresa una lista llamada data que las contiene.
def read_data():
    data = []
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(line.upper())
    return data


##Esta funcion selecciona una frase de la lista data
def select_hidden_word():
    data = read_data()
    count_data = int(len(data))
    word = data[random.randint(1, count_data)]
    word = word.strip()
    word = [i for i in word]
    return word
    

def run():
    play = True
    while play != False:
        os.system('cls')
        #Nos guarda en la lista hidden_word la palabra que selecciono la funcion de la lista data
        hidden_word = select_hidden_word()

        #Creamos una lista con un _ por cada letra que tiene nuestra hidden_word
        word = ["_" for i in range(0, len(hidden_word))]

        char = ""
        man_life = 0
        #Creamos una cadena con todos los _ que contiene nuestra lista
        #para luego compararla para asi saber si el usuario ingreso una letra correcta o incorrecta
        word_char_count = "".join(word).count("_")
        compare = word_char_count

        while word != hidden_word and man_life != 7:
            texthangman()
            
            phrase = "  THE WORD IS: "
            #Imprimimos en pantalla el HANGMANPIC correspondiente y la palabra
            print(HANGMANPICS[man_life]+ phrase+ str(word))

            #Solicitamos la letra al usuario y le aplicamos el metodo upper
            char = input("\nPlease enter a letter: ").upper()

            #Recorremos la lista hidden_word donde tenemos nuestra palabra secreta con la 
            #leta que ingreso el usuario para asi verificar si se encuentra en la palabra
            for i in range(0, len(hidden_word)):
                if char == hidden_word[i]:
                    #Si la letra se encuentra en la lista se remplazara el _ por la letra ingresada
                    word[i] = word[i].replace("_", char)

            #Comparamos si el usuario ingreso una letra correcta
            word_char_count = "".join(word).count("_")
            if word_char_count == compare:
                #si no es correcta la HANGMANPIC pasa a la siguiente
                man_life = man_life +1
            else:
                #si es correcta la HANGMANPIC se queda en la actual
                compare = word_char_count

            os.system('cls')

        if word == hidden_word:
            winner()
            print("YOU HAVE FOUND THE SECRET WORD!!")
        else:
            losser()
            print("         SORRY THE SECRET WORD WAS: " + str(hidden_word))

        print("\nDO YOU WANT TO PLAY AGAIN? YES OR NO")
        res = ""
        while res != "YES" and res != "NO":
            res = input("ANSWER: ").upper()

            if res == "YES":
                play = True
            elif res == "NO":
                play = False
            else:
                print("SELECT A CORRECT OPTION")
        

if __name__ == '__main__':
    run()

