import sys
import os
from pdf2image import convert_from_path, convert_from_bytes

# GUI imports
import tkinter
import customtkinter as ctk


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class Vertiffer(ctk.CTk):
    """Main class for verTIFFer"""

    WIDTH = 512
    HEIGHT = 256

    def __init__(self):
        super().__init__()

        self.title("verTIFFer 0.1.0")
        self.geometry(f"{Vertiffer.WIDTH}x{Vertiffer.HEIGHT}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.button = ctk.CTkButton(master=self, text="verTIFF mich!",
                       command=self.button_func)
        self.button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def button_func(self):
        pass

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = Vertiffer()
    app.start()
