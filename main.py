from pyrogram import Client
from pyrogram import  filters,enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup as mk, InlineKeyboardButton as btn
from pyrogram.types import ChatPermissions

from asSQL import Client as cl


data = cl("protect")
db = data['data']
db.create_table()
db.set("botname",['ميزو' , 'زوز' , 'بوت' ,'ميزوو' , 'موز'])
db.set("bad_words",['كس','عير','طيز','زب','كسمك','كسختك','طيزك','مص'])

plugins = dict(root="plugins")

Client("x",
api_id=15926347,
api_hash="a863d1580b7b4df0479e4578d8b5be2f",
bot_token="6139392566:AAETKx3PHr0l4gJ4NP31pTzAEWS_YuwctKU", plugins=plugins).run()