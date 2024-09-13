import os

try:
	import pyautogui, time, pathlib, sys, mouse, tqdm, win10toast, platform
except ImportError:
	os.system('title FlorestSpamer - ImportError.')
	input(f'[!] Невозможно запустить программное обеспечение, так как отсутствуют нужные модули\nСкачать их?\nНажмите на Enter для продолжения.')
	os.system('pip install pyautogui')
	os.system('pip install tqdm')
	os.system('pip install mouse')
	os.system('pip install win10toast')

os.system('title FlorestSpamer')
input(f'Привет! Добро пожаловать в программу от Флореста.\nОна умеет спамить, а также кликать на левую кнопку мыши неограниченное число раз.\nПрошу обратить внимание на то, что разработчик не ответственнен за Ваше злоупотреблением данного кода.\nВы можете изменять данную программу, так как Вам необходимо.\nМои социальные сети: https://taplink.cc/florestone4185\nНажмите на Enter для продолжения.')
b = int(input(f'Введи количество спама. Если бесконечно, то напиши 0.'))
d = input(f'Ты на майн сервере?')
s = input(f'Кликер, или спамер?')
notificator = win10toast.ToastNotifier()

time.sleep(5)

def get_text():
	with open(pathlib.Path(sys.argv[0]).parent.resolve() / 'spamers_text.txt', 'r') as file:
		return file.readlines()

def spam():
	c = 0
	if s == 'spamer':
		print(f'[!] Программа запущена в режиме "SPAM".')
		if platform.system() == 'Windows':
			notificator.show_toast('Успех.', 'Программа успешно запущена в режиме "SPAM".')
		if platform.system() == 'Linux':
			os.system('notify-send "Программа успешно запущена в режиме SPAM." "INFO"')
		if platform.system() == 'Mac':
			os.system('osascript -e \'display notification "Программа успешно запущена в режиме SPAM." with title "INFO"\'')
		while c <= b:
			if s == 'spamer':
				if d == 'yes':
					if b == 0:
						for a in tqdm.tqdm(get_text(), desc='Запускаем поток...'):
							pyautogui.press('t')
							pyautogui.write(a)
							pyautogui.press('enter')
					else:
						for a in tqdm.tqdm(get_text(), desc='Запускаем поток...'):
							pyautogui.press('t')
							pyautogui.write(a)
							pyautogui.press('enter')
							c += 1
							print(f'Пройден цикл. {c} из {b}.')
				else:
					if b == 0:
						for a in tqdm.tqdm(get_text(), desc='Запускаем поток...'):
							pyautogui.write(a)
							pyautogui.press('enter')
					else:
						for a in tqdm.tqdm(get_text(), desc='Запускаем поток...'):
							pyautogui.write(a)
							pyautogui.press('enter')
							c += 1
							print(f'Пройден цикл. {c} из {b}.')
	else:
			print(f'[!] Программа запущена в режиме "CLICKER".')
			if platform.system() == 'Windows':
				notificator.show_toast('INFO', f'Программа запущена в режиме "CLICKER".')
			if platform.system() == 'Linux':
				os.system(f'notify-send "Программа запущена в режиме CLICKER." "INFO"')
			if platform.system() == 'Mac':
				os.system(f'osascript -e \'display notification "Программа запущена в режиме CLICKER." with title "INFO"\'')
			while c <= b:
				mouse.click()
				if b == 0:
					pass
				else:
					c+=1
					print(f'Пройден цикл. {c} из {b}.')
				time.sleep(1)
	print(f'[!] Программа была деактивирована. Возможно, все возможные потоки были уже выполнены.')
	if platform.system() == 'Windows':
		notificator.show_toast('Успех.', f'Программа была деактивирована. Возможно, все возможные потоки были уже выполнены.')
	if platform.system() == 'Linux':
		os.system(f'notify-send "Программа была деактивирована. Возможно, все возможные потоки были уже выполнены." "Успех."')
	if platform.system() == 'Mac':
		os.system(f'osascript -e \'display notification "Программа была деактивирована. Возможно, все возможные потоки были уже выполнены." with title "Успех."\'')
	os.system('pause')

if __name__ == '__main__':
	spam()