import os
from selenium_tests.test import SeleniumTestCase
from selenium_tests.webdriver import CustomWebDriver
from selenium.webdriver.support.ui import Select
from selenium_tests.pages import ProjectsPage


class ViewParty(SeleniumTestCase):

    def setUp(self):
        self.wd = CustomWebDriver()

    def test_view_party(self):
        projects_page = ProjectsPage(self.wd, self)
        projects_page.go_to()
        projects_page.open_parties_page()

        self.wd.find_element_by_link_text("party-1").click()
        text = self.wd.find_element_by_xpath("//div[@class='page-title']/h2").text
        assert text == "PARTY DETAIL"

    def tearDown(self):
        self.wd.quit()

        
class EditParty(SeleniumTestCase):

    def setUp(self):
        self.wd = CustomWebDriver()

    def test_edit_party(self):
        projects_page = ProjectsPage(self.wd, self)
        projects_page.go_to()
        projects_page.open_parties_page()

        self.wd.find_element_by_link_text("party-1").click()
        self.wd.wait_for_xpath("//h2[contains(text(), 'Party detail')]")
        self.wd.find_element_by_xpath("//a[@title='Edit party']").click()
        self.wd.switch_to_window(self.wd.window_handles[-1])
        self.wd.find_element_by_id("id_name").clear()
        self.wd.find_element_by_id("id_name").send_keys("party-2")
        self.wd.find_element_by_name("submit").click()
        assert self.wd.wait_for_xpath("//*[contains(text(), 'party-2')]")

    def tearDown(self):
        self.wd.find_element_by_xpath("//a[@title='Edit party']").click()
        self.wd.switch_to_window(self.wd.window_handles[-1])
        self.wd.find_element_by_id("id_name").clear()
        self.wd.find_element_by_id("id_name").send_keys("party-1")
        self.wd.find_element_by_name("submit").click()
        self.wd.quit()


class DeleteParty(SeleniumTestCase):

    def setUp(self):
        self.wd = CustomWebDriver()

    def test_delete_party(self):
        projects_page = ProjectsPage(self.wd, self)
        projects_page.go_to()
        projects_page.open_parties_page()

        self.wd.find_element_by_link_text("party-1").click()
        self.wd.find_element_by_xpath("//a[@title='Delete party']").click()
        self.wd.switch_to_window(self.wd.window_handles[-1])
        self.wd.wait_for_xpath("//button[@value='Confirm']").click()

    def tearDown(self):
        self.wd.quit()

