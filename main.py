from Tree_Red_Black import RedBlackTree

if __name__ == '__main__':
    tree = RedBlackTree()
    print('print \'exit\' to exit program. Otherwise enter tree number')
    while True:
        tree.print_tree()
        try:
            user_input = input('> ')
            if user_input == 'exit':
                print('Exiting....')
                break
            node = tree.add_node(int(user_input))
        except ValueError:
            print('Incorrect')