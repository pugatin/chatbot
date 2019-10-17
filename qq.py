import telebot
import telebot.types
bot = telebot.TeleBot("926280268:AAF5-V9B4tpwdecTjw_LNk1GslvEYwEnzKY")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('сильвермолл', 'новый')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('кфс', 'сабвей')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('бургер', 'картошка')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row('самовывоз', 'доставка')
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)  # 89646563493
keyboard5.row('оформить заказ', 'отменить заказ')


@bot.message_handler(commands=['start'])
def handle_text(message):
    cid = message.chat.id
    msgPrice = bot.send_message(cid, 'Привет {name}! Выбери ТЦ:'.format(name=message.from_user.first_name), reply_markup=keyboard1)
    bot.register_next_step_handler(msgPrice, step_Set_Price)


def step_Set_Price(message):
    cid = message.chat.id
    userPrice = message.text
    bot.send_message(745923507, '{name} заказал в ТЦ {order}'.format(order=userPrice, name=message.from_user.first_name))

    msgRest= bot.send_message(cid,'Выбери ресторан:', reply_markup=keyboard2)
    bot.register_next_step_handler(msgRest, step_Set_Rest)
def step_Set_Rest(message):
    cid=message.chat.id
    userRest=message.text
    bot.send_message(745923507,
                     '{name} заказал в ТЦ [название в локальной переменной userPrice] в ресторане {rest}'.format(name=message.from_user.first_name, rest=userRest))
    msgMenu=bot.send_message(cid,'Чего желаете?', reply_markup=keyboard3)
    bot.register_next_step_handler(msgMenu, step_Set_Menu)
def step_Set_Menu(message):
    cid=message.chat.id
    userMenu=message.text
    bot.send_message(745923507,
                     '{name} заказал в ТЦ [название в локальной переменной userPrice] в ресторане [название в '
                     'локальной переменной userRest] выбрал {menu}'.format(name=message.from_user.first_name,
                                                                           menu=userMenu))
    msgDelivery=bot.send_message(cid,'Как будешь забирать?', reply_markup=keyboard4)
    bot.register_next_step_handler(msgDelivery, step_Set_Delivery)
def step_Set_Delivery(message):
    cid=message.chat.id
    userDelivery=message.text
    bot.send_message(745923507,
                     '{name} заказал в ТЦ [название в локальной переменной userPrice] в ресторане [название в '
                     'локальной переменной userRest] выбрал [название в лок пер userMenu]. Заказ заберет {Delivery}'.format(name=message.from_user.first_name,
                                                                           Delivery=userDelivery))
    msgConfirm=bot.send_message(cid,'Оформляем?', reply_markup=keyboard5)
    bot.register_next_step_handler(msgConfirm, step_Set_Confirm)
def step_Set_Confirm(message):
    cid=message.chat.id
    userConfirm=message.text
    bot.send_message(745923507,
                     '{name} заказал в ТЦ [название в локальной переменной userPrice] в ресторане [название в '
                     'локальной переменной userRest] выбрал [название в лок пер userMenu]. Заказ заберет [название в Лок пер userDelivery] и выбрал {Confirm}'.format(name=message.from_user.first_name,
                                                                           Confirm=userConfirm))
bot.polling(none_stop=True)