from pyrogram import Client, filters
from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup, Message, ReplyKeyboardRemove
from info import *
from b import *


@Client.on_message(filters.regex(fr"^{HIDE_BUTTON}$") & filters.incoming)
async def keyboard_handler(c:Client, m:Message):
    keyboard_button = []


    for x in HIDE_BUTTON1:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="SHOW BUTTONS")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Button Hided", reply_markup=reply_markup)




@Client.on_message(filters.regex(fr"^{OPEN_MENU_BUTTON}$") & filters.incoming)
async def keyboard_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Buttons hide Mode on For Exit Click close Boutton", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON2) & filters.incoming)
async def keyboard2_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON2:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)
    
    
@Client.on_message(filters.regex(OPEN_MENU_BUTTON3) & filters.incoming)
async def keyboard3_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON3:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON4) & filters.incoming)
async def keyboard4_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON4:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)

    
@Client.on_message(filters.regex(OPEN_MENU_BUTTON5) & filters.incoming)
async def keyboard5_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON5:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON6) & filters.incoming)
async def keyboard6_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON6:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)
    
    
@Client.on_message(filters.regex(OPEN_MENU_BUTTON7) & filters.incoming)
async def keyboard7_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON7:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON8) & filters.incoming)
async def keyboard8_handler(c:Client, m:Message):
    keyboard_button = []


    for x in BIGGBOSS:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)
    
    
@Client.on_message(filters.regex(OPEN_MENU_BUTTON9) & filters.incoming)
async def keyboard9_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON9:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON10) & filters.incoming)
async def keyboard10_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON10:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON11) & filters.incoming)
async def keyboard11_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON11:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)
    
    
@Client.on_message(filters.regex(OPEN_MENU_BUTTON12) & filters.incoming)
async def keyboard12_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON12:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON13) & filters.incoming)
async def keyboard13_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON13:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON14) & filters.incoming)
async def keyboard14_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON14:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON15) & filters.incoming)
async def keyboard15_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON15:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON16) & filters.incoming)
async def keyboard16_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON16:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON17) & filters.incoming)
async def keyboard17_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON17:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)

@Client.on_message(filters.regex(OPEN_MENU_BUTTON18) & filters.incoming)
async def keyboard18_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON18:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)

   
@Client.on_message(filters.regex(OPEN_MENU_BUTTON19) & filters.incoming)
async def keyboard19_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON19:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON20) & filters.incoming)
async def keyboard20_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON20:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)
     

@Client.on_message(filters.regex(OPEN_MENU_BUTTON21) & filters.incoming)
async def keyboard21_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON21:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON22) & filters.incoming)
async def keyboard22_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON22:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON23) & filters.incoming)
async def keyboard23_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON23:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON24) & filters.incoming)
async def keyboard24_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON24:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON25) & filters.incoming)
async def keyboard25_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON25:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON26) & filters.incoming)
async def keyboard26_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON26:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON27) & filters.incoming)
async def keyboard27_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON27:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON28) & filters.incoming)
async def keyboard28_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON28:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON29) & filters.incoming)
async def keyboard29_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON29:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON30) & filters.incoming)
async def keyboard30_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON30:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON31) & filters.incoming)
async def keyboard31_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON31:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)



@Client.on_message(filters.regex(OPEN_MENU_BUTTON32) & filters.incoming)
async def keyboard32_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON32:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON33) & filters.incoming)
async def keyboard33_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON33:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON34) & filters.incoming)
async def keyboard34_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON34:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON35) & filters.incoming)
async def keyboard35_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON35:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON36) & filters.incoming)
async def keyboard36_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON36:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON37) & filters.incoming)
async def keyboard37_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON37:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON38) & filters.incoming)
async def keyboard38_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON38:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON39) & filters.incoming)
async def keyboard39_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON39:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON40) & filters.incoming)
async def keyboard40_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON40:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON41) & filters.incoming)
async def keyboard41_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON41:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON42) & filters.incoming)
async def keyboard42_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON42:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


# Close
@Client.on_message(filters.regex(r"^Close$") & filters.incoming)
async def keyboard_close_handler(c:Client, m:Message):

    
    keyboard_button = [
        [KeyboardButton(text=OPEN_MENU_BUTTON)],
        [KeyboardButton(text=OPEN_MENU_BUTTON2)],
        [KeyboardButton(text=OPEN_MENU_BUTTON3)],
        [KeyboardButton(text=OPEN_MENU_BUTTON4)],
        [KeyboardButton(text=OPEN_MENU_BUTTON5)],
        [KeyboardButton(text=OPEN_MENU_BUTTON6)],
        [KeyboardButton(text=OPEN_MENU_BUTTON7)],
        [KeyboardButton(text=OPEN_MENU_BUTTON8)],
        [KeyboardButton(text=OPEN_MENU_BUTTON9)],
        [KeyboardButton(text=OPEN_MENU_BUTTON10)],
        [KeyboardButton(text=OPEN_MENU_BUTTON11)],
        [KeyboardButton(text=OPEN_MENU_BUTTON12)],
        [KeyboardButton(text=OPEN_MENU_BUTTON13)],
        [KeyboardButton(text=OPEN_MENU_BUTTON14)],
        [KeyboardButton(text=OPEN_MENU_BUTTON15)],
        [KeyboardButton(text=OPEN_MENU_BUTTON16)],
        [KeyboardButton(text=OPEN_MENU_BUTTON17)],
        [KeyboardButton(text=OPEN_MENU_BUTTON18)],
        [KeyboardButton(text=OPEN_MENU_BUTTON19)],
        [KeyboardButton(text=OPEN_MENU_BUTTON20)],
        [KeyboardButton(text=OPEN_MENU_BUTTON21)],
        [KeyboardButton(text=OPEN_MENU_BUTTON22)],
        [KeyboardButton(text=OPEN_MENU_BUTTON23)],
        [KeyboardButton(text=OPEN_MENU_BUTTON24)],
        [KeyboardButton(text=OPEN_MENU_BUTTON25)],
        [KeyboardButton(text=OPEN_MENU_BUTTON26)],
        [KeyboardButton(text=OPEN_MENU_BUTTON27)],
        [KeyboardButton(text=OPEN_MENU_BUTTON28)],
        [KeyboardButton(text=OPEN_MENU_BUTTON29)],
        [KeyboardButton(text=OPEN_MENU_BUTTON30)],
        [KeyboardButton(text=OPEN_MENU_BUTTON31)],
        [KeyboardButton(text=OPEN_MENU_BUTTON32)],
        [KeyboardButton(text=OPEN_MENU_BUTTON33)],
        [KeyboardButton(text=OPEN_MENU_BUTTON34)],
        [KeyboardButton(text=OPEN_MENU_BUTTON35)],
        [KeyboardButton(text=OPEN_MENU_BUTTON36)],
        [KeyboardButton(text=OPEN_MENU_BUTTON37)],
        [KeyboardButton(text=OPEN_MENU_BUTTON38)],
        [KeyboardButton(text=OPEN_MENU_BUTTON39)],
        [KeyboardButton(text=OPEN_MENU_BUTTON40)],
        [KeyboardButton(text=OPEN_MENU_BUTTON41)],
        [KeyboardButton(text=OPEN_MENU_BUTTON42)],
    ]

from pyrogram import Client, filters
from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup, Message, ReplyKeyboardRemove
from info import *



@Client.on_message(filters.regex(fr"^{OPEN_MENU_BUTTON}$") & filters.incoming)
async def keyboard_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON2) & filters.incoming)
async def keyboard2_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON2:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)
    
    
@Client.on_message(filters.regex(OPEN_MENU_BUTTON3) & filters.incoming)
async def keyboard3_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON3:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON4) & filters.incoming)
async def keyboard4_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON4:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)

    
@Client.on_message(filters.regex(OPEN_MENU_BUTTON5) & filters.incoming)
async def keyboard5_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON5:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON6) & filters.incoming)
async def keyboard6_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON6:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)
    
    
@Client.on_message(filters.regex(OPEN_MENU_BUTTON7) & filters.incoming)
async def keyboard7_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON7:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON8) & filters.incoming)
async def keyboard8_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON8:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)
    
    
@Client.on_message(filters.regex(OPEN_MENU_BUTTON9) & filters.incoming)
async def keyboard9_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON9:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON10) & filters.incoming)
async def keyboard10_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON10:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON11) & filters.incoming)
async def keyboard11_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON11:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)
    
    
@Client.on_message(filters.regex(OPEN_MENU_BUTTON12) & filters.incoming)
async def keyboard12_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON12:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON13) & filters.incoming)
async def keyboard13_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON13:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON14) & filters.incoming)
async def keyboard14_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON14:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON15) & filters.incoming)
async def keyboard15_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON15:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON16) & filters.incoming)
async def keyboard16_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON16:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON17) & filters.incoming)
async def keyboard17_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON17:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)

@Client.on_message(filters.regex(OPEN_MENU_BUTTON18) & filters.incoming)
async def keyboard18_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON18:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)

   
@Client.on_message(filters.regex(OPEN_MENU_BUTTON19) & filters.incoming)
async def keyboard19_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON19:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON20) & filters.incoming)
async def keyboard20_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON20:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)
     

@Client.on_message(filters.regex(OPEN_MENU_BUTTON21) & filters.incoming)
async def keyboard21_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON21:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON22) & filters.incoming)
async def keyboard22_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON22:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON23) & filters.incoming)
async def keyboard23_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON23:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON24) & filters.incoming)
async def keyboard24_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON24:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON25) & filters.incoming)
async def keyboard25_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON25:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON26) & filters.incoming)
async def keyboard26_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON26:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON27) & filters.incoming)
async def keyboard27_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON27:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON28) & filters.incoming)
async def keyboard28_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON28:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON29) & filters.incoming)
async def keyboard29_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON29:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON30) & filters.incoming)
async def keyboard30_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON30:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON31) & filters.incoming)
async def keyboard31_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON31:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)



@Client.on_message(filters.regex(OPEN_MENU_BUTTON32) & filters.incoming)
async def keyboard32_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON32:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON33) & filters.incoming)
async def keyboard33_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON33:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON34) & filters.incoming)
async def keyboard34_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON34:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON35) & filters.incoming)
async def keyboard35_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON35:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON36) & filters.incoming)
async def keyboard36_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON36:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON37) & filters.incoming)
async def keyboard37_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON37:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON38) & filters.incoming)
async def keyboard38_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON38:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON39) & filters.incoming)
async def keyboard39_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON39:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON40) & filters.incoming)
async def keyboard40_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON40:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON41) & filters.incoming)
async def keyboard41_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON41:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


@Client.on_message(filters.regex(OPEN_MENU_BUTTON42) & filters.incoming)
async def keyboard42_handler(c:Client, m:Message):
    keyboard_button = []


    for x in KEYBOARD_BUTTON42:
        keyboard_button.append([
            KeyboardButton(text=x),
        ],)

    keyboard_button.append([KeyboardButton(text="Close")],)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Choose any Movie", reply_markup=reply_markup)


# Close
@Client.on_message(filters.regex(r"^Close$") & filters.incoming)
async def keyboard_close_handler(c:Client, m:Message):

    
    keyboard_button = [
        [KeyboardButton(text=OPEN_MENU_BUTTON)],
        [KeyboardButton(text=OPEN_MENU_BUTTON2)],
        [KeyboardButton(text=OPEN_MENU_BUTTON3)],
        [KeyboardButton(text=OPEN_MENU_BUTTON4)],
        [KeyboardButton(text=OPEN_MENU_BUTTON5)],
        [KeyboardButton(text=OPEN_MENU_BUTTON6)],
        [KeyboardButton(text=OPEN_MENU_BUTTON7)],
        [KeyboardButton(text=OPEN_MENU_BUTTON8)],
        [KeyboardButton(text=OPEN_MENU_BUTTON9)],
        [KeyboardButton(text=OPEN_MENU_BUTTON10)],
        [KeyboardButton(text=OPEN_MENU_BUTTON11)],
        [KeyboardButton(text=OPEN_MENU_BUTTON12)],
        [KeyboardButton(text=OPEN_MENU_BUTTON13)],
        [KeyboardButton(text=OPEN_MENU_BUTTON14)],
        [KeyboardButton(text=OPEN_MENU_BUTTON15)],
        [KeyboardButton(text=OPEN_MENU_BUTTON16)],
        [KeyboardButton(text=OPEN_MENU_BUTTON17)],
        [KeyboardButton(text=OPEN_MENU_BUTTON18)],
        [KeyboardButton(text=OPEN_MENU_BUTTON19)],
        [KeyboardButton(text=OPEN_MENU_BUTTON20)],
        [KeyboardButton(text=OPEN_MENU_BUTTON21)],
        [KeyboardButton(text=OPEN_MENU_BUTTON22)],
        [KeyboardButton(text=OPEN_MENU_BUTTON23)],
        [KeyboardButton(text=OPEN_MENU_BUTTON24)],
        [KeyboardButton(text=OPEN_MENU_BUTTON25)],
        [KeyboardButton(text=OPEN_MENU_BUTTON26)],
        [KeyboardButton(text=OPEN_MENU_BUTTON27)],
        [KeyboardButton(text=OPEN_MENU_BUTTON28)],
        [KeyboardButton(text=OPEN_MENU_BUTTON29)],
        [KeyboardButton(text=OPEN_MENU_BUTTON30)],
        [KeyboardButton(text=OPEN_MENU_BUTTON31)],
        [KeyboardButton(text=OPEN_MENU_BUTTON32)],
        [KeyboardButton(text=OPEN_MENU_BUTTON33)],
        [KeyboardButton(text=OPEN_MENU_BUTTON34)],
        [KeyboardButton(text=OPEN_MENU_BUTTON35)],
        [KeyboardButton(text=OPEN_MENU_BUTTON36)],
        [KeyboardButton(text=OPEN_MENU_BUTTON37)],
        [KeyboardButton(text=OPEN_MENU_BUTTON38)],
        [KeyboardButton(text=OPEN_MENU_BUTTON39)],
        [KeyboardButton(text=OPEN_MENU_BUTTON40)],
        [KeyboardButton(text=OPEN_MENU_BUTTON41)],
        [KeyboardButton(text=OPEN_MENU_BUTTON42)],
    ]


    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Closed", reply_markup=reply_markup)

    reply_markup = ReplyKeyboardMarkup(keyboard_button, one_time_keyboard=True, resize_keyboard=True)

    await m.reply("Closed", reply_markup=reply_markup)
