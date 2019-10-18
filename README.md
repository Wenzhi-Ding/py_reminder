# py_reminder
This is a Python package that can send email for various purpose.

## Introduction
Often times we have some time-consuming task, and we want to leave it run alone without staring at the screen for 7\*24 hours.

This package will offer you a **simplified** experience of sending you email report with customized information.

## Installation
```bash
pip install py_reminder
```

## Initial configuration
You will suggest to use a unimportant mail box to receive message, since the password is going to store in plain text. (or if someone knows how to encrypt, please help!)

```python
from py_reminder import config

# For the first time, you should specify configuration
config(address='daveting@example.com',
       passwd='123456',
       smtp='smtp.example.com',
       port=999,
       default_to='daveting@example.com')
# If you receive a testing email, then the configuration is done.
# You can never include this code thereafter.
```

## Sample code
```python
from py_reminder import monitor, timer

# Use this if you also want to know the execution time.
ts = timer()

mt = monitor(task='do something', to='receiver@example.com')
# You can ignore "to" if you just send to your default email

try:
  for i in range(5):
    ts_in = timer()
    foo()
    send_email(status='p', timer=ts_in)  # 'p' stands for "progress"
  send_email(status='c', timer=ts)  # 'c' stands for "complete"
except:
  send_email(status='a', timer=ts)  # 'a' stands for "alarm"
```

## Plan
In the future, ideally, I want to change this function into a decorator.
```python
# "timer" indicates whether to count time
# The report status will reduce to only two types: "complete" or "alarm".
@monitor(to='receiver@example.com', task='do something', timer=True)
def foo()
  pass
  return 0
 
for i in range(5):
  foo() 
```
