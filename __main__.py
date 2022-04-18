from os import path
from glob import glob
from posixpath import split, splitext
from pdf2image import convert_from_bytes
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
from tkinter import END, filedialog
import customtkinter as ctk


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class Vertiffer(ctk.CTk):
    """Main class for verTIFFer"""

    WIDTH = 512
    HEIGHT = 256

    def __init__(self):
        super().__init__()

        self.title('verTIFFer 0.9.0')
        self.geometry(f'{Vertiffer.WIDTH}x{Vertiffer.HEIGHT}')
        # self.minsize('256x128')

        # Icons
        folder_ico = tkinter.PhotoImage(file=r'./icons/folder.png')

        # needed variables at startup
        self.src_folder = ''
        self.dst_folder = ''

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.run_bttn = ctk.CTkButton(master=self, text="verTIFF mich!",
                                      command=self.run_bttn_func)
        self.run_bttn.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

        self.src_label = ctk.CTkEntry(master=self, placeholder_text=self.src_folder,
                                      state='disabled', width=350)
        self.src_label.place(relx=0.37, rely=0.25, anchor=tkinter.CENTER)
        self.src_bttn = ctk.CTkButton(master=self, width=48, height=48,
                                      image=folder_ico,
                                      text="Quelle",
                                      command=self.src_bttn_func)
        self.src_bttn.place(relx=0.75, rely=0.25, anchor=tkinter.W)

        self.dst_label = ctk.CTkEntry(master=self, placeholder_text=self.dst_folder,
                                      state='disabled', width=350)
        self.dst_label.place(relx=0.37, rely=0.5, anchor=tkinter.CENTER)
        self.dst_bttn = ctk.CTkButton(master=self, width=48, height=48,
                                      image=folder_ico,
                                      text="Ziel",
                                      command=self.dst_bttn_func)
        self.dst_bttn.place(relx=0.75, rely=0.5, anchor=tkinter.W)

    def src_bttn_func(self):
        self.src_folder = filedialog.askdirectory(title='Quellverzeichnis wählen')
        self.src_label['state'] = 'normal'
        self.src_label.delete(0, END)
        self.src_label.insert(0, self.src_folder)
        self.src_label['state'] = 'readonly'

    def dst_bttn_func(self):
        self.dst_folder = filedialog.askdirectory(title='Zielverzeichnis wählen')
        self.dst_label['state'] = 'normal'
        self.dst_label.delete(0, END)
        self.dst_label.insert(0, self.dst_folder)
        self.dst_label['state'] = 'readonly'

    def run_bttn_func(self):
        def find_pdf(dir, ext='pdf'):
            return glob(path.join(dir,
                                  '*.{}'.format(ext)))
        for items in find_pdf(self.src_folder):
            filename_w_ext = split(items)
            print(filename_w_ext)
            filename_wo_ext = splitext(filename_w_ext[1])
            print(filename_wo_ext)
            savefile = path.join(self.dst_folder, '{}{}'.format(filename_wo_ext[0], '.tif'))
            print('Savefile: ')
            print(savefile)

            with tempfile.TemporaryDirectory() as tmp_path:
                images = convert_from_bytes(open(items, 'rb').read(),
                                            paths_only=True,
                                            output_folder=tmp_path,
                                            thread_count=4,
                                            fmt='tiff',
                                            dpi=300)
                ord_imgs = []
                for img in images:
                    ord_imgs.append(Image.open(img).convert('L'))
                if len(ord_imgs) == 1:
                    ord_imgs[0].save(savefile, save_all = True,
                                    compression='tiff_adobe_deflate')
                else:
                    ord_imgs[0].save(savefile, save_all = True,
                                    append_images = ord_imgs[1:],
                                    compression='tiff_adobe_deflate')

    def on_closing(self):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = Vertiffer()
    app.start()
