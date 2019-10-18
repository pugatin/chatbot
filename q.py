import telebot
from telebot import types
import random

bot = telebot.TeleBot("941558477:AAGShts4Z6AFqc1E5LEc3zxi5YdpzxJ4OKk")


kfc = {'такос':0, 'твистер':0, 'чизбургер':0}
subway = {'Steak&Cheese':0, 'ChickenTeryaki':0,'Italian BMT':0,'Meatball':0, 'Turkey&Ham':0}
arr = ['']*3


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('сильвермолл', 'новый')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('кфс', 'сабвей')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('Такос', 'Твистер','Чизбургер')
keyboard3s = telebot.types.ReplyKeyboardMarkup(True)
keyboard3s.row('Steak&Cheese', 'ChickenTeryaki','Italian BMT','Meatball', 'Turkey&Ham')
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
def food_amount(message):
	bot.send_message(message.chat.id, "сколько еды?")
	global amount 
	amount = message.text

def send_text(message):
	ans = message.text.lower()

	
	if ans == 'сильвермолл':
		bot.send_message(message.chat.id, "в какой ресторан пойдем?", reply_markup=keyboard2)
		arr[0] = ans

	elif ans == 'новый':
		bot.send_message(message.chat.id, "в какой ресторан пойдем?", reply_markup=keyboard2)
		arr[0] = ans

	elif ans == 'кфс' or message.text.lower() == 'нет':
		bot.send_photo(message.chat.id, open('Burger.jpg', 'rb'), reply_markup=keyboard3)
		if arr[1] != 'кфс':
			 arr[1] = ans
			 a = 

	elif ans == 'сабвей' or message.text.lower() == 'нет':
		bot.send_photo(message.chat.id, open('subway.jpg', 'rb'), reply_markup=keyboard3s)
		if arr[1] != 'сабвей':
			arr[1] = ans

	elif ans == 'такос':
		food_amount()
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)

		kfc['такос'] += 1

	elif ans == 'твистер':
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)       
		kfc['твистер'] += 1

	elif ans == 'чизбургер':
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)
		kfc['чизбургер'] += 1

	elif ans == 'steak&cheese':
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)
		subway['steak&cheese'] += 1

	elif ans == 'italian bmt':
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)       
		subway['italian bmt'] += 1

	elif ans == 'chiсkenteryaki':
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)
		subway['chiсkenteryaki'] += 1

	elif ans == 'да':
		bot.send_message(message.chat.id, 'самовывоз или доставка?', reply_markup=keyboard4)

	elif ans == 'самовывоз':
		bot.send_message(message.chat.id, "оформить заказ?", reply_markup=keyboard5)
		arr[2] = ans

	elif ans == 'доставка':
		bot.send_message(message.chat.id, "оформить заказ?", reply_markup=keyboard5)
		arr[2] = ans

	elif ans == 'оформить заказ':
		rez = ''	
		bot.send_message(message.chat.id, 'Твой заказ принят')
		for i in range(len(arr)):
			if i == 1:
				if arr[i] == 'кфс':
					rez += arr[i] + ' , '
					for i in kfc:
						if kfc[i] > 0:
							rez += i + ' - ' + str(kfc[i]) + ' , '
				elif arr[i] == 'сабвей':
					rez += arr[i] + ' -> '
					for i in subway:
						if subway[i] > 0:
							rez += i + ' - ' + str(subway[i]) + ' , '

			elif i == 2:
				rez += arr[i]
				break

			else:
				rez += arr[i] + ' , '
		
		global req
		req = str(random.randint(1, 1000)) + ' ' + message.from_user.first_name
		rez += '    реквизиты: ' + req
		bot.send_message(785534105, '{order}'.format(order=rez))
		bot.send_message(message.chat.id, ("ко скольки приготовить заказ?(стандартное время ожидания = 5 минут)"))
		for i in kfc:
			kfc[i] = 0
		for i in subway:
			subway[i] = 0

	elif ans[0] in '0123456789':
		time_order = 'заказ по коду "' + req + '" должен быть готов к ' + ans
		bot.send_message(785534105, '{order}'.format(order=time_order))             

	
@bot.message_handler(content_types=['text'])
def food_amount(message):
	global w
	tb.send_message(chat_id, "Сколько вы хотите заказать?")
	w = message.text
	

	

bot.polling(none_stop = True)




