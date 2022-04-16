import sys
import os
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
    PDFPopplerTimeoutError
)
import tempfile
from PIL import Image

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

        self.title('verTIFFer 0.1.0')
        self.geometry(f'{Vertiffer.WIDTH}x{Vertiffer.HEIGHT}')
        # self.minsize('256x128')

        # Icons
        folder_ico = tkinter.PhotoImage(file=r'./icons/folder.png')

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.run_bttn = ctk.CTkButton(master=self, text="verTIFF mich!",
                                      command=self.run_bttn_func)
        self.run_bttn.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

        self.src_bttn = ctk.CTkButton(master=self, width=48, height=48,
                                      image=folder_ico,
                                      text="Quelle",
                                      command=self.src_bttn_func)
        self.src_bttn.place(relx=0.5, rely=0.25, anchor=tkinter.W)

        self.dst_bttn = ctk.CTkButton(master=self, width=48, height=48,
                                      image=folder_ico,
                                      text="Ziel",
                                      command=self.dst_bttn_func)
        self.dst_bttn.place(relx=0.5, rely=0.5, anchor=tkinter.W)

    def src_bttn_func(self):
        pass

    def dst_bttn_func(self):
        pass

    def run_bttn_func(self):
        with tempfile.TemporaryDirectory() as path:
            images = convert_from_bytes(open(r'test.pdf', 'rb').read(),
                                        paths_only=True,
                                        output_folder=path,
                                        thread_count=4,
                                        fmt='tiff',
                                        dpi=300)
            ord_imgs = []
            for img in images:
                ord_imgs.append(Image.open(img).convert('L'))
            if len(ord_imgs) == 1:
                ord_imgs[0].save('test.tif', save_all = True,
                                 compression='tiff_adobe_deflate')
            else:
                ord_imgs[0].save('test.tif', save_all = True,
                                 append_images = ord_imgs[1:],
                                 compression='tiff_adobe_deflate')

    def on_closing(self):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = Vertiffer()
    app.start()
