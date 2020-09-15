class Logit(object):
	"""docstring for logit"""
	def __init__(self, logfile='out.log'):
		self.logfile = logfile

	def __call__(self, func):
		log_string = func.__name__ + " была исполнена"
		print(log_string)
		# Open logfile and write data
		with open(self.logfile, "a") as opened_file:
			# We write log in concretic file
			opened_file.write(log_string + '\n')
		# Send massage
		self.notify()

	def notify(self):
		# Only write log
		pass

#class Email_logit(logit):
	"""
	docstring for email_logit
	Message sending function for admin
	"""
	#def __init__(self, arg):
		#self.email = email
		#super(logit, self).__init__(*args, **kwargs)
		
	#def notify(self):
		# Sending massage in self.email
		#pass

@Logit()
def my_func1(logfile='oleg.test'):
	pass

