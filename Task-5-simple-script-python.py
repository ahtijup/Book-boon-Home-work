
#storing all the tenth words in a list so that can call them
wordy = ["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety","hundred"]

for i in range(101):
    print(i)
	#checking if the number is divisible by 10 so that can get every tenth number.
    if i%10==0 and i/10 >0:
	# getting the quotient number so that list of wordy can be called.
     quotent= i/10
     intQuotent=int(quotent-1)
     print(wordy[intQuotent])