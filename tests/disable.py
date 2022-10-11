from py_reminder import monitor

@monitor('This success should be disabled', disable=True)
def foo(a=3, b=4):
	return a + b

@monitor('This error should be disabled', disable=True)
def err_foo(a=3, b=4):
	raise Exception('This is an error')

r = foo(4, b=1)
print(r)

r = err_foo(4, b=1)
print(r)