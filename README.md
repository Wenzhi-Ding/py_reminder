# py_reminder
This is a Python decorator that can send email for various purpose.

By the way, I am also planning to expand the receiving channels from email to Message, Telegram, Wechat, or even more.

<u>**If you are interested, let's work together!**</u>

## Introduction
Often we have some time-consuming script, and we want to leave it running for a while without having to check every few minutes if it has been completed.

This package will offer you a **one-line** experience (a function decorator) of sending you email report with customized information.

This is definitely an easy function, I believe many guys have written their own equivalent one. What I did is to simplify it into a decorator, so it is now even more convenient!

## Installation
```bash
pip install -U py_reminder
```

## Initial configuration
**We strongly recommend to use an unimportant mailbox to send messages**, since the password is going to be stored in plain text. We're looking for ways to work around this - you're welcome to help!

For the first time, you should specify configuration:
```python
from py_reminder import config

config(address='your_email@example.com',
       password='123456',
       smtp='smtp.example.com',
       port=999,  # currently it should be non-SSL port
       default_to='receiver@example.com')
```
You can ignore `default_to`. It will set to be the same as `address` by default.

If you receive a testing email, then the configuration is done. You don't have to include this code on following runs, but you can use it to change the parameters.

## Sample code

```python
from py_reminder import monitor

@monitor('Get Steam Data')  # this is an example
def foo():
	return 0
	
foo()
```

If you want to specify the receiver:
```python
@monitor(task='Get Steam Data', to='receiver@example.com')
```

And you will see:

<img src="https://github.com/Wenzhi-Ding/py_reminder/blob/master/assets/image/sample1.png">

For error, you will see:

<img src="https://github.com/Wenzhi-Ding/py_reminder/blob/master/assets/image/error_sample1.png">

## Email Service Provider
- GMail
    - I used a new registered account and was banned after one day.
    - Haven't tested personal account yet.
- Foxmail
    - I use my personal account and it is all good up to now (two months).
- 163
    - It works. Port should be `25`.

**Tests on other email vendors are welcome!**
