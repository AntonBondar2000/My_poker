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
	#cards=['krest','krest','krest','krest','krest',y41,'bubi']								#	Пробные масти
	rangs=[x12,x22,y12,y22,y32_c,y42_c,y52_c]
	#rangs=['6','7','8','9','2',y42_c,'10']													#   Пробные ранги
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
def flash_royal():
	global flash_royal_resut
	flash_royal_resut=False
	if flash_result==True and strit_t==True:
		flash_royal_resut=True
	else:
		pass	
	
def strit_flesh():
	global strit_flesh_result
	strit_flesh_result=False
	if flash_result==True and strit_result==True:
		strit_flesh_result=True
	else:
		pass			
def kare(rangs):
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
	global kare_result
	kare_result=False
	global karet
	karet=False
	global karek
	karek=False
	global kared
	kared=False
	global karev
	karev=False
	global kare10
	kare10=False
	global kare9
	kare9=False
	global kare8
	kare8=False
	global kare7
	kare7=False
	global kare6
	kare6=False
	global kare5
	kare5=False
	global kare4
	kare4=False
	global kare3
	kare3=False
	global kare2
	kare2=False	
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
	if pr1==4:
		karet=True
		kare_result=True
	if pr2==4:
		karek=True	
		kare_result=True
	if pr3==4:
		kared=True
		kare_result=True	
	if pr4==4:
		karev=True
		kare_result=True	
	if pr5==4:
		kare10=True
		kare_result=True	
	if pr6==4:
		kare9=True
		kare_result=True	
	if pr7==4:
		kare8=True
		kare_result=True	
	if pr8==4:
		kare7=True
		kare_result=True	
	if pr9==4:
		kare6=True
		kare_result=True	
	if pr10==4:
		kare5=True
		kare_result=True	
	if pr11==4:
		kare4=True
		kare_result=True	
	if pr12==4:
		kare3=True
		kare_result=True	
	if pr13==4:
		kare2=True
		kare_result=True	
	else:
		pass	
def full_house():
	global F_full
	F_full=False
	global ftk
	ftk=False
	global ftd
	ftd=False
	global ftv
	ftv=False
	global ft10
	ft10=False
	global ft9
	ft9=False
	global ft8
	ft8=False
	global ft7
	ft7=False
	global ft6
	ft6=False
	global ft5
	ft5=False
	global ft4
	ft4=False
	global ft3
	ft3=False
	global ft2
	ft2=False
	global fkt
	fkt=False
	global fkd
	fkd=False
	global fkv
	fkv=False
	global fk10
	fk10=False
	global fk9
	fk9=False
	global fk8
	fk8=False
	global fk7
	fk7=False
	global fk6
	fk6=False
	global fk5
	fk5=False
	global fk4
	fk4=False
	global fk3
	fk3=False
	global fk2
	fk2=False
	global fdt
	fdt=False
	global fdk
	fdk=False
	global fdv
	fdv=False
	global fd10
	fd10=False
	global fd9
	fd9=False
	global fd8
	fd8=False
	global fd7
	fd7=False
	global fd6
	fd6=False
	global fd5
	fd5=False
	global fd4
	fd4=False
	global fd3
	fd3=False
	global fd2
	fd2=False
	global fvt
	fvt=False
	global fvk
	fvk=False
	global fvd
	fvd=False
	global fv10
	fv10=False
	global fv9
	fv9=False
	global fv8
	fv8=False
	global fv7
	fv7=False
	global fv6
	fv6=False
	global fv5
	fv5=False
	global fv4
	fv4=False
	global fv3
	fv3=False
	global fv2
	fv2=False
	global f10t
	f10t=False
	global f10k
	f10k=False
	global f10d
	f10d=False
	global f10v
	f10v=False
	global f109
	f109=False
	global f108
	f108=False
	global f107
	f107=False
	global f106
	f106=False
	global f105
	f105=False
	global f104
	f104=False
	global f103
	f103=False
	global f102
	f102=False
	global f9t
	f9t=False
	global f9k
	f9k=False
	global f9d
	f9d=False
	global f9v
	f9v=False
	global f910
	f910=False
	global f98
	f98=False
	global f97
	f97=False
	global f96
	f96=False
	global f95
	f95=False
	global f94
	f94=False
	global f93
	f93=False
	global f92
	f92=False
	global f8t
	f8t=False
	global f8k
	f8k=False
	global f8d
	f8d=False
	global f8v
	f8v=False
	global f810
	f810=False
	global f89
	f89=False
	global f87
	f87=False
	global f86
	f86=False
	global f85
	f85=False
	global f84
	f84=False
	global f83
	f83=False
	global f82
	f82=False
	global f7t
	f7t=False
	global f7k
	f7k=False
	global f7d
	f7d=False
	global f7v
	f7v=False
	global f710
	f710=False
	global f79
	f79=False
	global f78
	f78=False
	global f76
	f76=False
	global f75
	f75=False
	global f74
	f74=False
	global f73
	f73=False
	global f72
	f72=False
	global f6t
	f6t=False
	global f6k
	f6k=False
	global f6d
	f6d=False
	global f6v
	f6v=False
	global f610
	f610=False
	global f69
	f69=False
	global f68
	f68=False
	global f67
	f67=False
	global f65
	f65=False
	global f64
	f64=False
	global f63
	f63=False
	global f62
	f62=False
	global f5t
	f5t=False
	global f5k
	f5k=False
	global f5d
	f5d=False
	global f5v
	f5v=False
	global f510
	f510=False
	global f59
	f59=False
	global f58
	f58=False
	global f57
	f57=False
	global f56
	f56=False
	global f54
	f54=False
	global f53
	f53=False
	global f52
	f52=False
	global f4t
	f4t=False
	global f4k
	f4k=False
	global f4d
	f4d=False
	global f4v
	f4v=False
	global f410
	f410=False
	global f49
	f49=False
	global f48
	f48=False
	global f47
	f47=False
	global f46
	f46=False
	global f45
	f45=False
	global f43
	f43=False
	global f42
	f42=False
	global f3t
	f3t=False
	global f3k
	f3k=False
	global f3d
	f3d=False
	global f3v
	f3v=False
	global f310
	f310=False
	global f39
	f39=False
	global f38
	f38=False
	global f37
	f37=False
	global f36
	f36=False
	global f35
	f35=False
	global f34
	f34=False
	global f32
	f32=False
	global f2t
	f2t=False
	global f2k
	f2k=False
	global f2d
	f2d=False
	global f2v
	f2v=False
	global f210
	f210=False
	global f29
	f29=False
	global f28
	f28=False
	global f27
	f27=False
	global f26
	f26=False
	global f25
	f25=False
	global f24
	f24=False
	global f23
	f23=False
	if zt==True and xk==True:
		F_full=True
		ftk=True
	if zt==True and xd==True:
		F_full=True
		ftd=True
	if zt==True and xv==True:
		F_full=True
		ftv=True
	if zt==True and x10==True:
		F_full=True
		ft10=True
	if zt==True and x9==True:
		F_full=True
		ft9=True
	if zt==True and x8==True:
		F_full=True
		ft8=True
	if zt==True and x7==True:
		F_full=True
		ft7=True
	if zt==True and x6==True:
		F_full=True
		ft6=True
	if zt==True and x5==True:
		F_full=True
		ft5=True
	if zt==True and x4==True:
		F_full=True
		ft4=True
	if zt==True and x3==True:
		F_full=True
		ft3=True
	if zt==True and x2==True:
		F_full=True
		ft2=True
	if zk==True and xt==True:
		F_full=True
		fkt=True	
	if zk==True and xd==True:
		F_full=True
		fkd=True	
	if zk==True and xv==True:
		F_full=True
		fkv=True	
	if zk==True and x10==True:
		F_full=True
		fk10=True	
	if zk==True and x9==True:
		F_full=True
		fk9=True	
	if zk==True and x8==True:
		F_full=True
		fk8=True	
	if zk==True and x7==True:
		F_full=True
		fk7=True	
	if zk==True and x6==True:
		F_full=True
		fk6=True	
	if zk==True and x5==True:
		F_full=True
		fk5=True	
	if zk==True and x4==True:
		F_full=True
		fk4=True	
	if zk==True and x3==True:
		F_full=True
		fk3=True	
	if zk==True and x2==True:
		F_full=True
		fk2=True
	if zd==True and xt==True:
		F_full=True
		fdt=True	
	if zd==True and xk==True:
		F_full=True
		fdk=True
	if zd==True and xv==True:
		F_full=True
		fdv=True
	if zd==True and x10==True:
		F_full=True
		fd10=True
	if zd==True and x9==True:
		F_full=True
		fd9=True
	if zd==True and x8==True:
		F_full=True
		fd8=True
	if zd==True and x7==True:
		F_full=True
		fd7=True
	if zd==True and x6==True:
		F_full=True
		fd6=True
	if zd==True and x5==True:
		F_full=True
		fd5=True
	if zd==True and x4==True:
		F_full=True
		fd4=True
	if zd==True and x3==True:
		F_full=True
		fd3=True
	if zd==True and x2==True:
		F_full=True
		fd2=True			
	if zv==True and xt==True:
		F_full=True
		fvt=True	
	if zv==True and xk==True:
		F_full=True
		fvk=True	
	if zv==True and xd==True:
		F_full=True
		fvd=True	
	if zv==True and x10==True:
		F_full=True
		fv10=True	
	if zv==True and x9==True:
		F_full=True
		fv9=True	
	if zv==True and x8==True:
		F_full=True
		fv8=True	
	if zv==True and x7==True:
		F_full=True
		fv7=True	
	if zv==True and x6==True:
		F_full=True
		fv6=True	
	if zv==True and x5==True:
		F_full=True
		fv5=True	
	if zv==True and x4==True:
		F_full=True
		fv4=True	
	if zv==True and x3==True:
		F_full=True
		fv3=True	
	if zv==True and x2==True:
		F_full=True
		fv2=True	
	if z10==True and xt==True:
		F_full=True
		f10t=True	
	if z10==True and xk==True:
		F_full=True
		f10k=True
	if z10==True and xd==True:
		F_full=True
		f10d=True
	if z10==True and xv==True:
		F_full=True
		f10v=True
	if z10==True and x9==True:
		F_full=True
		f109=True
	if z10==True and x8==True:
		F_full=True
		f108=True
	if z10==True and x7==True:
		F_full=True
		f107=True
	if z10==True and x6==True:
		F_full=True
		f106=True
	if z10==True and x5==True:
		F_full=True
		f105=True
	if z10==True and x4==True:
		F_full=True
		f104=True
	if z10==True and x3==True:
		F_full=True
		f103=True
	if z10==True and x2==True:
		F_full=True
		f102=True
	if z9==True and xt==True:
		F_full=True
		f9t=True	
	if z9==True and xk==True:
		F_full=True
		f9k=True
	if z9==True and xd==True:
		F_full=True
		f9d=True
	if z9==True and xv==True:
		F_full=True
		f9v=True
	if z9==True and x10==True:
		F_full=True
		f910=True
	if z9==True and x8==True:
		F_full=True
		f98=True
	if z9==True and x7==True:
		F_full=True
		f97=True
	if z9==True and x6==True:
		F_full=True
		f96=True
	if z9==True and x5==True:
		F_full=True
		f95=True
	if z9==True and x4==True:
		F_full=True
		f94=True
	if z9==True and x3==True:
		F_full=True
		f93=True
	if z9==True and x2==True:
		F_full=True
		f92=True
	if z8==True and xt==True:
		F_full=True
		f8t=True	
	if z8==True and xk==True:
		F_full=True
		f8k=True
	if z8==True and xd==True:
		F_full=True
		f8d=True
	if z8==True and xv==True:
		F_full=True
		f8v=True
	if z8==True and x10==True:
		F_full=True
		f810=True
	if z8==True and x9==True:
		F_full=True
		f89=True
	if z8==True and x7==True:
		F_full=True
		f87=True
	if z8==True and x6==True:
		F_full=True
		f86=True
	if z8==True and x5==True:
		F_full=True
		f85=True
	if z8==True and x4==True:
		F_full=True
		f84=True
	if z8==True and x3==True:
		F_full=True
		f83=True
	if z8==True and x2==True:
		F_full=True
		f82=True	
	if z7==True and xt==True:
		F_full=True
		f7t=True	
	if z7==True and xk==True:
		F_full=True
		f7k=True
	if z7==True and xd==True:
		F_full=True
		f7d=True
	if z7==True and xv==True:
		F_full=True
		f7v=True
	if z7==True and x10==True:
		F_full=True
		f710=True
	if z7==True and x9==True:
		F_full=True
		f79=True
	if z7==True and x8==True:
		F_full=True
		f78=True
	if z7==True and x6==True:
		F_full=True
		f76=True
	if z7==True and x5==True:
		F_full=True
		f75=True
	if z7==True and x4==True:
		F_full=True
		f74=True
	if z7==True and x3==True:
		F_full=True
		f73=True
	if z7==True and x2==True:
		F_full=True
		f72=True		
	if z6==True and xt==True:
		F_full=True
		f6t=True	
	if z6==True and xk==True:
		F_full=True
		f6k=True	
	if z6==True and xd==True:
		F_full=True
		f6d=True	
	if z6==True and xv==True:
		F_full=True
		f6v=True	
	if z6==True and x10==True:
		F_full=True
		f610=True	
	if z6==True and x9==True:
		F_full=True
		f69=True	
	if z6==True and x8==True:
		F_full=True
		f68=True	
	if z6==True and x7==True:
		F_full=True
		f67=True	
	if z6==True and x5==True:
		F_full=True
		f65=True	
	if z6==True and x4==True:
		F_full=True
		f64=True	
	if z6==True and x3==True:
		F_full=True
		f63=True	
	if z6==True and x2==True:
		F_full=True
		f62=True
	if z5==True and xt==True:
		F_full=True
		f5t=True		
	if z5==True and xk==True:
		F_full=True
		f5k=True
	if z5==True and xd==True:
		F_full=True
		f5d=True
	if z5==True and xv==True:
		F_full=True
		f5v=True
	if z5==True and x10==True:
		F_full=True
		f510=True
	if z5==True and x9==True:
		F_full=True
		f59=True
	if z5==True and x8==True:
		F_full=True
		f58=True
	if z5==True and x7==True:
		F_full=True
		f57=True
	if z5==True and x6==True:
		F_full=True
		f56=True
	if z5==True and x4==True:
		F_full=True
		f54=True
	if z5==True and x3==True:
		F_full=True
		f53=True
	if z5==True and x2==True:
		F_full=True
		f52=True	
	if z4==True and xt==True:
		F_full=True
		f4t=True	
	if z4==True and xk==True:
		F_full=True
		f4k=True	
	if z4==True and xd==True:
		F_full=True
		f4d=True	
	if z4==True and xv==True:
		F_full=True
		f4v=True	
	if z4==True and x10==True:
		F_full=True
		f410=True	
	if z4==True and x9==True:
		F_full=True
		f49=True	
	if z4==True and x8==True:
		F_full=True
		f48=True	
	if z4==True and x7==True:
		F_full=True
		f47=True	
	if z4==True and x6==True:
		F_full=True
		f46=True	
	if z4==True and x5==True:
		F_full=True
		f45=True	
	if z4==True and x3==True:
		F_full=True
		f43=True	
	if z4==True and x2==True:
		F_full=True
		f42=True		
	if z3==True and xt==True:
		F_full=True
		f3t=True	
	if z3==True and xk==True:
		F_full=True
		f3k=True	
	if z3==True and xd==True:
		F_full=True
		f3d=True	
	if z3==True and xv==True:
		F_full=True
		f3v=True	
	if z3==True and x10==True:
		F_full=True
		f310=True	
	if z3==True and x9==True:
		F_full=True
		f39=True	
	if z3==True and x8==True:
		F_full=True
		f38=True	
	if z3==True and x7==True:
		F_full=True
		f37=True	
	if z3==True and x6==True:
		F_full=True
		f36=True	
	if z3==True and x5==True:
		F_full=True
		f35=True	
	if z3==True and x4==True:
		F_full=True
		f34=True	
	if z3==True and x2==True:
		F_full=True
		f32=True	
	if z2==True and xt==True:
		F_full=True
		f2t=True
	if z2==True and xk==True:
		F_full=True
		f2k=True
	if z2==True and xd==True:
		F_full=True
		f2d=True
	if z2==True and xv==True:
		F_full=True
		f2v=True
	if z2==True and x10==True:
		F_full=True
		f210=True
	if z2==True and x9==True:
		F_full=True
		f29=True
	if z2==True and x8==True:
		F_full=True
		f28=True
	if z2==True and x7==True:
		F_full=True
		f27=True
	if z2==True and x6==True:
		F_full=True
		f26=True
	if z2==True and x5==True:
		F_full=True
		f25=True
	if z2==True and x4==True:
		F_full=True
		f24=True
	if z2==True and x3==True:
		F_full=True
		f23=True																																																																													
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
	kare(rangs)
	flash(cards)
	strit(rangs)
	flash_royal()
	strit_flesh()
	set(rangs)
	pairs(rangs)
	full_house()
	two_pairs()
	result_kiker=kiker(rangs)
	if flash_royal_resut==True:
		print('У вас Роял Флеш, самая высокая комбинация в игре')
	elif strit_flesh_result==True:
		print('У вас Стрит флэш')	
	elif kare_result==True:
		if karet==True:
			print('У вас каре из тузов')
		elif karek==True:
			print('У вас каре из королей')
		elif kared==True:
			print('У вас каре из дам')
		elif karev==True:
			print('У вас каре из вальтов')
		elif kare10==True:
			print('У вас каре из десяток')
		elif kare9==True:
			print('У вас каре из девяток')
		elif kare8==True:
			print('У вас каре из восьмерок')
		elif kare7==True:
			print('У вас каре из семерок')
		elif kare6==True:
			print('У вас каре из шестерок')
		elif kare5==True:
			print('У вас каре из пятерок')
		elif kare4==True:
			print('У вас каре из четверок')
		elif kare3==True:
			print('У вас каре из троек')
		elif kare2==True:
			print('У вас каре из двоек')														
	elif F_full==True:
		if	ftk==True:
			print('У вас фулл Хаус из 3 тузов и 2 королей')
		elif ftd==True:
			print('У вас фулл Хаус из 3 тузов и 2 дам')
		elif ftv==True:
			print('У вас фулл Хаус из 3 тузов и 2 вальтов')
		elif ft10==True:
			print('У вас фулл Хаус из 3 тузов и 2 девяток')
		elif ft9==True:
			print('У вас фулл Хаус из 3 тузов и 2 девяток')
		elif ft8==True:
			print('У вас фулл Хаус из 3 тузов и 2 восьмерок')
		elif ft7==True:
			print('У вас фулл Хаус из 3 тузов и 2 семерок')
		elif ft6==True:
			print('У вас фулл Хаус из 3 тузов и 2 шестерок')
		elif ft5==True:
			print('У вас фулл Хаус из 3 тузов и 2 пятерок')
		elif ft4==True:
			print('У вас фулл Хаус из 3 тузов и 2 четверок')
		elif ft3==True:
			print('У вас фулл Хаус из 3 тузов и 2 троек')
		elif ft2==True:
			print('У вас фулл Хаус из 3 тузов и 2 двоек')	
		elif fkt==True:
			print('У вас фулл Хаус из 3 королей и 2 тузов')		
		elif fkd==True:
			print('У вас фулл Хаус из 3 королей и 2 дам')
		elif fkv==True:
			print('У вас фулл Хаус из 3 королей и 2 вальтов')
		elif fk10==True:
			print('У вас фулл Хаус из 3 королей и 2 десяток')
		elif fk9==True:
			print('У вас фулл Хаус из 3 королей и 2 девяток')
		elif fk8==True:
			print('У вас фулл Хаус из 3 королей и 2 восьмерок')
		elif fk7==True:
			print('У вас фулл Хаус из 3 королей и 2 семерок')
		elif fk6==True:
			print('У вас фулл Хаус из 3 королей и 2 шестерок')
		elif fk5==True:
			print('У вас фулл Хаус из 3 королей и 2 пятерок')
		elif fk4==True:
			print('У вас фулл Хаус из 3 королей и 2 четверок')
		elif fk3==True:
			print('У вас фулл Хаус из 3 королей и 2 троек')
		elif fk2==True:
			print('У вас фулл Хаус из 3 королей и 2 двоек')
		elif fdt==True:
			print('У вас фулл Хаус из 3 дам и 2 тузов')
		elif fdk==True:
			print('У вас фулл Хаус из 3 дам и 2 королей')
		elif fdv==True:
			print('У вас фулл Хаус из 3 дам и 2 вальтов')
		elif fd10==True:
			print('У вас фулл Хаус из 3 дам и 2 десяток')
		elif fd9==True:
			print('У вас фулл Хаус из 3 дам и 2 девяток')
		elif fd8==True:
			print('У вас фулл Хаус из 3 дам и 2 восьмерок')
		elif fd7==True:
			print('У вас фулл Хаус из 3 дам и 2 семерок')
		elif fd6==True:
			print('У вас фулл Хаус из 3 дам и 2 шестерок')
		elif fd5==True:
			print('У вас фулл Хаус из 3 дам и 2 пятерок')
		elif fd4==True:
			print('У вас фулл Хаус из 3 дам и 2 четверок')
		elif fd3==True:
			print('У вас фулл Хаус из 3 дам и 2 троек')		
		elif fd2==True:
			print('У вас фулл Хаус из 3 дам и 2 двоек')		
		elif fvt==True:
			print('У вас фулл Хаус из 3 вальтов и 2 тузов')	
		elif fvk==True:
			print('У вас фулл Хаус из 3 вальтов и 2 королей')	
		elif fvd==True:
			print('У вас фулл Хаус из 3 вальтов и 2 дам')	
		elif fv10==True:
			print('У вас фулл Хаус из 3 вальтов и 2 десяток')	
		elif fv9==True:
			print('У вас фулл Хаус из 3 вальтов и 2 девяток')	
		elif fv8==True:
			print('У вас фулл Хаус из 3 вальтов и 2 восьмерок')	
		elif fv7==True:
			print('У вас фулл Хаус из 3 вальтов и 2 семерок')	
		elif fv6==True:
			print('У вас фулл Хаус из 3 вальтов и 2 шестерок')	
		elif fv5==True:
			print('У вас фулл Хаус из 3 вальтов и 2 пятерок')	
		elif fv4==True:
			print('У вас фулл Хаус из 3 вальтов и 2 четверок')	
		elif fv3==True:
			print('У вас фулл Хаус из 3 вальтов и 2 троек')	
		elif fv2==True:
			print('У вас фулл Хаус из 3 вальтов и 2 двоек')	
		elif f10t==True:
			print('У вас фулл Хаус из 3 десяток и 2 тузов')	
		elif f10k==True:
			print('У вас фулл Хаус из 3 десяток и 2 королей')	
		elif f10d==True:
			print('У вас фулл Хаус из 3 десяток и 2 дам')	
		elif f10v==True:
			print('У вас фулл Хаус из 3 десяток и 2 вальтов')	
		elif f109==True:
			print('У вас фулл Хаус из 3 десяток и 2 девяток')	
		elif f108==True:
			print('У вас фулл Хаус из 3 десяток и 2 восьмерок')	
		elif f107==True:
			print('У вас фулл Хаус из 3 десяток и 2 семерок')	
		elif f106==True:
			print('У вас фулл Хаус из 3 десяток и 2 шестерок')	
		elif f105==True:
			print('У вас фулл Хаус из 3 десяток и 2 пятерок')	
		elif f104==True:
			print('У вас фулл Хаус из 3 десяток и 2 четверок')	
		elif f103==True:
			print('У вас фулл Хаус из 3 десяток и 2 троек')	
		elif f102==True:
			print('У вас фулл Хаус из 3 десяток и 2 двоек')	
		elif f9t==True:
			print('У вас фулл Хаус из 3 девяток и 2 тузов')		
		elif f9k==True:
			print('У вас фулл Хаус из 3 девяток и 2 королей')
		elif f9d==True:
			print('У вас фулл Хаус из 3 девяток и 2 дам')
		elif f9v==True:
			print('У вас фулл Хаус из 3 девяток и 2 вальтов')
		elif f910==True:
			print('У вас фулл Хаус из 3 девяток и 2 десяток')
		elif f98==True:
			print('У вас фулл Хаус из 3 девяток и 2 восьмерок')
		elif f97==True:
			print('У вас фулл Хаус из 3 девяток и 2 семерок')
		elif f96==True:
			print('У вас фулл Хаус из 3 девяток и 2 шестерок')
		elif f95==True:
			print('У вас фулл Хаус из 3 девяток и 2 пятерок')
		elif f94==True:
			print('У вас фулл Хаус из 3 девяток и 2 четверок')
		elif f93==True:
			print('У вас фулл Хаус из 3 девяток и 2 троек')
		elif f92==True:
			print('У вас фулл Хаус из 3 девяток и 2 двоек')
		elif f8t==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 тузов')	
		elif f8k==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 королей')	
		elif f8d==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 дам')	
		elif f8v==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 вальтов')	
		elif f810==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 десяток')	
		elif f89==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 девяток')	
		elif f87==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 семерок')	
		elif f86==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 шестерок')	
		elif f85==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 пятерок')	
		elif f84==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 четверок')	
		elif f83==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 троек')	
		elif f82==True:
			print('У вас фулл Хаус из 3 восьмерок и 2 двоек')	
		elif f7t==True:
			print('У вас фулл Хаус из 3 семерок и 2 тузов')	
		elif f7k==True:
			print('У вас фулл Хаус из 3 семерок и 2 королей')	
		elif f7d==True:
			print('У вас фулл Хаус из 3 семерок и 2 дам')	
		elif f7v==True:
			print('У вас фулл Хаус из 3 семерок и 2 вальтов')	
		elif f710==True:
			print('У вас фулл Хаус из 3 семерок и 2 десяток')	
		elif f79==True:
			print('У вас фулл Хаус из 3 семерок и 2 девяток')	
		elif f78==True:
			print('У вас фулл Хаус из 3 семерок и 2 восьмерок')	
		elif f76==True:
			print('У вас фулл Хаус из 3 семерок и 2 шестерок')	
		elif f75==True:
			print('У вас фулл Хаус из 3 семерок и 2 пятерок')	
		elif f74==True:
			print('У вас фулл Хаус из 3 семерок и 2 четверок')	
		elif f73==True:
			print('У вас фулл Хаус из 3 семерок и 2 троек')	
		elif f72==True:
			print('У вас фулл Хаус из 3 семерок и 2 двоек')	
		elif f6t==True:
			print('У вас фулл Хаус из 3 шестерок и 2 тузов')
		elif f6k==True:
			print('У вас фулл Хаус из 3 шестерок и 2 королей')	
		elif f6d==True:
			print('У вас фулл Хаус из 3 шестерок и 2 дам')	
		elif f6v==True:
			print('У вас фулл Хаус из 3 шестерок и 2 вальтов')	
		elif f610==True:
			print('У вас фулл Хаус из 3 шестерок и 2 десяток')	
		elif f69==True:
			print('У вас фулл Хаус из 3 шестерок и 2 девяток')	
		elif f68==True:
			print('У вас фулл Хаус из 3 шестерок и 2 восьмерок')	
		elif f67==True:
			print('У вас фулл Хаус из 3 шестерок и 2 семерок')	
		elif f65==True:
			print('У вас фулл Хаус из 3 шестерок и 2 пятерок')	
		elif f64==True:
			print('У вас фулл Хаус из 3 шестерок и 2 четверок')	
		elif f63==True:
			print('У вас фулл Хаус из 3 шестерок и 2 троек')	
		elif f62==True:
			print('У вас фулл Хаус из 3 шестерок и 2 двоек')
		elif f5t==True:
			print('У вас фулл Хаус из 3 пятерок и 2 тузов')		
		elif f5k==True:
			print('У вас фулл Хаус из 3 пятерок и 2 королей')	
		elif f5d==True:
			print('У вас фулл Хаус из 3 пятерок и 2 дам')	
		elif f5v==True:
			print('У вас фулл Хаус из 3 пятерок и 2 вальтов')	
		elif f510==True:
			print('У вас фулл Хаус из 3 пятерок и 2 десяток')	
		elif f59==True:
			print('У вас фулл Хаус из 3 пятерок и 2 девяток')	
		elif f58==True:
			print('У вас фулл Хаус из 3 пятерок и 2 восьмерок')	
		elif f57==True:
			print('У вас фулл Хаус из 3 пятерок и 2 семерок')	
		elif f56==True:
			print('У вас фулл Хаус из 3 пятерок и 2 шестерок')	
		elif f54==True:
			print('У вас фулл Хаус из 3 пятерок и 2 четверок')	
		elif f53==True:
			print('У вас фулл Хаус из 3 пятерок и 2 троек')	
		elif f52==True:
			print('У вас фулл Хаус из 3 пятерок и 2 двоек')	
		elif f4t==True:
			print('У вас фулл Хаус из 3 четверок и 2 тузов')	
		elif f4k==True:
			print('У вас фулл Хаус из 3 четверок и 2 королей')	
		elif f4d==True:
			print('У вас фулл Хаус из 3 четверок и 2 дам')	
		elif f4v==True:
			print('У вас фулл Хаус из 3 четверок и 2 вальтов')	
		elif f410==True:
			print('У вас фулл Хаус из 3 четверок и 2 десяток')	
		elif f49==True:
			print('У вас фулл Хаус из 3 четверок и 2 девяток')	
		elif f48==True:
			print('У вас фулл Хаус из 3 четверок и 2 восьмерок')	
		elif f47==True:
			print('У вас фулл Хаус из 3 четверок и 2 семерок')	
		elif f46==True:
			print('У вас фулл Хаус из 3 четверок и 2 шестерок')	
		elif f45==True:
			print('У вас фулл Хаус из 3 четверок и 2 пятерок')	
		elif f43==True:
			print('У вас фулл Хаус из 3 четверок и 2 троек')	
		elif f42==True:
			print('У вас фулл Хаус из 3 четверок и 2 двоек')	
		elif f3t==True:
			print('У вас фулл Хаус из 3 троек и 2 тузов')	
		elif f3k==True:
			print('У вас фулл Хаус из 3 троек и 2 королей')
		elif f3d==True:
			print('У вас фулл Хаус из 3 троек и 2 дам')
		elif f3v==True:
			print('У вас фулл Хаус из 3 троек и 2 вальтов')
		elif f310==True:
			print('У вас фулл Хаус из 3 троек и 2 десяток')
		elif f39==True:
			print('У вас фулл Хаус из 3 троек и 2 девяток')
		elif f38==True:
			print('У вас фулл Хаус из 3 троек и 2 восьмерок')
		elif f37==True:
			print('У вас фулл Хаус из 3 троек и 2 семерок')
		elif f36==True:
			print('У вас фулл Хаус из 3 троек и 2 шестерок')
		elif f35==True:
			print('У вас фулл Хаус из 3 троек и 2 пятерок')
		elif f34==True:
			print('У вас фулл Хаус из 3 троек и 2 четверок')
		elif f32==True:
			print('У вас фулл Хаус из 3 троек и 2 двоек')
		elif f2t==True:
			print('У вас фулл Хаус из 3 двоек и 2 тузов')	
		elif f2k==True:
			print('У вас фулл Хаус из 3 двоек и 2 королей')
		elif f2d==True:
			print('У вас фулл Хаус из 3 двоек и 2 дам')
		elif f2v==True:
			print('У вас фулл Хаус из 3 двоек и 2 вальтов')
		elif f210==True:
			print('У вас фулл Хаус из 3 двоек и 2 десяток')
		elif f29==True:
			print('У вас фулл Хаус из 3 двоек и 2 девяток')
		elif f28==True:
			print('У вас фулл Хаус из 3 двоек и 2 восьмерок')
		elif f27==True:
			print('У вас фулл Хаус из 3 двоек и 2 семерок')
		elif f26==True:
			print('У вас фулл Хаус из 3 двоек и 2 шестерок')
		elif f25==True:
			print('У вас фулл Хаус из 3 двоек и 2 пятерок')
		elif f24==True:
			print('У вас фулл Хаус из 3 двоек и 2 четверок')
		elif f23==True:
			print('У вас фулл Хаус из 3 двоек и 2 троек')	
		else:
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
	#Сделать адекватный стрит флеш и флеш рояль
	
