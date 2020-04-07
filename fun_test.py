from selenium import webdriver  
from selenium.webdriver.common.keys import Keys 
import unittest
import time

class NewVisitorTest(unittest.TestCase): #(1)
    def setUp(self):
        self.browser = webdriver.Firefox()    #(3)

    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):#2
        # Edith has heard about a cool new online to-do app. she goes
        #to check out its homepage
        self.browser.get('http://localhost:8000')   #(3)
        self.assertIn('To-Do',self.browser.title)#(4)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )

        inputbox.send_keys('Buy peacok feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_lisy_table')        
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacok feathers' for row in rows)
            )
        self.fail('Finish the test!')
    
    
if __name__ == '__main__':#(6)
    #12345677
    unittest.main(warnings='ignore')#(7)
#She notices the page title and header mention to-do lists


# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box(Edith's hobby 
# is tying fly-fishing lures)

#when she hits enter, the page updates, and now the page lists
#"1: buy peacock feathers" as an item in a to-do list

#There is still a text box inviting her to add another item. She
#enters "Use peacock feathers to make a fly"(Edith is very methodical)

#the page updates again, and now shows both items on her list

#Edith wonders whether the site will remember her list. Then she sees
#that the site has generated a unique URL for her -- there is some
#explanatory text to that effect

#She visits that URL - her to-do list is still there.

#Satisfied, she goes back to sleep

#browser.quit()
