import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageUploadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Upload App")

        # Upload Button
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=20)

        # Display Uploaded Image
        self.image_label = tk.Label(root)
        self.image_label.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            # Open and display the selected image
            image = Image.open(file_path)
            image.thumbnail((300, 300))  # Resize for display
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference to avoid garbage collection issues

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageUploadApp(root)
    root.mainloop()
