# code for running the MINMAX algorithm

## importing the system module in case we want to provide any command line arguement
import sys

# defining a class node
class NODE:
    def __init__ (self,value,typetype,level):  # class node will have type nodes value, node type (min or max), node level
        self.value = value
        self.typetype = typetype
        self.children= []
        self.level = level

    def add_children(self,children):             # adding the children in the nodes
        self.children.append(children)

    def update_value(self,value):               # updating the node value
        self.value = value


def generate_node(value,typetype,level):    # function to return the node generated
    return NODE(value,typetype,level)

 # minmax function definition
def minimax(node):
    if isLeafNode(node):   # if the node is leaf node, then take its utility values
        return node.value
    if node.typetype=="MAX":  # if the node type is MAX node, 
       MAXVALUE=-float("inf")  # iniitalising the max value to negative infinity
       for child in node.children:   
           MAXCHILDVALUE= minimax(child)  # take the minimax value of each child
           child.update_value(MAXCHILDVALUE)  # update the child value
           MAXVALUE= max(MAXCHILDVALUE,MAXVALUE)  #max value function
       return MAXVALUE  # return the max value for the max node
    if node.typetype=="MIN":  #if the node type is MIN node,
       MINVALUE=float("inf")  # iniitalising the max value to positive infinity
       for child in node.children:
           MINCHILDVALUE= minimax(child)   # get the minimax value of each child
           child.update_value(MINCHILDVALUE)  
           MINVALUE= min(MINCHILDVALUE,MINVALUE)
       return MINVALUE        
    return output  # return the minimax value of the game tree

# function to check if the node is a leaf node or not
def isLeafNode(node):
    if len(node.children)==0:
        return True
    else:
        return False
#  function to find the final solution path
def findsolutionpath(node,result,queue):
    count=0                       # initialsing the count variable to find out which node to select in the solution path among child nodes.
    if len(node.children)==0:     # check if we have reached the leaf node
       print("Solution path is: ", end = "") 
       for value in queue:         # printing the solution path
          print(value, end = ",")
       return   
    for nodes in node.children:        # traverse from root node of the tree to leaf node in order to find the solution path
        count = count+1
        if(nodes.value) == result:     # to check if the node value matches the final minmax value of the tree
           queue.append(count)
           break
    findsolutionpath(nodes,result,queue)

# a function construct tree to construct a tree out of an expression
def  CONSTRUCT_TREE(expression):
    opencount = 0                 #initilasing the variable open count which will keep count of open braces
    closedcount = 0                 # initilasing the variable closed count which will keep count of closed braces
    stack = []                     # a stack to hold the nodes of the tree being generated
    totalcount = 0
    negativeFound = 0             # a flag to indicate whether the number is negative or not
    numberstarted= 0              # a flag to indicate whether the number has ended or not
    value = ""
    for char in expression:
        if isOpenParantheses(char):  # TO check if we have open parantheses, 
             opencount = opencount+1
             stack.append(generate_node(0,MAXMIN(opencount-closedcount-1),opencount-closedcount-1)) # create a node with each open parantheses, define its level and type
        elif isClosedParantheses(char):    # to check if there is closed parantheses 
             closedcount = closedcount+1
             if(numberstarted):           # to check if the number had already started and used to create a node for the last number inside the braces
                    if(negativeFound):      # if the number is negative, generate the node will negative number
                        value = -int(value)
                        negativeFound = 0
                    nodenew = generate_node(int(value),MAXMIN(opencount-closedcount+1),opencount-closedcount+1) # creating a new node
                    parentnode=stack.pop()     # pop out the previous node in the stack
                    parentnode.add_children(nodenew) # make the new node being generated to child of the parent node
                    stack.append(parentnode)  # add the parent node in the stack itself
                    numberstarted = 0
                    value = ""
             Tobedeletednode=stack.pop()     # take the node from the stack
             if len(stack)!= 0:             # if we still have nodes in the stack, pop the node out and make this node as the parent of alread popped out node
                 parentnode = stack.pop()
                 parentnode.add_children(Tobedeletednode)
                 stack.append(parentnode)
             else:                             # if we have the last node from the stack, it will become root node and return i
                 return Tobedeletednode       
        else:
             if char != ' ':        # Used to find out the spaces in the expression
               if char !='-':       # Used to check if we have negative character in the expression
                  value = value+char     # Used to generate multiple digit number
                  numberstarted = 1  # a flag to indicate that number has started
               else:
                  negativeFound=1
             else:
                 if(numberstarted):
                    if(negativeFound):
                        value = -int(value)
                        negativeFound = 0
                    nodenew = generate_node(int(value),MAXMIN(opencount-closedcount),opencount-closedcount)
                    parentnode=stack.pop()
                    parentnode.add_children(nodenew)
                    stack.append(parentnode)
                    numberstarted = 0
                    value = ""
                    

# a function to indicate whether node is max or min
def MAXMIN(value):
    if (value%2==0):
        return "MAX"
    else:
        return "MIN"
    

# A function to find out open parantheses in expression
def isOpenParantheses(char):
     if (char=='('):
         return True
     else:
         return False
# A function to find out closed parantheses in expression
def isClosedParantheses(char):
     if (char==')'):
         return True
     else:
         return False      
    



def main ():
       #expression = "((4 (7 9 8) 8) (((3 6 4) 2 6) ((9 2 9) 4 7 (6 4 5))))"  # the given expression
       #expression= "(((1 4) (3 (5 2 8 0) 7 (5 7 1)) (8 3)) (((3 6 4) 2 (9 3 0)) ((8 1 9) 8 (3 4 ))))"
       #expression =  "(5 (((4 7 -2) 7) 6))"
       #expression = "((8 (7 9 8) 4) (((3 6 4) 2 1) ((6 2 9) 4 7 (6 4 5))))"
       expression = "(((1 (4 7)) (3 ((5 2) (2 8 9) 0 -2) 7 (5 7 1)) (8 3)) (((8 (9 3 2) 5) 2 (9 (3 2) 0)) ((3 1 9) 8 (3 4 ))))"
       print("Input expression is:")
       for value in expression:
            print(value, end="")
       print ("\n")
       rootnode=CONSTRUCT_TREE(expression)   # Construct the tree from expression
       for nodes in rootnode.children:    # printing the node values of the tree before MINMAX operation, assuming all the internal nodes to have value 0 initially
           print("value of the child nodes of the root node before MINMAX Operation = %d, level of the node= %d, type of the node = %s" % (nodes.value, nodes.level, nodes.typetype))
       print("\n")
       result = minimax(rootnode)  # getting the minmax value of the tree
       for nodes in rootnode.children:     # generating the MINMAX node values after MIN MAX operation
           print("value of the child nodes of the root node after MINMAX Operation = %d, level of the node= %d, type of the node = %s" % (nodes.value, nodes.level, nodes.typetype))
       print("\n")
       print ("MINIMAX value of the tree is %d" % result)
       queue = []
       findsolutionpath(rootnode,result,queue)  # Function call for solution path


if __name__ == '__main__':
   main()
