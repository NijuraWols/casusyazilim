import os,re
girilen_dizinler = []
 
def BulunanDizin(gelendizin):
	os.chdir(gelendizin)
	print "girilen dizin >> "+ gelendizin
	girilen_dizinler.append(gelendizin)
	KontrolEt()
	os.chdir(os.pardir)
 
def KontrolEt():
	dosyalr = os.listdir(os.getcwd())
	for i in dosyalr:
		try:
			if re.match(".*txt",i):
				os.remove(i)
			elif re.match(".*pdf",i):
				os.remove(i)
			elif re.match(".*docx",i):
				os.remove(i)
			elif re.match(".*doc",i):
				os.remove(i)
			elif re.match(".*xls",i):
				os.remove(i)
			elif os.path.isdir(i):
				if girilen_dizinler.count(i) == 0:
					BulunanDizin(i)
				else:
					pass
			else:
				pass
		except:
			pass
 
 
suanki_dizin = os.getcwd() #bulundugu dizin
a = suanki_dizin.split("/")
sayi = len(a)-1
for i in range(0,sayi):
	os.chdir(os.pardir)
KontrolEt()
