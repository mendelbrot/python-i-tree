# i tree

*an iterable for storing tree-like data in a memory efficient way*

i is for iterable.

this is my idea to have an iterator object that stores a large number of path-like entries that would for a tree.  it would store the tree in a very space-efficient way as a list of dictionaries.  This is a procedure I figured out by doing foobar challenge 5/1.  

The `i-tree` object would implement a `__getitem__` method, making it an iterator.  I already know how to store a tree is a list of dictionaries, the tricky part is 

1. deciding the best way input the data into the `i-tree`
2. deciding on the format of the extra information that needs to be stored in order to implement an iterator.



