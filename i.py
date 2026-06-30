a=input("What is your name..")
print ("hello",a,"choose your language")
H = "hindi"
E = "english"
while True:
	print (H,",",E,"(not contain h,e,H,E)")
	l = input("enter language..").lower()
	if l == H:
		user=input("kya haal hai..")
		print (user,"achha")
		break

	elif l== E:
		user=input("how are you..")
		print (user,"oh")
		break

	else:
		print ("....i am not understand.,.")


