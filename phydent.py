from numpy import *
import subprocess
import pandas as pd
# import tkinter as tk
# from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print(file_path)

def open_opus():
    subprocess.Popen('{}'.format(file_path))
    print("Opus succesfully opened")

open_opus()