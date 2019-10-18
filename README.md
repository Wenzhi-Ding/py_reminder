# py_reminder
This is a Python package that can send email for various purpose.

## Introduction
Often times we have some time-consuming task, and we want to leave it run alone without staring at the screen for 7\*24 hours.

This package will offer you a **simplified** experience of sending you email report with customized information.

## Installation
```bash
pip install -U py_reminder
```

## Initial configuration
**You will suggest to use a unimportant mail box to receive message**, since the password is going to store in plain text. (or if someone knows how to encrypt, please help!)

For the first time, you should specify configuration
```python
from py_reminder import config

config(address='daveting@example.com',
       passwd='123456',
       smtp='smtp.example.com',
       port=999,
       default_to='daveting@example.com')
```
If you receive a testing email, then the configuration is done. You can never include this code thereafter.

## Sample code
```python
from py_reminder import monitor

@monitor(task='do something', to='receiver@example.com', timer=True)
def foo()
  time.sleep(10)
  return 0
 
foo() 
```
"timer" indicates whether to know the execution time. Default is True.
You can ignore "to" if you send to your default receiver.

So the most simple and suggested way to use this decorator is:
```python
@monitor('do something')
def foo()
  time.sleep(10)
  return 0
 
foo() 
```
