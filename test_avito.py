import unittest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import *
from time import sleep


class FavouritesFunctionalityTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def test_pop_up_screen_correct_text(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)

        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        wait = WebDriverWait(driver, 20)

        popup_element = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                   popup_xpath)))
        expected_text = "Добавлено в избранное"
        actual_text = popup_element.text
        driver.implicitly_wait(5)
        self.assertTrue(expected_text == actual_text,
                        f"Текст во всплывающем окне не соответствует ожидаемому. Ожидалось:"
                        f" '{expected_text}', получено: '{actual_text}'")

    def test_favs_screen_correct_behavior_after_click_on_advert_name(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        wait = WebDriverWait(driver, 20)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH,
                                                       popup_xpath))).click()

            advert_name_link = driver.find_element(By.XPATH,
                                                   advert_name_xpath).get_attribute("href")
            driver.implicitly_wait(5)
            self.assertTrue(advert_name_link == base_url,
                            f"Ссылка при нажатии на название обьявления в окне избранного не " \
                            f"совпадает со ссылкой на обьявление. Ожидалось {base_url},Получено {advert_name_link}")
        except TimeoutException:
            self.assertTrue(False)

    def test_favs_screen_correct_behavior_after_click_on_advert_image(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        wait = WebDriverWait(driver, 20)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH,
                                                       popup_xpath))).click()
            advert_image_link = driver.find_element(By.XPATH, advert_image_xpath).get_attribute(
                "href")
            right_link = base_url
            driver.implicitly_wait(5)
            self.assertTrue(advert_image_link == right_link,
                            f"Ссылка при нажатии на картинку обьявления в окне избранного не "
                            f"совпадает со ссылкой на обьявление. Ожидалось {base_url},Получено {advert_image_link}")
        except TimeoutException:
            self.assertTrue(False)

    def test_get_phone_pop_up_on_main_screen_correct_behavior(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)

        phone_button = driver.find_element(By.XPATH,
                                           get_phone_button)
        phone_button.click()
        wait = WebDriverWait(driver, 20)
        try:
            dialog = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='dialog']")))
            driver.implicitly_wait(5)
            self.assertTrue(dialog.is_displayed())
        except TimeoutException:
            self.assertTrue(False, f"При нажатии на кнопку \"Показать телефон\" всплывающее окно с авторизацией не "
                                   f"возникло")

    def test_pop_up_screen_correct_text_after_double_add(self):
        driver = self.driver

        driver.get(
            base_url)
        add_to_favourites = driver.find_element(By.XPATH,
                                                add_to_favourites_xpath)
        add_to_favourites.click()
        sleep(3)
        add_to_favourites.click()
        sleep(3)
        wait = WebDriverWait(driver, 20)
        try:
            popup_element = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                       popup_xpath)))
            driver.implicitly_wait(5)
            self.assertTrue(popup_element.text == "Удалено из избранного", f"{popup_element.text}")
        except TimeoutException:
            self.assertTrue(False, "TimeoutException")

    def test_pop_up_text_after_add_is_clickable(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)
        add_to_favourites = driver.find_element(By.XPATH,
                                                add_to_favourites_xpath)
        add_to_favourites.click()
        wait = WebDriverWait(driver, 5)

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, popup_xpath)))
            driver.implicitly_wait(5)
            self.assertTrue(True)
        except TimeoutException:
            self.assertTrue(False, TimeoutException)

    def test_pop_up_screen_created_after_click(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)
        add_to_favourites = driver.find_element(By.XPATH,
                                                add_to_favourites_xpath)
        add_to_favourites.click()
        wait = WebDriverWait(driver, 15)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH,
                                                       popup_xpath)))
            driver.implicitly_wait(5)
            self.assertTrue(True)
        except TimeoutException:
            self.assertTrue(False, "Timeout Exception")

    def test_pop_up_screen_not_created_without_click(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)
        wait = WebDriverWait(driver, 20)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH,
                                                       popup_xpath)))

            self.assertTrue(False, "Элемент о добавлении в избранное появился вопреки ожиданиям")
        except TimeoutException:
            driver.implicitly_wait(5)
            self.assertTrue(True)

    def test_favourites_button_text_changed_after_click(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)

        expected_text = "В избранном"
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        driver.implicitly_wait(5)
        self.assertTrue(expected_text != add_to_favourites_button.text,
                        "После нажатия на кнопку \"Добавить в избранное\" ее текст не изменился")

    def test_favourites_button_text_unchanged_after_double_click(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)

        expected_text = "Добавить в избранное"
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        sleep(3)
        add_to_favourites_button.click()
        sleep(3)
        self.assertTrue(expected_text == add_to_favourites_button.text, "После двойного нажатия на кнопку \"Добавить в "
                                                                        "избранное\" ее текст изменился,хотя должен "
                                                                        "быть неизменным")

    def test_go_to_favs_click(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        wait = WebDriverWait(driver, 20)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH,
                                                       popup_xpath))).click()
            driver.implicitly_wait(5)

            self.assertTrue(driver.current_url == favourites_url, "При нажатии на синюю часть кнопки \"Добавлено в "
                                                                  "избранное\" не осуществлен переход в избранное")
        except TimeoutException:
            self.assertTrue(False)

    def test_favs_does_not_contains_added_item_after_add(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        sleep(3)

        driver.get("https://www.avito.ru/favorites")
        self.assertTrue("Domain-Driven Design Distilled Vaughn Vernon" in driver.page_source, "При нажатии "
                                                                                              "на кнопку "
                                                                                              "\"Добавить в "
                                                                                              "избранное\" элемент "
                                                                                              "не добавился в "
                                                                                              "избранное")

    def test_favs_does_not_contains_added_item_after_double_add(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        sleep(3)
        add_to_favourites_button.click()
        sleep(3)
        driver.get("https://www.avito.ru/favorites")
        self.assertTrue("Domain-Driven Design Distilled Vaughn Vernon" not in driver.page_source, "При двойном нажатии "
                                                                                                  "на кнопку "
                                                                                                  "\"Добавить в "
                                                                                                  "избранное\" элемент "
                                                                                                  "добавился в "
                                                                                                  "избранное")

    def test_favs_does_not_contains_added_item_after_click_on_red_heart(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)
        add_to_favourites = driver.find_element(By.XPATH,
                                                add_to_favourites_xpath)
        add_to_favourites.click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   popup_xpath))).click()

        heart = wait.until(EC.presence_of_element_located((By.XPATH,
                                                           heart_xpath)))
        heart.click()
        driver.refresh()
        driver.implicitly_wait(5)
        self.assertTrue("Domain-Driven Design Distilled Vaughn Vernon" not in driver.page_source,
                        "При нажатии на красное сердце на странице избранного элемент остался в избранном при "
                        "перезагрузке странице")

    def test_red_heart_button_on_favs_screen_after_add_to_favs(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   popup_xpath))).click()

        heart = wait.until(EC.presence_of_element_located((By.XPATH,
                                                           heart_xpath)))
        driver.implicitly_wait(5)
        self.assertTrue(heart,
                        "При добавлении объявления в избранное на странице избранного не появилось красного сердца ")

    def test_correct_category_in_favs_screen_after_add(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)

        category = driver.find_element(By.XPATH,
                                       category_text_xpath)
        correct_text = category.text
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   popup_xpath))).click()

        category_of_favourites = driver.find_element(By.XPATH,
                                                     category_text_favourites_screen)
        driver.implicitly_wait(5)
        self.assertTrue(correct_text in category_of_favourites.text, "При добавлении в избранное на сранице избранного "
                                                                     "у объявления неверно отображается категория")

    def test_favs_correct_label_on_added_item(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)

        label_text = driver.find_element(By.XPATH, label_text_xpath).text
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   popup_xpath))).click()

        favourites_label_text = driver.find_element(By.XPATH, label_text_favourites_screen) \
            .text
        driver.implicitly_wait(5)
        self.assertTrue(label_text == favourites_label_text, "При добавлении в избранное на странице избранного "
                                                             "у объявления неверно отображается название ")

    def test_correct_city_on_added_item(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)

        label_text = driver.find_element(By.XPATH,
                                         adverts_city_text).text
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   popup_xpath))).click()

        favourites_label_text = driver.find_element(By.XPATH,
                                                    adverts_city_favourites_screen) \
            .text
        driver.implicitly_wait(5)
        self.assertTrue(label_text == favourites_label_text, "При добавлении в избранное на странице избранного "
                                                             "у объявления неверно отображается город ")

    def test_correct_price_on_added_item(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)

        label_text_amount_of_currency = driver.find_element(By.XPATH,
                                                            amount_of_currency_xpath).text.strip()

        label_text_name_of_currency = driver.find_element(By.XPATH,
                                                          name_of_currency_xpath).text.strip()
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   popup_xpath))).click()

        favourites_label_text_currency = driver.find_element(By.XPATH,
                                                             cost_of_adverts_favourites_screen_xpath) \
            .text
        driver.implicitly_wait(5)
        self.assertTrue(
            label_text_amount_of_currency + " " + label_text_name_of_currency == favourites_label_text_currency,
            "При добавлении в избранное на странице избранного "
            "у объявления неверно отображается цена ")

    def test_correct_date_of_advert_on_added_item(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)

        label_text = driver.find_element(By.XPATH,
                                         date_xpath).text.replace(
            "·", " ").lstrip()
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   popup_xpath))).click()

        favourites_label_text = driver.find_element(By.XPATH,
                                                    date_favourite_screen_xpath) \
            .text.replace(",", " в")
        driver.implicitly_wait(5)
        self.assertTrue(label_text in favourites_label_text, "При добавлении в избранное на странице избранного "
                                                             "у объявления неверно отображается дата публикации")

    def test_product_screen_favs_button_correct_text_after_click_on_red_heart_button_on_favs_screen(self):
        driver = self.driver
        sleep(3)
        driver.get(
            base_url)
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        add_to_favourites_button.click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   popup_xpath))).click()
        heart = driver.find_element(By.XPATH,
                                    heart_xpath)
        heart.click()
        sleep(5)
        driver.get(
            base_url)
        add_to_favourites_button = driver.find_element(By.XPATH,
                                                       add_to_favourites_xpath)
        expected_text = "Добавить в избранное"
        actual_text = add_to_favourites_button.text
        driver.implicitly_wait(5)
        self.assertTrue(expected_text == actual_text,
                        f"Текст во всплывающем окне не соответствует ожидаемому. Ожидалось:{expected_text}, получено: {actual_text}")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
