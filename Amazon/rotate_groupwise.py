'''
Problem Statement : Given a linked list, write a function to
reverse every k nodes (where k is an input to the function).
If a linked list is given as 1->2->3->4->5->6->7->8->NULL
then output will be 3->2->1->6->5->4->8->7->NULL.

Link - https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/
'''

class Node(object):
	def __init__(self,val,link=None):
		self.val = val
		self.link = link

def print_ll(root):
	head = root
	while(head):
		if head.link:
			print("{} -> ".format(head.val),end='')
		else:
			print(head.val)
		head = head.link

def rotate_groupwise(root,group_order):
	if root and group_order:
		k = 1
		previous_head = None
		previous = None
		start = root
		current = root
		root = None
		while(current):
			next_link = current.link
			current.link = previous
			previous = current
			if(k == group_order or not next_link):
				if not root:
					root = current
				if previous_head:
					previous_head.link = current
				previous_head = start
				start = next_link
				previous = None
				k = 0
			current = next_link
			k += 1
	return root

def main():
	head = None
	root = Node(1)
	two = Node(2)
	root.link = two
	three = Node(3)
	two.link = three
	four = Node(4)
	three.link = four
	five = Node(5)
	four.link = five
	six = Node(6)
	five.link = six
	seven = Node(7)
	six.link = seven
	eight = Node(8)
	seven.link = eight
	head = root

	k  = int(input("Enter k: "))
	print("Before Rotation:",end=' ')
	print_ll(head)
	head = rotate_groupwise(head,k)
	print("After Rotation:",end=' ')
	print_ll(head)

if __name__ == '__main__':
	main()