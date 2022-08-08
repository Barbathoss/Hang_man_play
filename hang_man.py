import random
import os

PICS = ["""
   +--+
   |  |
      |
      |
      |
      |
  =====""",
 """
   +--+
   |  |
   O  |
      |
      |
      |
  =====""",
 """
   +--+
   |  |
   O  |
   |  |
      |
      |
  =====""",
 """
   +--+
   |  |
   O  |
  /|  |
      |
      |
  =====""",
 """
   +--+
   |  |
   O  |
  /|\ |
      |
      |
  =====""",
 """
   +--+
   |  |
   O  |
  /|\ |
  /   |
      |
=====""",
 """
   +--+
   |  |
   O  |
  /|\ |
  / \ |
      |
  ====="""]


def read_data():
    word_data = []
    with open ("./data.txt","r",encoding="utf-8") as f:
        for line in f:
            word_data.append(line)
    w=random.choice(word_data)
    w=w.strip()   
    return w


def normalize(norm):
    a,b='áéíóú','aeiou'
    trans=str.maketrans(a,b)
    nm=norm.translate(trans)
    return nm


def hiding_word(h):
    word_hide=h
    mask=""
    for i in word_hide:
        mask+="_" 
    print("   ")    
    print(mask)
    return (mask)


def check_word(m,k,letter_in):
    win_word=m
    mask_word=k
    count=0
    for i in win_word:
                
        if letter_in == i:                
            mask_word=list(mask_word) #convierte en lista
            mask_word[count]=letter_in #envia letra ingresada a la posicion de la w maskara                  
            count+=1
        else:
            count+=1                                                 
    mask_word="".join(mask_word)
    print(mask_word.upper())
    return mask_word       



def run():
    word_win=read_data()
    word_win=normalize(word_win)
    word_mask=hiding_word(word_win)
    global lose
    lose=0
    resul=word_mask
    win=False
    while lose<7 or win == False:
        letter=input("Ingrese una letra por favor  ")
        
        if letter in word_win:
            os.system("clear")
            visto =check_word(word_win,resul,letter)
            resul=visto
            if resul in word_win:
                win=True
                os.system("clear")
                print(resul.upper())
                print("GANASTE !!!!!!!")
                break
            
        else:
            lose +=1
            os.system("clear")
            print("Te queda ",7-lose," ❤")
            print(resul.upper())
            print(PICS[lose]) 
            if lose >= 6:
                print("PERDISTE!!!!!!!!")
                break 
        
    


if __name__ == "__main__":
    run()