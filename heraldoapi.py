from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from robobrowser import RoboBrowser
import json
import time
class HeraldoApi:

    def __init__(self, mode="parser"):
        """ Modes: 
        parser -> Only start the parser elements (RoboBrowser)
        writer -> Only start the writing elemnts (Selenium)
        join -> Starts whole system (RoboBrowser and Selenium)"""
        if mode == "parser":
            self.start_parser()
        elif mode == "writer":
            self.start_writer()
        elif mode == "join":
            self.start_parser()
            self.start_writer()

    def start_parser(self):
        self.browser = RoboBrowser(history=True, parser = 'html.parser')
        
    def start_writer(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def parse_section(self, section = "aragon"):
        self.browser.open("http://www.heraldo.es/noticias/{}/portada/".format(section))
        scripts = self.browser.find_all("script",type="text/javascript")

        for script in scripts:
            
            if "trackPaginaAJAX(numeroPagina)" in script.text:
                for line in script.text.split("\n"):
                    if "var atributos" in line:
                        data = json.loads(line.strip()[16:-1])
        print(data)
        self.browser.open("http://www.heraldo.es/ajax.php", method = "post", data=data)
        print(self.browser.parsed)        
        for link in self.browser.find_all("a"):
            print(link.text)
    
    def register_account(self, user, password, email):
        self.driver.get("http://www.heraldo.es/")
        time.sleep(8)
        self.driver.find_element_by_id("toggl_capa_perfil").click()
        time.sleep(8)
        self.driver.find_element_by_css_selector("a.registerGigya.trk_menuSuperiorscroll").click()
        time.sleep(8)
        email_field = self.driver.find_element_by_name("email")
        email_field.clear()
        email_field.send_keys(email)
        user_field = self.driver.find_element_by_name("profile.firstName")
        user_field.clear()
        user_field.send_keys(user)
        password_field = self.driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys(password)
        password_retype = self.driver.find_element_by_name("passwordRetype")
        password_retype.clear()
        password_retype.send_keys(password)
        checkbox = self.driver.find_element_by_name("data.terms")
        checkbox.click()
        self.driver.find_element_by_css_selector("input.gigya-input-submit").click()
        time.sleep(8)
        self.driver.get(self.verification_link(email))
        time.sleep(30)
        return True


    def verification_link(self, email):
        mails = []
        self.browser.open("http://www.yopmail.com/es/inbox.php?login={}&p=1&d=&ctrl=&scrl=&spam=true&yf=005&yp=PBGH1AwtkBGLmZQV0AGZmZj&yj=DAwZ0AQD0AQR0BGt4AwD1AD&v=2.7&r_c=&id=".format(email))
        elements = self.browser.find_all("a",{"class":"lm"})
        for element in elements:
            if "Heraldo" in element.text:
                mails.append(element["href"])

        for mail in mails:
            self.browser.open("http://www.yopmail.com/es/{}".format(mail))
            activation_link = self.browser.find("a",{"rel":"nofollow"})["href"]

        return activation_link





    def __del__(self):
        try:
            self.driver.close()
        except:
            pass



