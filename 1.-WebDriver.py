from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r'D:\Documentos\Alex\chromedriver.exe')

driver.get('https://www.python.org/')

driver.get("http://eportal.mapama.gob.es/websiar/SeleccionParametrosMap.aspx?dst=1")
driver.implicitly_wait(5)
driver.maximize_window()
elem = Select(driver.find_element_by_name("ctl00$ContentPlaceHolder1$DropDownListCCAA"))
elem.select_by_visible_text("Castilla-La Mancha")
time.sleep(2)

elem = Select(driver.find_element_by_name("ctl00$ContentPlaceHolder1$DropDownListProvincia"))
elem.select_by_visible_text("Toledo")

elem = Select(driver.find_element_by_name("ctl00$ContentPlaceHolder1$DropDownListEstacion"))
elem.select_by_visible_text("Los Navalmorales")
time.sleep(1)
elem = driver.find_element_by_name("ctl00$ContentPlaceHolder1$ButtonAgregar")
elem.click()

elem = driver.find_element_by_name("ctl00$ContentPlaceHolder1$CheckBoxVViento")
elem.click()

elem = driver.find_element_by_name("ctl00$ContentPlaceHolder1$CheckBoxListParametros$CheckBoxListParametros_2")
elem.click()

elem = driver.find_element_by_name("ctl00$ContentPlaceHolder1$CheckBoxListParametros$CheckBoxListParametros_8")
elem.click()

elem = driver.find_element_by_name("ctl00$ContentPlaceHolder1$CheckBoxListParametros$CheckBoxListParametros_4")
elem.click()

elem = driver.find_element_by_name("ctl00$ContentPlaceHolder1$CheckBoxListParametros$CheckBoxListParametros_10")
elem.click()

elem = driver.find_element_by_name("ctl00$ContentPlaceHolder1$CheckBoxDViento")
elem.click()

elem = driver.find_element_by_name("ctl00$ContentPlaceHolder1$btnConsultar")
elem.click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
content = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ExportarCSV"]')
content.click()                               
time.sleep(3) #Tiempo prudencial para que descarge

driver.quit() # Si usamos “quit” cerramos todo el navegador, no solo la página actual

driver.close()