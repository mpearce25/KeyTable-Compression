def getInputArray(text):
    inputArray = text.split(" ")
    inputArray[len(inputArray) -1] = inputArray[len(inputArray) -1] [0: len(inputArray[len(inputArray) -1]) -1] #removes the last line break

    '''for k in range(len(inputArray)):
        if "\n" in inputArray[k]:
            startingBreak = inputArray[k].index("\n")
            endingBreak = inputArray[k].rindex("\n") + 1
    '''#for removing \n's

    return inputArray