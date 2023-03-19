import os
import json
import tkinter as tk
from tkinter import *
import urllib.request
from datetime import datetime
from PIL import ImageTk, Image
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = None
Name = ''
Age = ''
MoreInfo = ''
Image1 = ''
Image2 = ''
Image3 = ''


# Reset function to reset everything when like or dislike button is pressed.
def reset_all():
    global Name
    global Age
    global MoreInfo
    global Image1
    global Image2
    global Image3
    
    Name = ''
    Age = ''
    MoreInfo = ''
    Image1 = ''
    Image2 = ''
    Image3 = ''

    like_lbl.config(text='')
    dislike_lbl.config(text='')
    name_lbl.config(text='')
    age_lbl.config(text='')
    moreinfo_lbl.config(text='')
    image_lbl.config(text='')
    save_lbl.config(text='')

    show_image_lbl1.config(image=None)
    show_image_lbl2.config(image=None)
    show_image_lbl3.config(image=None)


# Login function
def login_click():
    global driver
    
    driver = uc.Chrome()
    driver.maximize_window()
    driver.get('https://tinder.com/')

    wait = WebDriverWait(driver, 60)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/button')))

    login_lbl.config(text='Login Successfull')


# Define the function to execute when Like Button is clicked
def like_click():
    # Resetting all the Labels because new profile is opened
    reset_all()
    
    global driver

    # Pressing Right Arrow key to Like
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()

    # Update the text in the Liked Label
    like_lbl.config(text='Profile Liked Successfully')

# Function to execute when Dislike Button is clicked
def dislike_click():
    # Resetting all the Labels because new profile is opened
    reset_all()
    
    global driver

    # Pressing Left Arrow key to dislike
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_LEFT)
    actions.perform()

    # Update the text in the Dislike Label
    dislike_lbl.config(text='Profile Disliked Successfully')


# Function to execute when Name Button is clicked
def name_click():
    global driver
    global Name
    
    Name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div/div/span').text

    # Update the text in the name Label
    name_lbl.config(text=f'{Name}') 


# Function to execute when Age Button is clicked
def age_click():
    global driver
    global Age
    
    Age = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div/span[2]').text

    # Update the text in the age Label
    age_lbl.config(text=f'{Age}')


# Function to execute when MoreInfo Button is clicked
def moreinfo_click():
    global MoreInfo
    MoreInfo = ''
    
    # Pressing Up Arrow key to open more info
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_UP)
    actions.perform()

    try:
        temp = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    except:
        temp = driver.find_elements(By.CSS_SELECTOR, 'div.Row > div:nth-child(2)')
        

    for i in temp:
        MoreInfo += i.text + ', '

    MoreInfo = MoreInfo[:-2]

    # Update the text in the moreinfo Label
    moreinfo_lbl.config(text=f'{MoreInfo}')


# Function to execute when Image Button is clicked
def image_click():
    global driver

    global Image1
    global Image2
    global Image3

    global img1
    global img2
    global img3

    # Pressing Up Arrow key to open more info
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_UP)
    actions.perform()

    """
        NOTE: You have to CLICK on the arrow button on the image to go to 2nd image and then press the Image button
    """

    # Finding all images
    images = driver.find_elements(By.CSS_SELECTOR, 'div.profileCard__slider__imgShadow')

    # Retrieving the 3 images and saving it in the same folder 
    i = 1
    for image in images:
        current_dateTime = str(datetime.now()).replace('-', '_'). replace(':', '_').replace(' ', '_').split('.')[0]
        filename = Name.strip() + '_' + Age.strip() + '_' + current_dateTime + f'_{i}' + '.jpg'

        link = image.get_attribute('innerHTML').split()[6].strip('url(");&quot').replace("&amp;", "&")
        urllib.request.urlretrieve(link, filename)

        if i == 1:
            Image1 = filename

            # Label showing 1st Image
            img1 = Image.open(Image1)
            img1 = img1.resize((150,150), Image.Resampling.LANCZOS)
            img1 = ImageTk.PhotoImage(img1)
            show_image_lbl1['image'] = img1

            # Update the text in the Image Label
            image_lbl.config(text='1st Images Saved')
        elif i == 2:
            Image2 = filename
            print('2nd Image: ', Image2)

            # Label showing 2nd image
            img2 = Image.open(Image2)
            img2 = img2.resize((150,150), Image.Resampling.LANCZOS)
            img2 = ImageTk.PhotoImage(img2)
            show_image_lbl2['image'] = img2

            # Update the text in the Image Label
            image_lbl.config(text='2nd Images Saved')
        else:
            Image3 = filename
            print('3rd Image: ', Image3)

            # Label showing 3rd image
            img3 = Image.open(Image3)
            img3 = img3.resize((150,150), Image.Resampling.LANCZOS)
            img3 = ImageTk.PhotoImage(img3)
            show_image_lbl3['image'] = img3

            # Update the text in the Image Label
            image_lbl.config(text='3rd Images Saved')
        i += 1

    # Update the text in the Image Label
    image_lbl.config(text='All Images Saved')


# Function to execute when Save Button is clicked
def save_click():
    # If the file doesn't exist, create it and write an empty list as JSON data
    if not os.path.exists("data.json"):
        with open("data.json", "w") as f:
            json.dump([], f)
    
    with open("data.json", "r") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = []

    # Create a new dictionary to store the data to be appended
    new_data = {
                "Name": Name,
                "Age": Age,
                "MoreInfo": MoreInfo,
                "Image1": Image1,
                "Image2": Image1,
                "Image3": Image1
    }

    # Append the new data to the existing data
    data.append(new_data)

    # Write the updated data to the JSON file
    with open('data.json', 'w') as f:
        json.dump(data, f)
    
    all_info = f"{Name}, {Age}, {MoreInfo}, {Image1}, {Image2}, {Image3}"

    # # Set the width of the label to fit the text
    # save_lbl.config(width=len(all_info))

    # Update the text in the Save Label
    save_lbl.config(text=all_info)


if __name__ == '__main__':
    root = Tk()

    frame = tk.Frame(root)

    # Label showing image
    show_image_lbl1 = tk.Label(frame)

    # Label showing image
    show_image_lbl2 = tk.Label(frame)

    # Label showing image
    show_image_lbl3 = tk.Label(frame)

    # Login Button and Label
    login_btn = tk.Button(frame, text="login", command=login_click)
    # login_lbl = tk.Label(frame, height=1, width=30)
    login_lbl = tk.Label(frame, wraplength=200)

    # Like Button and Label
    like_btn = tk.Button(frame, text="Like", command=like_click)
    # like_lbl = tk.Label(frame, height=1, width=30)
    like_lbl = tk.Label(frame, wraplength=200)

    # Dislike Button and Label
    dislike_btn = tk.Button(frame, text="Dislike", command=dislike_click)
    # dislike_lbl = tk.Label(frame, height=1, width=30)
    dislike_lbl = tk.Label(frame, wraplength=200)

    # Name Button and Label
    name_btn = tk.Button(frame, text="Name", command=name_click)
    # name_lbl = tk.Label(frame, height=1, width=30)
    name_lbl = tk.Label(frame, wraplength=200)

    # Age Button and Label
    age_btn = tk.Button(frame, text="Age", command=age_click)
    # age_lbl = tk.Label(frame, height=1, width=30)
    age_lbl = tk.Label(frame, wraplength=200)

    # More info Button and Label
    moreinfo_btn = tk.Button(frame, text="MoreInfo", command=moreinfo_click)
    # moreinfo_lbl = tk.Label(frame, height=1, width=30)
    moreinfo_lbl = tk.Label(frame, wraplength=200)

    # More info Button and Label
    image_btn = tk.Button(frame, text="Image", command=image_click)
    # image_lbl = tk.Label(frame, height=1, width=30)
    image_lbl = tk.Label(frame, wraplength=200)

    # Save Button and Label
    save_btn = tk.Button(frame, text="Save All", command=save_click)
    # save_lbl = tk.Label(frame, height=1, width=30)
    save_lbl = tk.Label(frame, wraplength=200)

    frame.pack()

    login_btn.grid(row=0, column=0)
    login_lbl.grid(row=1, column=0)

    like_btn.grid(row=2, column=0)
    like_lbl.grid(row=3, column=0)

    dislike_btn.grid(row=4, column=0)
    dislike_lbl.grid(row=5, column=0)

    name_btn.grid(row=6, column=0)
    name_lbl.grid(row=7, column=0)

    age_btn.grid(row=8, column=0)
    age_lbl.grid(row=9, column=0)

    moreinfo_btn.grid(row=10, column=0)
    moreinfo_lbl.grid(row=11, column=0)

    image_btn.grid(row=12, column=0)
    image_lbl.grid(row=13, column=0)

    save_btn.grid(row=14, column=0)
    save_lbl.grid(row=15, column=0)

    show_image_lbl1.grid(row=0, column=1, rowspan=6)
    show_image_lbl2.grid(row=0, column=2, rowspan=6)
    show_image_lbl3.grid(row=0, column=3, rowspan=6)

    root.mainloop()