from customtkinter import CTkButton
from settings import *
import darkdetect

class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, span = 1, color = 'black'):
        super().__init__(
            master= parent,
            text= text,
            command=func,
            corner_radius= STYLING['corner-radius'],
            font=font,
            fg_color=COLORS[color]['fg'],
            hover_color= COLORS[color]['hover'],
            text_color=COLORS[color]['text']
        )
        self.grid(column=col, columnspan=span, row= row, sticky = 'NSEW', padx = STYLING['gap'], pady = STYLING['gap'])

class NumButton(CTkButton):
    def __init__(self, parent, text, func, col, row, span, font, color = 'black'):
        super().__init__(
            master= parent,
            text= text,
            command=lambda: func(text),
            corner_radius= STYLING['corner-radius'],
            font=font,
            fg_color=COLORS[color]['fg'],
            hover_color= COLORS[color]['hover'],
            text_color=COLORS[color]['numcolor']
        )
        self.grid(column=col, columnspan=span, row= row, sticky = 'NSEW', padx = STYLING['gap'], pady = STYLING['gap'])

class MathImageButton(CTkButton):
    def __init__(self, text, parent, operator, func, col, row, image, color):
        super().__init__(
            master= parent,
            text= text,
            command=lambda: func(operator),
            corner_radius= STYLING['corner-radius'],
            image= image,
            fg_color=COLORS[color]['fg'],
            hover_color= COLORS[color]['hover'],
        )
        self.grid(column=col, row= row, sticky = 'NSEW', padx = STYLING['gap'], pady = STYLING['gap'])

class ImageButton(CTkButton):
    def __init__(self, parent, text, func, col, row, image, color):
        super().__init__(
            master= parent,
            text= text,
            command=func,
            corner_radius= STYLING['corner-radius'],
            image= image,
            fg_color=COLORS[color]['fg'],
            hover_color= COLORS[color]['hover'],
        )
        self.grid(column=col, row= row, sticky = 'NSEW', padx = STYLING['gap'], pady = STYLING['gap'])