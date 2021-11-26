'''''
import math

def main():
    over_16 = True
    not_anumber = True
    while not_anumber:
        try:
            number, base = int(input("Type a number: ")), int(input("Type a base that is not over 16: "))
            not_anumber = False
        except Exception:
            print("\nError:\nYou can only use numbers\nTry again\n")

    while over_16:
        if base > 16:
            print("Your base was over 16\n")
            not_anumber = True
            while not_anumber:
                try:
                    base = int(input("Type a base that is not over 16: "))
                    not_anumber = False
                except Exception:
                    print("\nError\nYou can only use numbers\nTry again\n")
        else:
            over_16 = False
        i = True
        counter = 1
        list = []
        while i:
            list.append(str(math.floor(number / counter) % base))
            counter *= base

            if math.floor(number / counter) <= 1:
                i = False
        list.reverse()
        answer = ''
        for element in list:
            if int(element) > 9:
                dic = {
                    10: 'A',
                    11: 'B',
                    12: 'C',
                    13: 'D',
                    14: 'E',
                    15: 'F'
                        }
                element = dic[int(element)]
            answer += element
        print(answer)

main()
'''''''''
import os

def main():
    dictionary = []
    possibles = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encoded = input("Enter an encoded word: ").lower()
    for i in range(26):
        string = ""
        apart = list(encoded)
        for element in range(len(apart)):
            letter = alphabet.index(apart[element])
            apart[element] = alphabet[letter - i]
            string += str(apart[element])
        possibles.append(string)
    print(possibles)
    path = "C:/Users/jshay/Desktop/words_alpha.txt"
    Pass = False
    with open(path, 'r') as f:
        lines = f.read()
        lines = lines.split('\n')
        for word in lines:
            if Pass == False:
                for element in possibles:
                    #print(element)
                    if word == element:
                        print(word, element)
                        Pass = True
                        break
            else:
                break




        #print("worked", word, element)






main()

