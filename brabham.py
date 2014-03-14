








def brabham(A):
	n = len(A)

	print A

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

		
def main():

	A = [[0,5, 1], [5,0, 1], [1, 1, 0]]

	

	print brabham(A)









if __name__=="__main__":
	main()