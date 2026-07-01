from html.parser import commentclose

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

      #numero de telefone
      phone_button = (By.CLASS_NAME, "np-button")
      phone_input = (By.ID, "phone")
      next_button = (
          By.XPATH,
          "//button[contains(@class,'button') and contains(., 'Próximo')]"
      )

      # Código SMS
      code_input = (By.ID, "code")
      confirm_button = (
          By.XPATH,
          "//button[contains(@class,'button') and contains(., 'Confirmar')]"
      )


      # Inserir cartão de crédito

      payment_method = (
          By.CLASS_NAME,
          "pp-text"
      )
      add_card = (
          By.XPATH,
          "//div[text()='Adicionar cartão']"
      )
      card_number = (
          By.CSS_SELECTOR,
          "input.card-input#number"
      )
      card_code = (
          By.XPATH,
          "//div[contains(@class,'card-code-input')]//input"
      )
      add_card_button = (
          By.XPATH,
          "//button[text()='Adicionar']"
      )
      payment_close_button = (
          By.CSS_SELECTOR,
          ".payment-picker.open .section.active .section-close"
      )

      # Comentário para o motorista
      comment_input = (By.ID, "comment")

      # Cobertor e lenços
      blanket_switch = (
          By.XPATH,
          "//div[@class='r-sw-container']//span[@class='slider round']"
      )

      blanket_checkbox = (
          By.XPATH,
          "//div[@class='r-sw-container']//input[@type='checkbox']"
      )


      # Sorvete
      ice_cream_plus = (
          By.XPATH,
          "(//div[contains(@class,'counter-plus')])[1]"
      )

      ice_cream_count = (
          By.XPATH,
          "(//div[contains(@class,'counter-value')])[1]"
      )

      # Pedir o táxi

      order_button = (
          By.CLASS_NAME,
          "smart-button"
      )

      car_search_modal = (
          By.CLASS_NAME,
          "order"
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
          self._click(self.comfort_button)

      def comfort_is_selected(self):
          comfort = self._find(self.comfort_button)
          return "active" in comfort.get_attribute("class")

      #colocar numero de telefone

      def click_phone_button(self):
          self._click(self.phone_button)

      def fill_phone_number(self, phone_number):
          self._type(self.phone_input, phone_number)

      def click_next_button(self):
          self._click(self.next_button)

      def fill_confirmation_code(self, code):
          self._type(self.code_input, code)

      def click_confirm_button(self):
          self._click(self.confirm_button)

          #cartão

      def click_payment_method(self):
          self._click(self.payment_method)

      def click_add_card(self):
          self._click(self.add_card)

      def set_card_number(self, number):
          self._type(self.card_number, number)

      def set_card_code(self, code):
          element = self.wait.until(
              EC.visibility_of_element_located(self.card_code)
          )
          element.clear()
          element.send_keys(code)
          element.send_keys(Keys.TAB)

      def click_add_button(self):
          self.wait.until(
              EC.element_to_be_clickable(self.add_card_button)
          ).click()

      def close_payment_window(self):
          self._click(self.payment_close_button)

          #menssagem motorista

      def set_driver_comment(self, comment):
          self._type(self.comment_input, comment)

          # cobertor e lenços

      def click_blanket_and_tissues(self):
          element = self.wait.until(
              EC.element_to_be_clickable(self.blanket_switch)
          )

          self.driver.execute_script(
              "arguments[0].scrollIntoView({block:'center'});",
              element
          )

          element.click()

      def blanket_and_tissues_selected(self):
          checkbox = self.wait.until(
              EC.presence_of_element_located(self.blanket_checkbox)
          )
          return checkbox.is_selected()

          # Pedir sorvetes

      def click_ice_cream_plus(self):
              self._click(self.ice_cream_plus)

      def get_ice_cream_count(self):
              return self._find(self.ice_cream_count).text

              # Pedir um táxi com a tarifa "Comfort"

      def click_order_button(self):
            self._click(self.order_button)

      def car_search_modal_is_displayed(self):
            return self._find(self.car_search_modal).is_displayed()