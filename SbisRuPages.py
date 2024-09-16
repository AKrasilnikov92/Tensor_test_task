from BaseApp import BasePage
from selenium.webdriver.common.by import By



class SbisRuLocators:
    
    LOCATOR_SBISRU_CONTACTS_BAR = (By.LINK_TEXT, 'Контакты')
    LOCATOR_SBISRU_TENSOR_LOGO = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
    LOCATOR_SBISRU_PARTNERS = (By.XPATH, "//*[@id=\"contacts_list\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]")
    LOCATOR_SBISRU_REGIONS = (By.XPATH, "//*[@id=\"container\"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span")
    LOCATOR_SBISRU_REGION_KAMCHATKA = (By.XPATH, "//*[@id=\"popup\"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span")


class TensorRuLocators:
    
    LOCATOR_TENSORRU_POWER_PEOPLE_BLOCK = (By.XPATH, "//*[@id=\"container\"]/div[1]/div/div[5]/div/div/div[1]/div")
    LOCATOR_TENSORRU_MORE_DETAILS_LINK = (By.XPATH, "//a[@href=\"/about\" and contains(., 'Подробнее')]")
    LOCATOR_TENSORRU_ABOUT_BLOCK_IMG = (By.XPATH, "//img[contains(@class,'tensor_ru-About__block3')]")
    
    
class PagesHelper(BasePage):

    def click_on_the_contacts_bar(self):
        return self.find_element(SbisRuLocators.LOCATOR_SBISRU_CONTACTS_BAR, 3).click()

    def click_on_the_tensor_logo(self):
        return self.find_element(SbisRuLocators.LOCATOR_SBISRU_TENSOR_LOGO, 3).click()

    def partners_info(self):
        return self.find_element(SbisRuLocators.LOCATOR_SBISRU_PARTNERS, 3)
    
    def region_info(self):
        return self.find_element(SbisRuLocators.LOCATOR_SBISRU_REGIONS, 3)
    
    def change_region_to_kamchatka(self):
        self.region_info().click()
        return self.find_element(SbisRuLocators.LOCATOR_SBISRU_REGION_KAMCHATKA, 3).click()
    
    def get_url(self):
        return self.current_url
    
    def power_people_block(self):
        return self.find_element(TensorRuLocators.LOCATOR_TENSORRU_POWER_PEOPLE_BLOCK, 3)
    
    def find_power_people_block(self):
        return self.element_is_diplayed(
            TensorRuLocators.LOCATOR_TENSORRU_POWER_PEOPLE_BLOCK, 3)
        
    def more_details_click(self):
        more_details = self.find_element(TensorRuLocators.LOCATOR_TENSORRU_MORE_DETAILS_LINK, 3)
        return self.driver.execute_script("arguments[0].click();", more_details)
    
    def get_img_list(self):
        return self.find_elements(TensorRuLocators.LOCATOR_TENSORRU_ABOUT_BLOCK_IMG, 3)
    
    