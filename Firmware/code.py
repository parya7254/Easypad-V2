import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.rgb import RGB
from kmk.modules.layers import Layers
from kmk.extensions.display import Display, SSD1306, TextEntry
from kmk.modules.encoder import EncoderHandler
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

mousekeys = MouseKeys(
    max_speed = 10,
    acc_interval = 100, # Delta ms to apply acceleration
    move_step = 0.6
)

keyboard.modules.append(MouseKeys())

encoder_handler = EncoderHandler()

encoder_handler.pins = ((board.GP1, board.GP2, None, False),)

keyboard.col_pins = (board.GP7, board.GP8, board.GP9, board.GP10)
keyboard.row_pins = (board.GP3, board.GP4, board.GP5, board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.modules.append(Layers())

rgb = RGB(pixel_pin=board.GP0, num_pixels=18)
keybaord.extensions.append(rgb)

i2c_bus = busio.I2C(board.GP11, board.GP12)
display_driver = SSD1306(
    i2c=i2c_bus,
)

display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Mode: ', x=0, y=32, y_anchor='B'),
        TextEntry(text='Numpad', x=40, y=32, y_anchor='B', layer=0),
        TextEntry(text='RGB', x=40, y=32, y_anchor='B', layer=1),
        TextEntry(text='FUNC', x=40, y=32, y_anchor='B', layer=2),
        TextEntry(text='0 1 2', x=0, y=4),
        TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
        TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
        TextEntry(text='2', x=24, y=4, inverted=True, layer=2),
    ],
    
    width=128,
    height=32,
    dim_time=4,
    dim_target=0,
    off_time=10,
    brightness=1,
)

keyboard.extensions.append(display)

keyboard.modules.append(Macros())

L0= KC.DF(0)
L1= KC.DF(1)
L2= KC.DF(2)

keyboard.keymap = [
    # Keymap for Layer 0 (Numpad Mode)
    [
        KC.KP_7, KC.KP_8, KC.KP_9, L1,
        KC.KP_4, KC.KP_5, KC.KP_6, KC.KP_PLUS,
        KC.KP_7. KC.KP_8, KC.KP_9, KC.KP_ENTER,
        KC.KP_0, KC.KP_0, KC.KP_DOT, KC.KP_ENTER,
    ],
    # Keymap for Layer 1 (RGB Control)
    [
        KC.RGB_TOG, KC.RGB_HUI, KC.RGB_HUD, L2
        KC.RGB_SAI, KC.RGB_SAD, KC.RGB_VAI,  KC.RGB_VAD,
        KC.RGB_MODE_SWIRL, KC.RGB_MODE_KNIGHT, KC.RGB_MODE_BREATHE_RAINBOW, KC.RGB_MODE_RAINBOW,
        KC.RGB_MODE_BREATHE, KC.RGB_MODE_PLAIN, KC.RGB_ANI, KC.RGB_AND,
    ],
    # Keymap for Layer 2 (Function Keys)
    [
        KC.F1, KC.F2, KC.F3, L0
        KC.F4, KC.F5, KC.F6, KC.F7,
        KC.F8, KC.F9, KC.F10, KC.F11,
        KC.F12, KC.NO, KC.NO, KC.NO,
    ],
]

encoder_handler.map = [ ((KC.MW_UP, KC.MW_DOWN),),
                        ((KC.MW_UP, KC.MW_DOWN),),
                        ((KC.MW_UP, KC.MW_DOWN),),
                        ]