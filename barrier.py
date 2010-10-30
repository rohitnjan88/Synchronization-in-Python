import threading
import time

class Thread1(threading.Thread):
	'''a thread class'''
	vlock = threading.Lock()
	vmutex = threading.Lock()
	vlock.acquire()
	count = 0
	def __init__(self,val):
		'''initialising the thread'''
		threading.Thread.__init__(self)
		self.param = val
	

	def run(self):
		''' body of the thread'''
		Thread1.vmutex.acquire()
		print "thread",self.param,"arrived"
		Thread1.count += 1
		Thread1.vmutex.release()
	
		if Thread1.count == 10:
			time.sleep(2)
			Thread1.vlock.release()
			
		Thread1.vlock.acquire()
		Thread1.vlock.release()
		print "thread  ",self.param," eating"
		
threads = []	
for i in range (1 , 11):
	threads.append(Thread1(i))

for i in threads:
	i.start()
