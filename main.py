from core import core
from gui import gui

class Main:
    def __init__(self):
        self.app_gui = gui()
        self.app_core = core(self.app_gui)

        self.app_gui.drop_label.bind('<Button-1>', self.app_core.browse_file)
        self.app_gui.drop_label.dnd_bind('<<Drop>>', self.app_core.drop_file)
        self.app_gui.download_label.bind("<Button-1>", self.app_core.download_image)
        self.app_gui.copy_label.bind('<Button-1>', self.app_core.copy_image_to_clipboard)
        self.app_gui.root.bind('<Command-v>', self.app_core.paste_image_from_clipboard)
    
    def run(self):
        self.app_gui.root.mainloop()

if __name__ == "__main__":
    app = Main()
    app.run()