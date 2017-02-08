from input import getInputArray
from compression import compress
import sys
from tkinter import *

#from compression import *
master = Tk()
master.title("Key Compressor")
textBox = Text(master, height=15, width=30)
textBox.pack(fill = 'x')
textBoxText = "Insert Text Here"
textBox.insert(END,textBoxText)

compressionRatioLabel = Label(master, text="Compression Ratio: 1")
compressionRatioLabel.pack()


def updateCompressionRatio(compressed, uncompressed):
    print(sys.getsizeof(compressed))
    print(sys.getsizeof(uncompressed))
    compressionRatio = float(sys.getsizeof(compressed)) / float(sys.getsizeof(uncompressed))
    compressionRatioLabel.config(text = "Compression Ratio: " + str(compressionRatio))

def compressText():
    textBoxText = textBox.get('1.0', END)
    inputArray = getInputArray(textBoxText)
    initialText = inputArray
    #print("chopped2", inputArray)
    compressedText = compress(inputArray)
    textBox.delete('1.0', END)
    textBox.insert(END, compressedText)
    updateCompressionRatio(compressedText, initialText)


compressButton = Button(master, text = "Compress", command = compressText)
compressButton.pack()

mainloop()