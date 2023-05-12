import os


class Tree:
    def __init__(self, RELEASE_PATH, VERSION):
        self.DIR = fr"{RELEASE_PATH}/{VERSION}/"

    def tree(self):
        return Tree.tree_objects(self, self.DIR)

    def tree_objects(self, *args):
        tree_obj = {'name': os.path.basename(args[0])}

        if os.path.isdir(args[0]):
            tree_obj['type'] = "directory"
            tree_obj['children'] = [Tree.tree_objects(self, os.path.join(args[0], x)) for x in os.listdir(args[0])]
        else:
            tree_obj['type'] = 'file'
        
        return tree_obj