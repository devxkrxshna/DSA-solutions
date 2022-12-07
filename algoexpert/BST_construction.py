class BST:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
        #AVERAGE: O(log(n)) time and o(1)space)
        #worst : O(N) time and 0(1) space
        
        
        
    def insert(self,value):
        currentNode=self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left=BST(value)
                    break
                else:
                    currentNode=currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right=BST(value)
                    break
                else:
                    currentNode=currentNode.right
        return self
    #testbst.insert(1).insert(5) #chaining the insert method call is the relevance of return self
    
    
               
    def search(self,value):
        currentNode=self
        while True:
            if value==currentNode.value:
                return True
            elif value<currentNode.value:
                if currentNode.left is None:
                    return False
                else:
                    currentNode=currentNode.left
            else:
                if currentNode.right is None:
                    return False
                else:
                    currentNode=currentNode.right
       
       
           
    def remove(self,value,parentNOde=None):
        currentNode=self
        while currentNode is not None:
            if value< currentNode.value:
                parentNOde=currentNode
                currentNode=currentNode.left
            elif value>currentNode.value:
                parentNOde=currentNode
                currentNode=currentNode.right 
            else:
                #two children nodes , in that case find the smallest value in the right subtree and replace it with the current value
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value,currentNode)