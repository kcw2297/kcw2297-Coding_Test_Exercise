from collections import deque

def isSymmetric(self, root) -> bool:
    
	level = deque([root])

	while level:
		# process the entire level (root is always symmetric so no need to process it)
		for i in range(len(level)):
			node = level.popleft()

			# add the next level
			if node:
				level.append(node.left)
				level.append(node.right)

		# check if the new level is symmetric
		n = len(level)
		for i in range(n//2):
			endIndx = n-1-i
			if level[i] and level[endIndx]:
				if level[i].val != level[endIndx].val:
					return False
			elif level[i] or level[endIndx]:
				return False
	return True
    