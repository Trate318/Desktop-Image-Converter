import sys # for copy/paste
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import ImageGrab, Image, ImageTk
import pillow_heif
from tkinter import filedialog, messagebox, ttk
import os

pillow_heif.register_heif_opener()

FILE_TYPE_DICT = {
    'jpeg' : 'JPEG',
    'jpg' : 'JPEG',
    'png' : 'PNG',
    'heic' : 'HEIC',
    'heif' : 'HEIF',
}

FONT = "Thonburi"
TEXT_COLOR = "#000000"

current_img : Image = None
preview_img : Image = None

file_type : str = "png"

def browse_file(event=None):
    global current_img
    filepath = filedialog.askopenfilename(
        title="Select an Image",
        initialdir=os.path.expanduser("~")
        )
    current_img = Image.open(filepath)
    display_image_name(os.path.basename(filepath))
    display_image()

def drop_file(event):
    global current_img
    filepath = event.data.strip('{}')
    current_img = Image.open(filepath)
    display_image_name(os.path.basename(filepath))
    display_image()

def display_image():
    global preview_img
    preview_img = current_img.copy()
    preview_img.thumbnail((input_frame.winfo_width(),input_frame.winfo_height()))
    preview_img = ImageTk.PhotoImage(preview_img)
    drop_label.config(image=preview_img, text="")

def display_image_name(filename):
    filename_input_text.config(state='normal')
    filename_input_text.delete(0, tk.END)
    filename_no_ext = os.path.splitext(filename)[0]
    filename_input_text.insert(0, filename_no_ext)

def download_image(event=None):
    global current_img
    new_filename = filename_input_text.get()
    downloads_path = os.path.expanduser("~/Downloads")
    if new_filename:
        convert(current_img)
        current_img.save(os.path.join(downloads_path, f"{new_filename}.{file_type}"), format='PNG')

def convert(image : Image):
   if image.format == 'PNG':
       image = image.convert('RGB')

root = TkinterDnD.Tk()
root.geometry("600x420")
root.title("Image Converter")
root.resizable(False, False)
root.configure(bg="#c02727")

canvas = tk.Canvas(root, width=600, height=420, bg="#e6ebe9")
canvas.pack()

input_frame = tk.Frame(root, width=450, height=250, bg="#bdc3c1")
input_frame.pack_propagate(False)

filename_input_frame = tk.Frame(root, width=320, height=40, bg="#A1D8B5")

input_buttons_frame = tk.Frame(root, width=120, height=40, bg="#4CB572")

drop_label = tk.Label(
    input_frame,
    text="Drag & Drop, Paste, or Click to Enter File",
    bg=input_frame["bg"],
    wraplength=180,
    justify="center",
    font=(FONT, 13),
    fg=TEXT_COLOR
)

filename_input_text = tk.Entry(
    filename_input_frame, 
    width=320,
    bg="#A1D8B5",
    borderwidth=0,
    highlightthickness=0,
    justify='center',
    font=(FONT, 13),
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    state='readonly',
    readonlybackground="#A1D8B5",
)

select_file_type_label = tk.Label(
    input_buttons_frame, 
    width=200, 
    height=40, 
    bg="#4CB572",
    text="Select Type",
    font=(FONT, 13),
    fg=TEXT_COLOR,
    )


output_buttons_frame = tk.Frame(root, width=450, height=40, bg="#e6ebe9")

download_label = tk.Label(
    output_buttons_frame, 
    width=95, 
    height=40, 
    bg="#4CB572",
    text="Download",
    font=(FONT, 13),
    fg=TEXT_COLOR
    )

copy_label = tk.Label(
    output_buttons_frame, 
    width=95, 
    height=40, 
    bg="#4CB572",
    text="Copy",
    font=(FONT, 13),
    fg=TEXT_COLOR
    )


drop_label.pack(expand=True, fill="both")
filename_input_text.place(x=0, y=0, width=320, height=40)
copy_label.place(x=230, y=0, width=220, height= 40)
download_label.place(x=0, y=0, width=220, height= 40)
select_file_type_label.place(x=0, y=0, width=120, height=40)


canvas.create_window(75, 40, anchor="nw", window=input_frame)
canvas.create_window(405, 300, anchor="nw", window=input_buttons_frame)

canvas.create_window(75, 300, anchor="nw", window=filename_input_frame)
canvas.create_window(75, 350, anchor="nw", window=output_buttons_frame)

drop_label.bind("<Button-1>", browse_file)

drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind('<<Drop>>', drop_file)

download_label.bind("<Button-1>", download_image)

def center_window(window, width=300, height=200):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# temp hides it so it doesn't flash top left
root.withdraw()
center_window(root, 600, 420)
root.deiconify() 

root.mainloop()