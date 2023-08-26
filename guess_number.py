import random
start = input("Please enter a start number: ")
end = input("Please enter a end number: ")
start = int(start)
end = int(end)
r = random.randint(start, end)
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