'''
	This code is looking from 1 through 100 
	* for numbers which they are disiable with 3 it prints fizz
	* for numbers which they are divisable with 5 it prints buzz
	* for numbers which they are divisable with 15 ot prints fizzbuzz
 
'''
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('fizzbuzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)
    

