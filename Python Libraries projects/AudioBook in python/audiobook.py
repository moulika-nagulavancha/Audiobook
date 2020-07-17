import pyttsx3
import PyPDF2
import webbrowser

book =open('Learn Microservices with Spring Boot.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
webbrowser.open_new(r'Learn Microservices with Spring Boot.pdf')


speaker = pyttsx3.init()
for num in range(1, pages):
	page = pdfReader.getPage(num)
	text = page.extractText()
	speaker.say(text)
	speaker.runAndWait()