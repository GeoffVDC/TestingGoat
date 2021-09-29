from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        # User opens the homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test")

        # User is invited to enter a to-do item straight away

        # User types "But peacock feathers" into a text box

        # When user hits enter, the page updates and lists
        # "Buy peacock feathers"

        # There is still a text box inviting the user to add another item.
        # The user enters "Use peacock feathers to make a fly"

        # The page updates again and now shows both items on the list

        # The user notices a unique URL with explanatory text

        # The user visits the url and the to-do list is still there

        # The user closes the browser

if __name__ == "__main__":
    unittest.main()