from tkinter import *

#partie logique
hash = ["000", "001", "002", "003", "004", "005", "006", "007", "008", "009", "101", "202", "303",
        "404", "505", "606", "707", "808", "909", "145", "256", "678", "986", "456", "888", "090"]

hash_number = ["0b", "9t", "8u", "7y", "6a", "5h", "4l", "3w", "2p", "1o"]

number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

special = [".", "'", ";", "/", ":", "!", "§", "?", ",", "<", ">", "ù",
           "%", "*", "µ", "$", "£", "^", "¨", "=", "+", ")", "°", "}", "]",
           "à", "@", "ç", "^", "_", "\\", "è", "`", "-", "|", "(", "[", "{",
           '"', "#", "é", "~", "&", "€", ]


def hashage():
    word = inputWord.get()
    wordHashList = []
    wordChain = list(word.lower())
    print(wordChain)
    for letter in wordChain:
        try:
            int(letter)
            wordHashList.append(hash_number[number.index(letter)])
        except:
            if letter in special:
                wordHashList.append(special[special.index(letter) - 1])
            elif letter == " ":
                pass
            else:
                wordHashList.append(hash[alphabet.index(letter)])
    print(wordHashList)
    outputWord.delete(0, END)
    outputWord.insert(0, "".join(wordHashList))



def center_window(w=300, h=200):
    # get screen width and height
    ws = master.winfo_screenwidth()
    hs = master.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    master.geometry('%dx%d+%d+%d' % (w, h, x, y))


# creation de la fenetre
bgColor = '#ffffff'
master = Tk()
center_window(600, 400)
# personalisation de master
master.title("Crypto Word")
master.resizable(width=0, height=0)
master.iconbitmap("14080.ico")
master.config(background=bgColor)

# ajout de composant

# ajout de frame

titleFrame = Frame(master, bg=bgColor)


# title text

textTitle = Label(titleFrame, text='Bienvenue sur Crypto Word.', font=('Helvetica', 20), bg=bgColor)
textTitle.grid(row=0)

# subtitle text
textSubTitle = Label(titleFrame, text='Cryptage de mot basique.', font=('Helvetica', 15), bg=bgColor)
textSubTitle.grid(row=1)
titleFrame.pack(pady=10)

# input word
input = ""
inputWord = Entry(master, font=('Helvetica', 15), bg='#d6d6d6', textvariable=input)

enterHere = Label(master, text='Entrer un mot ici :', font=('Helvetica', 15)).pack(after=titleFrame)
inputWord.pack(after=enterHere)
# output word
outHere = Label(master, text='Voici un cryptage basique:', font=('Helvetica', 15))
outputWord = Entry(master, font=('Helvetica', 15), bg='#d6d6d6', width=50)

# crypt button
cryptButton = Button(master, text='Chifrer', font=('Helvetica', 15), bg=bgColor, command=hashage)
cryptButton.pack(after=inputWord, pady=10)
outHere.pack(after=cryptButton)
outputWord.pack(after=outHere)

# Version text
versionText = Label(text='V1.0', bg=bgColor).place(x=-1)
# Credits Text
creditText = Label(text='Made By\nLycode', font=('Helvetica', 10), bg=bgColor).place(x=-1, y=16)

# affichage fenetre

master.mainloop()