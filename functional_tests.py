from selenium import webdriver

browser = webdriver.Firefox()

# A user goes to the homepage to check out the website
browser.get("http://localhost:8000")

# The user notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# The user is invited to enter a to-do item straight away

# The user types "Buy peacock feathers" into a text box

# When the user hits enter, the page updates and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting the user to add another item. The user enters 
# "Use peacock feathers to make a fly"

# The page updates again, and now shows both items on their list

# The user sees a unique url and some explanatory message about saving the list

# The user visits the url and the to-do list is still there

# The user quits the application
browser.quit()