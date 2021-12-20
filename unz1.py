from zipfile import ZipFile


i=50
while True:
	
	zipname='not_here'+str(i)+'.zip'
	with ZipFile(zipname,'r')as file:
		file.extractall()
	i=i-1
	print(zipname)
	if i==0:
		break;
	
