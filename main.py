import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from utils import encode_image
from gemini_caption import initialize_gemini, get_caption
from tts_converter import text_to_speech
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def browse_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if path:
        img = Image.open(path)
        img.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
        image_label.path = path

def generate_caption():
    try:
        image_path = image_label.path
        image_b64 = encode_image(image_path)
        caption = get_caption(image_b64)
        caption_text.set(caption)
        text_to_speech(caption)
        with open("caption.txt", "w") as f:
            f.write(caption)
        messagebox.showinfo("Caption Saved", "Caption saved as caption.txt and converted to speech!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Initialize Gemini with API Key loaded from .env file
initialize_gemini()

# Initialize GUI
app = tk.Tk()
app.title("Image Caption Generator")
app.geometry("400x500")

image_label = tk.Label(app)
image_label.pack(pady=10)

tk.Button(app, text="Upload Image", command=browse_image).pack()

tk.Button(app, text="Generate Caption", command=generate_caption).pack(pady=10)

caption_text = tk.StringVar()
tk.Label(app, textvariable=caption_text, wraplength=380, justify="center").pack(pady=10)

app.mainloop()
