"""An abstract base class corresponding to the tree ADT
"""


from structs.linked_queue import LinkedQueue


class Tree:
    """Abstract base class representing a tree structure"""
    # nested Position class
    class Position:
        """An Abstract representing the location of a single element"""
        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            # opposite of __eq__
            return not (self == other)

    # Abstract methods that concrete subclass must support
    def root(self):
        """Return Position representing the tree's root (None if empty)"""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return Position representing the p's parent (None if p is root)"""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """Return number of children that Position p has"""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError("must be implemented by subclass")

    # concrete methods implemented in this class
    def is_root(self, p):
        """Return True if Position p represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if tree is empty"""
        return len(self) == 0

    # If p is the root, then the depth of p is 0
    # Otherwise, the depth of p is one plus the depth of the parent of p
    def depth(self, p):
        """Return the number of levels separating Position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    # If p is a leaf, then the height of p is 0
    # Otherwise, the height of p is one more than the maximum of the heights of
    # p's children
    def _height1(self, p):
        """Return the height of the tree"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """Return the height of the subtree rooted at Position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p):
        """Return the height of the subtree rooted at Position p
        If p is None, return the height of the entire tree
        """
        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        """Generate an iteration of the tree's elements"""
        for p in self.positions():
            yield p.element()

    # =============preorder and postorder traversal of a tree=================
    def preorder(self):
        """Generate a preorder iteration of positions in the tree"""
        if not self.is_empty():
            # start recursion
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p"""
        # visit p before its subtree
        yield p
        for c in self.children(p):
            # do preorder of c's subtree
            for other in self._subtree_preorder(c):
                # yielding each to our caller
                yield other

    # return the entire iteration as an object
    def positions(self):
        """Generate an iteration of the tree's positions"""
        return self.preorder()

    def postorder(self):
        """Generate a postorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p
        """
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    # =============breadth-first traversal of a tree==========================
    def breadthfirst(self):
        """Generate a breadth-firest iteration of the positions of the tree"""
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)

# ===========================binary tree ADT==================================
# A binary tree is an ordered tree with the following properties:
# 1. Every node has at most two children
# 2. Each child node is labeled as being either a left child or a right child
# 3. A left child precedes a right child in the order of children of a node

# Example: An arithmetic expression can be represented by a binary tree whose
# leaves are associated with variables or constants, and whose internal nodes
# are associated with one of the operators +, -, *, and /.
# Each node in such a tree has a value associated with it.
#   If a node is leaf, then its value is that of its variable or constant.
#   If a node is internal, then its value is defined by applying its operation
#   to the values of its children.


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure"""
    # additional abstract methods
    def left(self, p):
        """Return a Position representing p's left child
        Return None if p does not have a left child
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Return a Position representing p's right child
        Return None if p does not have a right child
        """
        raise NotImplementedError("must be implemented by subclass")

    # concrete methods implemented in this class
    def sibling(self, p):
        """Return a Position representing p's sibling (None if no sibling)"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Position representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # =============inorder traversal of a binary tree=========================
    def inorder(self):
        """Generate an inorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p
        """
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # override inherited version to make inorder the default
    def positions(self):
        return self.inorder()


# Concrete classes
class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure"""

    # Lightweight, nonpublic class for storing a node
    class _Node:
        __slot__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An Abstract representing the location of a single element"""
        def __init__(self, container, node):
            """Constructor should not be invoked by user"""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position"""
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    # LinkedBinaryTree class methods
    def _validate(self, p):
        """Return associated node, if Position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (None if no node)"""
        return self.Position(self, node) if node is not None else None

    # Constructor
    def __init__(self):
        """Create an initially empty binary tree"""
        self._root = None
        self._size = 0

    # Public accessors
    def __len__(self):
        """Return the total number of elements in the tree"""
        return self._size

    def root(self):
        """Return the root Position of the tree (None if tree is empty)"""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (None if no left child)"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (None if no right child)"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    # Nonpublic update methods
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position
        Raise ValueError if tree nonempty
        """
        if self._root is not None:
            raise ValueError("Root already exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e
        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has a left child
        """
        node = self._validate(p)
        if self._left is not None:
            raise ValueError("left child already exists")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e
        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has a right
        child
        """
        node = self._validate(p)
        if self._right is not None:
            raise ValueError("right child already exists")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at Position p with e, and return old element"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any
        Return the element that had been stored at Position p
        Raise ValueError if Position p is invalid or p has two children
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p"""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            # attach t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            # set t1 instance to empty
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            # attach t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            # set t2 instance to empty
            t2._root = None
            t2._size = 0


class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree"""
    def __init__(self, token, left=None, right=None):
        """Create an expression tree.

        In a single parameter form, token should be a leaf value(e.g., '42'),
        and the expression tree will have that value at an isolated node.

        In a three-parameter version, token should be an operator,
        and left and right should be existing ExpressionTree instances that
        become the operands for the binary operator.
        """
        super().__init__()  # LinkedBinaryTree initiallization
        if not isinstance(token, str):
            raise TypeError("Token must be a string")
        self._add_root(token)
        if left is not None:  # presumably three-parameter form
            if token not in "+-*x/":
                raise ValueError("token must be valid operator")
            self._attach(self.root(), left, right)

    def __str__(self):
        """Return string representation of the expression"""
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return "".join(pieces)

    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list"""
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append("(")
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)
            result.append(")")

    # ExpressionTree Evaluation
    def evaluate(self):
        """Return the numeric result of the expression"""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p"""
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == "+":
                return left_val + right_val
            elif op == "-":
                return left_val - right_val
            elif op == "/":
                return left_val / right_val
            else:
                return left_val * right_val
