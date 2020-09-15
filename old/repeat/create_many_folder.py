import os
for i in range(100*150):
	name = 'with_love_for_Danya_from_your_friends-{}'.format(i)
	if not os.path.exists(name):
		os.makedirs(name)
print("Ok")
