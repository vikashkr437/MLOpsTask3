file1=open("/root/workspace/iterations.txt","r")
i=int(file1.read())
file1.close()

file1=open("/root/workspace/layers.txt","r")
l=int(file.read())
file1.close()

file1=open("/root/workspace/repeats.txt","r")
r=int(file1.read())
file1.close()

if i < 3 :
	l+=1
	file1=open("/root/workspace/layers.txt","w")
	file1.write(str(l))
	file1.close()
else :
	r+=1
	file1=open("/root/workspace/repeats.txt","w")
	file1.write(str(r))
	file1.close()

i+=1
file1=open("/root/workspace/iterations.txt","w")
file1.write(str(i))
file1.close()
