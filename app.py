import tkinter as tk
from tkinter import filedialog,END
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
   
        # Watermark Image
        self.watermark_image = Image.open(self.file_path)  # Replace with your watermark image
        self.watermark_image = self.watermark_image.resize((300, 300))
        self.watermark_image = ImageTk.PhotoImage(self.watermark_image)
        self.watermark_label = tk.Label(root, image=self.watermark_image)
        self.watermark_label.pack(pady=10)


        self.water_input_path = self.file_path
        self.water_output_path = f"{os.path.splitext(self.water_input_path)[0]}_water.png"
        self.water_text = "Map Am"

    def add_watermark(self,input_image_path, output_image_path, watermark_text):
        # Open the image
        original_image = Image.open(input_image_path)
        original_image.thumbnail((300, 300))


        # Create a drawing object
        draw = ImageDraw.Draw(original_image)

        # Choose a font and size for the watermark
        font = ImageFont.load_default()  # You can replace this with your preferred font
        font_size = 20

        # Get the font size in pixels
        font_size_pixels = int(original_image.height * font_size / 100)  # Adjust as needed

        # Load the font
        font = ImageFont.truetype("arial.ttf", font_size_pixels)

        # Calculate the position to center the watermark
        watermark_text_size = draw.textlength(watermark_text, font)
        # watermark_width, watermark_height = watermark_text_size
        x = (original_image.width - watermark_text_size) // 2
        y = (original_image.height - watermark_text_size) // 2

        # Add the watermark text to the image
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

        # Save the watermarked image
        original_image.save(output_image_path)


if __name__ == "__main__":
    root = tk.Tk()
    root.wait_visibility() 
    app = WatermarkApp(root)
    button = tk.Button(root, text="Add Watermark", command=app.add_watermark(
    app.water_input_path,app.water_output_path,app.water_text))
    button.pack(pady=10)
    root.mainloop()
