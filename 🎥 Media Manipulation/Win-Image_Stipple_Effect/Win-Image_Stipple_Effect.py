import tkinter as tk
from tkinter import filedialog, Label, Button, Scale, IntVar, OptionMenu, StringVar, Entry, Frame, colorchooser, Checkbutton
from tkinter.scrolledtext import ScrolledText
import cv2
import numpy as np
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageOps
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
        
        # Always-visible threshold slider variable (used for both adaptive thresholding and dithering)
        self.threshold_val = IntVar(value=14)
        # Settings available only when dithering method is "None"
        self.dot_size = tk.DoubleVar(value=1.4)    
        self.contrast = IntVar(value=6)            
        self.brightness = IntVar(value=0)          
        self.spacing = tk.DoubleVar(value=3.2)      
        
        self.dot_shape = StringVar(value="Square")   # Options: Circle, Square, Triangle, Character
        self.dot_char = StringVar(value="*")         # For Character shape
        
        # Background and dot colors (hex values)
        self.bg_color = StringVar(value="#FFFFFF")
        self.dot_color = StringVar(value="#000000")
        
        # Export background toggle (True: include background; False: transparent)
        self.export_with_bg = tk.BooleanVar(value=True)
        
        # Reverse Colors toggle variable
        self.reverse_colors = tk.BooleanVar(value=False)
        
        # Export format option (choose "Both", "SVG", or "PNG")
        self.export_format = StringVar(value="Both")
        
        # Dithering method selection ("None", "Bayer", "Floyd-Steinberg", "Atkinson")
        self.dithering_method = StringVar(value="None")
        
        # --- Layout ---
        # Create the sidebar control frame with a fixed narrow width.
        self.control_frame = Frame(root, width=400)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        # Prevent the frame from expanding to its contents.
        self.control_frame.pack_propagate(False)
        
        canvas_frame = Frame(root)
        canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title label
        title_label = Label(self.control_frame, text="Advanced Stipple Effect Editor", font=("Helvetica", 14, "bold"),
                            fg=self.heading_fg, anchor="w")
        title_label.pack(fill=tk.X, pady=(0, 10))
        
        # Dithering Method Option (always shown)
        dither_label = Label(self.control_frame, text="Dithering Method", font=self.heading_font, fg=self.heading_fg, anchor="w")
        dither_label.pack(fill=tk.X, pady=(10, 0))
        dither_menu = OptionMenu(self.control_frame, self.dithering_method, "None", "Bayer", "Floyd-Steinberg", "Atkinson",
                                 command=lambda x: [self.update_none_settings_visibility(), self.apply_stipple(), self.update_status(f'Dithering method set to "{x}"', clear=False)])
        dither_menu.config(font=self.heading_font, fg=self.heading_fg)
        dither_menu.pack(fill=tk.X, pady=5)
        
        # Threshold slider (always visible)
        threshold_slider = Scale(self.control_frame, from_=-50, to=255, orient=tk.HORIZONTAL,
                                 label="Threshold", variable=self.threshold_val,
                                 command=lambda x: self.apply_stipple(), font=self.heading_font, fg=self.heading_fg)
        threshold_slider.pack(fill=tk.X, pady=5)
        
        # Create a container for settings that apply only when dithering is "None"
        self.none_settings_frame = Frame(self.control_frame)
        self.none_settings_frame.pack(fill=tk.X)
        
        # Dot Size slider
        self.dot_size_slider = Scale(self.none_settings_frame, from_=0.1, to=5.0, resolution=0.1, orient=tk.HORIZONTAL,
                                     label="Dot Size", variable=self.dot_size,
                                     command=lambda x: self.apply_stipple(), font=self.heading_font, fg=self.heading_fg)
        self.dot_size_slider.pack(fill=tk.X, pady=5)
        
        # Dot Spacing slider
        self.spacing_slider = Scale(self.none_settings_frame, from_=0.1, to=5.0, resolution=0.1, orient=tk.HORIZONTAL,
                                    label="Dot Spacing", variable=self.spacing,
                                    command=lambda x: self.apply_stipple(), font=self.heading_font, fg=self.heading_fg)
        self.spacing_slider.pack(fill=tk.X, pady=5)
        
        # Contrast slider
        self.contrast_slider = Scale(self.none_settings_frame, from_=0, to=50, orient=tk.HORIZONTAL,
                                     label="Contrast", variable=self.contrast,
                                     command=lambda x: self.apply_stipple(), font=self.heading_font, fg=self.heading_fg)
        self.contrast_slider.pack(fill=tk.X, pady=5)
        
        # Brightness slider
        self.brightness_slider = Scale(self.none_settings_frame, from_=-50, to=50, orient=tk.HORIZONTAL,
                                       label="Brightness", variable=self.brightness,
                                       command=lambda x: self.apply_stipple(), font=self.heading_font, fg=self.heading_fg)
        self.brightness_slider.pack(fill=tk.X, pady=5)
        
        # Dot Shape and Dot Character (only for "None")
        self.dot_shape_label = Label(self.none_settings_frame, text="Dot Shape", font=self.heading_font, fg=self.heading_fg, anchor="w")
        self.dot_shape_label.pack(pady=(10, 0))
        self.dot_shape_frame = Frame(self.none_settings_frame)
        self.dot_shape_frame.pack(pady=5, fill=tk.X)
        self.dot_shape_menu = OptionMenu(self.dot_shape_frame, self.dot_shape, "Circle", "Square", "Triangle", "Character",
                                         command=lambda x: self.toggle_dot_char_entry())
        self.dot_shape_menu.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 2))
        self.dot_char_entry = Entry(self.dot_shape_frame, textvariable=self.dot_char)
        self.dot_char_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(2, 0))
        self.dot_char_entry.config(state="disabled")
        
        # Background Color (two-column layout)
        self.bg_color_frame = Frame(self.control_frame)
        self.bg_color_frame.pack(fill=tk.X, pady=5)
        bg_color_label = Label(self.bg_color_frame, text="Background Color", font=self.heading_font, fg=self.heading_fg)
        bg_color_label.grid(row=0, column=0, columnspan=2, sticky="w")
        self.bg_color_entry = Entry(self.bg_color_frame, textvariable=self.bg_color, font=self.heading_font)
        self.bg_color_entry.grid(row=1, column=0, sticky="ew", padx=(0, 5))
        bg_color_btn = Button(self.bg_color_frame, text="Pick", command=self.pick_bg_color, font=self.heading_font)
        bg_color_btn.grid(row=1, column=1, sticky="ew")
        self.bg_color_frame.columnconfigure(0, weight=1)
        self.bg_color_frame.columnconfigure(1, weight=1)
        
        # Export with Background toggle
        export_bg_check = Checkbutton(self.control_frame, text="Export with Background", variable=self.export_with_bg,
                                      command=lambda: [self.apply_stipple(), self.update_status("Export with background toggled.", clear=False)],
                                      font=self.heading_font, fg=self.heading_fg, anchor="w")
        export_bg_check.pack(fill=tk.X, pady=5)
        
        # Reverse Colors toggle
        reverse_colors_check = Checkbutton(self.control_frame, text="Reverse Colors", variable=self.reverse_colors,
                                      command=lambda: [self.apply_stipple(), self.update_status("Reverse colors toggled.", clear=False)],
                                      font=self.heading_font, fg=self.heading_fg, anchor="w")
        reverse_colors_check.pack(fill=tk.X, pady=5)
        
        # Export Format option (always visible)
        export_format_label = Label(self.control_frame, text="Export Format", font=self.heading_font, fg=self.heading_fg, anchor="w")
        export_format_label.pack(fill=tk.X, pady=(10, 0))
        export_format_menu = OptionMenu(self.control_frame, self.export_format, "Both", "SVG", "PNG")
        export_format_menu.config(font=self.heading_font, fg=self.heading_fg)
        export_format_menu.pack(fill=tk.X, pady=5)
        
        # Dot Color (two-column layout)
        dot_color_frame = Frame(self.control_frame)
        dot_color_frame.pack(fill=tk.X, pady=5)
        dot_color_label = Label(dot_color_frame, text="Dot Color", font=self.heading_font, fg=self.heading_fg)
        dot_color_label.grid(row=0, column=0, columnspan=2, sticky="w")
        self.dot_color_entry = Entry(dot_color_frame, textvariable=self.dot_color, font=self.heading_font)
        self.dot_color_entry.grid(row=1, column=0, sticky="ew", padx=(0, 5))
        dot_color_btn = Button(dot_color_frame, text="Pick", command=self.pick_dot_color, font=self.heading_font)
        dot_color_btn.grid(row=1, column=1, sticky="ew")
        dot_color_frame.columnconfigure(0, weight=1)
        dot_color_frame.columnconfigure(1, weight=1)
        
        # Upload and Export buttons
        self.upload_btn = Button(self.control_frame, text="Upload Image(s)", command=self.upload_images)
        self.upload_btn.pack(pady=10, fill=tk.X)
        self.export_btn = Button(self.control_frame, text="Export", command=self.export_svg)
        self.export_btn.pack(pady=5, fill=tk.X)
        self.export_all_btn = Button(self.control_frame, text="Export All (Same Settings)", command=self.export_all_svg)
        self.export_all_btn.pack(pady=5, fill=tk.X)
        self.reset_btn = Button(self.control_frame, text="Reset", command=self.reset)
        self.reset_btn.pack(pady=5, fill=tk.X)
        
        # Status area: a scrollable text widget for messages
        self.status_text = ScrolledText(self.control_frame, wrap=tk.WORD, height=6, font=("Helvetica", 12, "bold"))
        self.status_text.pack(pady=5, fill=tk.X)
        self.status_text.config(state=tk.DISABLED)
        
        # Live preview canvas
        self.canvas = tk.Canvas(canvas_frame, bg=self.safe_hex_color(self.bg_color.get(), "#FFFFFF"))
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Scrollable Thumbnail gallery
        self.gallery_canvas = tk.Canvas(canvas_frame, height=120)
        self.gallery_canvas.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        gallery_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.gallery_canvas.xview)
        gallery_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.gallery_canvas.configure(xscrollcommand=gallery_scrollbar.set)
        self.gallery_inner_frame = Frame(self.gallery_canvas)
        self.gallery_canvas.create_window((0, 0), window=self.gallery_inner_frame, anchor="nw")
        self.gallery_inner_frame.bind("<Configure>", lambda e: self.gallery_canvas.configure(scrollregion=self.gallery_canvas.bbox("all")))
        
        self.thumbnail_images = []
        
        # Trace changes for live updates
        self.dot_char.trace("w", lambda *args: self.apply_stipple())
        self.bg_color.trace("w", lambda *args: [self.update_bg_color(), self.update_status("Background color updated.", clear=False)])
        self.dot_color.trace("w", lambda *args: self.apply_stipple())
        
        # Initially update visibility of none_settings_frame
        self.update_none_settings_visibility()
        self.update_status("Ready.", clear=True)
    
    def safe_hex_color(self, hex_color, default):
        """Ensure the hex color string is valid; otherwise return default."""
        color = hex_color.strip()
        if color.startswith("#"):
            color = color[1:]
        if len(color) != 6:
            return default
        try:
            int(color, 16)
        except ValueError:
            return default
        return "#" + color.upper()
    
    def hex_to_rgb(self, hex_color):
        safe_color = self.safe_hex_color(hex_color, "#000000")
        safe_color = safe_color.lstrip('#')
        return tuple(int(safe_color[i:i+2], 16) for i in (0, 2, 4))
    
    def invert_hex_color(self, hex_color):
        safe_color = self.safe_hex_color(hex_color, "#000000")
        safe_color = safe_color.lstrip('#')
        try:
            r = 255 - int(safe_color[0:2], 16)
            g = 255 - int(safe_color[2:4], 16)
            b = 255 - int(safe_color[4:6], 16)
        except ValueError:
            r, g, b = 255, 255, 255
        return f"#{r:02X}{g:02X}{b:02X}"
    
    def update_none_settings_visibility(self):
        if self.dithering_method.get() == "None":
            if not self.none_settings_frame.winfo_ismapped():
                self.none_settings_frame.pack(before=self.bg_color_frame, fill=tk.X)
        else:
            self.none_settings_frame.pack_forget()
    
    def update_status(self, message, clear=False):
        self.status_text.config(state=tk.NORMAL)
        if clear:
            self.status_text.delete("1.0", tk.END)
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)
    
    def toggle_dot_char_entry(self):
        if self.dot_shape.get() == "Character":
            self.dot_char_entry.config(state="normal")
        else:
            self.dot_char_entry.config(state="disabled")
        self.apply_stipple()
    
    def update_bg_color(self):
        valid_bg = self.safe_hex_color(self.bg_color.get(), "#FFFFFF")
        self.bg_color.set(valid_bg)
        self.canvas.config(bg=valid_bg)
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
            self.update_status(f"Uploaded {len(self.image_paths)} image(s).", clear=False)
        else:
            self.update_status("No image selected.", clear=False)
    
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
                label.bind("<Button-1>", lambda e, p=path: self.load_image(p))
            except Exception as e:
                self.update_status(f"Error loading thumbnail: {e}", clear=False)
    
    def load_image(self, path):
        try:
            self.current_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            self.current_image_path = path
            self.apply_stipple()
            self.update_status(f"Loaded image: {os.path.basename(path)}", clear=False)
        except Exception as e:
            self.update_status(f"Error loading image: {e}", clear=False)
    
    def apply_stipple(self, *args):
        if self.current_image is None:
            self.update_status("No image loaded to process.", clear=False)
            return
        img = self.current_image.copy()
        if self.dithering_method.get() == "None":
            contrast = self.contrast.get() / 10.0
            brightness = self.brightness.get()
            img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
            thresh_const = self.threshold_val.get()
            stippled = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, 11, thresh_const)
        else:
            if self.dithering_method.get() == "Bayer":
                stippled = self.bayer_dithering(img)
            elif self.dithering_method.get() == "Floyd-Steinberg":
                stippled = self.floyd_steinberg_dithering(img)
            elif self.dithering_method.get() == "Atkinson":
                stippled = self.atkinson_dithering(img)
            else:
                stippled = img
        self.processed_image = stippled
        self.render_preview()
    
    def bayer_dithering(self, img):
        bayerThresholdMap = np.array([
            [15, 135, 45, 165],
            [195, 75, 225, 105],
            [60, 180, 30, 150],
            [240, 120, 210, 90]
        ], dtype=np.float32)
        h, w = img.shape
        tiled = np.tile(bayerThresholdMap, (h // 4 + 1, w // 4 + 1))[:h, :w]
        map_matrix = ((img.astype(np.float32) + tiled) / 2.0)
        threshold = self.threshold_val.get()
        dithered = np.where(map_matrix < threshold, 0, 255).astype(np.uint8)
        return dithered
    
    def floyd_steinberg_dithering(self, img):
        dithered = img.astype(np.float64)
        h, w = dithered.shape
        threshold = self.threshold_val.get()
        for y in range(h):
            for x in range(w):
                old_pixel = dithered[y, x]
                new_pixel = 0 if old_pixel < threshold else 255
                dithered[y, x] = new_pixel
                error = math.floor((old_pixel - new_pixel) / 16)
                if x + 1 < w:
                    dithered[y, x + 1] += error * 7
                if y + 1 < h and x > 0:
                    dithered[y + 1, x - 1] += error * 3
                if y + 1 < h:
                    dithered[y + 1, x] += error * 5
                if y + 1 < h and x + 1 < w:
                    dithered[y + 1, x + 1] += error * 1
        dithered = np.clip(dithered, 0, 255)
        return dithered.astype(np.uint8)
    
    def atkinson_dithering(self, img):
        dithered = img.astype(np.float64)
        h, w = dithered.shape
        threshold = self.threshold_val.get()
        for y in range(h):
            for x in range(w):
                old_pixel = dithered[y, x]
                new_pixel = 0 if old_pixel < threshold else 255
                error = math.floor((old_pixel - new_pixel) / 8)
                dithered[y, x] = new_pixel
                for dx, dy in [(1, 0), (2, 0), (-1, 1), (0, 1), (1, 1), (0, 2)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        dithered[ny, nx] += error
        dithered = np.clip(dithered, 0, 255)
        return dithered.astype(np.uint8)
    
    def render_preview(self):
        if self.processed_image is None:
            return
        h, w = self.processed_image.shape
        if self.reverse_colors.get():
            dot_color_used = self.invert_hex_color(self.dot_color.get())
            bg_color_used = self.invert_hex_color(self.bg_color.get())
        else:
            dot_color_used = self.safe_hex_color(self.dot_color.get(), "#000000")
            bg_color_used = self.safe_hex_color(self.bg_color.get(), "#FFFFFF")
        if self.dithering_method.get() == "None":
            preview_img = Image.new("RGB", (w, h), bg_color_used)
            draw = ImageDraw.Draw(preview_img)
            spacing = self.spacing.get()
            dot_size = self.dot_size.get()
            shape = self.dot_shape.get()
            for y in np.arange(0, h, spacing):
                for x in np.arange(0, w, spacing):
                    if self.processed_image[int(y), int(x)] == 0:
                        if shape == "Circle":
                            draw.ellipse((x - dot_size, y - dot_size, x + dot_size, y + dot_size),
                                         fill=dot_color_used)
                        elif shape == "Square":
                            draw.rectangle((x - dot_size, y - dot_size, x + dot_size, y + dot_size),
                                           fill=dot_color_used)
                        elif shape == "Triangle":
                            side = 2 * dot_size
                            height_tri = dot_size * math.sqrt(3)
                            points = [
                                (x, y - 2/3 * height_tri),
                                (x - side/2, y + 1/3 * height_tri),
                                (x + side/2, y + 1/3 * height_tri)
                            ]
                            draw.polygon(points, fill=dot_color_used)
                        elif shape == "Character":
                            char = self.dot_char.get() if self.dot_char.get() else "*"
                            font_size = max(int(2 * dot_size), 8)
                            try:
                                preview_font = ImageFont.truetype("arial.ttf", font_size)
                            except Exception:
                                preview_font = ImageFont.load_default()
                            text_w, text_h = draw.textsize(char, font=preview_font)
                            draw.text((x - text_w/2, y - text_h/2), char, fill=dot_color_used, font=preview_font)
            # Optionally add overlay text (comment out if not needed)
            overlay_text = f"Dot Size: {self.dot_size.get():.2f}, Spacing: {self.spacing.get():.2f}"
            try:
                overlay_font = ImageFont.truetype("arial.ttf", 12)
            except Exception:
                overlay_font = ImageFont.load_default()
            draw.text((10, 10), overlay_text, fill="red", font=overlay_font)
        else:
            dot_rgb = self.hex_to_rgb(dot_color_used)
            bg_rgb = self.hex_to_rgb(bg_color_used)
            binary = self.processed_image
            preview_array = np.zeros((h, w, 3), dtype=np.uint8)
            preview_array[binary == 0] = dot_rgb
            preview_array[binary != 0] = bg_rgb
            preview_img = Image.fromarray(preview_array, "RGB")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        preview_img.thumbnail((canvas_width, canvas_height))
        img_tk = ImageTk.PhotoImage(preview_img)
        self.canvas.delete("all")
        self.canvas.create_image(canvas_width // 2, canvas_height // 2, image=img_tk, anchor=tk.CENTER)
        self.canvas.image = img_tk
    
    def create_png_image(self, stippled, h, w):
        """Create a full-resolution PIL image from the processed (stippled) data."""
        if self.reverse_colors.get():
            dot_color_used = self.invert_hex_color(self.dot_color.get())
            bg_color_used = self.invert_hex_color(self.bg_color.get())
        else:
            dot_color_used = self.safe_hex_color(self.dot_color.get(), "#000000")
            bg_color_used = self.safe_hex_color(self.bg_color.get(), "#FFFFFF")
        if self.dithering_method.get() == "None":
            final_img = Image.new("RGB", (w, h), bg_color_used)
            draw = ImageDraw.Draw(final_img)
            spacing = self.spacing.get()
            dot_size = self.dot_size.get()
            shape = self.dot_shape.get()
            for y in np.arange(0, h, spacing):
                for x in np.arange(0, w, spacing):
                    if stippled[int(y), int(x)] == 0:
                        if shape == "Circle":
                            draw.ellipse((x - dot_size, y - dot_size, x + dot_size, y + dot_size), fill=dot_color_used)
                        elif shape == "Square":
                            draw.rectangle((x - dot_size, y - dot_size, x + dot_size, y + dot_size), fill=dot_color_used)
                        elif shape == "Triangle":
                            side = 2 * dot_size
                            height_tri = dot_size * math.sqrt(3)
                            points = [
                                (x, y - 2/3 * height_tri),
                                (x - side/2, y + 1/3 * height_tri),
                                (x + side/2, y + 1/3 * height_tri)
                            ]
                            draw.polygon(points, fill=dot_color_used)
                        elif shape == "Character":
                            char = self.dot_char.get() if self.dot_char.get() else "*"
                            font_size = max(int(2 * dot_size), 8)
                            try:
                                preview_font = ImageFont.truetype("arial.ttf", font_size)
                            except Exception:
                                preview_font = ImageFont.load_default()
                            text_w, text_h = draw.textsize(char, font=preview_font)
                            draw.text((x - text_w/2, y - text_h/2), char, fill=dot_color_used, font=preview_font)
            return final_img
        else:
            dot_rgb = self.hex_to_rgb(dot_color_used)
            bg_rgb = self.hex_to_rgb(bg_color_used)
            preview_array = np.zeros((h, w, 3), dtype=np.uint8)
            preview_array[stippled == 0] = dot_rgb
            preview_array[stippled != 0] = bg_rgb
            final_img = Image.fromarray(preview_array, "RGB")
            return final_img
    
    def process_image(self, path):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            self.update_status(f"Warning: Could not open image {path}", clear=False)
            return None
        if self.dithering_method.get() == "None":
            contrast = self.contrast.get() / 10.0
            brightness = self.brightness.get()
            img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
            thresh_const = self.threshold_val.get()
            processed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, 11, thresh_const)
        else:
            if self.dithering_method.get() == "Bayer":
                processed = self.bayer_dithering(img)
            elif self.dithering_method.get() == "Floyd-Steinberg":
                processed = self.floyd_steinberg_dithering(img)
            elif self.dithering_method.get() == "Atkinson":
                processed = self.atkinson_dithering(img)
            else:
                processed = img
        return processed
    
    def export_svg(self):
        """Export the currently displayed image based on the export format selection."""
        if self.current_image is None or not self.current_image_path:
            self.update_status("Error: No image uploaded. Please upload an image before exporting.", clear=False)
            return
        export_dir = filedialog.askdirectory(title="Select Folder to Export")
        if not export_dir:
            self.update_status("Export cancelled.", clear=False)
            return
        
        self.update_status("Export in progress...", clear=False)
        path = self.current_image_path
        stippled = self.process_image(path)
        if stippled is None:
            self.update_status("Error processing image; export aborted.", clear=False)
            return
        h, w = stippled.shape
        if self.dithering_method.get() == "None":
            spacing = self.spacing.get()
            dot_size = self.dot_size.get()
            shape = self.dot_shape.get()
        else:
            spacing = 1
            dot_size = 0.5
            shape = "Square"
        
        if self.reverse_colors.get():
            dot_fill = self.invert_hex_color(self.dot_color.get())
            bg_fill = self.invert_hex_color(self.bg_color.get())
        else:
            dot_fill = self.safe_hex_color(self.dot_color.get(), "#000000")
            bg_fill = self.safe_hex_color(self.bg_color.get(), "#FFFFFF")
        
        basename = os.path.splitext(os.path.basename(path))[0]
        export_choice = self.export_format.get()
        
        # If exporting SVG (or Both), build and save the SVG as before.
        if export_choice in ("SVG", "Both"):
            svg_filename = basename + ".svg"
            svg_filepath = os.path.join(export_dir, svg_filename)
            dwg = svgwrite.Drawing(svg_filepath, size=(w, h))
            if self.export_with_bg.get():
                dwg.add(dwg.rect(insert=(0, 0), size=(w, h), fill=bg_fill))
            if self.dithering_method.get() == "None":
                for y in np.arange(0, h, spacing):
                    for x in np.arange(0, w, spacing):
                        if stippled[int(y), int(x)] == 0:
                            if shape == "Circle":
                                dwg.add(dwg.circle(center=(x, y), r=dot_size, fill=dot_fill))
                            elif shape == "Square":
                                dwg.add(dwg.rect(insert=(x - dot_size, y - dot_size),
                                                 size=(2 * dot_size, 2 * dot_size), fill=dot_fill))
                            elif shape == "Triangle":
                                side = 2 * dot_size
                                height_tri = dot_size * math.sqrt(3)
                                points = [
                                    (x, y - 2/3 * height_tri),
                                    (x - side/2, y + 1/3 * height_tri),
                                    (x + side/2, y + 1/3 * height_tri)
                                ]
                                dwg.add(dwg.polygon(points=points, fill=dot_fill))
                            elif shape == "Character":
                                char = self.dot_char.get() if self.dot_char.get() else "*"
                                dwg.add(dwg.text(char, insert=(x, y), fill=dot_fill,
                                                 style=f"font-size:{2 * dot_size}px; text-anchor: middle; dominant-baseline: central"))
            else:
                for y in range(h):
                    x = 0
                    while x < w:
                        if stippled[y, x] == 0:
                            start = x
                            while x < w and stippled[y, x] == 0:
                                x += 1
                            run_length = x - start
                            dwg.add(dwg.rect(insert=(start, y), size=(run_length, 1), fill=dot_fill))
                        else:
                            x += 1
            dwg.save()
        
        # For PNG export, bypass SVG conversion by generating the image directly.
        if export_choice in ("PNG", "Both"):
            png_filename = basename + ".png"
            png_filepath = os.path.join(export_dir, png_filename)
            final_img = self.create_png_image(stippled, h, w)
            final_img.save(png_filepath)
        
        # If exporting PNG only, no temporary SVG is created.
        self.update_status(f"Export complete for '{basename}'.", clear=False)
    
    def export_all_svg(self):
        """Export all uploaded images based on the export format selection."""
        if not self.image_paths:
            self.update_status("Error: No images uploaded. Please upload at least one image.", clear=False)
            return
        export_dir = filedialog.askdirectory(title="Select Folder to Export Files")
        if not export_dir:
            self.update_status("Export cancelled.", clear=False)
            return
        self.update_status("Exporting all images...", clear=False)
        export_choice = self.export_format.get()
        count = 0
        for path in self.image_paths:
            stippled = self.process_image(path)
            if stippled is None:
                continue
            h, w = stippled.shape
            if self.dithering_method.get() == "None":
                spacing = self.spacing.get()
                dot_size = self.dot_size.get()
                shape = self.dot_shape.get()
            else:
                spacing = 1
                dot_size = 0.5
                shape = "Square"
            if self.reverse_colors.get():
                dot_fill = self.invert_hex_color(self.dot_color.get())
                bg_fill = self.invert_hex_color(self.bg_color.get())
            else:
                dot_fill = self.safe_hex_color(self.dot_color.get(), "#000000")
                bg_fill = self.safe_hex_color(self.bg_color.get(), "#FFFFFF")
            basename = os.path.splitext(os.path.basename(path))[0]
            if export_choice in ("SVG", "Both"):
                svg_filename = basename + ".svg"
                svg_filepath = os.path.join(export_dir, svg_filename)
                dwg = svgwrite.Drawing(svg_filepath, size=(w, h))
                if self.export_with_bg.get():
                    dwg.add(dwg.rect(insert=(0, 0), size=(w, h), fill=bg_fill))
                if self.dithering_method.get() == "None":
                    for y in np.arange(0, h, spacing):
                        for x in np.arange(0, w, spacing):
                            if stippled[int(y), int(x)] == 0:
                                if shape == "Circle":
                                    dwg.add(dwg.circle(center=(x, y), r=dot_size, fill=dot_fill))
                                elif shape == "Square":
                                    dwg.add(dwg.rect(insert=(x - dot_size, y - dot_size),
                                                     size=(2 * dot_size, 2 * dot_size), fill=dot_fill))
                                elif shape == "Triangle":
                                    side = 2 * dot_size
                                    height_tri = dot_size * math.sqrt(3)
                                    points = [
                                        (x, y - 2/3 * height_tri),
                                        (x - side/2, y + 1/3 * height_tri),
                                        (x + side/2, y + 1/3 * height_tri)
                                    ]
                                    dwg.add(dwg.polygon(points=points, fill=dot_fill))
                                elif shape == "Character":
                                    char = self.dot_char.get() if self.dot_char.get() else "*"
                                    dwg.add(dwg.text(char, insert=(x, y), fill=dot_fill,
                                                     style=f"font-size:{2 * dot_size}px; text-anchor: middle; dominant-baseline: central"))
                else:
                    for y in range(h):
                        x = 0
                        while x < w:
                            if stippled[y, x] == 0:
                                start = x
                                while x < w and stippled[y, x] == 0:
                                    x += 1
                                run_length = x - start
                                dwg.add(dwg.rect(insert=(start, y), size=(run_length, 1), fill=dot_fill))
                            else:
                                x += 1
                dwg.save()
            if export_choice in ("PNG", "Both"):
                png_filename = basename + ".png"
                png_filepath = os.path.join(export_dir, png_filename)
                final_img = self.create_png_image(stippled, h, w)
                final_img.save(png_filepath)
            count += 1
        self.update_status(f"Export complete: {count} file(s) saved to {export_dir}", clear=False)
    
    def reset(self):
        self.image_paths = []
        self.current_image = None
        self.current_image_path = None
        for widget in self.gallery_inner_frame.winfo_children():
            widget.destroy()
        self.thumbnail_images = []
        self.threshold_val.set(14)
        self.dot_size.set(1.4)
        self.contrast.set(6)
        self.brightness.set(0)
        self.spacing.set(3.2)
        self.dot_shape.set("Square")
        self.dot_char.set("*")
        self.bg_color.set("#FFFFFF")
        self.dot_color.set("#000000")
        self.dithering_method.set("None")
        self.export_with_bg.set(True)
        self.reverse_colors.set(False)
        self.export_format.set("Both")
        self.dot_char_entry.config(state="disabled")
        if not self.none_settings_frame.winfo_ismapped():
            self.none_settings_frame.pack(before=self.bg_color_frame, fill=tk.X)
        self.canvas.delete("all")
        self.update_status("Reset to original state.", clear=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = StippleApp(root)
    root.mainloop()
