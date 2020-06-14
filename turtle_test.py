import turtle
import time

myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        time.sleep(1)
        t.right(20)
        time.sleep(1)
        tree(branchLen - 15, t)
        time.sleep(1)
        t.left(40)
        time.sleep(1)
        tree(branchLen - 10, t)
        time.sleep(1)
        t.right(20)
        time.sleep(1)
        t.backward(branchLen)


tree(80, myTurtle)

