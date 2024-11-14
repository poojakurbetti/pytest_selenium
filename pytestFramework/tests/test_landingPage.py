import pytest
from tests.test_Base import BaseTest
from pages.LandingPage import LandingPage

class Test_Landing(BaseTest):
    def test_validateLandingPageTabSize(self):
        self.landingPage = LandingPage(self.driver)
        self.landingPage.validateNavigationTabs(8)

    def test_validatePresenceOfMostWantedTab(self):
        self.landingPage = LandingPage(self.driver)
        self.landingPage.validateTabPresence('Most Wanted')

    def test_GoToTab(self):
        self.landingPage = LandingPage(self.driver)
        self.landingPage.goToTab('Most Wanted')
