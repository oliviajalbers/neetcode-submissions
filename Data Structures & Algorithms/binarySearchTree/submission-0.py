class Leaf:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        leaf = Leaf(key, val)
        if not self.root:
            self.root = leaf
            return
        else:
            current = self.root
            while current:
                if key < current.key:
                    if not current.left:
                        current.left = leaf
                        return
                    current = current.left
                elif key > current.key:
                    if not current.right:
                        current.right = leaf
                        return
                    current = current.right
                else:
                    current.val = val
                    return

    def get(self, key: int) -> int:
        if not self.root:
            return -1
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1


    def getMin(self) -> int:
        if not self.root:
            return -1
        current = self.root
        while current.left:
            current = current.left
        return current.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        current = self.root
        while current.right:
            current = current.right
        return current.val

    def remove(self, key: int) -> None:
        def remove_node(root, key):
            if not root:
                return None
            if key < root.key:
                root.left = remove_node(root.left, key)
            elif key > root.key:
                root.right = remove_node(root.right, key)
            else:
                if not root.left and not root.right:
                    return None
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left

                successor = root.right
                while successor.left:
                    successor = successor.left
                root.key = successor.key
                root.val = successor.val
                root.right = remove_node(root.right, successor.key)
            return root
        self.root = remove_node(self.root, key)
        


    def getInorderKeys(self) -> List[int]:
        my_list = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            my_list.append(root.key)
            inorder(root.right)
        inorder(self.root)
        return my_list



