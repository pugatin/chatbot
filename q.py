import telebot
from telebot import types
import random
import time
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


@bot.message_handler(content_types = ['text'])
def send_text(message):
	ans = message.text.lower()
	
	global amount
	
	
	if ans == 'сильвермолл':
		bot.send_message(message.chat.id, "в какой ресторан пойдем?", reply_markup=keyboard2)
		arr[0] = ans

	elif ans == 'новый':
		bot.send_message(message.chat.id, "в какой ресторан пойдем?", reply_markup=keyboard2)
		arr[0] = ans

	elif ans == 'кфс' or message.text.lower() == 'нет':
		bot.send_photo(message.chat.id, open('Burger.jpg', 'rb'),'сколько штук?', reply_markup=keyboard3)
		if arr[1] != 'кфс':
			 arr[1] = ans

	elif ans == 'сабвей' or message.text.lower() == 'нет':		
		bot.send_photo(message.chat.id, open('subway.jpg', 'rb'),'сколько штук?', reply_markup=keyboard3s)
		if arr[1] != 'сабвей':
			arr[1] = ans

	elif ans == 'такос':	
	
		kfc[ans] += amount

		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)
		

	elif ans == 'твистер':
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)       
		kfc[ans] += amount

	elif ans == 'чизбургер':
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)
		kfc[ans] += amount

	elif ans == 'steak&cheese':
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)
		subway[ans] += amount

	elif ans == 'italian bmt':  ,
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)       
		subway[ans] += amount

	elif ans == 'chiсkenteryaki':
		bot.send_message(message.chat.id, "закончить покупки?", reply_markup=keyboardChoose)
		subway[ans] += amount

	elif ans == 'да':
		bot.send_message(message.chat.id, 'самовывоз или доставка?', reply_markup=keyboard4)

	elif ans == 'самовывоз':
		bot.send_message(message.chat.id, "оформить заказ?", reply_markup=keyboard5)
		arr[2] = ans

	elif ans == 'доставка':
		keyboard=types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
		button_geo=types.KeyboardButton(text='Отправить местоположение', request_location=True)
		keyboard.add(button_geo)
		bot.send_message(message.chat.id, 'Привет! Нажми на кнопку и передай мне своё местоположение.', reply_markup=keyboard)
		if message.location is not None:
			global geo_N
			geo_N=message.location.latitude
			global geo_W
			geo_W=message.location.longitude
			print (geo_W)
			print(geo_N)
			bot.send_message(message.chat.id, 'Спасибо! Можешь приступить к заказу нажав /order')

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
		savior = False
		global req
		req = str(random.randint(1, 1000)) + ' ' + message.from_user.first_name
		rez += '    реквизиты: ' + req
		
		if arr[2] == 'доставка':
			bot.send_message(785534105, '{geon} {geow}'.format(geon=geo_N,geow=geo_W))

		bot.send_message(message.chat.id, ("ко скольки приготовить заказ?(стандартное время ожидания = 5 минут)"))
		for i in kfc:
			kfc[i] = 0
		for i in subway:
			subway[i] = 0

	elif ans[0] in '0123456789':
		
		if arr[2] == 'самовывоз':
			time_order = 'заказ по коду "' + req + '" должен быть готов к ' + ans
			bot.send_message(785534105, '{order}'.format(order=time_order)) 

		else:
			amount = int(ans)

	
@bot.message_handler(content_types=['text'])
def get_geo(message):
	if message.text == 'доставка':
		def geo(message):
			keyboard=types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
			button_geo=types.KeyboardButton(text='Отправить местоположение', request_location=True)
			keyboard.add(button_geo)
			bot.send_message(message.chat.id, 'Привет! Нажми на кнопку и передай мне своё местоположение.', reply_markup=keyboard)

@bot.message_handler(content_types=['location'])
def location(message):
	if message.location is not None:
		global geo_N
		geo_N=message.location.latitude
		global geo_W
		geo_W=message.location.longitude
	print (geo_W)
	print(geo_N)
	bot.send_message(message.chat.id, 'Спасибо! Можешь приступить к заказу нажав /order')
			

bot.polling(none_stop = True)




