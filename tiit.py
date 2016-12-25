import vk
import random
import time
from datetime import datetime
from text_tiit import text, text_final

api = vk.API(vk.AuthSession(app_id = '5648577', user_login = 'maksim.golosov@mail.ru',
							user_password = 'ak-13.ak-13.akm-18.max', scope = 'messages'))


def message(day, minute, hour):
	day_x = 28
	hour_x = 11
	minute_x = 40

	clock = (minute_x - minute) + 60 * (hour_x - hour) + 24 * 60 * abs(day - day_x)

	d_day = clock // 60 // 24
	d_hour = clock // 60 % 24
	d_minute = clock % 60

	return "До зачета по ТИИТ осталось : "+str(d_day)+" сут., "+str(d_hour)+" час., "+str(d_minute)+" мин.!\n"


def main():
		(day, minute, hour) = (int(str(datetime.now())[8:10]), int(str(datetime.now())[14:16]),
							   int(str(datetime.now())[11:13]))
		
		print(day, hour, minute)

		if day == 25:
			api.messages.send(chat_id = 63, message = message(day, minute, hour) + text())
			time.sleep(3 * 3600)
			return main()
		elif day == 27:
			api.messages.send(chat_id = 63, message = message(day, minute, hour) + text())
			time.sleep(2 * 3600)
			return main()
		elif day == 28:
			if 11 > hour >= 9:
				api.messages.send(chat_id = 63, message = message(day, minute, hour) + text())
				time.sleep(1800)
				return main()
			if hour == 11:
				api.messages.send(chat_id = 63, message = message(day, minute, hour) + text())
				time.sleep(2400)
				api.messages.send(chat_id = 63, message = text_final())
				return SystemExit
			else:
				api.messages.send(chat_id = 63, message = message(day, minute, hour) + text())
				time.sleep(3600)
				return main()
		else:
			return main()


if __name__ == "__main__":
	main()
