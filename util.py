##### Filename: util.py
##### Author: Leo Hentschker
##### Date: September 1, 2016
##### Email: leohentschker@college.harvard.edu

import copy
from collections import deque
import abc

## Problem 1

def matrix_multiply(x, y):
    """
    Takes in two matrices x and y and performs
    matrix multiplication on them, returning
    the result. This function considers the matrix
    product of two empty matrices to be the empty
    matrix
    """

    # handle the base case of receiving
    # two empty matrices
    if x == [] and y == []:
        return []

    # determine the number of rows and columns in the result matrix
    num_rows = len(x)
    num_cols = len(y[0])

    num_cross = len(x[0])

    # initialize the result matrix
    result_matrix = [[0] * num_cols for _ in xrange(num_rows)]

    # compute the values for each cell of the result
    # matrix
    for row_index in xrange(num_rows):
        for col_index in xrange(num_cols):

            # sum up the corresponding values from
            # x and y
            for multiplication_index in xrange(num_cross):

                x_value = x[row_index][multiplication_index]
                y_value = y[multiplication_index][col_index]

                result_matrix[row_index][col_index] += x_value * y_value

    return result_matrix

## Problem 2, 3

class MyDataStruct(object):
    
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """
        Set an empty deque as an attribute
        of the instantiation
        """
        self.deque = deque()

    def __len__(self):
        """
        Define the length of the struct
        to be the size of the deque associated
        with it
        """
        return len(self.deque)

    def __iter__(self):
        """
        Use the __iter__ method on the associated
        deque
        """
        return self.deque.__iter__()

    def __str__(self):

        # join together all of the elements of the deque
        # into a string separated by commas
        elements_string = ", ".join(map(str, self.__iter__()))

        # format a string that includes the name of the class
        # and the list of elements associated with the data
        # structure
        return "{collection_name}: {elements_string}" \
            .format(**{"collection_name": self.__class__.__name__,
                       "elements_string": elements_string})

    @classmethod
    def is_same_type_as_other(cls, other):
        """
        Checks to make sure that the other is
        the same class 
        """
        return isinstance(other, cls)

    def __eq__(self, other):
        """
        Determines whether or not
        the deque contained by this object
        is the same as the other
        """

        # make sure that self and other are
        # of the same type. Otherwise, a stack
        # and a queue of the same elements are considered
        # equal
        if not self.is_same_type_as_other(other):
            return False

        elif len(self) != len(other):
            # if the two deques have a different number
            # of elements, then they are different
            return False

        else:
            # otherwise, we need to check element by element
            # to make sure that they all match up
            for self_element, other_element in zip(self, other):
                if self_element != other_element:
                    return False

            return True

    def __ne__(self, other):
        """
        Define not being equal as the negation
        of being equal
        """
        return not self.__eq__(other)

    def push(self, val):
        """
        Both structs push by appending to the
        end of the data struct
        """
        return self.deque.append(val)

    @abc.abstractmethod
    def pop_from_deque(self):
        """
        Subclasses must implement how to pop
        an element from their associated deque
        """

    def pop(self):
        """
        Try to pop the element from the deque
        in the method defined by a subclass. On
        failure, return None
        """
        try:
            return self.pop_from_deque()
        except IndexError:
            return None


class MyQueue(MyDataStruct):

    def pop_from_deque(self):
        """
        FIFO
        """
        return self.deque.popleft()

class MyStack(MyDataStruct):

    def pop_from_deque(self):
        """
        LIFO
        """
        return self.deque.pop()


## Problem 4

def add_position_iter(lst, number_from=0):
    """
    Iterate through the list using a comprehension
    and return the result
    """
    return [value + number_from + value_index
            for value_index, value
            in enumerate(lst)]


def add_position_recur(lst, number_from=0):
    """
    Pop the first element off the list and
    then recursively call the function
    """
    # base case empty list returns the empty list
    if lst == []:
        return []

    else:
        initial_value = lst[0]
        return [initial_value + number_from] + \
            add_position_recur(lst[1:], number_from  + 1)


def add_position_map(lst, number_from=0):
    """
    Map over the values of the list and the
    indices at which they occur
    """
    return map(lambda (val, ind): val + ind + number_from, enumerate(lst))


## Problem 5

def remove_course(roster, student, course):
    """
    Removes the course from the list of courses
    associated with the student
    """
    roster[student].remove(course)

## Problem 6

def copy_remove_course(roster, student, course):
    new_roster = copy.deepcopy(roster)

    new_roster[student].remove(course)

    return new_roster
