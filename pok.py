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

#Функция сравнения карт
'''def flesh_royal():
	for i in cards:
		if i==i-1
			tir++
	if tir==5:
		for item in rangs:
			if item=='t' or item=='k' or item=='d' or item=='v' or item=='10':
				pr++	
	else:
		pass
	if pr==5:
		kr10=10	
		return kr10
	else:
		pass	
'''
'''		
def strit_flash:
	for item in rangs:
		if item=='k' or item=='d' or item=='v' or item=='10' or item=='9':
			for i in cards:
				if i==i-1:
					tir++
			if tir==5:		
			print('у вас стит флеш')
			return 9
		elif item=='v' or item=='10' or item=='9' or item=='8' or item=='7':	
			for i in cards:
				if i==i-1:
					tir++
			if tir==5:		
			print('у вас стит флеш')
			return 9
		elif item=='10' or item=='9' or item=='8' or item=='7' or item=='6':	
			for i in cards:
				if i==i-1:
					tir++
			if tir==5:		
			print('у вас стит флеш')
			return 9
		elif item=='d' or item=='v' or item=='10' or item=='9' or item=='8':
			for i in cards:
				if i==i-1:
					tir++
			if tir==5:		
			print('у вас стит флеш')
			return 9
		elif item=='9' or item=='8' or item=='7' or item=='6' or item=='5':		
			for i in cards:
				if i==i-1:
					tir++
			if tir==5:		
			print('у вас стит флеш')									*************************
																		*     Стрит и флеш-		*
			return 9													*************************
		elif item=='8' or item=='7' or item=='6' or item=='5' or item=='4':	
			for i in cards:
				if i==i-1:
					tir++
			if tir==5:		
			print('у вас стит флеш')
			return 9
		elif item=='7' or item=='6' or item=='5' or item=='4' or item=='3':	
			for i in cards:
				if i==i-1:
					tir++
			if tir==5:		
			print('у вас стит флеш')
			return 9
		elif item=='6' or item=='5' or item=='4' or item=='3' or item=='2':	
			for i in cards:
				if i==i-1:
					tir++
			if tir==5:		
			print('у вас стит флеш')
			return 9
def kare():
	var2=='2'
	var3=='3'
	var4=='4'
	var5=='5'
	var6=='6'
	var7=='7'
	var8=='8'
	var9=='9'
	var10=='10'
	varv=='v'
	vard=='d'
	vark=='k'
	vart=='t'
	for item in rangs:
		if items==var2 or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')						#Можно сделать если tr!=4 то проверяются другие карты, те добавить if else
			return 8
		else:
			pass
	tr=0
	for item in rangs:
		if items==var3 or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass
	tr=0		
	for item in rangs:
		if items==var4 or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass
	tr=0		
	for item in rangs:
		if items==var5 or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass
	tr=0		
	for item in rangs:
		if items==var6 or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass
	tr=0		
	for item in rangs:
		if items==var7 or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass
	tr=0		
	for item in rangs:
		if items==var8 or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass
	tr=0		
	for item in rangs:
		if items==var9 or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass
	tr=0		
	for item in rangs:
		if items==var10 or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass
	tr=0		
	for item in rangs:
		if items==varv or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass
	tr=0		
	for item in rangs:
		if items==vard or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass
	tr=0		
	for item in rangs:
		if items==vark or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass
	tr=0		
	for item in rangs:
		if items==vart or :
			tr++
		else:
			pass
		if tr==4:
			print('У вас каре')
			return 8
		else:
			pass

def full_house():

def flesh():
	var1='piki'
	var2='krest'
	var3='cherv'
	var4='bubi'
	for item in cards:
		if item==var1:
			pr++	
	if pr==4:
		print('У вас флеш')
		return 6
	elif pr!=4:
		pr=0
		for item in cards:
			if item==var2:
				pr++	
		if pr==4:
			print('У вас флеш')
			return 6
		elif pr!=4:
			pr=0
			for item in cards:
				if item==var3:
					pr++						#Заменить return 7 на 6
			if pr==4:
				print('У вас флеш')
				return 6
			elif pr!=4:
				pr=0
				for item in cards:
					if item==var4:
						pr++	
				if pr==4:
					print('У вас флеш')
					return 6
				else:
					pass	

def strit():
	for item in rangs:
		if item=='k':
			pr1++
		elif item=='d':
			pr2++
		elif item=='v':
			pr3++
		elif item=='10':
			pr4++
		elif item=='9':
			pr5++
		elif item=='8':
			pr6++
		elif item=='7':
			pr7++
		elif item=='6':
			pr8++
		elif item=='5':
			pr9++
		elif item=='4':
			pr10++
		elif item=='3':
			pr11++
		elif item=='2':
			pr12++										
	if pr1==1 and pr2==1 and pr3==1 and pr4==1 and pr5==1:
		print('У вас Стрит')
		return 5
	elif pr2==1 and pr3==1 and pr4==1 and pr5==1 and pr6==1:
		print('У вас Стрит')
		return 5
	elif pr3==1 and pr4==1 and pr5==1 and pr6==1 and pr7==1:
		print('У вас Стрит')
		return 5
	elif pr4==1 and pr5==1 and pr6==1 and pr7==1 and pr8==1:
		print('У вас Стрит')
		return 5
	elif pr5==1 and pr6==1 and pr7==1 and pr8==1 and pr9==1:
		print('У вас Стрит')
		return 5
	elif pr6==1 and pr7==1 and pr8==1 and pr9==1 and pr10==1:
		print('У вас Стрит')
		return 5
	elif pr7==1 and pr8==1 and pr9==1 and pr10==1 and pr11==1:
		print('У вас Стрит')
		return 5
	elif pr8==1 and pr9==1 and pr10==1 and pr11==1 and pr12==1:
		print('У вас Стрит')
		return 5						
	else:
		pass
		'''		

def set(rangs):
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
	for item in rangs:
		if item=='k':
			pr1=pr1+1
		elif item=='d':
			pr2=pr2+1								#Добавить чтобы выводился ранг сета(т.е из какой карты сет)
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
	if pr1==3:
		return 4
	if pr2==3:
		return 4	
	if pr3==3:
		return 4	
	if pr4==3:
		return 4	
	if pr5==3:
		return 4	
	if pr6==3:
		return 4	
	if pr7==3:
		return 4	
	if pr8==3:
		return 4	
	if pr9==3:
		return 4	
	if pr10==3:
		return 4	
	if pr11==3:
		return 4	
	if pr12==3:
		return 4													 
def pairs(rangs):
	pr1=0								#Переделать функцию чтобы не вызодила после первого if(т.е добавить так чтобы было без return и возможно объединить pairs и two)pairs
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
	global par1
	par1=0
	global par2		
	par2=0
	global par3
	par3=0
	global par4
	par4=0
	global par5
	par5=0
	global par6
	par6=0
	global par7
	par7=0
	global par8
	par8=0
	global par9
	par9=0
	global par10
	par10=0
	global par11
	par11=0
	global par12
	par12=0
	global par13
	par13=0
	for item in rangs:
		if item=='k':
			pr1=pr1+1
		if item=='d':
			pr2=pr2+1								#Добавить чтобы выводилась какая пара
		if item=='v':
			pr3=pr3+1
		if item=='10':
			pr4=pr4+1
		if item=='9':
			pr5=pr5+1
		if item=='8':
			pr6=pr6+1
		if item=='7':
			pr7=pr7+1
		if item=='6':
			pr8=pr8+1
		if item=='5':
			pr9=pr9+1
		if item=='4':
			pr10=pr10+1
		if item=='3':
			pr11=pr11+1
		if item=='2':
			pr12=pr12+1
		if item=='t':
			pr13=pr13+1
		else:
			pass	
	if pr1==2:
		par1='k'
		return 2
	if pr2==2:
		par2='d'
		return 2
	if pr3==2:
		par3='v'	
		return 2	
	if pr4==2:
		par4='10'
		return 2
	if pr5==2:
		par5='9'
		return 2	
	if pr6==2:
		par6='8'
		return 2
	if pr7==2:
		par7='7'
		return 2
	if pr8==2:	
		par8='6'
		return 2
	if pr9==2:		
		par9='5'
		return 2
	if pr10==2:		
		par10='4'
		return 2
	if pr11==2:		
		par11='3'
		return 2
	if pr12==2:		
		par12='2'
		return 2
	if pr13==2:		
		par13='t'
		return 2
	else:
		pass	
def two_pairs():
	if par13=='t' or par1=='k' or par2=='d' or par3=='v' or par4=='10' or par5=='9' or par6=='8' or par7=='7' or par8=='6' or par9=='5' or par10=='4' or par11=='3' or par12=='2':
		return 3
	elif par1=='k' or par13=='t' or par2=='d' or par3=='v' or par4=='10' or par5=='9' or par6=='8' or par7=='7' or par8=='6' or par9=='5' or par10=='4' or par11=='3' or par12=='2':
		return 3
	elif par2=='d' or par13=='t' or par1=='k' or par3=='v' or par4=='10' or par5=='9' or par6=='8' or par7=='7' or par8=='6' or par9=='5' or par10=='4' or par11=='3' or par12=='2':
		return 3
	elif par3=='v' or par13=='t' or par1=='k' or par2=='d' or par4=='10' or par5=='9' or par6=='8' or par7=='7' or par8=='6' or par9=='5' or par10=='4' or par11=='3' or par12=='2':
		return 3
	elif par4=='10' or par13=='t' or par1=='k' or par2=='d' or par3=='v' or par5=='9' or par6=='8' or par7=='7' or par8=='6' or par9=='5' or par10=='4' or par11=='3' or par12=='2' :
		return 3
	elif par5=='9' or par13=='t' or par1=='k' or par2=='d' or par3=='v' or par4=='10' or par6=='8' or par7=='7' or par8=='6' or par9=='5' or par10=='4' or par11=='3' or par12=='2':
		return 3
	elif par6=='8' or par13=='t' or par1=='k' or par2=='d' or par3=='v' or par4=='10' or par5=='9' or par7=='7' or par8=='6' or par9=='5' or par10=='4' or par11=='3' or par12=='2':
		return 3
	elif par7=='7' or par13=='t' or par1=='k' or par2=='d' or par3=='v' or par4=='10' or par5=='9' or par6=='8' or par8=='6' or par9=='5' or par10=='4' or par11=='3' or par12=='2' :
		return 3
	elif par8=='6' or par13=='t' or par1=='k' or par2=='d' or par3=='v' or par4=='10' or par5=='9' or par6=='8' or par7=='7' or par9=='5' or par10=='4' or par11=='3' or par12=='2':
		return 3
	elif par9=='5' or par13=='t' or par1=='k' or par2=='d' or par3=='v' or par4=='10' or par5=='9' or par6=='8' or par7=='7' or par8=='6' or par10=='4' or par11=='3' or par12=='2':
		return 3
	elif par10=='4' or par13=='t' or par1=='k' or par2=='d' or par3=='v' or par4=='10' or par5=='9' or par6=='8' or par7=='7' or par8=='6' or par9=='5' or par11=='3' or par12=='2':
		return 3
	elif par11=='3' or par13=='t' or par1=='k' or par2=='d' or par3=='v' or par4=='10' or par5=='9' or par6=='8' or par7=='7' or par8=='6' or par9=='5' or par10=='4' or par12=='2':
		return 3
	elif par12=='2' or par13=='t' or par1=='k' or par2=='d' or par3=='v' or par4=='10' or par5=='9' or par6=='8' or par7=='7' or par8=='6' or par9=='5' or par10=='4' or par11=='3':
		return 3
	else:
		print('Привет как дела')																																																																																
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
	for item in rangs:
		if item=='k':
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
	if pr1==1:
		return 1
	if pr2==1:
		return 1	
	if pr3==1:
		return 1	
	if pr4==1:
		return 1	
	if pr5==1:
		return 1	
	if pr6==1:
		return 1	
	if pr7==1:
		return 1	
	if pr8==1:
		return 1	
	if pr9==1:
		return 1	
	if pr10==1:
		return 1	
	if pr11==1:
		return 1	
	if pr12==1:
		return 1
def difference():
	print('Идет процесс сравнения выших карт и карт соперника\n')
	post10=kiker(rangs)
	post9=pairs(rangs)
#	post8=two_pairs()
	post7=set(rangs)
	if post7==4:
		print('У вас сет\n')
	elif post9==2:
		if 3==3:
			print('У вас 2 пары')
		else:	
			print('У вас одна пара\n')
	elif post10==1:
		print('У вас кикер')

	'''if #Флешрояль+
	elif #Стрит Флеш+
	elif #Каре
	elif #фуллхаус
	elif #Флеш
	elif #Стрит
	elif #Сет
	elif #две пары
	elif #старшая карта
	elif #пара'''






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



	#Добавить функцию сравнения карт(в процессе)