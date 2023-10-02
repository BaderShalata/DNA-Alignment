import random
class Node:
    def __init__(self,value):
        self.value = value
        self.children = []
    def addChild(self,Node):
        self.children.append(Node)
    def deleteChild(self,Node):
        self.children.remove(Node)
    def displayNode(self):
        print(self.value)
    def displayChildren(self):
        for child in self.children:
            print(child.value)
    def displayParent(self):
        print(self.value)
    def splitSeq(self):
        X = int(input("Input number of the fragments that you want: "))
        Y = int(input("Input length of the fragments that you want: "))
        random.seed()
        for i in range(X):
            split_index = random.randint(0,len(self.value) - Y)  # Here len(seq)-Y because I dont want to have split_index go out of bounds for the split(Bcz below we do split_index+Y, imagine if its the last char, split_index+Y wil be out of bounds)
            fragment = Node(self.value[split_index:split_index + Y])
            #AG, A -> G:
            parent = Node(fragment.value[0])
            for letter in fragment.value[1:]:
                print("Fragment")
                fragment.displayNode()
                letterNode = Node(letter)
                print("I am the letterNode:")
                letterNode.displayNode()
                parent.addChild(letterNode)
                print("I AM THE PARENT:")
                parent.displayNode()
                print("Parent Children:")
                parent.displayChildren()
                parent.compare()
                parent = letterNode
    # Compare the first char node child to root children and add them to their children
    def compare(self):
        for child in root.children:
            if self.value == child.value:
                child.addChild(self)
                print("HELLO I GOT ADDED TO THE TREE:")
                print(child.value + " " + self.value)
                print("AND HERE ARE MY CHILDREN:")
                for c in self.children:
                    print(c.value)
#NOW I NEED
root = Node(None)
A_Nuc = Node("A")
G_Nuc = Node("G")
C_Nuc = Node("C")
T_Nuc = Node("T")
root.addChild(A_Nuc)
root.addChild(G_Nuc)
root.addChild(C_Nuc)
root.addChild(T_Nuc)
seq = Node("AGCTAG")
seq.splitSeq()
