from functools import wraps

def logit(logfile='out.log'):
	def logging_decorator(func):
		@wraps(func)
		def wrapped_function(*args, **kwargs):
			log_string = func.__name__ + " была исполнена"
			print(log_string)
			# Open logfile and write data
			with open(logfile, 'a') as opened_file:
				# Write logs to a specific file
				opened_file.write(log_string + '\n')
		return wrapped_function
	return logging_decorator

@logit()
def my_func1():
	pass

my_func1()

@logit(logfile='func2.log')
def my_func2():
	pass

my_func2()