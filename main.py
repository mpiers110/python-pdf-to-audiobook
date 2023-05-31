import pyttsx3
import PyPDF2

bookname = 'oop.pdf' #name of book
book = open(bookname, 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = pdfReader.pages

#print out the number of pages
print(pages) 

#initialise the pyttsx3 library
speaker = pyttsx3.init() 

#loop thtrough the book for text
for num in range(7, len(pages)): #choose from which page the reader should start from in this case from page 7
    page = pdfReader.pages[7]
    text = page.extract_text() #extract all text from the pages
    speaker.say(text) #say out loud the text that has been extracted
    speaker.runAndWait()