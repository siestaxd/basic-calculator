import customtkinter as ctk
import darkdetect
from buttons import Button, ImageButton, NumButton, MathImageButton
from PIL import Image
from settings import *

class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        # setup
        # - fg_color = WHITE or BLACK
        super().__init__(fg_color= (WHITE,BLACK))
        # - set appearance to dark or light depending on is dark
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        # - get the start window size from the settings and disable window resizing
        # size windows
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        # disabled resizable
        self.resizable(False,False)
        # - hide the title and the icon
        # window title change
        self.title('XİAOMİ CLONE CALCULATOR')
        # window icon change
        self.iconbitmap('images\calculator.ico')

        # - grid layout
        self.rowconfigure(list(range(MAIN_ROWS)), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight = 1, uniform = 'a')

        # - data
        self.formula_string = ctk.StringVar(value='')
        self.result_string = ctk.StringVar(value='')
        self.display_nums = []
        self.full_operation = []
        # - widgets
        self.create_widgets(is_dark)

        self.mainloop()

    def create_widgets(self,is_dark):
        # - Font
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)
        # - output labels
        OutputLabel(self, 0, 'SE', main_font, self.formula_string) # Formula
        OutputLabel(self, 1, 'E', result_font, self.result_string) # Result
        # operator buttons
        # - AC / clear Button
        Button( 
            parent=self,
            text=OPERATORS['clear']['text'], 
            func=self.clear,
            col=OPERATORS['clear']['col'], 
            row=OPERATORS['clear']['row'],
            color=f'{"black" if is_dark else "white"}',
            font= main_font
            )
        # percent button
        Button( 
            parent=self,
            text=OPERATORS['percent']['text'], 
            func=self.percent,
            col=OPERATORS['percent']['col'], 
            row=OPERATORS['percent']['row'],
            color=f'{"black" if is_dark else "white"}',
            font= main_font
            )
        # invert button
        invert_image = ctk.CTkImage(
            dark_image=Image.open(OPERATORS['invert']['image path']),
            light_image=Image.open(OPERATORS['invert']['image path'])
        )
        ImageButton( 
            parent=self,
            text=OPERATORS['invert']['text'], 
            func=self.invert,
            col=OPERATORS['invert']['col'], 
            row=OPERATORS['invert']['row'],
            color=f'{"black" if is_dark else "white"}',
            image=invert_image
            )
        # number buttons
        for num, data in NUM_POSITIONS.items():
            NumButton( 
                parent=self,
                text=num, 
                func=self.num_press,
                col=data['col'], 
                row=data['row'],
                color=f'{"black" if is_dark else "white"}',
                font= main_font,
                span=data['span']
            )
        # math buttons
        for operator, data in MATH_POSITIONS.items():
            math_image = ctk.CTkImage(
                dark_image=Image.open(data['image path']),
                light_image=Image.open(data['image path'])
            )
            MathImageButton( 
                parent=self,
                operator=operator,
                text=data['character'],
                func=self.math_press,
                col=data['col'], 
                row=data['row'],
                color=f'{"black" if is_dark else "white"}',
                image=math_image
            )

    # num buttons function
    def num_press(self, value):
        self.display_nums.append(str(value))
        full_number = ''.join(self.display_nums)
        self.result_string.set(full_number)
    # math buttons function
    def math_press(self, value):
        current_number = ''.join(self.display_nums)
        if current_number:
            self.full_operation.append(current_number)

            if value != '=':
                # update data
                self.full_operation.append(value)
                self.display_nums.clear()
                # update output
                self.result_string.set('')
                self.formula_string.set(' '.join(self.full_operation))
            else:
                formula = ' '.join(self.full_operation)
                result = eval(formula)
                # format to result
                if isinstance(result, float):
                    # to many numbers after the decimal
                    # an integre is formatted like a float 4.0
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 3)
                # update data
                # clear the full operation list
                # display nums shoul have the value of the result
                self.full_operation.clear()
                self.display_nums = [str(result)]
                # update my output
                self.result_string.set(result)
                self.formula_string.set(formula)
                
    # operator buttons functions
    def clear(self):
        # clear the output
        self.result_string.set(0)
        self.formula_string.set('')
        # clear the data
        self.display_nums.clear()
        self.full_operation.clear()
    # davide the current value by 100
    def percent(self):
        if self.display_nums:
            # get the percentage number
            current_number = float(''.join(self.display_nums))
            percent_number = current_number / 100
            # update the data and output
            self.display_nums = list(str(percent_number))
            self.result_string.set(''.join(self.display_nums))
    def invert(self):
        current_number = ''.join(self.display_nums)
        if current_number:
            # positive / negative
            if float(current_number) > 0:
                self.display_nums.insert(0, '-')
            else:
                del self.display_nums[0]
            self.result_string.set(''.join(self.display_nums))


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, font=font, textvariable = string_var)
        self.grid(column = 0, columnspan = 4, row = row, sticky = anchor, padx = 10)

        # exercise
        # update the class so you can control which corner the label is attached to

if __name__ == '__main__':
    Calculator(darkdetect.isDark())