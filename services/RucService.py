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
from helpers import sunatconstants

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
            #options.add_argument("--headless=new") # Ejecutar en modo sin cabeza para no mostrar el navegador
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

            sunat_info.tipo_contribuyente = lista_info[0]
            sunat_info.nombre_comercial = lista_info[1]
            sunat_info.fecha_inscripcion = lista_info[2]
            sunat_info.fecha_inicio = lista_info[3]
            sunat_info.estado_contibuyente = lista_info[4]
            sunat_info.condicion_contribuyente = lista_info[5]
            sunat_info.domicilio_fiscal = lista_info[6]
            sunat_info.actividad_economica = lista_info[7]
            #falta agregar los demas campos
            """ sunat_info.comprobantes = lista_info[8]
            sunat_info.sistema_emision = lista_info[9]
            sunat_info.fecha_emisor_electronico = lista_info[10]
            sunat_info.comprobante_electronico = lista_info[11]
            sunat_info.afiliado_ple = lista_info[12]
            sunat_info.padrones = lista_info[13] """

            # RUC - Razon Social
            numero_ruc = soup.find_all(class_='list-group-item-heading')[1].contents[0]
            sunat_info.ruc = numero_ruc.split('-')[0].strip()
            sunat_info.razon_social = numero_ruc.split('-')[1].strip()

            print(sunat_info)
            """ sunat_cons = None
            if ruc[0] == '1':
                # Verificar Nuevo RUS
                nuevo_rus = (lista_info[3].find_all("td"))[2].contents[0].strip()
                if nuevo_rus == 'Afecto al Nuevo RUS:':
                    sunat_cons = sunatconstants.PersonaNaturalNuevoRusConstant
            elif ruc[0] == '2':
                sunat_cons = sunatconstants.PersonaJuridicaConstant

            sunat_info.nombre_comercial = (table_info[sunat_cons.nombre_comercial.value].find_all("td"))[1].contents[0]
            sunat_info.fecha_inscripcion = (table_info[sunat_cons.fecha_inscripcion.value].find_all("td"))[1].contents[0]
            sunat_info.estado_contibuyente = (table_info[sunat_cons.estado_contribuyente.value].find_all("td"))[1].contents[0]
            sunat_info.condicion_contribuyente \
                = (table_info[sunat_cons.condicion_contribuyente.value].find_all("td"))[1].contents[0].replace('\r', '') \
                .replace('\n', '').strip()

            # Domicilio Fiscal
            domicilio = (table_info[sunat_cons.domicilio_fiscal.value].find_all("td"))[1].contents[0]
            sunat_info.domicilio_fiscal = ' '.join(domicilio.split())

            # Actividad Económica
            act_ec_td = ((table_info[sunat_cons.actividad_economica.value].find_all("td"))[1])
            sunat_info.actividad_economica = act_ec_td.find('select').find('option').contents[0] """
            result = []
            result.append(sunat_info.to_json())
            return result
        except Exception as ex:
            print("error", str(ex))
            print("error", traceback.format_exc())
        finally:
            driver.quit()  # Cierra el navegador después de la consulta