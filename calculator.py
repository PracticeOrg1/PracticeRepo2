#!/usr/bin/python


def add(x,y):
  return x + y

def mult(x,y):
  return x * y

def inverse(x):
  return 1 / x

def exp(x,y):
  return x ** y

def test_add():
  assert add(5,5) == 10

def test_mult():
  assert mult(5,7) == 35
  
def test_inverse():
  assert inverse(5) == 0.2
  
def test_exp():
  assert exp(5,3) == 125
  
print("Hello, Calculator! I AM PYTHON!")
