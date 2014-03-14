
import random
from time import clock

import numpy

def naive_method(A):

	n = len(A)

	for i in range(n):
		for j in range(n):
			for k in range(n):
				if i!=j and i!=k and j!=k:
					if A[i][j] <= max(A[j][k], A[i][k]):
						pass
					else:
						print i, j, k
						print A[i][j], A[j][k], A[i][k]

						print A
						return False

	return True

def brabham(A):
	n = len(A)

	#print A
	if n==1:
		return True
	else:
		C = [B[0:n-1] for B in A[0:n-1]]

		x = brabham(C)

		if x==False:
			return False

		#sort along the column
		last_col = [(i, A[n-1][i]) for i in range(n)]

		col_sorted = sorted(last_col, key=lambda tup: tup[1])

		for i in range(n-1):
			cur_tup = col_sorted[i-1]
			next_tup = col_sorted[i+1]

			if cur_tup[1]==next_tup[1]:
				if A[cur_tup[0]][next_tup[0]]<=cur_tup[1]:
					pass
				else:
					return False
			elif cur_tup[1]<next_tup[1]:
				if A[cur_tup[0]][next_tup[0]]==next_tup[1]:
					pass
				else:
					return False

			elif cur_tup[1]>next_tup[1]:
				if A[cur_tup[0]][next_tup[0]]==cur_tup[1]:
					pass
				else:
					return False

		return True

		
def main():

	# A = [[0, 6, 4, 2],[6, 0, 1, 3],[4, 1, 0, 5],[2, 3, 5, 0]]
	# print brabham(A)
	# print naive_method(A)

	# A = [[0, 4.5, 4.5, 2],[4.5, 0, 1, 4.5],[4.5, 1, 0, 4.5],[2, 4.5, 4.5, 0]]
	# print brabham(A)
	# print naive_method(A)

	num_exp = 1
	max_int = 1
	for exp in range(num_exp):
		for dim in range(4,5):
			A = numpy.random.random_integers(0, max_int,size=(dim,dim))
			A_symm = (A + A.T)/2 - numpy.diag(A.diagonal())
			
			start = clock()
			x = brabham(A_symm)
			#print clock()-start

			start = clock()
			y = naive_method(A_symm)
			#print clock()-start

			if x!=y:
				print x, y


if __name__=="__main__":
	main()