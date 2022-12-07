import re

with open('input_test.txt') as input:
    raw = input.read()

lines = raw.split("\n")

class Tree(object):
    def __init__(self, name='root', type='directory', children=None, size=0):
        self.name = name
        self.children = []
        if children is None:
            self.size = size
        else:
            for child in children:
                self.add_child(child)
                self.type = type
            self.size = sum([child.size for child in self.children])
    def __repr__(self):
        return 'Tree:' + self.name + ' (size:' + str(self.size) + ')'
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
        self.size = sum([child.size for child in self.children])

def line_info(line_string):
    # cd command '(?:^\$ cd )(.*)'
    # list command '^\$ ls'
    # file '(\d+)(\s)(.*)'
    # directory '(dir\s)(\w)'
    # go up command ?

    thisdict = {
        "type": type,
        "name": name,
        "size": size
        }
    return thisdict

def find_children(lines, ls_line_number):
    children = []
    # start at ls line number + 1
    # while line type is file or directory
        # if it is not already in nodes list
            # create new tree object
            # add it to nodes list
        # add it to children list
    return children

nodes = []

#for line in lines:
    # if it is a directory command
        # if it doesn't already exist in nodes list
            # create new tree object
        # go to next line
        # if it is a list command
            # call find children function

# some fiddling around
d = Tree(name='d', type='directory')
a = Tree(name='a', type='directory', children=[d])
b = Tree(name='b', type='directory')
c = Tree(name='c', type='directory')
root = Tree(name='root', type='directory', children=[a, b, c,])
e = Tree(name='e', type='file', size=7)

a.add_child(e)

print(a.children)
print(a.size)