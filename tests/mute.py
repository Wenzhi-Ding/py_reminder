from py_reminder import monitor

@monitor('This success should be muted', mute_success=True)
def foo(a=3, b=4):
	return a + b

@monitor('This error should not be disabled', mute_success=True)
def err_foo(a=3, b=4):
	raise Exception('This is an error')

r = foo(4, b=1)
print(r)

r = err_foo(4, b=1)
print(r)