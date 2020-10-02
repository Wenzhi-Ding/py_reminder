import functools
import os
import json
import sys
from pathlib import Path
from socket import gethostname
import logging

from datetime import datetime
from timeit import default_timer as timer

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def config(address, password, smtp, port, default_to=''):
    '''
    Initial configuration. Please input your email info.
    You should enable SMTP service for your account.
    If you receive an testing email, the configuration is successful.
    ===============================================================

    Parameters
    ---------------
    address: 'your_email@example.com'
    password: '123456'
        Be cautious! It is stored in plain text temporarily.
    smtp: 'smtp.example.com'
    port: 587
        Please refer to your email service provider for 'smtp' and 'port'.
    default_to: 'receiver@example.com'
        The default receiving address.
        If you don't specify, it will be the same as 'address'.
    ---------------
    '''
    HOME_PATH = str(Path.home())
    CONFIG_PATH = HOME_PATH + '/.config'
    CONFIG = CONFIG_PATH + '/py_reminder.json'

    if '.config' not in os.listdir(HOME_PATH):
        os.system('mkdir "%s"' % CONFIG_PATH)
    with open(CONFIG, 'w') as f:
        json.dump({'ADDRESS': address, 'PASSWORD': password, 'SMTP': smtp, 'PORT': port, 'TO': default_to}, f)

    try:
        send_email(time_start=timer(), task='Testing Connection')
        print("Your configuration works!")
    except:
        print("Your configuration is not working. Please refer to help(config).")
        raise Exception


def send_email(time_start, task, args=None, kwargs=None, error='', to=''):
    HOME_PATH = str(Path.home())
    CONFIG_PATH = HOME_PATH + '/.config'
    CONFIG = CONFIG_PATH + '/py_reminder.json'

    if not os.path.isfile(CONFIG):
        print('You should use py_reminder.config() to specify your email connection info.')
        raise Exception
    with open(CONFIG) as json_data_file:
        config = json.load(json_data_file)

    s = SMTP(host=config['SMTP'], port=config['PORT'])
    s.starttls()
    s.login(config['ADDRESS'], config['PASSWORD'])
    print(s)

    msg = MIMEMultipart()
    msg['From'] = formataddr(['PyReminder', config['ADDRESS']])
    if to:
        msg['To'] = to
    else:
        msg['To'] = config['TO']

    formatted_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    time_usage = (timer() - time_start) / 60
    common = f"""Task: {task}
Time: {formatted_time}
Machine: {gethostname()}
Time Usage: {time_usage:.2f} mins
Args: {args if args else '-'}
Kwargs: {kwargs if kwargs else '-'}
Status: """
    if error:
        msg['X-Priority'] = '2'
        message = common + 'Error! Please check! \n\n%s' % (error)
        msg['Subject'] = '[PyReminder] Error for %s' % task
    else:
        message = common + 'Complete!'
        msg['Subject'] = '[PyReminder] Completion for %s' % task

    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg


def monitor(task='Your Task', to=''):
    '''
    This is a decorator to monitor the progress/status of your task. 
    Refer to sample code if you don't know how to use decorator.
    ===============================================================

    Parameters
    -----------------
    task: 'Your Task Description'
    to: 'receiver@example.com'
        By default, it is your sender address.
    ---------------

    Sample Code
    ---------------
        @monitor('One Heavy Task', 'alice@foo.com'):
        def one_heavy_task():
            time.sleep(100000)
        
        one_heavy_task()
    ---------------
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            logger = logging.Logger('catch_all')
            ts = timer()
            try:
                value = func(*args, **kwargs)
                send_email(time_start=ts, task=task, args=args, kwargs=kwargs, error='', to=to)
                return value
            except Exception as e:
                logger.error(e, exc_info=True)
                send_email(time_start=ts, task=task, args=args, kwargs=kwargs, error='%s\n%s\n%s' % sys.exc_info(), to=to)
        return wrapper_decorator
    return decorator