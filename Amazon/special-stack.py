"""
Problem Statement: Design a data-structure SpecialStack (using the STL of stack)
that supports all the stack operations like push(), pop(), isEmpty(), isFull()
and an additional operation getMin() which should return minimum element from
the SpecialStack in O(1) time using O(1) space. Your task is to complete all the
functions, using stack data-Structure.

Link:https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
"""

class SpecialStack(object):
	def __init__(self,size):
		self.stack = []
		self.size = size
		self.min = None

	def push(self, item):
		if self.is_full():
			print("Stack overflow!")
		else:
			if self.is_empty():
				self.min = item
				self.stack.append(item)
			elif item < self.min:
				# if current item is less than existing min
				# push value in encoded form such that we can
				# retrieve current min later easily.
				# push x, where x = current_item - current_min
				self.stack.append(item - self.min)
				self.min = item
			else:
				self.stack.append(item)

	def pop(self):
		if self.is_empty():
			print("Stack is empty")
		else:
			top = self.stack.pop()
			if(top < self.min):
				# removing corrent min from stack
				# retrieve next min and update the min like
				# next_min = current_min - top 
				prev_min = self.min
				self.min = self.min - top
				return prev_min
			else:
				return top

	def is_empty(self):
		return len(self.stack) == 0

	def is_full(self):
		return self.size == len(self.stack)	

	def get_min(self):
		return self.min

	def peek(self):
		if self.is_empty():
			return None
		else:
			return self.stack[-1]

def main():
	items = [18, 19, 29, 15, 16, 7, 24]
	stack = SpecialStack(len(items))
	for x in items:
		stack.push(x)

	print("Current Stack:",items)

	while(not stack.is_empty()):
		print("Current Minimum:", stack.get_min())
		x = stack.pop()
		print("Popped element:",x)

if __name__ == '__main__':
	main()