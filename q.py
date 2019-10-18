import telebot
from telebot import types
import random

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
arr = ['']*6
count = [0]*2
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('сильвермолл', 'новый')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True) 
keyboard2.row('кфс', 'сабвей')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('бургер', 'картошка')
keyboardChoose = telebot.types.ReplyKeyboardMarkup(True)
keyboardChoose.row('да', 'нет')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row('самовывоз', 'доставка')
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)                   
keyboard5.row('оформить заказ')


@bot.message_handler(commands = ['start'])
def start_message(message):
	bot.send_message(message.chat.id, "в какой тц пойдем?", reply_markup=keyboard1)



@bot.message_handler(content_types=['text'])
def send_text(message):
	ans = message.text.lower()
	
	if ans == 'сильвермолл':
		bot.send_message(message.chat.id, "в какой ресторан пойдем?", reply_markup=keyboard2)			
		arr[0] = ans

	elif ans == 'новый':
		bot.send_message(message.chat.id, "в какой ресторан пойдем?", reply_markup=keyboard2)
		arr[0] = 'новый'
		
	elif ans == 'кфс' or message.text.lower() == 'нет':
		bot.send_message(message.chat.id, "что будем есть?", reply_markup=keyboard3)
		if arr[1] != 'кфс':			
			arr[1] = ans

	elif ans == 'сабвей' or message.text.lower() == 'нет':
		bot.send_message(message.chat.id, "что будем есть?", reply_markup=keyboard3)
		if arr[1] != 'сабвей':
			arr[1] = ans

	elif ans == 'бургер':
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)					
		arr[2] = ans
		count[0] += 1

	elif ans == 'картошка':
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)
		arr[3] = 'картошка'
		count[1] += 1

	elif ans == 'да':
		bot.send_message(message.chat.id, 'самовывоз или доставка?', reply_markup = keyboard4)

	elif ans == 'самовывоз':	
		bot.send_message(message.chat.id, "оформить заказ?", reply_markup=keyboard5)
		arr[4] = ans

	elif ans == 'доставка':
		bot.send_message(message.chat.id, "оформить заказ?", reply_markup=keyboard5)
		arr[4] = ans

	elif ans == 'оформить заказ':
		
		
		rez = ''	
		bot.send_message(message.chat.id, 'Твой заказ принят')
		for i in range(len(arr)):
			if i == 2 and count[0] != 0:
				rez += str(count[0]) + ' - ' +  arr[2] + ' -> '
				continue
			elif i == 3 and count[1] != 0:
				rez += str(count[1]) + ' - ' + arr[3] + ' -> '
				continue
			elif i == 4:
				rez += arr[i]
				break
			else:
				rez += arr[i] + ' -> '
		req = str(random.randint(1, 1000)) + ' ' + message.from_user.first_name + ' ' +  message.from_user.second_name
		rez += '    время - ' + order_time
		rez += '    реквизиты: ' + req
		bot.send_message(785534105, '{order}'.format(order=rez))
               

	

bot.polling(none_stop = True)




