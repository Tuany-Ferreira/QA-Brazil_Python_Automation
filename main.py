import data
import helpers

from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)

    def _start_comfort_caminho(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_set_route(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.get_from_location() == data.ADDRESS_FROM
        assert self.page.get_to_location() == data.ADDRESS_TO

    def test_select_plan(self):
        self._start_comfort_caminho()
        self.page.click_call_taxi()
        self.page.select_comfort()
        assert self.page.comfort_is_selected()

    def test_fill_phone_number(self):
        self._start_comfort_caminho()
        self.page.click_call_taxi()
        self.page.select_comfort()

        self.page.click_phone_button()
        self.page.fill_phone_number(data.PHONE_NUMBER)
        self.page.click_next_button()

        code = helpers.retrieve_phone_code(self.driver)

        self.page.fill_confirmation_code(code)
        self.page.click_confirm_button()

    def test_fill_card(self):
        self._start_comfort_caminho()

        self.page.click_call_taxi()
        self.page.select_comfort()

        self.page.click_payment_method()
        self.page.click_add_card()

        self.page.set_card_number(data.CARD_NUMBER)
        self.page.set_card_code(data.CARD_CODE)

        self.page.click_add_button()

    def test_comment_for_driver(self):
        self._start_comfort_caminho()

        self.page.click_call_taxi()
        self.page.select_comfort()

        self.page.click_payment_method()
        self.page.click_add_card()
        self.page.set_card_number(data.CARD_NUMBER)
        self.page.set_card_code(data.CARD_CODE)
        self.page.click_add_button()

        self.page.set_driver_comment(data.MESSAGE_FOR_DRIVER)

    def test_order_blanket_and_handkerchiefs(self):
        self._start_comfort_caminho()

        self.page.click_call_taxi()
        self.page.select_comfort()

        self.page.click_blanket_and_tissues()

        assert self.page.blanket_and_tissues_selected()

    def test_order_2_ice_creams(self):
        self._start_comfort_caminho()

        self.page.click_call_taxi()
        self.page.select_comfort()
        self.page.click_payment_method()
        self.page.click_add_card()
        self.page.set_card_number(data.CARD_NUMBER)
        self.page.set_card_code(data.CARD_CODE)
        self.page.click_add_button()
        self.page.close_payment_window()

        self.page.set_driver_comment(data.MESSAGE_FOR_DRIVER)

        self.page.click_blanket_and_tissues()

        for _ in range(2):
            self.page.click_ice_cream_plus()

        assert self.page.get_ice_cream_count() == "2"

    def test_car_search_model_appears(self):
        self._start_comfort_caminho()
        self.page.click_call_taxi()
        self.page.select_comfort()

        self.page.set_driver_comment(data.MESSAGE_FOR_DRIVER)
        self.page.click_order_button()

        assert self.page.car_search_modal_is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()