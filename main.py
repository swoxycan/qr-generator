import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk
import os

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("500x600") 

        self.url_label = ctk.CTkLabel(root, text="Enter URL:")
        self.url_label.pack(pady=10)

        self.url_entry = ctk.CTkEntry(root, width=300)
        self.url_entry.pack(pady=10)

        self.generate_button = ctk.CTkButton(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        self.qr_image = None
        self.qr_image_label = ctk.CTkLabel(root)
        self.qr_image_label.pack(pady=10)

    def generate_qr_code(self):
        url = self.url_entry.get()
        if url:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)

            self.qr_image = qr.make_image(fill_color="black", back_color="white")

            self.qr_image.save("qr.png")

            self.display_qr_code()

    def display_qr_code(self):
        self.qr_image = self.qr_image.convert("RGB") 
        self.qr_image_tk = ImageTk.PhotoImage(self.qr_image) 

        self.qr_image_label.configure(image=self.qr_image_tk)
        self.qr_image_label.image = self.qr_image_tk 

    def save_qr_code(self):
        if self.qr_image:
            self.qr_image.save("qr.png")  
            print("QR code saved as qr.png")

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = QRCodeApp(root)
    root.mainloop()