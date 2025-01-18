class node:
	 def __init__ (self, data): # Create a node
	 	self.data = data
	 	self.ref  = None

class linkedlist:
	def __init__(self) :
 		self.head = None

	def trav_ll (self):				# Traversal of LL
	
		if self.head is None:
			print (" LL is empty")
		else:
			n = self.head
			while n is not None:
				print(n.data,"--->", end = " ")
				n = n.ref
		
 	def add_beg(self, data):		# add node at start
 		new_node = node(data)
 		new_node.ref = self.head
 		self.head = new_node

# 	def add_end (self,data):		# add node at end
# 		new_node = node(data)
# 		if self.head is None:
# 			self.head = new_node
# 		else:	
# 			n = self.head
# 			while n.ref is not None:
# 					n = n.ref
# 			n.ref=new_node		

# 	def add_after (self,data,x):	# add after a node x = already present node
# 		n = self.head
# 		while n is not None:
# 			if n.data == x:
# 				break
# 			n=n.ref
			
# 		if n is None:
# 			print (" Node is not present in ll")
# 		else:
# 			new_node = node(data)
# 			new_node.ref = n.ref
# 			n.ref = new_node			

# 	def add_bef (self,data,x):
# 		if self.head is None:
# 			print("LL is empty")
# 			return	

# 		if self.head.data ==x:
# 			new_node = node(data)
# 			new_node.ref = self.head
# 			self.head = new_node
# 			return

# 		n = self.head
# 		while n.ref is not None:
# 			if n.ref.data == x:
# 				break	
# 			n = n.ref	

# 		if n.ref is None:
# 			print (" Node is not found")

# 		else:
# 			new_node = node(data)
# 			new_node.ref = n.ref
# 			n.ref = new_node
				

# ll1 = linkedlist()
# ll1.add_beg(10)	
# ll1.add_end(20)
# ll1.add_after(30,10)
# ll1.add_bef(40,30)
# ll1.trav_ll()							 	
