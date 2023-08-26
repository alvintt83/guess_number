import random
r = random.randint(1, 50)
count = 0
while True:
	count += 1
	num = input("Enter your number: ")
	num = int(num)
	if r == num:
		print("You are right!")
		print("You've typed it in for the", count, "time now.")
		break
	elif r < num:
		print("The number you enter is too big!")
	elif r > num:
		print("The number you enter is small!")
	print("You've typed it in for the", count, "time now.")