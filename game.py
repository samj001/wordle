import sys,os,string
from dic import MyDic

'''
Annotations:
    'W' - wrong, guessed letter not in the answer word
    'R' - right, guessed letter is in the answer word and also in right position
    'P' - position, guessed letter is in the answer word but in wrong position
    'U' - letter never been guessed
'''

class Game:

    def __init__(self,length):
        self.dic = MyDic()
        self.chances = 6
        self.length = length
        self.answer = self.dic.GenerateAnswer(length)
        self.guessedletters = dict(zip(list(string.ascii_lowercase),['U']*26))
        self.end = False

    
    def HandleInput(self,user_guess):
        #user_guess = input(f"A word of {self.length} letters. No repeating letters. You have {self.chances} chances left.")
        self.chances -= 1
        result = self.dic.CheckWord(user_guess,self.answer)
        
        if result == "RightGuess":
            self.end = True
        
        letter_result = self.GuessResult(user_guess)
        return result,letter_result


    def HintResult(self):
        string = f"The right answer is: {self.answer}"
        self.end = True
        return string
    

    def GuessResult(self,user_guess):
        letters = []
        output = ['W'] * self.length
        for l in self.answer:
            letters.append(l)
        #print(letters)
        
        for i in range(len(user_guess)):
            if user_guess[i] == self.answer[i]:
                output[i] = 'R'
                self.guessedletters[user_guess[i]] = 'R'
            elif user_guess[i] in letters:
                output[i] = 'P'
                self.guessedletters[user_guess[i]] = 'P'
            else:
                self.guessedletters[user_guess[i]] = 'W'

        return output 
    
    


    

