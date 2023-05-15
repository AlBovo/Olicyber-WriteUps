import bs4, requests, re
from selenium import webdriver 
# il seguente codice potrebbe dare errori se la versione non è corretta
# potrebbe essere necessario riscrivere parte del codice

driver = webdriver.Firefox()
driver.get("http://infinite.challs.olicyber.it/")

while True:
	sito = "http://infinite.challs.olicyber.it/"
	risposta = requests.get(sito)
	#risposta.raise_for_status()
	zuppetta = bs4.BeautifulSoup(driver.page_source, 'html.parser')
	s, x, tempnum, su = 0, 0, 0, 0
	lettera, testosu, testolet = '', '', ''
	testo = ['']
	sfida = zuppetta.find('h2').text.strip()
	domanda = zuppetta.find('p').text.strip()

	if 'MATH TEST' in sfida:
		s = [int(s) for s in re.findall(r'-?\d+\.?\d*', domanda)]
		su = sum(s)

		driver.find_element_by_id("sum").send_keys(str(su));
		driver.find_element_by_css_selector("input[type='submit']").click()

	elif 'ART TEST' in sfida:
		testo = re.split(r'\s', domanda)
		for element in testo:
			if element.__contains__('Verde'):
				lettera = 'Verde'
				break
			elif element.__contains__('Rosso'): 
				lettera = 'Rosso'
				break
			elif element.__contains__('Blu'):
				lettera = 'Blu'
				break
		print(lettera)
		driver.find_element_by_id(lettera).click()		

	elif 'GRAMMAR TEST' in sfida:
		testo = re.split(r'\s', domanda)
		for element in testo:
			if element.__contains__('"') and su == 0:
				lettera = str(element)
				su += 1
			elif element.__contains__('"') and su != 0:
				testosu = element
		su = 0
		for word in testosu:
			if lettera.__contains__(word) and word != '"':
				su += 1
		driver.find_element_by_id("letter").send_keys(str(su))
		driver.find_element_by_name("submit").click()
	else:
		#flag
		print(sfida)
		break
	tempnum, su, s = 0, 0, 0