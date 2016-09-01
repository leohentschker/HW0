import util
import types

# ### Problem 1
# 
# Write a function called `matrix_multiply` which multiplies two 2-dimensional lists of real numbers. For instance,

mm = util.matrix_multiply([[1, 2], [3, 4]], [[4, 3], [2, 1]]) 
# should evaluate to
assert(mm == [[8, 5], [20, 13]])

# ### Problem 2
# Complete the definitions of the methods `init`, `push` and `pop` in the Python classes `MyQueue` and `MyStack`, using a deque data structure in Python. The operation pop should return, not print, the appropriate object in the structure. If empty, it should return None instead of throwing an error. On the other hand, operation push does not have to return anything. An example behavior is as follows:

q = util.MyQueue()
q.push(1); q.push(2)
# should evaluate to
assert(q.pop() == 1)

s = util.MyStack()
s.push(1)
s.push(2)
assert q.pop() == 2

# ### Problem 3
# For the two classes written in Problem 2, override __eq__, __ne__, and __str__ methods. You can read about these methods in detail here:
# 
# http://docs.python.org/reference/datamodel.html#basic-customization
# 
# Simply put, the above methods do the following:
# 
# * __eq__(self, other) returns True if self and other are `equal`.
# 
# * __ne__(self, other) returns True if self and other are `not equal`.
# 
# * __str__(self) returns a string representation of self. You may decide on whatever representation you want, but ideally the method should at least print the elements.
# 
# We will call two stacks or two queues _equal_ if and only if they contain the same elements and in the same order. You may assume that only elements they contain are integers.

s1 = util.MyStack()
s2 = util.MyStack()

q1 = util.MyQueue()
q2 = util.MyQueue()

# make sure that the empty queue is equal to the empty queue
# and the empty stack is equal to the empty stack
assert q1 == q2 and s1 == s2

# make sure that popping on empty stacks and queues
# returns None
assert s1.pop() is None and q1.pop() is None

# make sure that a stack isn't equal to a queue
assert s1 != q1

# add an element to one of the stacks and one of the
# queues and make sure that __ne__ works
s1.push(1)
q1.push(1)

assert q1 != q2 and s1 != s2

# make sure that __ne__ works when the elements are different
s2.push(2)
q2.push(2)
assert q1 != q2 and s1 != s2

# make sure that __ne__ works when the elements are just in the wrong
# order
s1.push(2)
q1.push(2)

s2.push(1)
q2.push(1)
assert q1 != q2 and s1 != s2

# make sure that the string representation works
assert isinstance(str(s1), types.StringType)
assert isinstance(str(q1), types.StringType)

# ### Problem 4
# Write three functions called `add_position_iter`, `add_position_recur`, and `add_position_map`, using iteration, recursion, and the built-in map function, respectively. All the versions should take a list of numbers and return a new list containing, in order, each of the original numbers incremented by the position of that number in the list. Positions in lists are numbered starting with 0, so:

iter_ret = util.add_position_iter([7, 5, 1, 4])
recur_ret = util.add_position_recur([7, 5, 1, 4])
map_ret = util.add_position_map([7, 5, 1, 4])

assert iter_ret == recur_ret == map_ret
assert(iter_ret == [7, 6, 3, 7])

# Remember that this function should not be destructive i.e.,
a = [7, 5, 1, 4]
iter_ret = util.add_position_iter(a)
recur_ret = util.add_position_recur(a)
map_ret = util.add_position_map(a)
assert(a != [7, 6, 3, 7])
assert(a == [7, 5, 1, 4])

# Furthermore, your function should also take an optional argument number_from which, although its default value should be 0, can be used to specify a different value from which to start numbering positions, such that instead of incrementing the first element by 0, the second by 1, etc., the function will increment the first element by the value of number_from, the second element by number_from+1,etc. For example:
iter_ret = util.add_position_iter([0, 0, 3, 1], number_from=3)
recur_ret = util.add_position_recur([0, 0, 3, 1], number_from=3)
map_ret = util.add_position_map([0, 0, 3, 1], number_from=3)
assert iter_ret == recur_ret == map_ret
assert(iter_ret == [3, 4, 8, 7])


# ### Problem 5
# 
# Write a function called `remove_course` which takes in `roster`, `student`, `course` as arguments and returns a modified roster. This function, unlike ones you've just written, should be destructive, meaning that roster should be modified directly.
# 
# * `roster` will be of type dictionary in Python. It will map a string (i.e., a student name) to a set. Each set will contain strings, representing courses the corresponding student is currently taking.
# * `student` will be of type string; it will represent the name of the student.
# * `course` will also be of type string.
# 
# You can read more about set and dict below:
# 
# http://docs.python.org/tutorial/datastructures.html#sets
# http://docs.python.org/tutorial/datastructures.html#dictionaries
# 
# An example behavior is as follows:
# 

roster = {'kyu': set(['cs182']), 'david': set(['cs182'])}
util.remove_course(roster, 'kyu', 'cs182')
assert(roster == {'kyu': set([]), 'david': set(['cs182'])})


# ### Problem 6
# Now write a function called `copy_remove_course`. The specifications are the same as above except the function should now be non-destructive. An example behavior is as follows:

roster = {'kyu': set(['cs182']), 'david': set(['cs182'])}
new_roster = util.copy_remove_course(roster, 'kyu', 'cs182')
assert(roster == {'kyu': set(['cs182']), 'david': set(['cs182'])})
assert(new_roster == {'kyu': set([]), 'david': set(['cs182'])})


# Hint: _copy_ the original roster and apply remove_course from Problem 5.
# 
# You can read more about the copy module below:
# http://docs.python.org/2/library/copy.html

