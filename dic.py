import sys,string,os
import random
import nltk

def BuildVocab():
    eng_vocab = nltk.corpus.words.words()
    freq_vocab = nltk.corpus.words.words('en-basic')
    wordLength_5 = []
    wordLength_6 = []
    word_frequent5 = []
    word_frequent6 = []

    for word in eng_vocab:
        if len(word) == 5:
            if (MyDic.CheckDuplicate(word) == False):
                wordLength_5.append(word.lower())

        elif len(word) == 6:
            if (MyDic.CheckDuplicate(word) == False):
                wordLength_6.append(word.lower())
    
    for word in freq_vocab:
        if len(word) == 5:
            if (MyDic.CheckDuplicate(word) == False):
                word_frequent5.append(word.lower())

        elif len(word) == 6:
            if (MyDic.CheckDuplicate(word) == False):
                word_frequent6.append(word.lower())
 
    open('wordof5.txt', 'w').close()
    with open(r'wordof5.txt','w') as fp:
        for i in wordLength_5:
            fp.write("%s\n" % i)
    fp.close()
    
    open('wordof6.txt', 'w').close()
    with open(r'wordof6.txt','w') as fp:
        for i in wordLength_6:
            fp.write("%s\n" % i)
    fp.close()
   
    return wordLength_5,wordLength_6,word_frequent5,word_frequent6


class MyDic:
    def __init__(self):
        wordlist5, wordlist6,freq5,freq6 = BuildVocab()
        self.wordlist5 = wordlist5
        self.wordlist6 = wordlist6
        self.freq5 = freq5
        self.freq6 = freq6

    def CheckDuplicate(word):
        have_letters = [word[0]]
        for i in range(len(word)-1):
            if word[i+1] in have_letters:
                return True
            have_letters.append(word[i+1])

        return False

    def GenerateAnswer(self,word_length):       
        if word_length == 5:
            word_index = random.randint(0,len(self.freq5))
            return self.freq5[word_index]
        
        if word_length == 6:
            word_index = random.randint(0,len(self.freq6))
            return self.freq6[word_index] 


    def CheckWord(self,user_input,answer):
        if len(user_input) == 5:
            if user_input in self.wordlist5:
                if user_input == answer:
                    return "RightGuess"
                else:
                    return "WrongGuess"
            else:
                return "NotLegitWord"
        
        elif len(user_input) == 6:
            if user_input in self.wordlist6:
                if user_input == answer:
                    return "RightGuess"
                else:
                    return "WrongGuess"
            else:
                return "NotLegitWord"
        
        elif len(user_input)!=len(answer):
            return "NotRightLength"
