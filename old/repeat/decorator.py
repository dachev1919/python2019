from functools import wraps
def decorator_name(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		if not can_run:
			return 'Функция не будет исполнена'
		return f(*args, **kwargs)
	return decorated

@decorator_name
def func():
	return 'Функция исполняется'

can_run = True
print(func())