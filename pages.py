from html.parser import commentclose

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class UrbanRoutesPage:

      # Seção De e Para
      from_field = (By.ID, 'from')
      to_field = (By.ID, 'to')

      # Fluxo de chamada de taxi

      call_taxi_button = (
          By.XPATH,
          "//button[contains(text(),'Chamar um táxi')]"
      )

      comfort_button = (
          By.XPATH,
          "//div[text()='Comfort']/ancestor::div[contains(@class,'tcard')]"
      )

      def __init__(self, driver):
          self.driver = driver
          self.wait = WebDriverWait(driver, 10)

          # Metodos COR POM

      def _find(self, locator):
          return self.wait.until(
              EC.visibility_of_element_located(locator)
          )

      def _click(self, locator):
          self.wait.until(
              EC.element_to_be_clickable(locator)
          ).click()

      def _type(self, locator, text):
          element = self._find(locator)
          element.clear()
          element.send_keys(text)

          #Endereço

      def _get_text(self, locator):
          return self._find(locator).text

      def _get_value(self, locator):
          return self._find(locator).get_attribute('value')


      def enter_locations(self, from_text, to_text):
          self._type(self.from_field, from_text)
          self._type(self.to_field, to_text)

      def get_from_location(self):
          return self._get_value(self.from_field)

      def get_to_location(self):
          return self._get_value(self.to_field)

         #Chamar táxi

      def click_call_taxi(self):
          self._click(self.call_taxi_button)

      def select_comfort(self):
          comfort = self._find(self.comfort_button)
          if "active" not in comfort.get_attribute("class"):
              comfort.click()

      def comfort_is_selected(self):
          comfort = self._find(self.comfort_button)
          return "active" in comfort.get_attribute("class")