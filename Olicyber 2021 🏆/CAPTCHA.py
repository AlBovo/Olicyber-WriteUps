import bs4, requests,wget, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract

driver = webdriver.Firefox()
driver.get("http://captcha.challs.olicyber.it/")

while True:
	sito = "http://captcha.challs.olicyber.it"
	risposta = requests.get(sito).text
	#risposta.raise_for_status()
	zuppetta = BeautifulSoup(risposta, 'html.parser')
	for i in range(100):
		sas = zuppetta
		sis = wget.download(sas)

		pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
		image = Image.open(sis)

		numero = pytesseract.image_to_string(image, lang='eng')

		driver.find_element_by_name("risposta").send_keys(numero)
		driver.find_element_by_id("next").click()
		os.remove(sis)