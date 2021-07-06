# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from selenium import webdriver


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def findform(self):

        self.driver.get('http://automationpractice.com/index.php')
        search = self.driver.find_element_by_xpath('//*[@id="search_query_top"]')
        search.send_keys('Hat')

        searchButton = self.driver.find_element_by_xpath('//*[@id="searchbox"]/button')
        searchButton.click()

        picOfClothing = self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[2]/h5/a')
        picOfClothing.click()

        addToCart = self.driver.find_element_by_xpath('//*[@id="add_to_cart"]/button')
        addToCart.click()

        self.driver.implicitly_wait(8)
        pToCheckout = self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')
        pToCheckout.click()

        s1 = self.driver.find_element_by_xpath("//*[@id=\"center_column\"]/p[2]/a[1]")
        s1.click()

        s2 = self.driver.find_element_by_xpath('//*[@id="email"]')
        s2.send_keys("gclotet@aol.com")

        s3= self.driver.find_element_by_xpath('//*[@id="passwd"]')
        s3.send_keys('Nabeel123')

        s4 = self.driver.find_element_by_xpath('//*[@id="SubmitLogin"]')
        s4.click()

        s5 = self.driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button')
        s5.click()

        s6 = self.driver.find_element_by_xpath('//*[@id="cgv"]')
        s6.click()

        s7 = self.driver.find_element_by_xpath('//*[@id="form"]/p/button')
        s7.click()

        s8 = self.driver.find_element_by_xpath('//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')
        s8.click()

        finishCheckout = self.driver.find_element_by_xpath('//*[@id="cart_navigation"]/button')
        finishCheckout.click()

bot = Bot()
bot.findform()
