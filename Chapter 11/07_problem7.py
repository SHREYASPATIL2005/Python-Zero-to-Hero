class Vector:
	def __init__(self, l):
		self.l = l

	def __len__(self):
		return len(self.l)

# Test the implementation
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([7, 8, 9])  # Same dimension vector

print(len(v1))  # Output: 3
print(len(v2))  # Output: 3
print(len(v3))  # Output: 3

