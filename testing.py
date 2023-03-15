import requests
import datetime
import tkinter as tk
import urllib.request
from time import sleep
from random import randint
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = None

def login_click():
    global driver
    driver = uc.Chrome()
    driver.get('https://tinder.com/')

    wait = WebDriverWait(driver, 60)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/button')))

# Define the function to execute when Like Button is clicked
def like_click():
    global driver
    
    # Update the text in the first text box
    like_txtbox.delete(1.0, tk.END)  # Clear the text box
    like_txtbox.insert(tk.END, "Profile Liked Successfully")

    # Pressing Right Arrow key to Like
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()


# Define the function to execute when Dislike Button is clicked
def dislike_click():
    global driver

    # Update the text in the second text box
    dislike_txtbox.delete(1.0, tk.END)  # Clear the text box
    dislike_txtbox.insert(tk.END, "Profile Disliked Successfully")

    # Pressing Left Arrow key to dislike
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_LEFT)
    actions.perform()


def save_click():
    global driver

    # Pressing Up Arrow key to open more info
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_UP)
    actions.perform()

    name = driver.find_element(By.XPATH, '//*[@id="s-1432688076"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div/div/span').text
    age = driver.find_element(By.XPATH, '//*[@id="s-1432688076"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div/span[2]').text
    moreinfo = ''

    # Update the text in the Save text box
    save_txtbox.delete(1.0, tk.END)  # Clear the text box
    save_txtbox.insert(tk.END, f"Full Info = {name}, {age}, {moreinfo}")

def name_click():
    global driver

    name = driver.find_element(By.XPATH, '//*[@id="s-1432688076"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div/div/span').text

    # Update the text in the name text box
    name_txtbox.delete(1.0, tk.END)  # Clear the text box
    name_txtbox.insert(tk.END, f"Name = {name}")


def age_click():
    global driver

    age = driver.find_element(By.XPATH, '//*[@id="s-1432688076"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div/span[2]').text

    # Update the text in the age text box
    age_txtbox.delete(1.0, tk.END)  # Clear the text box
    age_txtbox.insert(tk.END, f"Age = {age}")


def moreinfo_click():
    # Pressing Up Arrow key to open more info
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_UP)
    actions.perform()

    moreinfo = ''
    temp = driver.find_elements(By.XPATH, '//*[@id="s-1432688076"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div')

    for i in temp:
        moreinfo += i.text + ', '

    # Update the text in the moreinfo text box
    moreinfo_txtbox.delete(1.0, tk.END)  # Clear the text box
    moreinfo_txtbox.insert(tk.END, f"Moreinfo = {moreinfo}")


def image_click():
    global driver

    images = driver.find_elements(By.XPATH, '//*[@id="s-1432688076"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/span[1]/div')
    # images = driver.find_elements(By.XPATH, '//div[contains(@style, "background-image: url")]')
    i = 1
    for image in images:
        link = image.split()[1].strip('url(");&quot').replace("&amp;", "&")
        with open(f'{i}.png', "w") as f:

    # Update the text in the age text box
    image_txtbox.delete(1.0, tk.END)  # Clear the text box
    image_txtbox.insert(tk.END, f"Image Saved")

def stay_on_top():
   window.lift()
   window.after(2000, stay_on_top)


if __name__ == '__main__':
    # Create a new window
    window = tk.Tk()

    # Login Button
    login_btn = tk.Button(window, text="login", command=login_click)
    login_btn.pack()

    # Like Button and Textbox
    like_btn = tk.Button(window, text="Like", command=like_click)
    like_btn.pack()
    like_txtbox = tk.Text(window, height=1, width=30)
    like_txtbox.pack()

    # Dislike Button and Textbox
    dislike_btn = tk.Button(window, text="Dislike", command=dislike_click)
    dislike_btn.pack()
    dislike_txtbox = tk.Text(window, height=1, width=30)
    dislike_txtbox.pack()

   # Name Button and Textbox
    name_btn = tk.Button(window, text="Name", command=name_click)
    name_btn.pack()
    name_txtbox = tk.Text(window, height=1, width=30)
    name_txtbox.pack()

   # Age Button and Textbox
    age_btn = tk.Button(window, text="Age", command=age_click)
    age_btn.pack()
    age_txtbox = tk.Text(window, height=1, width=30)
    age_txtbox.pack()

   # More info Button and Textbox
    moreinfo_btn = tk.Button(window, text="MoreInfo", command=moreinfo_click)
    moreinfo_btn.pack()
    moreinfo_txtbox = tk.Text(window, height=1, width=30)
    moreinfo_txtbox.pack()

# More info Button and Textbox
    image_btn = tk.Button(window, text="Image", command=image_click)
    image_btn.pack()
    image_txtbox = tk.Text(window, height=1, width=30)
    image_txtbox.pack()

   # Save Button and Textbox
    save_btn = tk.Button(window, text="Save All", command=save_click)
    save_btn.pack()
    save_txtbox = tk.Text(window, height=1, width=30)
    save_txtbox.pack()

    # Call function to make the window stay on top
    stay_on_top()

    # Run the main event loop
    window.mainloop()