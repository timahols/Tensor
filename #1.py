from driver import driver, wait, EC, By, pytest, Keys


class Finding:
    def __init__(self, driver):
        self.driver = driver

    def yandex(self):
        self.driver.get("https://ya.ru/")
        assert "Яндекс" in self.driver.title, "Ошибка: главная станица не найдена"

    def search(self, query):
        input = self.driver.find_element(By.ID, "text")
        assert input.is_displayed(), "Ошибка: поле ввода для поиска не найдена"
        input.send_keys(query)
        suggest = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.mini-suggest__item')))
        assert suggest.is_displayed(), "Ошибка: таблица с подсказками (suggest) не найдена"
        input.send_keys(Keys.ENTER)

    def page(self):
        search_result = self.driver.find_element(By.ID, "search-result")
        assert search_result, 'Ошибка: страница результатов поиска не загрузилась'
    def link(self):
        website_tensor = self.driver.find_element(By.ID, 'search-result').find_element(By.TAG_NAME, "a")
        assert 'https://tensor.ru/' in website_tensor.get_attribute('href'), 'Ошибка: 1 сайт не ведет на ' \
                                                                             'https://tensor.ru/ '
        print('Все ок')


def test_tesnor_search():
    browser = Finding(driver)
    browser.yandex()
    browser.search("Тензор")
    browser.link()
    driver.quit()


if __name__ == "__main__":
    pytest.main()
