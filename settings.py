# size
APP_SIZE = (400,700)
MAIN_ROWS = 7
MAIN_COLUMNS = 4

# YAZI
FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE = 32

STYLING = {
    'gap': 0.5,
    'corner-radius': 0
}

NUM_POSITIONS = {
    '.' : {
        'col' : 2,
        'row' : 6,
        'span' : 1
    },
    0 : {
        'col' : 0,
        'row' : 6,
        'span' : 2
    },
    1 : {
        'col' : 0,
        'row' : 5,
        'span' : 1
    },
    2 : {
        'col' : 1,
        'row' : 5,
        'span' : 1
    },
    3 : {
        'col' : 2,
        'row' : 5,
        'span' : 1
    },
    4 : {
        'col' : 0,
        'row' : 4,
        'span' : 1
    },
    5 : {
        'col' : 1,
        'row' : 4,
        'span' : 1
    },
    6 : {
        'col' : 2,
        'row' : 4,
        'span' : 1
    },
    7 : {
        'col' : 0,
        'row' : 3,
        'span' : 1
    },
    8 : {
        'col' : 1,
        'row' : 3,
        'span' : 1
    },
    9 : {
        'col' : 2,
        'row' : 3,
        'span' : 1
    }
}

MATH_POSITIONS = {
    '/':{
        'col': 3,
        'row': 2,
        'character': '',
        'operator': '/',
        'image path': 'images\division.png'
    },
    '*':{
        'col': 3,
        'row': 3,
        'character': '',
        'operator': '*',
        'image path': 'images\close.png'
    },
    '-':{
        'col': 3,
        'row': 4,
        'character': '',
        'operator': '-',
        'image path': 'images\minus.png'
    },
    '=':{
        'col': 3,
        'row': 6,
        'character': '',
        'operator': '=',
        'image path': 'images\equal.png'
    },
    '+':{
        'col': 3,
        'row': 5,
        'character': '',
        'operator': '+',
        'image path': 'images\plus.png'
    }
}

OPERATORS = {
    'clear': {
        'col': 0,
        'row': 2,
        'text': 'AC',
        'image path': None 
    },
    'invert': {
        'col': 1,
        'row': 2,
        'text': '',
        'image path': 'images\half.png' 
    },
    'percent': {
        'col': 2,
        'row': 2,
        'text': '%',
        'image path': None
    }
}

COLORS = {
    'black': { 'fg': '#000000', 'hover': '#1c1c1c', 'text': '#FF9500','numcolor':'#FFFFFF'},
    'white': { 'fg': '#EEEEEE', 'hover': '#dddddd', 'text': '#FF9500','numcolor':'#000000'},
    'orange': { 'fg': '#FF9500', 'hover': '#ffb143', 'text': ('black','white') },
    'orange-highlight': { 'fg': 'white', 'hover': 'white', 'text': ('black','#FF9500') }
}

BLACK = '#000000'
WHITE = '#EEEEEE'