import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])


        # File Upload
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=10)

        # Watermark Text Input
        self.watermark_entry = tk.Entry(root, width=30)
        self.watermark_entry.pack(pady=10)

        # Watermark Image
        self.watermark_image = Image.open("C:\\Users\\Intern\\Pictures\\lexim.png")  # Replace with your watermark image
        self.watermark_image = self.watermark_image.resize((100, 100))
        self.watermark_image = ImageTk.PhotoImage(self.watermark_image)
        self.watermark_label = tk.Label(root, image=self.watermark_image)
        self.watermark_label.pack(pady=10)

        # Process Button
        self.water_input_path = "C:\\Users\\Intern\\Pictures\\lexim.png"
        self.water_output_path = "C:\\Users\\Intern\\Pictures\\leximwat.png"
        self.water_text = "Working"
        self.process_btn = tk.Button(root, text="Add Watermark", command=self.add_watermark(
            self.water_input_path,self.water_output_path,self.water_text))
        self.process_btn.pack(pady=10)

    def upload_image(self):
        if self.file_path:
            self.original_image = Image.open(self.file_path)
            self.original_image.thumbnail((300, 300))
            self.display_image = ImageTk.PhotoImage(self.original_image)
            
            self.image_label = tk.Label(root, image=self.display_image)
            self.image_label.pack(pady=10)



    def add_watermark(self,input_image_path, output_image_path, watermark_text):
        # Open the image
        original_image = Image.open(input_image_path)

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
    app = WatermarkApp(root)
    root.mainloop()
