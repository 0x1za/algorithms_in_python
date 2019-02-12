class Node:
	# The Node class takes in data and returns Node.next as None
	# By default.
	def __init__(self, data):
		self.data = data
		self.next = None

		return None

	def has_value(self, value):
		# Compare value in node.
		if self.data == value:
			return True
		else:
			return False

node = Node(12)

