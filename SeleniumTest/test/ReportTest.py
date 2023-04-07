#----------------------------------------------- REPORTE HTML ------------------------------
from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
os.system('cls')

def main():
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reporte'))

class Testing(unittest.TestCase):
    def setUp(cls):
        cls.driver = webdriver.Firefox()

    def test_01_busqueda(self):
        self.driver.get('https://www.palaciodelcine.com.do/#')
        time.sleep(1)
    
    def test_02_buscar_pelicula(self):
        self.driver.get('https://www.palaciodelcine.com.do/#')
        movie_click = self.driver.find_element(By.NAME, "lastname")
        movie_click.send_keys('SHAZAM (2D) ESP')

        search_click = self.driver.find_element(By.XPATH, "//input[@value='BUSCAR']")
        search_click.click()

    def test_03_seleccionar_sucursal(self):
        self.driver.get('https://www.palaciodelcine.com.do/#')
        sucursal_click = self.driver.find_element(By.NAME, "firstname")
        sucursal_click.click()
      
        place_click = self.driver.find_element(By.XPATH, f"//option[text()='Agora Mall']")
        place_click.click()
        time.sleep(1)

    def test_04_login(self):
        self.driver.get('https://www.palaciodelcine.com.do/#')
        LoginClick = self.driver.find_element(By.ID, "ctl00_topNavIngreso")
        LoginClick.click() 
        time.sleep(1)

        EmailClick = self.driver.find_element(By.ID, "inpLogId")
        EmailClick.send_keys('cristaltn03@gmail.com')
        PasswdClick = self.driver.find_element(By.ID, "inpLogPass")
        PasswdClick.send_keys('Cristal1234')
        time.sleep(1)

        CheckClick = self.driver.find_element(By.ID, "remember-me").click()

        LoginButton = self.driver.find_element(By.XPATH, "//input[@class='full-width' and @type='button' and @value='Ingresar Usuario']")
        LoginButton.click()
        time.sleep(1)

    def test_05_menu(self):
        self.driver.get('https://www.palaciodelcine.com.do/#')
        MenuClick = self.driver.find_element(By.ID, "cd-menu-trigger").click() 
        time.sleep(1)

        TrailersClick = self.driver.find_element(By.CLASS_NAME, "item-has-children").click()
        time.sleep(1)

        TClicks = self.driver.find_element(By.ID, "Semana_308").click()
        time.sleep(1)

        GeneroClick = self.driver.find_element(By.ID, "Genero_7").click()
        time.sleep(1)

        GeneroClick2 = self.driver.find_element(By.ID, "Genero_3").click()
        time.sleep(1)

        GeneroClick3 = self.driver.find_element(By.ID, "Genero_4").click()
        time.sleep(1)

        GeneroClick4 = self.driver.find_element(By.ID, "Genero_1").click()
        time.sleep(1)   
      
        GeneroClick6 = self.driver.find_element(By.ID, "Genero_8").click()
        time.sleep(1)
     
        HorarioClick = self.driver.find_element(By.CLASS_NAME, "botoncomplejosemana").click()
        time.sleep(1)
    
    def test_06_promos(self):
        self.driver.get('https://www.palaciodelcine.com.do/#')
        MenuClick2 = self.driver.find_element(By.ID, "cd-menu-trigger").click()
        time.sleep(1)

        PromoClick = self.driver.find_element(By.ID, "Seccion_11").click()
        time.sleep(1)

    def test_07_eventos(self):
        self.driver.get('https://www.palaciodelcine.com.do/#')
        MenuClick3 = self.driver.find_element(By.ID, "cd-menu-trigger").click()
        time.sleep(1)

        EventosClick = self.driver.find_element(By.ID, "Seccion_25").click()
        time.sleep(1)

    def test_08_contacto(self):
        self.driver.get('https://www.palaciodelcine.com.do/#')
        MenuClick = self.driver.find_element(By.ID, "cd-menu-trigger").click()
        time.sleep(1)

        ContactoClick = self.driver.find_element(By.ID, "Contacto").click()
        time.sleep(1)
        time.sleep(1)

    def test_09_HomePage(self):
        self.driver.get('https://www.palaciodelcine.com.do/#')
        LogoClick = self.driver.find_element(By.ID, "cd-logo").click()
        time.sleep(1)

    def test_10_SucursalCheck(self):
        self.driver.get('https://www.palaciodelcine.com.do/#')
        
        # Primero hay que iniciar sesión para tener acceso a este método de pago
        self.driver.get('https://www.palaciodelcine.com.do/#')
        LoginClick = self.driver.find_element(By.ID, "ctl00_topNavIngreso")
        LoginClick.click() 
        time.sleep(1)

        EmailClick = self.driver.find_element(By.ID, "inpLogId")
        EmailClick.send_keys('cristaltn03@gmail.com')
        PasswdClick = self.driver.find_element(By.ID, "inpLogPass")
        PasswdClick.send_keys('Cristal1234')
        time.sleep(1)

        CheckClick = self.driver.find_element(By.ID, "remember-me").click()

        LoginButton = self.driver.find_element(By.XPATH, "//input[@class='full-width' and @type='button' and @value='Ingresar Usuario']")
        LoginButton.click()
        time.sleep(1)
        
        SucursalClick = self.driver.find_element(By.NAME, "firstname").click()
        time.sleep(1)

        PlaceClick = self.driver.find_element(By.XPATH, "//option[@value='308']").click()
        time.sleep(1)

        MovieClick = self.driver.find_element(By.NAME, "lastname")
        time.sleep(1)

        MovieClick.send_keys("SUPER MARIO BROS (2D) SUB")
        time.sleep(1)

        SearchClick = self.driver.find_element(By.XPATH, "//input[@value='BUSCAR']").click()
        time.sleep(1)

        TicketsClick = self.driver.find_element(By.ID, "ticket").click()
        time.sleep(1)

        SelectCalendarClick = self.driver.find_element(By.XPATH, "//input[@name='cartSchedule' and @value='81137']").click() 
        time.sleep(1)

        NextCartClick = self.driver.find_element(By.ID, "inpSiguienteCarrito").click() 
        time.sleep(1)

        ButacasClick = self.driver.find_element(By.CLASS_NAME, "CboPrecios")
        time.sleep(1)

        ButacasClick.send_keys("1")
        time.sleep(1)

        CarritoNextClick = self.driver.find_element(By.ID, "inpAgregarAlCarrito").click()
        time.sleep(1)

        CarritoNextClick2 = self.driver.find_element(By.XPATH, "//input[@id='inpAgregarAlCarrito' and @onclick='goToCartStep(4)']").click()
        time.sleep(1)

        TarjetaClick = self.driver.find_element(By.ID, "DropDownCreditCards").click()
        time.sleep(1)

        NTarjetClick = self.driver.find_element(By.CLASS_NAME, "wizardInput")
        time.sleep(1)
   
        NTarjetClick.send_keys("000") 
        time.sleep(1)

        CheckTermsClick = self.driver.find_element(By.ID, "checkTermsConds").click()
        time.sleep(1)

    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    main()