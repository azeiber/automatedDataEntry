from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Load Excel data
df = pd.read_excel("data.xlsx")  # Ensure data.xlsx is in the same folder

# Set up WebDriver (Make sure chromedriver.exe is in your PATH)
driver = webdriver.Chrome()

# Open Google Form (replace with your form URL)
form_url = "https://forms.gle/your-form-link"  # Replace with actual link
driver.get(form_url)
time.sleep(3)  # Let the page load

# Loop through each row in Excel
for index, row in df.iterrows():
    name = row["Name"]
    email = row["Email"]
    
    # Find form fields and fill them (Modify selectors based on your form)
    name_field = driver.find_element(By.XPATH, "//input[@type='text']")  # Adjust selector
    name_field.send_keys(name)

    email_field = driver.find_element(By.XPATH, "//input[@type='email']")  # Adjust selector
    email_field.send_keys(email)

    # Submit the form (Modify if needed)
    submit_button = driver.find_element(By.XPATH, "//span[contains(text(),'Submit')]")  
    submit_button.click()
    
    time.sleep(2)  # Wait before next entry

    # Go back to the form for the next entry (adjust based on the form behavior)
    driver.get(form_url)
    time.sleep(3)

# Close the browser
driver.quit()
