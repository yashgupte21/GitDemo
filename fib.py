
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
Notes
fibo upto 4 million [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578]
32 terms, however while solving this problem we will assume that we have no previous knowledge and about fibonacci sequence expect for our alogrithm
'''
import time

def fibb(first, second):
	return first+second

def main():
	statTime = time.time()
	first = 0
	second = 1
	sum = 0
	next = 0

	while next<3000000:
		next = fibb(first,second)
		first = second
		second = next

		if next%2==0:
			sum = sum + next

	print('Sum :',sum)

	print('Time : %s seconds' % (time.time()-statTime))

if __name__ == "__main__":
    main()
