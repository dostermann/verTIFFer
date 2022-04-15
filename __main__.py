import os
from pdf2image import convert_from_path, convert_from_bytes

# GUI imports
import tkinter
import customtkinter as ctk


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

tk_window = ctk.CTk()
tk_window.geometry("512x256")

def button_func():
    pass
button = ctk.CTkButton(master=tk_window, text="verTIFF mich!",
                       command=button_func)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

tk_window.mainloop()


class Vertiffer:
    """Main class for verTIFFer"""

    def __init__(self):
        pass
