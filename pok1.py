#Изменить название переменных карт, тк они совпадают с двумя парами
import random
mast=['piki','krest','cherv', 'bubi']
rang=['2','3','4','5','6','7','8','9','10','v','d','k','t']
global money_users
money_users=500
global money_pc
money_pc=500	
#Функция выбора рандомной карты
	#Делаем рандомные карты
def card_mix(mast,rang):
	#Рандомом пуремешиваем список, потом рандомом выбираем номер элемента из списка
	rang_population=[0,1,2,3,0,1,2,3,0]
	random.shuffle(mast)
	rand=random.sample(rang_population, 9)
	global y3
	global y4
	global y5
	global x1
	global x2
	global z1
	global z2
	global y1
	global x11
	x11=mast[rand[0]]
	global x12
	x12=random.choice(rang)
	global x21
	x21=mast[rand[1]]
	global x22
	x22=random.choice(rang)
	global y11
	y11=mast[rand[2]]
	global y12
	y12=random.choice(rang)
	global y21
	y21=mast[rand[3]]
	global y22
	y22=random.choice(rang)
	global z11
	z11=mast[rand[7]]
	global z12
	z12=random.choice(rang)
	global z21
	z21=mast[rand[8]]
	global z22
	z22=random.choice(rang)
	global y31
	y31=mast[rand[4]]
	global y32
	y32=random.choice(rang)
	global y41
	y41=mast[rand[5]]
	global y42
	y42=random.choice(rang)
	global y51
	y51=mast[rand[6]]
	global y52
	y52=random.choice(rang)
	global y1
	global y2
	x1=x11+x12
	x2=x21+x22
	y1=y11+y12
	y2=y21+y22
	y3=y31+y32
	y4=y41+y42
	y5=y51+y52
	z1=z11+z12
	z2=z21+z22	
	global cards
	global rangs
	cards=[x11,x21,y11,y21,y31,y41,y51]
	rangs=[x12,x22,y12,y22,y32,y42,y52]
def rules(): #Функция ознакомления с правилами игры
	print("Добро пожаловать в игру покер, написанную на языке пайтон")
	print("Правила очень простые: вам раздается по 2 карты и на стол 5 карт")
	print("Вам нужно собрать комбинацию из 5 карт, используя свои карты и карты со стола")
	print("В игре есть 10 комбинаций: ")
	print("Флеш рояль - самые старшие одномастные карты, идущие в порядке")
	print("Стрит флеш - одномастные карты, идущие в порядке")
	print("Каре - четыре карты одного достоинства")
	print("Фулл хаус - 3 карты одного достоинства и 2 карты другого")
	print("Флеш - 5 карт одной масти")
	print("Стрит - 5 последовательно расположенных карт")
	print("Сет - 3 карты одного достоинства")
	print("Две пары - 2 пары карт одинакового достоинства")
	print("Пара - 2 карты одинакового достоинства ")
	print("Старшая карта - разные 5 карт, и выбирается самая старшая")
# С этого момента идут фунцкции раунда























def pairs(rangs):
	pr1=0
	pr2=0
	pr3=0
	pr4=0
	pr5=0
	pr6=0
	pr7=0
	pr8=0
	pr9=0
	pr10=0
	pr11=0
	pr12=0
	pr13=0
	global x
	x=0
	global xt
	xt=False
	global xk
	xk=False
	global xd
	xd=False
	global xv
	xv=False
	global x10
	x10=False
	global x9
	x9=False
	global x8
	x8=False
	global x7
	x7=False
	global x6
	x6=False
	global x5
	x5=False
	global x4
	x4=False
	global x3
	x3=False
	global x2
	x2=False
	for item in rangs:
		if item=='t':
			pr1=pr1+1
		elif item=='k':
			pr2=pr2+1
		elif item=='d':
			pr3=pr3+1
		elif item=='v':
			pr4=pr4+1
		elif item=='10':
			pr5=pr5+1
		elif item=='9':
			pr6=pr6+1
		elif item=='8':
			pr7=pr7+1
		elif item=='7':
			pr8=pr8+1
		elif item=='6':
			pr9=pr9+1
		elif item=='5':
			pr10=pr10+1
		elif item=='4':
			pr11=pr11+1
		elif item=='3':
			pr12=pr12+1
		elif item=='2':
			pr13=pr13+1
		else:										#////////////////х это с парой
			pass
	if pr1==2:
		xt=True
		x=1
	if pr2==2:
		xk=True	
		x=1
	if pr3==2:
		xd=True
		x=1	
	if pr4==2:
		xv=True
		x=1	
	if pr5==2:
		x10=True
		x=1	
	if pr6==2:
		x9=True
		x=1	
	if pr7==2:
		x8=True
		x=1	
	if pr8==2:
		x7=True
		x=1	
	if pr9==2:
		x6=True
		x=1	
	if pr10==2:
		x5=True
		x=1	
	if pr11==2:
		x4=True
		x=1	
	if pr12==2:
		x3=True
		x=1	
	if pr13==2:
		x2=True
		x=1	
	else:
		pass


def kiker(rangs):	
	pr1=0
	pr2=0
	pr3=0
	pr4=0
	pr5=0
	pr6=0
	pr7=0
	pr8=0
	pr9=0
	pr10=0
	pr11=0
	pr12=0
	pr13=0
	for item in rangs:
		if item=='t':
			pr13=pr13+1
		elif item=='k':
			pr1=pr1+1
		elif item=='d':
			pr2=pr2+1								#Добавить чтобы выводилась какая карта-кикер
		elif item=='v':
			pr3=pr3+1
		elif item=='10':
			pr4=pr4+1
		elif item=='9':
			pr5=pr5+1
		elif item=='8':
			pr6=pr6+1
		elif item=='7':
			pr7=pr7+1
		elif item=='6':
			pr8=pr8+1
		elif item=='5':
			pr9=pr9+1
		elif item=='4':
			pr10=pr10+1
		elif item=='3':
			pr11=pr11+1
		elif item=='2':
			pr12=pr12+1
	if pr13==1:
		return '1t'
	elif pr1==1:
		return '1k'
	elif pr2==1:
		return '1d'	
	elif pr3==1:
		return '1v'	
	elif pr4==1:
		return '10'	
	elif pr5==1:
		return '9'	
	elif pr6==1:
		return '8'	
	elif pr7==1:
		return '7'	
	elif pr8==1:
		return '6'	
	elif pr9==1:
		return '5'	
	elif pr10==1:
		return '4'	
	elif pr11==1:
		return '3'	
	elif pr12==1:
		return '2'
	else:
		pass		



#Функция сравнения карт	


def difference():
	pairs(rangs)
	result_kiker=kiker(rangs)
	if 3==4:
		pass
	elif x==1:
		if xt==True:
			print('У вас пара на тузах')
		elif xk==True:
			print('У вас пара на королях')	
		elif xd==True:
			print('У вас пара на дамах')	
		elif xv==True:
			print('У вас пара на вальтах')	
		elif x10==True:
			print('У вас пара на десятках')	
		elif x9==True:
			print('У вас пара на девятках')	
		elif x8==True:
			print('У вас пара на восьмерках')	
		elif x7==True:
			print('У вас пара на семерках')	
		elif x6==True:
			print('У вас пара на шестерках')	
		elif x5==True:
			print('У вас пара на пятерках')	
		elif x4==True:
			print('У вас пара на четверках')	
		elif x3==True:
			print('У вас пара на тройках')	
		elif x2==True:
			print('У вас пара на двойках')	
		else:
			pass												
	else:
		if result_kiker=='1t':
			print('У вас кикер туз')
		elif result_kiker=='1k':
			print('У вас кикер король')
		elif result_kiker=='1d':
			print('У вас кикер дама')
		elif result_kiker=='1v':
			print('У вас кикер валет')
		elif result_kiker=='10':
			print('У вас кикер десятка')
		elif result_kiker=='9':
			print('У вас кикер девятка')
		elif result_kiker=='8':
			print('У вас кикер восемерка')
		elif result_kiker=='7':
			print('У вас кикер семерка')
		elif result_kiker=='6':
			print('У вас кикер шестерка')
		elif result_kiker=='5':
			print('У вас кикер пятерка')
		elif result_kiker=='4':
			print('У вас кикер четверка')								
		elif result_kiker=='3':
			print('У вас кикер тройка')
		elif result_kiker=='2':
			print('У вас кикер двойка')












































def start():
	global money_pc
	global money_users
	print(' ')
	print("Игра началась")	
def first_round(money_users,money_pc):
	global condition
	print('\t 1 РАУНД')
	print('')
	print('')
	print('******************************************')
	print('Ваши карты: ')
	print(x1+' '+x2)
	print('******************************************')
	print('')
	print('')
	bet=input("Вы можете поставить ставку-bet, пропустить-check, или сбросить карты fold: ")
	global b1
	if bet=="bet":
		b1=int(input('Введите ставку: '))
		condition=1
		print('')
		print('')
		print('')

	elif bet=='check':
		b1=0
		condition=1
		print('')
		print('')
		print('')
	else:
		b1=0
		condition=0
		print('')
		print('')
		print('')
def second_round(money_users,money_pc):
	global condition
	print('\t 2 РАУНД')
	print('******************************************')
	print('Ваши карты: ')
	print(x1+' '+x2)
	print('')
	print('')
	print('')
	print('******************************************')
	print('Карты на столе: ')
	print(y1+' '+y2+' '+y3)
	print('******************************************')
	bet=input("Вы можете поставить ставку-bet, пропустить-check, или сбросить карты fold: ")
	global b2
	if bet=="bet":
		b2=int(input('Введите ставку: '))
		condition=1
		print('')
		print('')
		print('')
	elif bet=='check':
		b2=0
		condition=1
		print('')
		print('')
		print('')
	else:
		b2=0
		condition=0	
		print('')
		print('')
		print('')
def thirty_round(money_users,money_pc):
	global condition
	print('\t 3 РАУНД')
	print('******************************************')
	print('Добавляется 1 карта на стол: ')
	global b3
	print(y1+' '+y2+' '+y3+' '+y4)
	print('')
	print('')
	print('')
	print('******************************************')
	print('Ваши карты: ')
	print(x1+' '+x2)
	print('******************************************')
	bet=input("Вы можете поставить ставку-bet, пропустить-check, или сбросить карты fold: ")
	if bet=="bet":
		b3=int(input('Введите ставку: '))
		condition=1
		print('')
		print('')
		print('')
	elif bet=='check':
		b3=0
		condition=1
		print('')
		print('')
		print('')
	elif bet=='fold':
		b3=0
		condition=0
		print('')
		print('')
		print('')	
def last_round(money_users,money_pc):
	global condition
	global b4	
	print('\t 4 РАУНД')
	print('******************************************')
	print('Добавляется последняя карта на стол: ')
	print(y1+' '+y2+' '+y3+' '+y4+' '+y5)
	print('')
	print('')
	print('')
	print('******************************************')
	print('Ваши карты: ')
	print(x1+' '+x2)
	print('******************************************')
	print(' ')
	print('Последний раунд')
	bet=input("Вы можете поставить ставку-bet, пропустить-check, или сбросить карты fold: ")
	if bet=="bet":
		b4=int(input('Введите ставку: '))
		condition=1
		print('')
		print('')
		print('')
	elif bet=='check':
		b4=0
		condition=1
		print('')
		print('')
		print('')
	else:
		b4=0
		condition=0
		print('')
		print('')
		print('')
#Начало тела самой программы
rules()		
status=input('Если вы хотите начать играть то напишите start, если выйти то exit: ')	
if status=='start':	
	while not money_pc<=0 and not money_users<=0:
		card_mix(mast,rang)
		print('')
		print('')
		print('')
		print('******************************************')
		print('Ваши деньги: '+str(money_users))
		print('Деньги соперника: '+str(money_pc))
		print('******************************************')
		print('')
		start()
		first_round(money_users,money_pc)
		if condition==1:
			second_round(money_users,money_pc)
			if condition==1:
				thirty_round(money_users,money_pc)
				if condition==1:
					last_round(money_users,money_pc)
					if condition==1:
						#Проверка карт
						print('******************************************')
						print('Карты соперника: ')
						print(z1+' '+z2)
						print('******************************************')
						print('Ваши карты: ')
						print(x1+' '+x2)
						print('******************************************')
						print('Карты на столе')
						print(y1+' '+y2+' '+y3+' '+y4+' '+y5)	
						print('******************************************')
						print('')
						print('')
						difference()
						lok=str(input('Напишите кто выиграл: I(маленькой буквой) или pc '))
						if lok=='i':
							money_users=money_users+50+b1+b2+b3+b4
							money_pc=money_pc-50-b1-b4-b2-b3
						else:
							print('выиграл компьютер')
							money_pc=money_pc+50+b1+b2+b3+b4
							money_users=money_users-50-b1-b4-b2-b3	
					else:
						money_users=money_users-50-b1-b2-b3
						money_pc=money_pc+50+b1+b2+b3
						pass
				else:
					money_users=money_users-50-b1-b2
					money_pc=money_pc+50+b1+b2
					pass
			else:
				money_users=money_users-50-b1
				money_pc=money_pc+50+b1
				pass
		else:
			money_users=money_users-50
			money_pc=money_pc+50
			pass
	if money_users<=0:		
		print(' ')
		print('К сожалению, вы проиграли, повезет в следующий раз')	
	else:
		print('ВАУ, вы выиграли, возвращайтесь скорее')
else :
	exit(0)			

	#Сделать  чтобы ставка не могла превышать имеющиеся деньги
	#Сделать all-in
	#Добавить функцию сравнения карт(в процессе)
