import os
import time

pid = os.fork()
if (pid == 0):
	print(f"Parent pid =  {os.getpid()}")
	time.sleep(1000)
elif (pid > 0):
	for i in range(1,4):
		pid = os.fork()
		print(f"Child {i} pid =  {os.getpid()}")
	time.sleep(1000)
