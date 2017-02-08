def getInputArray(text):
    inputArray = text.split(" ")
    inputArray[len(inputArray) -1] = inputArray[len(inputArray) -1] [0: len(inputArray[len(inputArray) -1]) -1] #removes the last line break
    return inputArray