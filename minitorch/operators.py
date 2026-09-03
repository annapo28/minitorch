"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, List

#
# Implementation of a prelude of elementary functions.


def mul(x: float, y: float) -> float:
    """Multiplies two numbers"""
    return x * y


def id(x: float) -> float:
    """Returns the input unchanged"""
    return x


def add(x: float, y: float) -> float:
    """Adds two numbers"""
    return x + y


def neg(x: float) -> float:
    """Negates a number"""
    return -x


def lt(x: float, y: float) -> float:
    """Checks if one number is less than another"""
    return 1.0 if x < y else 0.0


# - eq


def eq(x: float, y: float) -> float:
    """Checks if two numbers are equal"""
    return 1.0 if x == y else 0.0


def max(x: float, y: float) -> float:
    """Returns the larger of two numbers"""
    return x if x > y else y


def is_close(x: float, y: float) -> float:
    """Checks if two numbers are close in value"""
    return abs(x - y) < 1e2


# - sigmoid
def sigmoid(x: float) -> float:
    """Calculates the sigmoid function"""
    return 1 / (1 + math.exp(-x)) if x >= 0 else math.exp(x) / (1 + math.exp(x))


# - relu
def relu(x: float) -> float:
    """Applies the ReLU activation function"""
    return x if x > 0 else 0


def log(x: float) -> float:
    """Calculates the natural logarithm"""
    return math.log(x)


# - exp
def exp(x: float) -> float:
    """Calculates the exponential function"""
    return math.exp(x)


# - log_back
def log_back(x: float, y: float) -> float:
    """Calculates the reciprocal"""
    return y / x


# - inv
def inv(x: float) -> float:
    """Computes the derivative of log times a second arg"""
    return 1 / x


# - inv_back
def inv_back(x: float, y: float) -> float:
    """Computes the derivative of reciprocal times a second arg"""
    return -y / (x * x)


# - relu_back
def relu_back(x: float, y: float) -> float:
    """Computes the derivative of ReLU times a second arg"""
    return y if x > 0 else 0


#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# ## Task 0.3

# Small practice library of elementary higher-order functions.


# Implement the following core functions
# - map
def map(func: Callable[[float], float], lst: Iterable[float]) -> List[float]:
    """Higher-order function that applies a given function to each element of an iterable"""
    return [func(x) for x in lst]


# - zipWith
def zipWith(
    func: Callable[[float, float], float], lst1: Iterable[float], lst2: Iterable[float]
) -> List[float]:
    """Higher-order function that combines elements from two iterables using a given function"""
    return [func(x, y) for x, y in zip(lst1, lst2)]


# - reduce
def reduce(
    func: Callable[[float, float], float], lst: Iterable[float], start: float = 0.0
) -> float:
    """Higher-order function that reduces an iterable to a single value using a given function"""
    ans = start
    for x in lst:
        ans = func(ans, x)
    return ans


# Use these to implement
# - negList : negate a list
def negList(lst: Iterable[float]) -> List[float]:
    """Negate all elements in a list using map"""
    return map(neg, lst)


# - addLists : add two lists together
def addLists(lst1: List[float], lst2: List[float]) -> List[float]:
    """Add corresponding elements from two lists using zipWith"""
    return zipWith(add, lst1, lst2)


# - sum: sum lists
def sum(lst: List[float]) -> float:
    """Sum all elements in a list using reduce"""
    return reduce(add, lst, 0)


# - prod: take the product of lists
def prod(lst: List[float]) -> float:
    """Calculate the product of all elements in a list using reduce"""
    return reduce(mul, lst, 1)
