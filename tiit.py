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
	
	return "До зачета по ТИИТ осталось : {0} с., {1} ч., {2} м.!\n".format(str(d_day), str(d_hour), str(d_minute))


def main():
	(day, minute, hour) = (int(str(datetime.now())[8:10]), int(str(datetime.now())[14:16]),
	                       int(str(datetime.now())[11:13]))
	
	if day == 22:
		api.messages.send(chat_id = 63, message = message(day, minute, hour) + text())
		time.sleep(4 * 3600)
		return main()
	elif day == 27:
		api.messages.send(chat_id = 63, message = message(day, minute, hour) + text())
		time.sleep(2 * 3600)
		return main()
	elif day == 28:
		if hour >= 9:
			api.messages.send(chat_id = 63, message = message(day, minute, hour))
			time.sleep(1800)
		elif hour == 11 and minute == 30:
			api.messages.send(chat_id = 63, message = text_final())
			return SystemExit
		else:
			time.sleep(3600)
		return main()


if __name__ == "__main__":
	main()
