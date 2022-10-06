from py_reminder import monitor

@monitor('This is a task')
def foo(a=3, b=4):
	return a + b

@monitor('This is a problematic task')
def err_foo(a=3, b=4):
	raise Exception('This is an error')

foo(4, b=1)

err_foo(4, b=1)