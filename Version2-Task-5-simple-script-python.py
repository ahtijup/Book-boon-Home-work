#Version 2 of task5 

# Please install the required module
# pip install num2words
import num2words
for i in range(101):
    print(i)
	#checking if the number is divisible by 10 so that can get every tenth number.
    if i%10==0 and i/10>0:
	num2words.num2words(i)