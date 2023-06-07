from driver import driver, wait, EC, By, pytest


class Images:
    def open(self):
        self.driver = driver
        self.driver.get("https://ya.ru/")

    def menu_display(self):
        search_bar = wait.until(EC.visibility_of_element_located((By.ID, 'text')))
        search_bar.click()
        self.driver.find_element(By.ID, 'text').click()
        all_services = driver.find_element(By.CLASS_NAME, 'services-suggest__icons-more')
        assert all_services.is_displayed(), "Ошибка: меню не отображается на странице"
        all_services.click()

    def transition_images(self):
        website_picture = self.driver.find_element(By.CLASS_NAME, 'services-more-popup__section-content').find_elements(
            By.TAG_NAME, "a")
        for link in website_picture:
            if link.get_attribute("href") == "https://yandex.ru/images/":
                link.click()
                break
        self.driver.switch_to.window(driver.window_handles[-1])
        assert self.driver.current_url == 'https://yandex.ru/images/', "Ошибка: не удалось перейти на сайт Яндекс.Картинки"

    def first_category(self):
        text_the_first_1 = self.driver.find_element(By.CLASS_NAME, 'PopularRequestList-SearchText').text
        self.driver.find_element(By.CLASS_NAME, 'PopularRequestList-Item_pos_0').click()
        assert text_the_first_1, 'Ошибка: первая категория не найдена '
        search_field_result = wait.until(EC.visibility_of_element_located((By.NAME, 'text')))
        search_field_result_2 = search_field_result.get_attribute("value")
        assert text_the_first_1 == search_field_result_2, 'Ошибка: название категории не отображается или ' \
                                                          'отображается некорректно в поле поиска'
    def open_image(self):
        open_first_picture = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'serp-item__preview')))
        open_first_picture.click()
        assert open_first_picture, "Ошибка: первая картинка не найдена"

    def next(self):
        next = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'CircleButton_type_next')))
        global image_element
        image_element = self.driver.find_element(By.CLASS_NAME, "MMImage-Origin").get_attribute('src')
        assert image_element, 'Ошибка: Картинка не открылась'
        next.click()
        new_image_element = self.driver.find_element(By.CLASS_NAME, "MMImage-Origin").get_attribute('src')
        assert image_element != new_image_element, "Ошибка: картинка не поменялась"

    def back(self):
        back = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.CircleButton_type_prev')))
        back.click()
        assert image_element == self.driver.find_element(By.CLASS_NAME, "MMImage-Origin").get_attribute(
            'src'), "Ошибка: картинка не вернулась в исходную из 8 пункта"


def test_tesnor_search():
    browser = Images()
    browser.open()
    browser.menu_display()
    browser.transition_images()
    browser.first_category()
    browser.open_image()
    browser.next()
    browser.back()


if __name__ == "__main__":
    pytest.main()
