from SbisRuPages import PagesHelper


class Test:
    
    def test_scenario_first(self, browser):
        
        sbis_main_page = PagesHelper(browser)
        
        sbis_main_page.go_to_site()
        sbis_main_page.click_on_the_contacts_bar()
        sbis_main_page.click_on_the_tensor_logo()
        
        sbis_main_page.driver.switch_to.window(sbis_main_page.driver.window_handles[1])
        
        assert "https://tensor.ru/" in sbis_main_page.driver.current_url
        
        power_in_peoples = sbis_main_page.find_power_people_block()
        assert power_in_peoples.is_displayed() == True

        sbis_main_page.more_details_click()
        
        img_list = sbis_main_page.get_img_list()
        
        width_img_list  = []
        height_img_list = []
        
        for img in img_list:
            width_img_list.append(img.value_of_css_property('width'))
            height_img_list.append(img.value_of_css_property('height'))
        
        assert width_img_list.count(width_img_list[0]) == len(width_img_list)
        assert height_img_list.count(height_img_list[0]) == len(height_img_list)
        
        
    def test_scenario_second(self, browser):
        
        sbis_main_page = PagesHelper(browser)
        
        sbis_main_page.go_to_site()
        sbis_main_page.click_on_the_contacts_bar()
        
        partners = sbis_main_page.partners_info()
        assert partners.get_attribute('title') == "СБИС - Ярославль"
        
        region_info = sbis_main_page.region_info()
        assert region_info.text == 'Ярославская обл.'
        
        sbis_main_page.change_region_to_kamchatka()
        
        partners = sbis_main_page.partners_info()
        assert partners.get_attribute('title') == 'СБИС - Камчатка'
        
        region_info = sbis_main_page.region_info()
        assert region_info.text == 'Камчатский край'
        