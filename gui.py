import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import ImageTk
from tkinter import ttk
import pillow_heif
import os

pillow_heif.register_heif_opener()

FILE_TYPE_DICT = {
    'jpeg': 'JPEG',
    'jpg': 'JPEG',
    'png': 'PNG',
    'heic': 'HEIF',
    'heif': 'HEIF',
}

class gui:
    FONT = "Thonburi"
    TEXT_COLOR = "#000000"

    def __init__(self):
        self.preview_img = None
        self._create_window()
        self._create_widgets()
        self._position_widgets()
        self._setup_drag_drop()
        self._center_window()

    def _create_window(self):
        self.root = TkinterDnD.Tk()
        self.root.geometry("600x420")
        self.root.title("Image Converter")
        self.root.resizable(False, False)
        self.root.configure(bg="#c02727")

    def _create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=600, height=420, bg="#e6ebe9")
        self.canvas.pack()

        self.input_frame = tk.Frame(self.root, width=450, height=250, bg="#bdc3c1")
        self.input_frame.pack_propagate(False)

        self.filename_input_frame = tk.Frame(self.root, width=320, height=40, bg="#A1D8B5")
        self.input_buttons_frame = tk.Frame(self.root, width=120, height=40, bg="#4CB572")
        self.output_buttons_frame = tk.Frame(self.root, width=450, height=40, bg="#e6ebe9")

        self.drop_label = tk.Label(
            self.input_frame,
            text="Drag & Drop, Paste, or Click to Enter File",
            bg=self.input_frame["bg"],
            wraplength=180,
            justify="center",
            font=(self.FONT, 13),
            fg=self.TEXT_COLOR
        )

        self.filename_input_text = tk.Entry(
            self.filename_input_frame,
            width=320,
            bg="#A1D8B5",
            borderwidth=0,
            highlightthickness=0,
            justify='center',
            font=(self.FONT, 13),
            fg=self.TEXT_COLOR,
            insertbackground=self.TEXT_COLOR,
            state='readonly',
            readonlybackground="#A1D8B5",
        )

        self.selected_type = tk.StringVar(value="Select Type")

        self.select_file_type_dropdown = ttk.Combobox(
            self.input_buttons_frame,
            textvariable=self.selected_type,
            values=["Select Type"] + list(FILE_TYPE_DICT.keys()),
            state="readonly",
            font=(self.FONT, 13),
            style='TCombobox',
            justify='center'
        )

        # Style the dropdown
        style = ttk.Style()
        style.theme_use('default')
        style.configure(
            'TCombobox',
            fieldbackground="#4CB572",
            background="#4CB572",
            foreground=self.TEXT_COLOR,
            arrowcolor=self.TEXT_COLOR,
            borderwidth=0,
            relief="flat"
        )
        style.map('TCombobox',
            fieldbackground=[('readonly', '#4CB572')],
            selectbackground=[('readonly', '#4CB572')],
            selectforeground=[('readonly', self.TEXT_COLOR)]
        )

        self.download_label = tk.Label(
            self.output_buttons_frame,
            width=95,
            height=40,
            bg="#4CB572",
            text="Download",
            font=(self.FONT, 13),
            fg=self.TEXT_COLOR
        )

        self.copy_label = tk.Label(
            self.output_buttons_frame,
            width=95,
            height=40,
            bg="#4CB572",
            text="Copy to Clipboard",
            font=(self.FONT, 13),
            fg=self.TEXT_COLOR
        )

    def _position_widgets(self):
        self.drop_label.pack(expand=True, fill="both")
        self.filename_input_text.place(x=0, y=0, width=320, height=40)
        self.copy_label.place(x=230, y=0, width=220, height=40)
        self.download_label.place(x=0, y=0, width=220, height=40)
        self.select_file_type_dropdown.place(x=0, y=0, width=120, height=40)

        self.canvas.create_window(75, 40, anchor="nw", window=self.input_frame)
        self.canvas.create_window(405, 300, anchor="nw", window=self.input_buttons_frame)
        self.canvas.create_window(75, 300, anchor="nw", window=self.filename_input_frame)
        self.canvas.create_window(75, 350, anchor="nw", window=self.output_buttons_frame)

    def _setup_drag_drop(self):
        self.drop_label.drop_target_register(DND_FILES)

    def _center_window(self):
        self.root.withdraw()
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 600) // 2
        y = (screen_height - 420) // 2
        self.root.geometry(f"600x420+{x}+{y}")
        self.root.deiconify()

    def get_current_type(self):
        return self.selected_type.get()

    def get_filename_text(self):
        return self.filename_input_text.get()

    def display_image(self, img):
        self.preview_img = img.copy()
        self.preview_img.thumbnail((self.input_frame.winfo_width(), self.input_frame.winfo_height()))
        self.preview_img = ImageTk.PhotoImage(self.preview_img)
        self.drop_label.config(image=self.preview_img, text="")

    def display_image_name(self, filename):
        self.filename_input_text.config(state='normal')
        self.filename_input_text.delete(0, tk.END)
        filename_no_ext = os.path.splitext(filename)[0]
        self.filename_input_text.insert(0, filename_no_ext)
        self.filename_input_text.config(state='normal')