import telebot
from bot_tg2 import raspisanie
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot('7986319730:AAFEy6An6SodZpPb3hYbaMHnmcMyg-IbB98');
#Словарь для хранения группы пользователя
user_groups = {}
group = ""
@bot.message_handler(content_types=['text', 'document', 'audio'])

def get_text_messages(message):
    user_id = message.from_user.id
    if message.text == '/lesson':
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton("МС-11", callback_data="МС-11")
        button2 = InlineKeyboardButton("МДСМ-12", callback_data="МДСМ-12")
        button3 = InlineKeyboardButton("ПД-13", callback_data="ПД-13")
        button4 = InlineKeyboardButton("ИС-14", callback_data="ИС-14")
        button5 = InlineKeyboardButton("ЮР-15", callback_data="ЮР-15")
        button6 = InlineKeyboardButton("ТО-16", callback_data="ТО-16")
        button7 = InlineKeyboardButton("ЭБ-17", callback_data="ЭБ-17")
        button8 = InlineKeyboardButton("ЭР-18", callback_data="ЭР-18")
        button9 = InlineKeyboardButton("ПД-23", callback_data="ПД-23")
        button10 = InlineKeyboardButton("ИС-24 (РА)", callback_data="ИС-24 (РА)")
        button11 = InlineKeyboardButton("ИС-24 (В)", callback_data="ИС-24 (В)")
        button12 = InlineKeyboardButton("ПС-25", callback_data="ПС-25")
        button13 = InlineKeyboardButton("ЭБ-27", callback_data="ЭБ-27")
        button14 = InlineKeyboardButton("МС-31", callback_data="МС-31")
        button15 = InlineKeyboardButton("МД-32", callback_data="МД-32")
        button16 = InlineKeyboardButton("МС-41", callback_data="МС-41")
        button17 = InlineKeyboardButton("ИС-44", callback_data="ИС-44")
        button18 = InlineKeyboardButton("ТО-46", callback_data="ТО-46")

        button19 = InlineKeyboardButton("МС-21", callback_data="МС-21")
        button20 = InlineKeyboardButton("МД-22", callback_data="МД-22")
        button21 = InlineKeyboardButton("ПД-33", callback_data="ПД-33")
        button22 = InlineKeyboardButton("ИС-34 (РА)", callback_data="ИС-34 (РА)")
        button23 = InlineKeyboardButton("ИС-34 (В)", callback_data="ИС-34 (В)")
        button24 = InlineKeyboardButton("ПС-35", callback_data="ПС-35")
        button25 = InlineKeyboardButton("ЭБ-37", callback_data="ЭБ-37")


        markup.add(button1,button2,button3,button4,button5,button6,button7,button8,
                   button9,button10,button11,button12,button13,button14,button15,button16,
                   button17,button18,button19,button20,button21,button22,button23,button24,button25)
        bot.send_message(user_id,"Выберите группу:", reply_markup=markup)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, text='Я умею выводить пары на день. Напиши /lesson')
    else:
        bot.send_message(message.from_user.id, text='Я тебя не понимаю. Напиши /help')
@bot.callback_query_handler(func=lambda call: True)
def callback(query):
    user_id = query.from_user.id
    global group
    if (query.data == "МС-11" or query.data == "МДСМ-12" or query.data == "ПД-13" or query.data == "ИС-14" or query.data == "ЮР-15" or query.data == "ТО-16" or query.data == "ЭБ-17"
            or query.data == "ЭР-18" or query.data == "ПД-23" or query.data == "ИС-24 (РА)" or query.data == "ИС-24 (В)" or query.data == "ПС-25" or query.data == "ЭБ-27"
                or query.data == "МС-31" or query.data == "МД-32" or query.data == "МС-41" or query.data == "ИС-44" or query.data == "ТО-46"):
        group = query.data
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton("понедельник",callback_data="понедельник")
        button2 = InlineKeyboardButton("вторник", callback_data="вторник")
        button3 = InlineKeyboardButton("среда", callback_data="среда")
        button4 = InlineKeyboardButton("четверг", callback_data="четверг")
        button5 = InlineKeyboardButton("пятница", callback_data="пятница")
        markup.add(button1,button2,button3,button4,button5)
        bot.send_message(user_id, "Выберите день:", reply_markup=markup)

    elif (query.data == "МС-21" or query.data == "МД-22" or query.data == "ПД-33" or query.data == "ИС-34 (В) "
          or query.data == "ИС-34 (РА)" or query.data == "ИС-34 (В)" or query.data == "ИС-34 (РА)"
            or query.data == "ПС-35" or query.data == "ЭБ-37"):
        group = query.data
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton("понедельник",callback_data="понедельник")
        button2 = InlineKeyboardButton("вторник", callback_data="вторник")
        button3 = InlineKeyboardButton("среда", callback_data="среда")
        button4 = InlineKeyboardButton("четверг", callback_data="четверг")
        button5 = InlineKeyboardButton("пятница", callback_data="пятница")
        markup.add(button1,button2,button3,button4,button5)
        bot.send_message(user_id, "Выберите день:", reply_markup=markup)

    elif query.data in ["понедельник","вторник","среда","четверг","пятница"]:
        day = query.data
        raspis = raspisanie(day, group)
        set_schedule = "\n".join(str(i) for i in raspis)
        bot.send_message(user_id, set_schedule)
    bot.delete_message(user_id, query.message.message_id)
bot.polling(none_stop=True, interval=0)
