import tkinter as tk
from PIL import Image, ImageTk
import random

class BouncingBurgerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Burger")

        self.canvas_width = 800
        self.canvas_height = 600
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Load burger image
        self.burger_image = Image.open("burger.png").resize((100, 100))  # Resize if needed
        self.burger_photo = ImageTk.PhotoImage(self.burger_image)

        # Create burger on canvas
        self.burger = self.canvas.create_image(100, 100, image=self.burger_photo, anchor="nw")

        # Add name label (on top of burger)
        self.name_text = self.canvas.create_text(150, 150, text="Daluperit Japhet", fill="black", font=("Arial", 16, "bold"))

        # Animation variables
        self.dx = 5
        self.dy = 5
        self.paused = False

        # Start animation
        self.animate()

        # Keyboard bindings
        self.root.bind("<space>", self.toggle_pause)

    def animate(self):
        if not self.paused:
            self.canvas.move(self.burger, self.dx, self.dy)
            self.canvas.move(self.name_text, self.dx, self.dy)

            # Get coordinates
            bx1, by1 = self.canvas.coords(self.burger)

            # Edge checking
            if bx1 <= 0 or bx1 + 100 >= self.canvas_width:
                self.dx *= -1
                self.change_text_color()
            if by1 <= 0 or by1 + 100 >= self.canvas_height:
                self.dy *= -1
                self.change_text_color()

        # Schedule next frame
        self.root.after(16, self.animate)  # ~60 FPS

    def change_text_color(self):
        # Random color in hex
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        self.canvas.itemconfig(self.name_text, fill=color)

    def toggle_pause(self, event):
        self.paused = not self.paused

if __name__ == "__main__":
    root = tk.Tk()
    app = BouncingBurgerApp(root)
    root.mainloop()
