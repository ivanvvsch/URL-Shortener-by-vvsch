from tkinter import *
import pyshorteners
import pyperclip

window = Tk()
s = pyshorteners.Shortener()

window.geometry('540x540')
window.title("URL Shortener by VVSCH")
window.resizable(height = False, width = False)

label1 = Label(window, text = 'URL Shortener', font = ("Arial", 50))
label1.pack()

getLink = Entry(window, bg = 'grey')
getLink.pack()

def makeShortLink():
    shortLink = s.tinyurl.short(getLink.get())
    label2 = Label(window, text = shortLink, font = ("Arial", 20))
    label2.pack()
    label3 = Label(window, text = 'Ссылка скопирована!', font = ("Arial", 10))
    label3.pack()
    pyperclip.copy(shortLink)

btn1 = Button(window, bg = 'grey', text = 'Сократить ссылку', command = makeShortLink)
btn1.pack()

window.mainloop()
