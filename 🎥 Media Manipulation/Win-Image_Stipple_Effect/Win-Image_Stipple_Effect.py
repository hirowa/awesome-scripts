import tkinter as tk
from tkinter import filedialog, Label, Button, Scale, IntVar, OptionMenu, StringVar, Entry, Frame, colorchooser
import cv2
import numpy as np
from PIL import Image, ImageTk, ImageDraw, ImageFont
import svgwrite
import os
import math
import cairosvg  # Needed for converting SVG to PNG

class StippleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Stipple Effect Editor")
        self.root.geometry("900x700")
        
        # Define heading style for all headings
        self.heading_font = ("Helvetica", 10)
        self.heading_fg = "black"
        
        # Variables for image and customization (original/default settings)
        self.image_paths = []
        self.current_image = None
        self.current_image_path = None  # store the path of the currently loaded image
        self.processed_image = None
        
        self.threshold_val = IntVar(value=14)   # Adaptive threshold constant (dot density)
        self.dot_size = tk.DoubleVar(value=1.4)    # Dot size (float: 0.1–5.0)
        self.contrast = IntVar(value=6)            # Contrast
        self.brightness = IntVar(value=0)          # Brightness
        self.spacing = tk.DoubleVar(value=3.2)      # Dot spacing (float: 1.0–5.0)
        
        self.dot_shape = StringVar(value="Square")   # Options: Circle, Square, Triangle, Character
        self.dot_char = StringVar(value="*")         # For Character shape
        
        # New: Background and dot colors (hex values)
        self.bg_color = StringVar(value="#FFFFFF")
        self.dot_color = StringVar(value="#000000")
        
        # --- Layout ---
        # GUI setup
        root.title("Stipple Effect Editor")
        control_frame = Frame(root)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Title label at top of control panel (left-justified)
        title_label = Label(control_frame, text="Advanced Stipple Effect Editor", font=("Helvetica", 14, "bold"), fg=self.heading_fg, anchor="w")
        title_label.pack(fill=tk.X, pady=(0, 10))
        
        canvas_frame = Frame(root)
        canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # a. Threshold slider
        threshold_slider = Scale(control_frame, from_=-50, to=50, orient=tk.HORIZONTAL,
                                label="Threshold (Dot Density)", variable=self.threshold_val,
                                command=lambda x: self.apply_stipple(), font=self.heading_font, fg=self.heading_fg)
        threshold_slider.pack(fill=tk.X, pady=5)

        # b. Dot Size slider
        dot_size_slider = Scale(control_frame, from_=0.1, to=5.0, resolution=0.1, orient=tk.HORIZONTAL,
                                label="Dot Size", variable=self.dot_size,
                                command=lambda x: self.apply_stipple(), font=self.heading_font, fg=self.heading_fg)
        dot_size_slider.pack(fill=tk.X, pady=5)

        # c. Dot Spacing slider
        spacing_slider = Scale(control_frame, from_=1.0, to=5.0, resolution=0.1, orient=tk.HORIZONTAL,
                            label="Dot Spacing", variable=self.spacing,
                            command=lambda x: self.apply_stipple(), font=self.heading_font, fg=self.heading_fg)
        spacing_slider.pack(fill=tk.X, pady=5)

        # d. Contrast slider
        contrast_slider = Scale(control_frame, from_=0, to=50, orient=tk.HORIZONTAL,
                                label="Contrast", variable=self.contrast,
                                command=lambda x: self.apply_stipple(), font=self.heading_font, fg=self.heading_fg)
        contrast_slider.pack(fill=tk.X, pady=5)

        # e. Brightness slider
        brightness_slider = Scale(control_frame, from_=-50, to=50, orient=tk.HORIZONTAL,
                                label="Brightness", variable=self.brightness,
                                command=lambda x: self.apply_stipple(), font=self.heading_font, fg=self.heading_fg)
        brightness_slider.pack(fill=tk.X, pady=5)

        # h. Background Color with two-column layout
        bg_color_frame = Frame(control_frame)
        bg_color_frame.pack(fill=tk.X, pady=5)

        bg_color_label = Label(bg_color_frame, text="Background Color", font=self.heading_font, fg=self.heading_fg)
        bg_color_label.grid(row=0, column=0, columnspan=2, sticky="w")

        self.bg_color_entry = Entry(bg_color_frame, textvariable=self.bg_color, font=self.heading_font)
        self.bg_color_entry.grid(row=1, column=0, sticky="ew", padx=(0, 5))

        bg_color_btn = Button(bg_color_frame, text="Pick", command=self.pick_bg_color, font=self.heading_font)
        bg_color_btn.grid(row=1, column=1, sticky="ew")

        bg_color_frame.columnconfigure(0, weight=1)
        bg_color_frame.columnconfigure(1, weight=1)

        # i. Dot Color with two-column layout
        dot_color_frame = Frame(control_frame)
        dot_color_frame.pack(fill=tk.X, pady=5)

        dot_color_label = Label(dot_color_frame, text="Dot Color", font=self.heading_font, fg=self.heading_fg)
        dot_color_label.grid(row=0, column=0, columnspan=2, sticky="w")

        self.dot_color_entry = Entry(dot_color_frame, textvariable=self.dot_color, font=self.heading_font)
        self.dot_color_entry.grid(row=1, column=0, sticky="ew", padx=(0, 5))

        dot_color_btn = Button(dot_color_frame, text="Pick", command=self.pick_dot_color, font=self.heading_font)
        dot_color_btn.grid(row=1, column=1, sticky="ew")

        dot_color_frame.columnconfigure(0, weight=1)
        dot_color_frame.columnconfigure(1, weight=1)

        # g. Dot Shape option with dot character entry (side by side, half width each)
        dot_shape_label = Label(control_frame, text="Dot Shape", font=self.heading_font, fg=self.heading_fg)
        dot_shape_label.pack(pady=(10, 0))
        dot_shape_frame = Frame(control_frame)
        dot_shape_frame.pack(pady=5, fill=tk.X)
        dot_shape_menu = OptionMenu(dot_shape_frame, self.dot_shape, "Circle", "Square", "Triangle", "Character", command=lambda x: self.toggle_dot_char_entry())
        dot_shape_menu.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 2))
        self.dot_char_entry = Entry(dot_shape_frame, textvariable=self.dot_char)
        self.dot_char_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(2, 0))
        # Disable the dot_char_entry by default (since the default shape is not "Character")
        self.dot_char_entry.config(state="disabled")

        # j. Upload button (full width)
        self.upload_btn = Button(control_frame, text="Upload Image(s)", command=self.upload_images)
        self.upload_btn.pack(pady=10, fill=tk.X)

        # k. Export button (full width) for the current image
        self.export_btn = Button(control_frame, text="Export", command=self.export_svg)
        self.export_btn.pack(pady=5, fill=tk.X)

        # New: Button to export all images with the same settings
        self.export_all_btn = Button(control_frame, text="Export All with same settings", command=self.export_all_svg)
        self.export_all_btn.pack(pady=5, fill=tk.X)

        # New: Reset button to restore original state (no uploaded images + original settings)
        self.reset_btn = Button(control_frame, text="Reset", command=self.reset)
        self.reset_btn.pack(pady=5, fill=tk.X)

        # Status label (below export buttons) with wraplength so text wraps instead of expanding sidebar
        self.status_label = Label(control_frame, text="", font=("Helvetica", 12, "bold"), wraplength=180)
        self.status_label.pack(pady=5)

        # Responsive live preview canvas on the right
        self.canvas = tk.Canvas(canvas_frame, bg=self.bg_color.get())
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Scrollable Thumbnail gallery below the preview
        self.gallery_canvas = tk.Canvas(canvas_frame, height=120)
        self.gallery_canvas.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        gallery_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.gallery_canvas.xview)
        gallery_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.gallery_canvas.configure(xscrollcommand=gallery_scrollbar.set)
        self.gallery_inner_frame = Frame(self.gallery_canvas)
        self.gallery_canvas.create_window((0, 0), window=self.gallery_inner_frame, anchor="nw")
        self.gallery_inner_frame.bind("<Configure>", lambda e: self.gallery_canvas.configure(scrollregion=self.gallery_canvas.bbox("all")))
        
        self.thumbnail_images = []
        
        # Trace changes on dot_char, bg_color, and dot_color for live updates
        self.dot_char.trace("w", lambda *args: self.apply_stipple())
        self.bg_color.trace("w", lambda *args: self.update_bg_color())
        self.dot_color.trace("w", lambda *args: self.apply_stipple())
        
    def toggle_dot_char_entry(self):
        """Enable or disable the dot character entry based on the selected dot shape."""
        if self.dot_shape.get() == "Character":
            self.dot_char_entry.config(state="normal")
        else:
            self.dot_char_entry.config(state="disabled")
        self.apply_stipple()
    
    def update_bg_color(self):
        self.canvas.config(bg=self.bg_color.get())
        self.apply_stipple()
    
    def pick_bg_color(self):
        color = tk.colorchooser.askcolor(title="Choose Background Color", initialcolor=self.bg_color.get())
        if color[1]:
            self.bg_color.set(color[1])
    
    def pick_dot_color(self):
        color = tk.colorchooser.askcolor(title="Choose Dot Color", initialcolor=self.dot_color.get())
        if color[1]:
            self.dot_color.set(color[1])
    
    def upload_images(self):
        paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
        if paths:
            self.image_paths = list(paths)
            self.update_gallery()
            self.load_image(self.image_paths[0])
    
    def update_gallery(self):
        for widget in self.gallery_inner_frame.winfo_children():
            widget.destroy()
        self.thumbnail_images = []
        thumbnail_size = (100, 100)
        for i, path in enumerate(self.image_paths):
            try:
                img = Image.open(path)
                img.thumbnail(thumbnail_size)
                img_tk = ImageTk.PhotoImage(img)
                self.thumbnail_images.append(img_tk)
                label = Label(self.gallery_inner_frame, image=img_tk, borderwidth=2, relief="solid")
                label.grid(row=0, column=i, padx=5)
                # Clicking a thumbnail simply loads the image for preview
                label.bind("<Button-1>", lambda e, p=path: self.load_image(p))
            except Exception as e:
                print(e)
    
    def load_image(self, path):
        self.current_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        self.current_image_path = path  # save the path of the currently loaded image
        self.apply_stipple()
    
    def apply_stipple(self, *args):
        if self.current_image is None:
            return
        img = self.current_image.copy()
        contrast = self.contrast.get() / 10.0
        brightness = self.brightness.get()
        img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
        thresh_const = self.threshold_val.get()
        stippled = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY, 11, thresh_const)
        self.processed_image = stippled
        self.render_preview()
    
    def render_preview(self):
        if self.processed_image is None:
            return
        h, w = self.processed_image.shape
        preview_img = Image.new("RGB", (w, h), self.bg_color.get())
        draw = ImageDraw.Draw(preview_img)
        spacing = int(round(self.spacing.get()))
        dot_size = self.dot_size.get()
        shape = self.dot_shape.get()
        # For shapes other than "Character", the default drawing works fine.
        for y in range(0, h, spacing):
            for x in range(0, w, spacing):
                if self.processed_image[y, x] == 0:
                    if shape == "Circle":
                        draw.ellipse((x - dot_size, y - dot_size, x + dot_size, y + dot_size), fill=self.dot_color.get())
                    elif shape == "Square":
                        draw.rectangle((x - dot_size, y - dot_size, x + dot_size, y + dot_size), fill=self.dot_color.get())
                    elif shape == "Triangle":
                        side = 2 * dot_size
                        height_tri = dot_size * math.sqrt(3)
                        points = [
                            (x, y - 2/3 * height_tri),
                            (x - side/2, y + 1/3 * height_tri),
                            (x + side/2, y + 1/3 * height_tri)
                        ]
                        draw.polygon(points, fill=self.dot_color.get())
                    elif shape == "Character":
                        char = self.dot_char.get() if self.dot_char.get() else "*"
                        # Calculate a dynamic font size (using 2*dot_size, with a minimum size)
                        font_size = max(int(2 * dot_size), 8)
                        try:
                            preview_font = ImageFont.truetype("arial.ttf", font_size)
                        except Exception:
                            preview_font = ImageFont.load_default()
                        text_w, text_h = draw.textsize(char, font=preview_font)
                        draw.text((x - text_w/2, y - text_h/2), char, fill=self.dot_color.get(), font=preview_font)
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        preview_img.thumbnail((canvas_width, canvas_height))
        img_tk = ImageTk.PhotoImage(preview_img)
        self.canvas.delete("all")
        self.canvas.create_image(canvas_width // 2, canvas_height // 2, image=img_tk, anchor=tk.CENTER)
        self.canvas.image = img_tk
    
    def export_svg(self):
        """Export the currently displayed image as an SVG and a PNG using its original filename."""
        if self.current_image is None or not self.current_image_path:
            return
        export_dir = filedialog.askdirectory(title="Select Folder to Export SVG & PNG")
        if not export_dir:
            return
        # Reprocess the current image using the current settings
        path = self.current_image_path
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        contrast = self.contrast.get() / 10.0
        brightness = self.brightness.get()
        img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
        thresh_const = self.threshold_val.get()
        stippled = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY, 11, thresh_const)
        h, w = stippled.shape
        spacing = float(self.spacing.get())
        dot_size = self.dot_size.get()
        shape = self.dot_shape.get()
        basename = os.path.splitext(os.path.basename(path))[0]
        svg_filename = basename + ".svg"
        svg_filepath = os.path.join(export_dir, svg_filename)
        dwg = svgwrite.Drawing(svg_filepath, size=(w, h))
        dwg.add(dwg.rect(insert=(0, 0), size=(w, h), fill=self.bg_color.get()))
        for y in range(0, h, int(round(spacing))):
            for x in range(0, w, int(round(spacing))):
                if stippled[y, x] == 0:
                    if shape == "Circle":
                        dwg.add(dwg.circle(center=(x, y), r=dot_size, fill=self.dot_color.get()))
                    elif shape == "Square":
                        dwg.add(dwg.rect(insert=(x - dot_size, y - dot_size), size=(2 * dot_size, 2 * dot_size), fill=self.dot_color.get()))
                    elif shape == "Triangle":
                        side = 2 * dot_size
                        height_tri = dot_size * math.sqrt(3)
                        points = [
                            (x, y - 2/3 * height_tri),
                            (x - side/2, y + 1/3 * height_tri),
                            (x + side/2, y + 1/3 * height_tri)
                        ]
                        dwg.add(dwg.polygon(points=points, fill=self.dot_color.get()))
                    elif shape == "Character":
                        char = self.dot_char.get() if self.dot_char.get() else "*"
                        dwg.add(dwg.text(char, insert=(x, y), fill=self.dot_color.get(),
                                         style=f"font-size:{2 * dot_size}px; text-anchor: middle; dominant-baseline: central"))
        dwg.save()
        
        # Convert the saved SVG to PNG using CairoSVG
        png_filename = basename + ".png"
        png_filepath = os.path.join(export_dir, png_filename)
        try:
            cairosvg.svg2png(url=svg_filepath, write_to=png_filepath)
        except Exception as e:
            print("Error converting SVG to PNG:", e)
        
        self.status_label.config(text=f"Exported current image as {svg_filename} and {png_filename} to {export_dir}")
    
    def export_all_svg(self):
        """Export all uploaded images as SVG and PNG using their original filenames."""
        if not self.image_paths:
            return
        export_dir = filedialog.askdirectory(title="Select Folder to Export SVG & PNG Files")
        if not export_dir:
            return
        spacing = float(self.spacing.get())
        dot_size = self.dot_size.get()
        shape = self.dot_shape.get()
        count = 0
        for path in self.image_paths:
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            contrast = self.contrast.get() / 10.0
            brightness = self.brightness.get()
            img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
            thresh_const = self.threshold_val.get()
            stippled = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY, 11, thresh_const)
            h, w = stippled.shape
            basename = os.path.splitext(os.path.basename(path))[0]
            svg_filename = basename + ".svg"
            svg_filepath = os.path.join(export_dir, svg_filename)
            dwg = svgwrite.Drawing(svg_filepath, size=(w, h))
            dwg.add(dwg.rect(insert=(0, 0), size=(w, h), fill=self.bg_color.get()))
            for y in range(0, h, int(round(spacing))):
                for x in range(0, w, int(round(spacing))):
                    if stippled[y, x] == 0:
                        if shape == "Circle":
                            dwg.add(dwg.circle(center=(x, y), r=dot_size, fill=self.dot_color.get()))
                        elif shape == "Square":
                            dwg.add(dwg.rect(insert=(x - dot_size, y - dot_size), size=(2 * dot_size, 2 * dot_size), fill=self.dot_color.get()))
                        elif shape == "Triangle":
                            side = 2 * dot_size
                            height_tri = dot_size * math.sqrt(3)
                            points = [
                                (x, y - 2/3 * height_tri),
                                (x - side/2, y + 1/3 * height_tri),
                                (x + side/2, y + 1/3 * height_tri)
                            ]
                            dwg.add(dwg.polygon(points=points, fill=self.dot_color.get()))
                        elif shape == "Character":
                            char = self.dot_char.get() if self.dot_char.get() else "*"
                            dwg.add(dwg.text(char, insert=(x, y), fill=self.dot_color.get(),
                                             style=f"font-size:{2 * dot_size}px; text-anchor: middle; dominant-baseline: central"))
            dwg.save()
            # Convert SVG to PNG
            png_filename = basename + ".png"
            png_filepath = os.path.join(export_dir, png_filename)
            try:
                cairosvg.svg2png(url=svg_filepath, write_to=png_filepath)
            except Exception as e:
                print("Error converting SVG to PNG:", e)
            count += 1
        self.status_label.config(text=f"Exported {count} SVG/PNG file pairs to {export_dir}")
    
    def reset(self):
        """Reset the interface to its original state: no uploaded images and default settings."""
        self.image_paths = []
        self.current_image = None
        self.current_image_path = None
        # Clear any thumbnails in the gallery
        for widget in self.gallery_inner_frame.winfo_children():
            widget.destroy()
        self.thumbnail_images = []
        # Reset all control variables to their defaults
        self.threshold_val.set(14)
        self.dot_size.set(1.4)
        self.contrast.set(6)
        self.brightness.set(0)
        self.spacing.set(3.2)
        self.dot_shape.set("Square")
        self.dot_char.set("*")
        self.bg_color.set("#FFFFFF")
        self.dot_color.set("#000000")
        self.dot_char_entry.config(state="disabled")  # Ensure it's disabled since dot_shape is "Square"
        self.canvas.delete("all")
        self.status_label.config(text="Reset to original state.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StippleApp(root)
    root.mainloop()
