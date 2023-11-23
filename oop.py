from pyvirtualdisplay import Display
from selenium import webdriver

# Start a virtual display
display = Display(visible=0, size=(800, 600))
display.start()

# Create a WebDriver instance (in this case, using Firefox)
driver = webdriver.Firefox()

# Navigate to a website
driver.get("https://stackoverflow.com/questions/14314596/how-to-reset-to-a-specific-commit")

# Perform some actions
# For example, let's print the title of the page
print("Title of the page:", driver.title)

# Close the browser
driver.quit()

# Stop the virtual display
display.stop()
