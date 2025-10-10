# Desktop Image Converter

A lightweight desktop application for converting images between different formats with a simple drag-and-drop interface.

## Features

- **Multiple Input Methods**: Drag & drop, file browser, or paste images directly
- **Format Support**: Convert between JPEG, JPG, PNG, HEIC, and HEIF formats
- **Image Preview**: View your image before conversion
- **Quick Actions**: Download converted images or copy them directly to clipboard
- **Custom Naming**: Rename your files before saving
- **Simple Interface**: Clean, user-friendly design with minimal clicks required

## Supported Formats

- **Input**: JPEG, JPG, PNG, HEIC, HEIF
- **Output**: JPEG, JPG, PNG, HEIC, HEIF

## Usage


1. Load an image using one of these methods:
   - **Drag & Drop**: Drag an image file onto the drop area
   - **Click to Browse**: Click the drop area to open a file browser
   - **Paste**: Paste an image from your clipboard

2. Edit the filename (optional)

3. Select your desired output format from the dropdown menu

4. Choose an action:
   - **Download**: Save the converted image to your Downloads folder
   - **Copy to Clipboard**: Copy the converted image directly to your clipboard

## How It Works

- **main.py**: Initializes the application and connects the GUI with core functionality
- **gui.py**: Handles all visual elements, window creation, and widget positioning
- **core.py**: Manages image processing, file operations, and format conversion

## Notes

- Converted images are automatically saved to your Downloads folder
- Images are copied to clipboard as image.png