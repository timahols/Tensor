from driver import driver, wait, EC, By, pytest, Keys


class Finding:
    def __init__(self, driver):
        self.driver = driver

    def yandex(self):
        self.driver.get("https://ya.ru/")
        assert "Яндекс" in self.driver.title

    def search(self, query):
        input = self.driver.find_element(By.ID, "text")
        assert input.is_displayed()
        input.send_keys(query)
        suggest = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.mini-suggest__item')))
        assert suggest.is_displayed()
        input.send_keys(Keys.ENTER)

    def link(self):
        website_tensor = self.driver.find_element(By.ID, 'search-result').find_element(By.TAG_NAME, "a")
        assert 'https://tensor.ru/' in website_tensor.get_attribute('href')
        print('Все ок')


def test_tesnor_search():
    page = Finding(driver)
    page.yandex()
    page.search("Тензор")
    page.link()
    driver.quit()


if __name__ == "__main__":
    pytest.main()

