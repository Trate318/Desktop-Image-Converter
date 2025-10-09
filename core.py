from PIL import Image
import pillow_heif
import os
from tkinter import filedialog

pillow_heif.register_heif_opener()

FILE_TYPE_DICT = {
    'jpeg': 'JPEG',
    'jpg': 'JPEG',
    'png': 'PNG',
    'heic': 'HEIF',
    'heif': 'HEIF',
}

class core:
    def __init__(self, gui_instance):
        self.gui = gui_instance
        self.current_img = None

    def browse_file(self, event=None):
        filepath = filedialog.askopenfilename(
            title="Select an Image",
            initialdir=os.path.expanduser("~")
        )
        if filepath:
            self.current_img = Image.open(filepath)
            self.gui.display_image_name(os.path.basename(filepath))
            self.gui.display_image(self.current_img)

    def drop_file(self, event):
        filepath = event.data.strip('{}')
        self.current_img = Image.open(filepath)
        self.gui.display_image_name(os.path.basename(filepath))
        self.gui.display_image(self.current_img)

    def download_image(self, event=None):
        if self.current_img:
            new_filename = self.gui.get_filename_text()
            current_type = self.gui.get_current_type()
            
            if new_filename and current_type != "Select Type":
                downloads_path = os.path.expanduser("~/Downloads")
                converted_img = self.convert(self.current_img)
                converted_img.save(
                    os.path.join(downloads_path, f"{new_filename}.{current_type}"),
                    format=FILE_TYPE_DICT[current_type]
                )

    def convert(self, image: Image):
        if image.format == 'PNG':
            return image.convert('RGB')
        return image

    def copy_image_to_clipboard(self, event=None):
        if self.current_img:
            pass