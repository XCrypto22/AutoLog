#!/usr/bin/env python3
# Free source code
# By Elton Fungirai aka XCrypto
# Project 1

from selenium import webdriver
from time import sleep
import tkinter as tk


HEIGHT = 400
WIDTH = 400

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://facebook.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log In')]").click()
        self.driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"pass\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(10)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='green')
frame.place(relx=0.5, rely=0.1, relwidth=0.25, relheight=0.25, anchor='n')

button = tk.Button(frame, text='Facebook', command=lambda: InstaBot('example@gmail.com', 'password'))  # Use your email/phone number and password instead
button.pack(fill='both', expand='y')

root.mainloop()



