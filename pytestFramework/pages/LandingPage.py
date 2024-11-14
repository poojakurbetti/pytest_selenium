from config.config import TestData
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    SHOPIFY_HEADER = (By.ID, "shopify-section-header")
    NAV_MOSTWANTED = (By.ID, "nav-most-wanted")
    NAV_COMPOSTING = (By.ID, "nav-composting")
    NAV_WATERSAVING = (By.ID, "nav-water-saving")
    NAV_GARDENING = (By.ID, "nav-gardening")
    NAV_RECYCLING = (By.ID, "nav-recycling")
    NAV_BRANDS = (By.ID, "nav-brands")
    NAV_LEARN = (By.XPATH, "//li[contains(@id, 'nav-learn')]/a")
    NAV_SUPPORT = (By.ID, 'nav-support')
    NAV_TABS = (By.CSS_SELECTOR, "[data-nav-item='true']")

    HEADING = (By.CSS_SELECTOR,".heading-1")
    WHATSNEW = (By.CSS_SELECTOR,'a[href="/collections/new-in"]')
    LISTOFPRODUCTS = (By.CSS_SELECTOR , ".grid-item")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def validateNavigationTabs(self, count):
        assert self.findElementsSizeBy(self.NAV_TABS) == count, "size mismatch"

    def validateTabPresence(self, tabName):
        if tabName == 'Most Wanted':
            assert self.is_present(self.NAV_MOSTWANTED), tabName+ " Tab not found"
        elif tabName == 'Composting':
            assert self.is_present(self.NAV_COMPOSTING), tabName+ " Tab not found"
        elif tabName == 'Water Saving':
            assert self.is_present(self.NAV_WATERSAVING), tabName + " Tab not found"
        elif tabName == 'Gardening':
            assert self.is_present(self.NAV_GARDENING), tabName + " Tab not found"
        elif tabName == 'Recycling':
            assert self.is_present(self.NAV_RECYCLING), tabName + " Tab not found"
        elif tabName == 'Brands':
            assert self.is_present(self.NAV_BRANDS), tabName + " Tab not found"
        elif tabName == 'Learn':
            assert self.is_present(self.NAV_LEARN), tabName + " Tab not found"
        elif tabName == 'Support':
            assert self.is_present(self.NAV_SUPPORT), tabName + " Tab not found"

    def goToTab(self, tabName):
        if tabName == 'Most Wanted':
            self.click(self.NAV_MOSTWANTED)
            assert self.is_present(self.WHATSNEW)
            self.click(self.WHATSNEW)
            assert self.is_present(self.HEADING), "Not found"
            assert self.get_text(self.HEADING)=='New In', "Not found"
        elif tabName == 'Composting':
            self.click(self.NAV_COMPOSTING)
        elif tabName == 'Water Saving':
            self.click(self.NAV_WATERSAVING)
        elif tabName == 'Gardening':
            self.click(self.NAV_GARDENING)
        elif tabName == 'Recycling':
            self.click(self.NAV_RECYCLING)
        elif tabName == 'Brands':
            self.click(self.NAV_BRANDS)
        elif tabName == 'Learn':
            self.click(self.NAV_LEARN)
        elif tabName == 'Support':
            self.click(self.NAV_SUPPORT)





