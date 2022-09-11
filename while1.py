import time
while True:
	time.sleep(2)
	mode = input('請輸入傘兵隊形: ')
	if mode == 'q':
		break
	elif mode == '1':
		time.sleep(2)
		print('機降式')
	elif mode == '2':
		time.sleep(2)
		print('飛輪式')
	else:
		print('請輸入1/2/q')

