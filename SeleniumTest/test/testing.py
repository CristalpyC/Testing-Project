from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
os.system('cls')

def main():
    pagina = Testing()

    # Usos
    pagina.test_Config('https://www.palaciodelcine.com.do/#')
    pagina.test_seleccionar_sucursal('Agora Mall')
    pagina.test_buscar_pelicula('SHAZAM (2D) ESP')
    pagina.test_login('cristaltn03@gmail.com', 'Cristal1234')
    pagina.test_menu()
    pagina.test_generos()
    pagina.test_promos()
    pagina.test_eventos()
    pagina.test_contacto()
    pagina.test_HomePage()
    pagina.test_SucursalCheck("SUPER MARIO BROS (2D) ESP")
    pagina.test_compra("1")
    pagina.test_pago("000")

    # Cierre
    pagina.Quit()

class Testing():
    def test_Config(self, url):
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_busqueda.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)
        self.waiting = WebDriverWait(self.driver, 25)
        
    def Quit(self):
        self.driver.quit()
    
    def test_buscar_pelicula(self, nombre_pelicula):
        self.waiting.until(EC.presence_of_element_located((By.NAME, "lastname")))
        movie_click = self.driver.find_element(By.NAME, "lastname")
        movie_click.send_keys(nombre_pelicula)
        search_click = self.driver.find_element(By.XPATH, "//input[@value='BUSCAR']")
        search_click.click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_busqueda.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)
        self.waiting.until(EC.presence_of_element_located((By.XPATH, "//input[@value='BUSCAR']")))

    def test_seleccionar_sucursal(self, nombre_sucursal):
        self.waiting.until(EC.presence_of_element_located((By.NAME, "firstname")))
        sucursal_click = self.driver.find_element(By.NAME, "firstname")
        sucursal_click.click()
     
        place_click = self.driver.find_element(By.XPATH, f"//option[text()='{nombre_sucursal}']")
        place_click.click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_sucursal.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)
   

    def test_login(self, nombre, passwd):
        self.waiting.until(EC.presence_of_element_located((By.ID, "ctl00_topNavIngreso")))
        LoginClick = self.driver.find_element(By.ID, "ctl00_topNavIngreso")
        LoginClick.click() 

        self.waiting.until(EC.presence_of_element_located((By.ID,"inpLogId")))
        EmailClick = self.driver.find_element(By.ID, "inpLogId")
        EmailClick.send_keys(nombre)

        self.waiting.until(EC.presence_of_element_located((By.ID, "inpLogPass")))
        PasswdClick = self.driver.find_element(By.ID, "inpLogPass")
        PasswdClick.send_keys(passwd)

        self.waiting.until(EC.presence_of_element_located((By.ID, "remember-me")))
        CheckClick = self.driver.find_element(By.ID, "remember-me").click()

        self.waiting.until(EC.presence_of_element_located((By.XPATH, "//input[@class='full-width' and @type='button' and @value='Ingresar Usuario']")))
        LoginButton = self.driver.find_element(By.XPATH, "//input[@class='full-width' and @type='button' and @value='Ingresar Usuario']")
        LoginButton.click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_login.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

    def test_menu(self):
        # EN CASO DE QUE NO FUNCIONE EL <<SELF.WAITING>> EN ESTA PARTE, <<HACER>> LO SIGUIENTE:
        #--self.waiting.until(EC.visibility_of_element_located((By.ID, "popUserLogin")))
        #--self.waiting.until(EC.invisibility_of_element_located((By.ID, "popUserLogin")))
        self.waiting.until(EC.presence_of_element_located((By.ID, "cd-menu-trigger")))
        MenuClick = self.driver.find_element(By.ID, "cd-menu-trigger").click() 

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_menu.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        TrailersClickW = self.waiting.until(EC.presence_of_element_located((By.CLASS_NAME,"item-has-children")))
        TrailersClick = self.driver.find_element(By.CLASS_NAME, "item-has-children").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_MenuOption1.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        self.waiting.until(EC.presence_of_element_located((By.ID,"Semana_308")))
        TClicks = self.driver.find_element(By.ID, "Semana_308").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_SucursalCheck.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)


    def test_generos(self):
        self.waiting.until(EC.presence_of_element_located((By.ID,"Genero_7")))
        GeneroClick = self.driver.find_element(By.ID, "Genero_7").click()
        time.sleep(1) 

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_Genero.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        self.waiting.until(EC.presence_of_element_located((By.ID,"Genero_3")))
        GeneroClick2 = self.driver.find_element(By.ID, "Genero_3").click()

        self.waiting.until(EC.presence_of_element_located((By.ID,"Genero_4")))
        GeneroClick3 = self.driver.find_element(By.ID, "Genero_4").click()

        self.waiting.until(EC.presence_of_element_located((By.ID,"Genero_1")))
        GeneroClick4 = self.driver.find_element(By.ID, "Genero_1").click() 

        self.waiting.until(EC.presence_of_element_located((By.ID,"Genero_8")))
        GeneroClick6 = self.driver.find_element(By.ID, "Genero_8").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_Genero2.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        self.waiting.until(EC.presence_of_element_located((By.CLASS_NAME,"botoncomplejosemana")))
        HorarioClick = self.driver.find_element(By.CLASS_NAME, "botoncomplejosemana").click()

        time.sleep(1)
        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_Horario.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)
    
    def test_promos(self):
        self.waiting.until(EC.presence_of_element_located((By.ID,"cd-menu-trigger")))
        MenuClick2 = self.driver.find_element(By.ID, "cd-menu-trigger").click()
       

        self.waiting.until(EC.presence_of_element_located((By.ID,"Seccion_11")))
        PromoClick = self.driver.find_element(By.ID, "Seccion_11").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_busquedaPromo.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

    def test_eventos(self):
        self.waiting.until(EC.presence_of_element_located((By.ID,"cd-menu-trigger")))
        MenuClick3 = self.driver.find_element(By.ID, "cd-menu-trigger").click()

        self.waiting.until(EC.presence_of_element_located((By.ID,"Seccion_25")))
        EventosClick = self.driver.find_element(By.ID, "Seccion_25").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_busquedaEventos.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

    def test_contacto(self):
        self.waiting.until(EC.presence_of_element_located((By.ID,"cd-menu-trigger")))
        MenuClick = self.driver.find_element(By.ID, "cd-menu-trigger").click()

        self.waiting.until(EC.presence_of_element_located((By.ID,"Contacto")))
        ContactoClick = self.driver.find_element(By.ID, "Contacto").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_busquedaContacto.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

    def test_HomePage(self):
        self.waiting.until(EC.presence_of_element_located((By.ID,"cd-logo")))
        LogoClick = self.driver.find_element(By.ID, "cd-logo").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_Homepage.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

    def test_SucursalCheck(self, pelicula):
        self.waiting.until(EC.presence_of_element_located((By.NAME,"firstname")))
        SucursalClick = self.driver.find_element(By.NAME, "firstname").click()

        self.waiting.until(EC.presence_of_element_located((By.XPATH,"//option[@value='308']")))
        PlaceClick = self.driver.find_element(By.XPATH, "//option[@value='308']").click()

        self.waiting.until(EC.presence_of_element_located((By.NAME,"lastname")))
        MovieClick = self.driver.find_element(By.NAME, "lastname")
        MovieClick.send_keys(pelicula)
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_busquedaPelicula.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        self.waiting.until(EC.presence_of_element_located((By.XPATH,"//input[@value='BUSCAR']")))
        SearchClick = self.driver.find_element(By.XPATH, "//input[@value='BUSCAR']").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_busquedaInfo.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

    def test_compra(self, CantButacas):
        # OJO: La página suele actualizar las fechas.
        self.waiting.until(EC.presence_of_element_located((By.ID,"ticket")))
        TicketsClick = self.driver.find_element(By.ID, "ticket").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_tickets.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        self.waiting.until(EC.presence_of_element_located((By.XPATH,"//input[@name='cartSchedule' and @value='80764']")))
        SelectCalendarClick = self.driver.find_element(By.XPATH, "//input[@name='cartSchedule' and @value='80764']").click() 
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_calendario.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        self.waiting.until(EC.presence_of_element_located((By.ID,"inpSiguienteCarrito")))
        NextCartClick = self.driver.find_element(By.ID, "inpSiguienteCarrito").click() 
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_Snacks.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        self.waiting.until(EC.presence_of_element_located((By.CLASS_NAME,"CboPrecios")))
        ButacasClick = self.driver.find_element(By.CLASS_NAME, "CboPrecios")
        ButacasClick.send_keys(CantButacas)
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_busquedaAsientos.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        self.waiting.until(EC.presence_of_element_located((By.ID,"inpAgregarAlCarrito")))
        CarritoNextClick = self.driver.find_element(By.ID, "inpAgregarAlCarrito").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_AgregarAsiento.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        self.waiting.until(EC.presence_of_element_located((By.XPATH,"//input[@id='inpAgregarAlCarrito' and @onclick='goToCartStep(4)']")))
        CarritoNextClick2 = self.driver.find_element(By.XPATH, "//input[@id='inpAgregarAlCarrito' and @onclick='goToCartStep(4)']").click()
        time.sleep(2)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_SiguientePago.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

    def test_pago(self, codigo):
        self.waiting.until(EC.presence_of_element_located((By.ID,"DropDownCreditCards")))
        TarjetaClick = self.driver.find_element(By.ID, "DropDownCreditCards").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_busquedaPagoTarjeta.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        self.waiting.until(EC.presence_of_element_located((By.CLASS_NAME,"wizardInput")))
        NTarjetClick = self.driver.find_element(By.CLASS_NAME, "wizardInput")
        NTarjetClick.send_keys(codigo) 
        time.sleep(1)
        
        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_IdTarjeta.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)

        self.waiting.until(EC.presence_of_element_located((By.ID,"checkTermsConds")))
        CheckTermsClick = self.driver.find_element(By.ID, "checkTermsConds").click()
        time.sleep(1)

        # CAPTURA
        carpeta = r"C:\\Users\\DELL\\OneDrive\\Escritorio\\ITLA cuatrimestres\\Quinto cuatrimestre\\Prog. III\SeleniumTest\\capturas"
        archivo = "Cap_Terminos.png"
        ruta = carpeta + "/" + archivo
        self.driver.save_screenshot(ruta)
        
if __name__ == "__main__":
    main()
    

