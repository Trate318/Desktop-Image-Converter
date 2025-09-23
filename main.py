import sys # for copy/paste
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import ImageGrab, Image, ImageTk
from tkinter import filedialog, messagebox
import os

VALID_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".bmp")
FONT = "Thonburi"
current_img = None
display_image = None


def browse_file(event=None):
    global current_img
    filepath = filedialog.askopenfilename(
        title="Select an Image",
        initialdir=os.path.expanduser("~")
        )
    current_img = Image.open(filepath)
    display_image()

def display_image():
    global display_image
    display_image = current_img.copy()
    display_image.thumbnail((200,200))
    display_image = ImageTk.PhotoImage(display_image)

    drop_label.config(image=display_image, text="")

root = TkinterDnD.Tk()
root.geometry("600x400")
root.title("Image Converter")
root.resizable(False, False)
root.configure(bg="#c02727")

canvas = tk.Canvas(root, width=600, height=400, bg="#e6ebe9")
canvas.pack()

input_frame = tk.Frame(root, width=200, height=200, bg="#bdc3c1")
input_frame.pack_propagate(False)


drop_label = tk.Label(
    input_frame,
    text="Drag & Drop, Paste, or Click to Enter File",
    bg=input_frame["bg"],
    wraplength=180,
    justify="center",
    font=(FONT, 13)
)

drop_label.pack(expand=True, fill="both")

output_frame = tk.Frame(root, width=200, height=200, bg="#bdc3c1")
output_frame.pack_propagate(False)


filename_input_frame = tk.Frame(
    root,
    width=200, 
    height=40,
    bg="#A1D8B5"
    )

filename_input_label = tk.Label(
    filename_input_frame, 
    width=200, 
    height=40, 
    bg="#A1D8B5",
    text="",
    font=(FONT, 13)
    )
filename_input_label.place(x=0, y=0, width=200, height=40)

filename_output_frame = tk.Frame(
    root,
    width=200, 
    height=40,
    bg="#A1D8B5"
    )


input_buttons_frame = tk.Frame(root, width=200, height=40, bg="#4CB572")
select_file_type_label = tk.Label(
    input_buttons_frame, 
    width=200, 
    height=40, 
    bg="#4CB572",
    text="Select File Type",
    font=(FONT, 13)
    )
select_file_type_label.place(x=0, y=0, width=200, height=40)

output_buttons_frame = tk.Frame(root, width=200, height=40, bg="#e6ebe9")

download_label = tk.Label(
    output_buttons_frame, 
    width=95, 
    height=40, 
    bg="#4CB572",
    text="Download",
    font=(FONT, 13)
    )
download_label.place(x=0, y=0, width=95, height= 40)

copy_label = tk.Label(
    output_buttons_frame, 
    width=95, 
    height=40, 
    bg="#4CB572",
    text="Copy",
    font=(FONT, 13)
    )
copy_label.place(x=105, y=0, width=95, height= 40)


convert_frame = tk.Frame(root, width=80, height=40, bg="#4CB572")

convert_label = tk.Label(
    convert_frame, 
    width=80, 
    height=40, 
    bg="#4CB572",
    text="Convert",
    font=(FONT, 13)
    )
convert_label.place(x=0, y=0, width=80, height= 40)

canvas.create_window(40, 40, anchor="nw", window=input_frame)
canvas.create_window(40, 300, anchor="nw", window=input_buttons_frame)
canvas.create_window(40, 250, anchor="nw", window=filename_input_frame)

canvas.create_window(300, 200, anchor="center", window=convert_frame)

canvas.create_window(600 - 40, 40, anchor="ne", window=output_frame)
canvas.create_window(600 - 40, 250, anchor="ne", window=filename_output_frame)
canvas.create_window(600 - 40, 300, anchor="ne", window=output_buttons_frame)

drop_label.bind("<Button-1>", browse_file)

root.mainloop()