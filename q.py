import telebot
from telebot import types
ans= 'Заказ'
bot = telebot.TeleBot("941558477:AAGShts4Z6AFqc1E5LEc3zxi5YdpzxJ4OKk")
#ans1 = 1
#ans2=2
#отправка сообщения по айди
'''@bot.message_handler(commands=['start'])
def start_message(message):
    sent = bot.send_message(message.chat.id, 'Привет, {name}! Как мне тебя называть?'.format(name=message.from_user.first_name))
    bot.register_next_step_handler(sent, hello)
def hello(message):
            bot.send_message(745923507, '{name} заказал в {moll}'.format(moll=ans, name=message.text))
ans=1

'''

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('сильвермолл', 'новый')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('кфс', 'сабвей')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('бургер', 'картошка')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row('самовывоз', 'доставка')
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)                    #89646563493
keyboard5.row('оформить заказ')
@bot.message_handler(commands = ['start'])
def start_message(message):
	bot.send_message(message.chat.id, "в какой тц пойдем?", reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
	ans='заказон'
	if message.text.lower() == 'сильвермолл':
		bot.send_message(message.chat.id, "в какой ресторан пойдем?", reply_markup=keyboard2)	
		bot.send_message(745923507, '{name} заказал в ТЦ {order}'.format(order='сильвермолл', name=message.from_user.first_name))
		
	elif message.text.lower() == 'новый':
		bot.send_message(message.chat.id, "в какой ресторан пойдем?", reply_markup=keyboard2)
		bot.send_message(745923507, '{name} заказал в ТЦ {order}'.format(order='сильвермолл', name=message.from_user.first_name))
		
	elif message.text.lower() == 'кфс':
		bot.send_message(message.chat.id, "что будем есть?", reply_markup=keyboard3)
		bot.send_message(745923507, '{order}'.format(order='кфс'))
	elif message.text.lower() == 'сабвей':
		bot.send_message(message.chat.id, "что будем есть?", reply_markup=keyboard3)
		bot.send_message(745923507, '{order}'.format(order='сабвей'))
	elif message.text.lower() == 'бургер':
		bot.send_message(message.chat.id, "самовывоз или доставка?", reply_markup=keyboard4)
		bot.send_message(745923507, '{order}'.format(order='бургер'))
	elif message.text.lower() == 'картошка':
		bot.send_message(message.chat.id, "самовывоз или доставка?", reply_markup=keyboard4)
		bot.send_message(745923507, '{order}'.format(order='картошка'))
	elif message.text.lower() == 'самовывоз':
		bot.send_message(message.chat.id, "оформить заказ?", reply_markup=keyboard5)
		bot.send_message(745923507, '{order}'.format(order='самовывоз'))
	elif message.text.lower() == 'доставка':
		bot.send_message(message.chat.id, "оформить заказ?", reply_markup=keyboard5)
		bot.send_message(745923507, '{order}'.format(order='доставка'))
	elif message.text.lower() == 'оформить заказ':
		bot.send_message(745923507, '{order}'.format(order='заказ готов'))
		bot.send_message(745923507, '{rder}'.format(rder=a))
		bot.send_message(message.chat.id, 'Твой заказ принят')

	

bot.polling(none_stop = True)


 #ест - меню - способ доставки - если самовывоз то время когда забрать заказ - оплата