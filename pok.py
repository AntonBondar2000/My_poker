import random
mast=['piki','krest','cherv', 'bubi']
rang=['2','3','4','5','6','7','8','9','10','v','d','k','t']
global money_users
money_users=500
global money_pc
money_pc=500	
#Делаем рандомные карты
def card_mix(mast,rang):
	#Рандомом пуремешиваем список, потом рандомом выбираем номер элемента из списка
	rang_population=[0,1,2,3,0,1,2,3,0]
	random.shuffle(mast)
	rand=random.sample(rang_population, 9)
	global y3_c
	global y4_c
	global y52_c
	global x1_c
	global x2_c
	global z1_c
	global z2_c
	global y1_c
	global x11
	global y5_c
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
	global y32_c
	y32_c=random.choice(rang)
	global y41
	y41=mast[rand[5]]
	global y42_c
	y42_c=random.choice(rang)
	global y51
	y51=mast[rand[6]]
	global y52_c
	y52_c=random.choice(rang)
	global y1_c
	global y2_c
	x1_c=x11+x12
	x2_c=x21+x22
	y1_c=y11+y12
	y2_c=y21+y22
	y3_c=y31+y32_c
	y4_c=y41+y42_c
	y5_c=y51+y52_c
	z1_c=z11+z12
	z2_c=z21+z22	
	global cards
	global rangs
	cards=[x11,x21,y11,y21,y31,y41,y51]
	rangs=[x12,x22,y12,y22,y32_c,y42_c,y52_c]
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

def flash(cards):
	global flash_result
	flash_result=False
	global flashp
	flashp=False
	global flashb
	flashb=False
	global flashc
	flashc=False
	global flashk
	flashk=False
	flash_p=0
	flash_b=0
	flash_k=0
	flash_c=0
	for item in cards:
		if item=='piki':
			flash_p=flash_p+1
		if item=='bubi':
			flash_b=flash_b+1
		if item=='krest':
			flash_k=flash_k+1
		if item=='cherv':
			flash_c=flash_c+1	
	if flash_k==5:
		flash_result=True
		flashk=True	
	elif flash_b==5:
		flash_result=True
		flashb=True	
	elif flash_p==5:
		flash_result=True
		flashp=True	
	elif flash_c==5:
		flash_result=True
		flashc=True			
def strit(rangs):
	global stritt
	stritt=False
	global stritk
	stritk=False
	global stritd
	stritd=False
	global stritv
	stritv=False
	global strit10
	strit10=False
	global strit9
	strit9=False
	global strit8
	strit8=False
	global strit7
	strit7=False
	global strit6
	strit6=False
	global strit5
	strit5=False
	global strit4
	strit4=False
	global strit3
	strit3=False
	global strit2
	strit2=False
	global strit_result
	strit_result=False
	global strit_t
	strit_t=False
	global strit_k
	strit_k=False
	global strit_d
	strit_d=False
	global strit_v
	strit_v=False
	global strit_10
	strit_10=False
	global strit_9
	strit_9=False
	global strit_8
	strit_8=False
	global strit_7
	strit_7=False
	global strit_6
	strit_6=False
	for item in rangs:
		if item=='t':
			stritt=True
		if item=='k':
			stritk=True	
		if item=='d':
			stritd=True
		if item=='v':
			stritv=True
		if item=='10':
			strit10=True
		if item=='9':
			strit9=True
		if item=='8':
			strit8=True
		if item=='7':
			strit7=True
		if item=='6':
			strit6=True
		if item=='5':
			strit5=True
		if item=='4':
			strit4=True
		if item=='3':
			strit3=True
		if item=='2':
			strit2=True
	if stritt==True and stritk==True and stritd==True and stritv==True and strit10==True:
		strit_result=True
		strit_t=True
	if stritk==True and stritd==True and stritv==True and strit10==True and strit9==True:
		strit_result=True
		strit_k=True
	if stritd==True and stritv==True and strit10==True and strit9==True and strit8==True:
		strit_result=True
		strit_d=True
	if stritv==True and strit10==True and strit9==True and strit8==True and strit7==True:
		strit_result=True
		strit_v=True
	if strit10==True and strit9==True and strit8==True and strit7==True and strit6==True:
		strit_result=True
		strit_10=True
	if strit9==True and strit8==True and strit7==True and strit6==True and strit5==True:
		strit_result=True
		strit_9=True
	if strit8==True and strit7==True and strit6==True and strit5==True and strit4==True:
		strit_result=True
		strit_8=True
	if strit7==True and strit6==True and strit5==True and strit4==True and strit3==True:
		strit_result=True
		strit_7=True
	if strit6==True and strit5==True and strit4==True and strit3==True and strit2==True:
		strit_result=True
		strit_6=True								
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
	pr13=0
	global zp
	zp=False
	global zt
	zt=False
	global zk
	zk=False
	global zd
	zd=False
	global zv
	zv=False
	global z10
	z10=False
	global z9
	z9=False
	global z8
	z8=False
	global z7
	z7=False
	global z6
	z6=False
	global z5
	z5=False
	global z4
	z4=False
	global z3
	z3=False
	global z2
	z2=False	
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
	if pr1==3:
		zt=True
		zp=True
	if pr2==3:
		zk=True	
		zp=True
	if pr3==3:
		zd=True
		zp=True	
	if pr4==3:
		zv=True
		zp=True	
	if pr5==3:
		z10=True
		zp=True	
	if pr6==3:
		z9=True
		zp=True	
	if pr7==3:
		z8=True
		zp=True	
	if pr8==3:
		z7=True
		zp=True	
	if pr9==3:
		z6=True
		zp=True	
	if pr10==3:
		z5=True
		zp=True	
	if pr11==3:
		z4=True
		zp=True	
	if pr12==3:
		z3=True
		zp=True	
	if pr13==3:
		z2=True
		zp=True	
	else:
		pass	
def two_pairs():
	global ytk
	ytk=False
	global ytd
	ytd=False
	global ytv
	ytv=False
	global yt10
	yt10=False
	global yt9
	yt9=False
	global yt8
	yt8=False
	global yt7
	yt7=False
	global yt6
	yt6=False
	global yt5
	yt5=False
	global yt4
	yt4=False
	global yt3
	yt3=False
	global yt2
	yt2=False
	global ykd
	ykd=False
	global ykv
	ykv=False
	global yk10
	yk10=False
	global yk9
	yk9=False
	global yk8
	yk8=False
	global yk7
	yk7=False
	global yk6
	yk6=False
	global yk5
	yk5=False
	global yk4
	yk4=False
	global yk3
	yk3=False
	global yk2
	yk2=False
	global ydv
	ydv=False
	global yd10
	yd10=False
	global yd9
	yd9=False
	global yd8
	yd8=False
	global yd7
	yd7=False
	global yd6
	yd6=False
	global yd5
	yd5=False
	global yd4
	yd4=False
	global yd3
	yd3=False
	global yd2
	yd2=False
	global yv10
	yv10=False
	global yv9
	yv9=False
	global yv8
	yv8=False
	global yv7
	yv7=False
	global yv6
	yv6=False
	global yv5
	yv5=False
	global yv4
	yv4=False
	global yv3
	yv3=False
	global yv2
	yv2=False
	global y109
	y109=False
	global y108
	y108=False
	global y107
	y107=False
	global y106
	y106=False
	global y105
	y105=False
	global y104
	y104=False
	global y103
	y103=False
	global y102
	y102=False
	global y98
	y98=False
	global y97
	y97=False
	global y96
	y96=False
	global y95
	y95=False
	global y94
	y94=False
	global y93
	y93=False
	global y92
	y92=False
	global y87
	y87=False
	global y86
	y86=False
	global y85
	y85=False
	global y84
	y84=False
	global y83
	y83=False
	global y82
	y82=False
	global y76
	y76=False
	global y75
	y75=False
	global y74
	y74=False
	global y73
	y73=False
	global y72
	y72=False
	global y65
	y65=False
	global y64
	y64=False
	global y63
	y63=False
	global y62
	y62=False
	global y54
	y54=False
	global y53
	y53=False
	global y52
	y52=False
	global y43
	y43=False
	global y42
	y42=False
	global y32
	y32=False
	global y
	y=0
	if xt==True and xk==True:
		ytk=True
		y=1
	if xt==True and xd==True:
		ytd=True
		y=1
	if xt==True and xv==True:
		ytv=True
		y=1	
	if xt==True and x10==True:
		yt10=True	
		y=1
	if xt==True and x9==True:
		yt9=True
		y=1	
	if xt==True and x8==True:
		yt8=True
		y=1	
	if xt==True and x7==True:
		yt7=True
		y=1	
	if xt==True and x6==True:
		yt6=True
		y=1	
	if xt==True and x5==True:
		yt5=True
		y=1	
	if xt==True and x4==True:
		yt4=True
		y=1	
	if xt==True and x3==True:
		yt3=True
		y=1	
	if xt==True and x2==True:
		yt2=True
		y=1	
	if xk==True and xd==True:
		ykd=True
		y=1	
	if xk==True and xv==True:
		ykv=True
		y=1
	if xk==True and x10==True:
		yk10=True
		y=1
	if xk==True and x9==True:
		yk9=True
		y=1
	if xk==True and x8==True:
		yk8=True
		y=1
	if xk==True and x7==True:
		yk7=True
		y=1
	if xk==True and x6==True:
		yk6=True
		y=1
	if xk==True and x5==True:
		yk5=True
		y=1
	if xk==True and x4==True:
		yk4=True
		y=1
	if xk==True and x3==True:
		yk3=True
		y=1
	if xk==True and x2==True:
		yk2=True
		y=1
	if xd==True and xv==True:
		ydv=True
		y=1
	if xd==True and x10==True:
		yd10=True
		y=1	
	if xd==True and x9==True:
		yd9=True
		y=1
	if xd==True and x8==True:
		yd8=True
		y=1
	if xd==True and x7==True:
		yd7=True
		y=1
	if xd==True and x6==True:
		yd6=True
		y=1
	if xd==True and x5==True:
		yd5=True
		y=1
	if xd==True and x4==True:
		yd4=True
		y=1
	if xd==True and x3==True:
		yd3=True
		y=1
	if xd==True and x2==True:
		yd2=True
		y=1
	if xv==True and x10==True:
		yv10=True
		y=1
	if xv==True and x9==True:
		yv9=True	
		y=1
	if xv==True and x8==True:
		yv8=True
		y=1	
	if xv==True and x7==True:
		yv7=True
		y=1	
	if xv==True and x6==True:
		yv6=True
		y=1	
	if xv==True and x5==True:
		yv5=True
		y=1	
	if xv==True and x4==True:
		yv4=True
		y=1	
	if xv==True and x3==True:
		yv3=True
		y=1	
	if xv==True and x2==True:
		yv2=True
		y=1	
	if x10==True and x9==True:
		y109=True	
		y=1
	if x10==True and x8==True:
		y108=True	
		y=1
	if x10==True and x7==True:
		y107=True	
		y=1
	if x10==True and x6==True:
		y106=True	
		y=1
	if x10==True and x5==True:
		y105=True	
		y=1
	if x10==True and x4==True:
		y104=True	
		y=1
	if x10==True and x3==True:
		y103=True	
		y=1
	if x10==True and x2==True:
		y102=True
		y=1
	if x9==True and x8==True:
		y98=True	
		y=1
	if x9==True and x7==True:
		y97=True
		y=1
	if x9==True and x6==True:
		y96=True
		y=1
	if x9==True and x5==True:
		y95=True
		y=1
	if x9==True and x4==True:
		y94=True
		y=1
	if x9==True and x3==True:
		y93=True
		y=1
	if x9==True and x2==True:
		y92=True
		y=1
	if x8==True and x7==True:
		y87=True
		y=1
	if x8==True and x6==True:
		y86=True
		y=1
	if x8==True and x5==True:
		y85=True
		y=1
	if x8==True and x4==True:
		y84=True
		y=1
	if x8==True and x3==True:
		y83=True
		y=1
	if x8==True and x2==True:
		y82=True
		y=1
	if x7==True and x6==True:
		y76=True
		y=1	
	if x7==True and x5==True:
		y75=True
		y=1
	if x7==True and x4==True:
		y74=True
		y=1
	if x7==True and x3==True:
		y73=True
		y=1
	if x7==True and x2==True:
		y72=True
		y=1
	if x6==True and x5==True:
		y65=True	
		y=1
	if x6==True and x4==True:
		y64=True
		y=1
	if x6==True and x3==True:
		y63=True
		y=1
	if x6==True and x2==True:
		y62=True
		y=1
	if x5==True and x4==True:
		y54=True
		y=1
	if x5==True and x3==True:
		y53=True
		y=1
	if x5==True and x2==True:
		y52=True
		y=1
	if x4==True and x3==True:
		y43=True
		y=1
	if x4==True and x2==True:
		y42=True
		y=1
	if x3==True and x2==True:
		y32=True	
		y=1																											
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
			pr2=pr2+1								
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
	flash(cards)
	strit(rangs)
	set(rangs)
	pairs(rangs)
	two_pairs()
	result_kiker=kiker(rangs)
	if 3==4:
		pass
	elif flash_result==True:
		if flashp==True:
			print('У вас флеш из Пик')	
		if flashb==True:
			print('У вас флеш из Бубей')
		if flashc==True:
			print('У вас флеш из Червей')
		if flashk==True:
			print('У вас флеш из Крестей')			
	elif strit_result==True:
		if strit_t==True:
			print('У вас стрит с 10 до туза')	
		elif strit_k==True:
			print('У вас стрит с 9 до короля')	
		elif strit_d==True:
			print('У вас стрит с 8 до дамы')	
		elif strit_v==True:
			print('У вас стрит с 7 до вальта')	
		elif strit_10==True:
			print('У вас стрит с 6 до 10')	
		elif strit_9==True:
			print('У вас стрит с 5 до 9')	
		elif strit_8==True:
			print('У вас стрит с 4 до 8')	
		elif strit_7==True:
			print('У вас стрит с 3 до 7')	
		elif strit_6==True:
			print('У вас стрит с 2 до 6')	
		else:
			pass										
	elif zp==True:
		if zt==True:
			print('У вас сет на тузах')
		elif zk==True:
			print('У вас сет на королях')	
		elif zd==True:
			print('У вас сет на дамах')	
		elif zv==True:
			print('У вас сет на вальтах')	
		elif z10==True:
			print('У вас сет на десятках')	
		elif z9==True:
			print('У вас сет на девятках')	
		elif z8==True:
			print('У вас сет на восьмерках')	
		elif z7==True:
			print('У вас сет на семерках')	
		elif z6==True:
			print('У вас сет на шестерках')	
		elif z5==True:
			print('У вас сет на пятерках')	
		elif z4==True:
			print('У вас сет на четверках')	
		elif z3==True:
			print('У вас сет на тройках')	
		elif z2==True:
			print('У вас сет на двойках')	
		else:
			pass				
	elif y==1:
		if ytk==True:
			print("У вас 2 пары из тузов и королей")
		elif ytd==True:
			print("У вас 2 пары из тузов и дам")
		elif ytv==True:
			print("У вас 2 пары из тузов и вальтов")
		elif yt10==True:
			print("У вас 2 пары из тузов и десяток")
		elif yt9==True:
			print("У вас 2 пары из тузов и девяток")
		elif yt8==True:
			print("У вас 2 пары из тузов и восьмерок")
		elif yt7==True:
			print("У вас 2 пары из тузов и семерок")
		elif yt6==True:
			print("У вас 2 пары из тузов и шестерок")
		elif yt5==True:
			print("У вас 2 пары из тузов и пятерок")
		elif yt4==True:
			print("У вас 2 пары из тузов и четверок")
		elif yt3==True:
			print("У вас 2 пары из тузов и троек")
		elif yt2==True:
			print("У вас 2 пары из тузов и двоек")
		elif ykd==True:
			print("У вас 2 пары из королей и дам")
		elif ykv==True:
			print("У вас 2 пары из королей и вальтов")
		elif yk10==True:
			print("У вас 2 пары из королей и девяток")
		elif yk9==True:
			print("У вас 2 пары из королей и девяток")
		elif yk8==True:
			print("У вас 2 пары из королей и восьмерок")
		elif yk7==True:
			print("У вас 2 пары из королей и семерок")
		elif yk6==True:
			print("У вас 2 пары из королей и шестерок")
		elif yk5==True:
			print("У вас 2 пары из королей и пятерок")
		elif yk4==True:
			print("У вас 2 пары из королей и четверок")
		elif yk3==True:
			print("У вас 2 пары из королей и троек")
		elif yk2==True:
			print("У вас 2 пары из королей и двоек")	
		elif ydv==True:
			print("У вас 2 пары из дам и вальтов")	
		elif yd10==True:
			print("У вас 2 пары из дам и десяток")	
		elif yd9==True:
			print("У вас 2 пары из дам и девяток")	
		elif yd8==True:
			print("У вас 2 пары из дам и восьмерок")	
		elif yd7==True:
			print("У вас 2 пары из дам и семерок")	
		elif yd6==True:
			print("У вас 2 пары из дам и шестерок")	
		elif yd5==True:
			print("У вас 2 пары из дам и пятерок")	
		elif yd4==True:
			print("У вас 2 пары из дам и четверок")	
		elif yd3==True:
			print("У вас 2 пары из дам и троек")	
		elif yd2==True:
			print("У вас 2 пары из дам и двоек")
		elif yv10==True:
			print("У вас 2 пары из вальтов и десяток")			
		elif yv9==True:
			print("У вас 2 пары из вальтов и девяток")	
		elif yv8==True:
			print("У вас 2 пары из вальтов и восьмерок")	
		elif yv7==True:
			print("У вас 2 пары из вальтов и семерок")	
		elif yv6==True:
			print("У вас 2 пары из вальтов и шестерок")	
		elif yv5==True:
			print("У вас 2 пары из вальтов и пятерок")	
		elif yv4==True:
			print("У вас 2 пары из вальтов и четверок")	
		elif yv3==True:
			print("У вас 2 пары из вальтов и троек")																																										
		elif yv2==True:
			print("У вас 2 пары из вальтов и двоек")
		elif yv10==True:
			print("У вас 2 пары из вальтов и десяток")	
		elif y109==True:
			print("У вас 2 пары из десяток и девяток")	
		elif y108==True:
			print("У вас 2 пары из десяток и восьмерок")	
		elif y107==True:
			print("У вас 2 пары из десяток и семерок")	
		elif y106==True:
			print("У вас 2 пары из десяток и шестерок")	
		elif y105==True:
			print("У вас 2 пары из десяток и пятерок")	
		elif y104==True:
			print("У вас 2 пары из десяток и четверок")	
		elif y103==True:
			print("У вас 2 пары из десяток и троек")	
		elif y102==True:
			print("У вас 2 пары из десяток и двоек")	
		elif y98==True:
			print("У вас 2 пары из девяток и восьмерок")		
		elif y97==True:
			print("У вас 2 пары из девяток и семерок")
		elif y96==True:
			print("У вас 2 пары из девяток и шестерок")
		elif y95==True:
			print("У вас 2 пары из девяток и пятерок")
		elif y94==True:
			print("У вас 2 пары из девяток и четверок")
		elif y93==True:
			print("У вас 2 пары из девяток и троек")
		elif y92==True:
			print("У вас 2 пары из девяток и двоек")
		elif y87==True:
			print("У вас 2 пары из восьмерок и семерок")	
		elif y86==True:
			print("У вас 2 пары из восьмерок и шестерок")
		elif y85==True:
			print("У вас 2 пары из восьмерок и пятерок")
		elif y84==True:
			print("У вас 2 пары из восьмерок и четверок")
		elif y83==True:
			print("У вас 2 пары из восьмерок и троек")
		elif y82==True:
			print("У вас 2 пары из восьмерок и двоек")
		elif y76==True:
			print("У вас 2 пары из семерок и шестерок")	
		elif y75==True:
			print("У вас 2 пары из семерок и пятерок")	
		elif y74==True:
			print("У вас 2 пары из семерок и четверок")	
		elif y73==True:
			print("У вас 2 пары из семерок и троек")	
		elif y72==True:
			print("У вас 2 пары из семерок и двоек")	
		elif y65==True:
			print("У вас 2 пары из шестерок и пятерок")	
		elif y64==True:
			print("У вас 2 пары из шестерок и четверок")	
		elif y63==True:
			print("У вас 2 пары из шестерок и троек")	
		elif y62==True:
			print("У вас 2 пары из шестерок и двоек")	
		elif y54==True:
			print("У вас 2 пары из пятерок и четверок")		
		elif y53==True:
			print("У вас 2 пары из пятерок и троек")	
		elif y52==True:
			print("У вас 2 пары из пятерок и двоек")	
		elif y43==True:
			print("У вас 2 пары из четверок и троек")	
		elif y42==True:
			print("У вас 2 пары из четверок и двоек")																																			
		elif y32==True:
			print("У вас 2 пары из троек и двоек")
		else:
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
	print(x1_c+' '+x2_c)
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
	print(x1_c+' '+x2_c)
	print('')
	print('')
	print('')
	print('******************************************')
	print('Карты на столе: ')
	print(y1_c+' '+y2_c+' '+y3_c)
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
	print(y1_c+' '+y2_c+' '+y3_c+' '+y4_c)
	print('')
	print('')
	print('')
	print('******************************************')
	print('Ваши карты: ')
	print(x1_c+' '+x2_c)
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
	print(y1_c+' '+y2_c+' '+y3_c+' '+y4_c+' '+y5_c)
	print('')
	print('')
	print('')
	print('******************************************')
	print('Ваши карты: ')
	print(x1_c+' '+x2_c)
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
						print(z1_c+' '+z2_c)
						print('******************************************')
						print('Ваши карты: ')
						print(x1_c+' '+x2_c)
						print('******************************************')
						print('Карты на столе')
						print(y1_c+' '+y2_c+' '+y3_c+' '+y4_c+' '+y5_c)	
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


	#Сделать нормальный рандом карт(т.е добавить проверку повторяющихся карт)
	#Сделать простейший исскуственный интеллект
	#Сделать картинки для каждой карты
	#Сделать вывод комбинации и для карт ПК
	#Сделать автоматическое сравнение между картами
	#Сделать так чтобы bet не могла быть больше имеющихся денег
	#организовать all-in
	#Добавить функцию сравнения карт(в процессе)
