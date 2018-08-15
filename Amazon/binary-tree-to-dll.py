'''
Problem Statement: Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place.
The left and right pointers in nodes are to be used as previous and next pointers respectively
in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree.
The first node of Inorder traversal (left most node in BT) must be head node of the DLL.

Link: https://www.geeksforgeeks.org/convert-a-given-binary-tree-to-doubly-linked-list-set-4/

Example - Consider this tree
			
			   10
		     /    \
           12     15
         /   \    /
        27   30  36
       /    /  \ 
      7    21  38
                \
                25
Inorder = 7->27->12->21->30->38->25->10-36->15
'''
class Node(object):
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None
head = None

def print_dll(root,direction="left_right"):
	while(root):
		if direction == "left_right":
			if root.right:
				print(root.key,"=>",end='')
			else:
				print(root.key)

			root = root.right
		else:
			if root.left:
				print(root.key,"=>",end='')
			else:
				print(root.key)

			root = root.left

def binary_to_dll(root):
	if(root):
		global head
		binary_to_dll(root.right)
		root.right = head
		if head:
			head.left  = root
		head = root
		binary_to_dll(root.left)

def main():
	global head
	root = Node(10)
	root.right = Node(15)
	root.right.left = Node(36)
	root.left = Node(12)
	root.left.right = Node(30)
	root.left.right.right = Node(38)
	root.left.right.right.right = Node(25)
	root.left.right.left = Node(21)
	root.left.left = Node(27)
	root.left.left.left = Node(7)
	binary_to_dll(root)
	print("Left to right: ",end="")
	print_dll(head)
	while head.right:
		head = head.right
	print("Right to left: ",end="")
	print_dll(head, direction="right_left")

if __name__ == '__main__':
	main()