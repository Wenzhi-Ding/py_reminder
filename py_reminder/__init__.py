from __future__ import absolute_import
from .py_reminder import *

name = "py_reminder"

__version__ = "1.0.2"

__doc__ = """
py_reminder: a simple decorator help you monitor your task progress.
====================================================================
!!! Be remeber to config your email connection first !!!

This package can send you email notification about your task 
progress.

Basically, it can tell you:

- What is the notification about? (the only thing you need to specify)
- When it is finished?
- On which machine?
- How many time it takes?
- The error and prompt message (if error happens)

Initialization
---------------
from py_reminder import config

config(address='your_email@example.com',
       password='123456',
       smtp='smtp.example.com',
       port=999,
       default_to='receiver@example.com')
---------------

Monitor Your Task
---------------
from py_reminder import monitor
import time

@monitor('Your Task Description')
def foo():
    time.sleep(10)

foo()
---------------
"""