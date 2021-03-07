https://docs.python.org/3/reference/datamodel.html#object.__getitem__

https://docs.python.org/3/glossary.html search iterable

https://docs.python.org/3/reference/datamodel.html#object.__iter__

### Data formats that could be passed in...

Data could be passed in all at once or incrementally

#### all at once:

* another itree object
* an itree array of data from an itree object
* a list of paths
* a list of incremental inputs (lists of tuples):
```
[
	[(char, prev_node, node), ...]
]

prev_node = the previous node that this node follows from
node = the current node being considered
char  = a character specifying how this should be processed
for char:
'c' = continue: this node continues a path
'p' = prune: remove all paths that lead up to this node
'n' = end: mark this node as the end of a path
if char is 'p' then prev_node is not required
```

I'm thinking about what to call a list of incremental inputs.  They are all at the same level, same distance from a root, a full level.  Radius is appropriate.  Actually, the circumference is the set of points equally distant from the center, the radius is the line from the center to the circumference.  So maybe, by analogy, a path is a radius, a incremental inputs list is a circumference.  perhaps they can have the names `rad` and `circ` ?  `rad` and `next_circ`?

#### incrementally

* a `rad`
* the next `circ`

Also, should one be able to put in or delete the rad at a specific index?  I'm thinking probably not for put in: the object should have complete control over what index the new items go in, mainly because duplicate entries aren't useful/shouldn't be accommodated.    For remove, YES.  There should be the ability to remove items by value or by index.

