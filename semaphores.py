import threading
import time

class Thread1(threading.Thread):
	'''a thread class'''
	vsem = threading.Semaphore()
	vsem.__init__(5)

	def __init__(self,val):
		'''initialising the thread'''
		threading.Thread.__init__(self)
		self.param = val

	def run(self):
		''' body of the thread'''
		Thread1.vsem.acquire()
		print "thread",self.param,"eating"
		time.sleep(1)		
		Thread1.vsem.release()
		print "thread",self.param,"leaving"

		
threads = []	
for i in range (1 , 11):
	threads.append(Thread1(i))

for i in threads:
	i.start()
