from random import *
import sys
def getWordFrequency(inputArray, minLength):
    wordCount = []
    for i in range(len(inputArray)):
        word = inputArray[i]
        if len(word) >= minLength: #change this number for minimun number of characters
            # first run
            if len(wordCount) == 0:
                wordInfo = [word, 1]
                wordCount.append(wordInfo)
            # subsequent runs
            else:
                match = False
                matchIndex = 0
                for k in range(len(wordCount)):
                    if (word == wordCount[k][0]):
                        match = True
                        matchIndex = k
                        break;  # neccessary for it to find the correct index
                if match:
                    wordCount[k][1] = wordCount[k][1] + 1
                else:
                    wordSet = [word, 1]
                    wordCount.append(wordSet)
    return wordCount
def getWordsToReplace(frequencyArray, minOcc):
    wordsToReplace = []
    for k in range(len(frequencyArray)):
        if frequencyArray[k][1] >= minOcc: #change this number for minium number of occurances
            wordsToReplace.append(frequencyArray[k][0])
    return wordsToReplace

def inArray(s, array):
    match = -1
    for k in range(len(array)):
        if s == array[k]:
            match = k
            #print("match found", s, array[k])
    return match

def substituteChars(wordsToReplace, inputArray):
    #print("wrods to replace", wordsToReplace, "input array", inputArray )
    substitutionChars = []
    startingUnicodeIndex = 5000
    for k in range (len(wordsToReplace)):
        replacementChar = chr(5000 + k)
        substitutionChars.append([wordsToReplace[k],[replacementChar]])

    print(substitutionChars)
    for i in range(len(inputArray)):
        if inArray(inputArray[i], wordsToReplace) > -1:
            index = inArray(inputArray[i], wordsToReplace)
            #print(str(substitutionChars[index][1])[2])
            inputArray[i] = str(substitutionChars[index][1])[2]
    return inputArray

def joinArray(array):
    #print(array)
    string = ""
    for k in range(len(array)):
        string += str(array[k]) + " "
    return string


def compress(inputArray, minOcc, minLength):
    wordFrequency = getWordFrequency(inputArray, minLength)
    wordsToReplace = getWordsToReplace(wordFrequency, minOcc)
    compressedArray = substituteChars(wordsToReplace, inputArray)
    compressedText = joinArray(compressedArray)
    return compressedText