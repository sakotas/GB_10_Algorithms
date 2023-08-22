class Color:
    BLACK: int = 0
    RED: int = 1


class Node:
    def __init__(self, value: int, color: int = Color.RED, left=None, right=None) -> None:
        self.value = value
        self.color = color
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.value=} {self.color=} {self.left=} {self.right=}'


class RedBlackTree:
    def __init__(self, root: Node = None) -> None:
        self.root = root

    def add_node(self, value: int) -> bool:
        if self.root:
            result: bool = self.__add_node(self.root, value)
            self.root = self.__rebalance(self.root)
            self.root.color = Color.BLACK
            return result
        else:
            self.root = Node(value, Color.BLACK)
            return True

    def __add_node(self, node: Node, value: int) -> bool:
        if node.value == value:
            return False
        else:
            if node.value > value:
                if node.left:
                    is_added: bool = self.__add_node(node.left, value)
                    node.left = self.__rebalance(node.left)
                    return is_added
                else:
                    node.left = Node(value)
                    return True
            else:
                if node.right:
                    is_added: bool = self.__add_node(node.right, value)
                    node.right = self.__rebalance(node.right)
                    return is_added
                else:
                    node.right = Node(value)
                    return True

    def __rebalance(self, node: Node) -> Node:
        result: Node = node
        is_balanced: bool = True
        while is_balanced:
            is_balanced = False
            if (result.right and result.right.color == Color.RED
                    and (result.left is None or result.left.color == Color.BLACK)):
                is_balanced = True
                result = self.__right_turn(result)
            if (result.left and result.left.color == Color.RED
                    and (result.left.left and result.left.left.color == Color.RED)):
                is_balanced = True
                result = self.__left_turn(result)
            if (result.left and result.left.color == Color.RED
                    and (result.right and result.right.color == Color.RED)):
                is_balanced = True
                self.__color_exchange(result)
        return result

    @staticmethod
    def __right_turn(node: Node) -> Node:
        right: Node = node.right
        between: Node = right.left
        right.left = node
        node.right = between
        right.color = node.color
        node.color = Color.RED
        return right

    @staticmethod
    def __left_turn(node: Node) -> Node:
        left: Node = node.left
        between: Node = left.right
        left.right = node
        node.left = between
        left.color = node.color
        node.color = Color.RED
        return left

    @staticmethod
    def __color_exchange(node: Node) -> None:
        node.right.color = Color.BLACK
        node.left.color = Color.BLACK
        node.color = Color.RED

    def print_tree(self) -> None:
        if self.root:
            self.__print_tree(self.root, 'root', 0)
        else:
            print('Empty Tree')

    def __print_tree(self, node: Node, node_type: str, starting_indent: int) -> None:
        color: str = '_Black' if node.color == 0 else '_Red'
        if node_type == 'root':
            print(f'root__', end='')
            print(f'{node.value}{color}')
            starting_indent += 3
        for i in range(starting_indent // 3 - 1):
            if i == 0:
                print('   ', end='')
            print(f'|  ', end='')
        if node_type == 'left':
            print(f'L__{node.value}{color}')
        if node_type == 'right':
            print(f'R__{node.value}{color}')
        if node.left or node.right:
            starting_indent += 3
            if node.left:
                self.__print_tree(node.left, 'left', starting_indent)
            if node.right:
                self.__print_tree(node.right, 'right', starting_indent)
        else:
            starting_indent -= 3