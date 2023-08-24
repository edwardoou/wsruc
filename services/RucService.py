import traceback
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Models
from models.RucModel import Ruc

def get_table(a,soup):
    tabla = soup.find_all('table')[a]
    rows = tabla.find_all('td')
    row = [' '.join(i.text.split()) for i in rows]
    return row

class RucService():

    @classmethod
    def get_dataruc(cls, ruc):
        try:
            # Configuración del navegador
            options = webdriver.ChromeOptions()
            options.page_load_strategy = 'eager'
            options.add_argument("start-maximized")
            options.add_argument("--disable-gpu")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
            options.add_argument("--headless=new") # Ejecutar en modo sin cabeza para no mostrar el navegador
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument('--disable-blink-features=AutomationControlled')
            driver = webdriver.Chrome(options=options)

            # Abre la página en el navegador
            driver.get("https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp")
            time.sleep(10)

            # Encuentra el campo de entrada y envía una solicitud
            driver.find_element(By.ID, 'txtRuc').send_keys(ruc)
            time.sleep(3)
            driver.find_element(By.ID,"btnAceptar").click()
            time.sleep(15)
            response = driver.page_source
            #obtiene el resultado
            soup = BeautifulSoup(response, "html.parser")
            html_lista = soup.find_all(class_='list-group-item-text')
            sunat_info = Ruc()
            lista_info = []

            for elemento in html_lista:
                texto = elemento.get_text(strip=True) # strip=True para eliminar espacios en blanco
                lista_info.append(texto)
            
            # RUC - Razon Social
            numero_ruc = soup.find_all(class_='list-group-item-heading')[1].contents[0]
            sunat_info.ruc = numero_ruc.split('-')[0].strip()
            sunat_info.razon_social = numero_ruc.split('-')[1].strip()
            # lista_info 
            sunat_info.tipo_contribuyente = lista_info[0]
            sunat_info.nombre_comercial = ' '.join(lista_info[1].split())
            sunat_info.fecha_inscripcion = lista_info[2]
            sunat_info.fecha_inicio = lista_info[3]
            sunat_info.estado_contibuyente = lista_info[4]
            sunat_info.condicion_contribuyente = lista_info[5]
            sunat_info.domicilio_fiscal = ' '.join(lista_info[6].split())
            sunat_info.sistema_emision_comprobante = lista_info[7]
            sunat_info.actividad_comercio_exterior = lista_info[8]
            sunat_info.sistema_contabilidad = lista_info[9]
            sunat_info.fecha_emisor_electronico = lista_info[10]
            sunat_info.comprobante_electronico = lista_info[11]
            sunat_info.afiliado_ple = lista_info[12]
            sunat_info.actividades_economicas = get_table(0,soup)
            sunat_info.comprobantes_pago = get_table(1,soup)
            sunat_info.sistema_emision_electronica = get_table(2,soup)
            sunat_info.padrones = get_table(3,soup)
            
            result = []
            result.append(sunat_info.to_json())
            return result
        except Exception as ex:
            print("error", str(ex))
            print("error", traceback.format_exc())
        finally:
            driver.quit()  # Cierra el navegador después de la consulta