THE_FILE = "saveFile.txt"
READ_MODE = "r"
WRITE_MODE = "w"

def main():
    text = getText()
    saveText(text, THE_FILE)
    print("File Saved.")
    contents = readFile(THE_FILE)
    print("Reading File Contents.")
    print(contents)
    return

def getText():
    text = input("What information would you like to save: ")
    return text

def saveText(text, fileName) :
    myfile = open(fileName, mode=WRITE_MODE)
    myfile.write(text)
    myfile.close()
    return

def readFile(fileName) :
    myfile = open(fileName, mode=READ_MODE)
    fileContents = myfile.read()
    myfile.close()
    return fileContents

main()
