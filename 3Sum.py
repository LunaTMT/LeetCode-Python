class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		res = set()

		#1. Split nums into three lists: negative numbers, positive numbers, and zeros
		def determine_signs(signs, n):
			if n > 0:
					signs[0].append(n)
			elif n < 0:
					signs[1].append(n)
			else:
					signs[2].append(n)
			return signs

		p, n, z = reduce(determine_signs, nums, [[],[],[]])


		#2. Create a separate set for negatives and positives for O(1) look-up times
		P, N = set(p), set(n)


		#3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
		#   i.e. (-3, 0, 3) = 0
		if z:
			for i in n:
				if -i in p:
					res.add((i, 0, -i))


		#3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
		if len(z) >= 3: res.add((0,0,0))

		#4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
		#   exists in the positive number set
		for i in range(len(n)):
			for j in range(i+1, len(n)):
				complement = -(n[i] + n[j])
				if complement in P:
					res.add(tuple(sorted([n[i],n[j],complement])))


		#5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
		#   exists in the negative number set

		for i in range(len(p)):
			for j in range(i + 1, len(p)):
					complement = -(p[i] + p[j])
					if complement in N:
						res.add(tuple(sorted([p[i],p[j],complement])))

		return res