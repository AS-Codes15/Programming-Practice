import random
word_list=['apple','beautiful','potato']
choosen_word=random.choice(word_list)
print(choosen_word)
lives=6
display=[]
for i in range(len(choosen_word)):
    display+='_'
print(display)    
game_over=False
while not game_over:
    guessed_letter=input("guess a ltter")
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)        
    if guessed_letter not in choosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("you loose")
    if '_' not in display:
        game_over=True
        print("you win")        
