from copy import copy
from struct import pack
from tokenize import String
import pyperclip
import pyshorteners
from tkinter import *
import validators

# GUI
root = Tk()
root.geometry("500x300")  # window size
root.title("URL Shortener ")  #  window title
root.configure(bg="#FFCCFF")  #  background color

# Define Variables for URL
urlmain = StringVar()
urlshortmain = StringVar()

# Define Function
def urlShortener():
    urladdress = urlmain.get()
    if not validators.url(urladdress):
        urlshortmain.set('Invalid URL')
    else:
        try:
            urlshort = shorten_url(urladdress)
            urlshortmain.set(urlshort)
        except Exception as e:
            urlshortmain.set('Error: ' + str(e))

def copyUrl():
    urlshort = urlshortmain.get()
    pyperclip.copy(urlshort)

def clearFields():
    urlmain.set('')
    urlshortmain.set('')

# Create the short URL
def shorten_url(original_url):
    shortener = get_shortener()  # Get the selected shortening service
    urlshort = shortener.short(original_url)
    return urlshort

# Get the selected shortening service
def get_shortener():
    selected_service = shortening_service.get()
    if selected_service == 'TinyURL':
        return pyshorteners.Shortener().tinyurl
    elif selected_service == 'Bit.ly':
        return pyshorteners.Shortener().bitly
    else:
        # Add more shortening services as needed
        return pyshorteners.Shortener().tinyurl

# GUI Components
Label(root, text="URL Shortener", font=('Arial', 16, 'bold')).pack(pady=10)
Entry(root, textvariable=urlmain, width=50, font=('Arial', 14)).pack(padx=10, pady=10)

# Shortening service selection
shortening_service = StringVar()
shortening_service.set('TinyURL')  # Default selection
Radiobutton(root, text="TinyURL", variable=shortening_service, value='TinyURL', font=('Arial', 12)).pack()
Radiobutton(root, text="Bit.ly", variable=shortening_service, value='Bit.ly', font=('Arial', 12)).pack()

Button(root, text="Generate Short URL", command=urlShortener, font=('Arial', 12)).pack(pady=7)
Entry(root, textvariable=urlshortmain, width=50, font=('Arial', 14)).pack(padx=10, pady=10)
Button(root, text="Copy Short URL", command=copyUrl, font=('Arial', 12)).pack(pady=5)
Button(root, text="Clear Fields", command=clearFields, font=('Arial', 12)).pack(pady=5)

root.mainloop()
