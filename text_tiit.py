import pickle

'''\with open("number.pickle", "wb") as f:
	pickle.dump(0, f)

with open("number.pickle", "rb") as f:
	number = pickle.load(f)
		
print(number)
'''


def text():
	with open("number.pickle", "rb") as f:
		number = pickle.load(f)
	a = ["Беги, Форест, беги!!!",
	     "Случается, что бегство – оптимальная ответная реакция.",
	     "Бэнг, бэнг, бэнг, бэнг.",
	     "А ЯЯЯ лабы точно сдал???",
	     "Родина вам этого не забудет)",
	     "Дорогие первокурсники, вместо того, чтобы сидеть и пялиться в списки сдавших или не сдавших долги по ТИИТ, "
	     "шли бы вы учиться!!",
	     "И если кто не понял ещё, что надо учить и разбираться, чтобы успешно допуститься к зачету, а затем его сдать, "
	     "то я вам сочувствую.",
	     "Вам только осталось не буйствовать и учиться)",
	     "Так, господа, забираем документы, не задерживаем очередь!",
	     "Здравствуй, небо в облаках,"
	     "Здравствуй, юность в сапогах!"
	     "Пропади, моя тоска,"
	     "Вот он я, привет, войска!",
	     "А это точно не больно?",
	     "Это мой первый раз - поаккуратнее там.",
	     "Ща буит миасо))00",
	     "Ну вы держитесь там👊👊👊",
	     "Мы имеем дело с особой формой разума.",
	     "Я весь год готовился к экзаменам, но когда увидел вопросы, все знания тут же таинственным образом исчезли.",
	     "Тюрьма не хуй, сиди кайфуй.",
	     "Да ты успокойся!!",
	     "Да че ты очкуешь? Я так 100 раз делал…",
	     "Сложна, сложна не понимаю блять.",
	     "Кчауу",
	     "Слишком сложно - дасвидания…",
	     "Я головой то понимаю…",
	     "только ртом сказать не могу…",
	     "Мало кто поймет, но кто поймет, тот мало кто.",
	     "Цікай з городу, тобі пізда.",
	     "Щас бы в армию.",
	     "Когда снежок говорит, что он реальный ниггер.",
	     "Prepare your anus.",
	     "Если не читали конспект, то прочтите хоть это(http://www.piluli.ru/product/Vazelin)",
	     "Ваши знания должны быть так же глубоки, как и мой банан"]
	num = number
	number += 1
	with open("number.pickle", "wb") as file:
		pickle.dump(number, file)
	return a[num]


def text_final():
	return "Давайте не будем забывать, что это не все, ведь впереди еще ФИЛОСОФИЯ❤❤❤"
