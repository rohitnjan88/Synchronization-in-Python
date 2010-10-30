import threading
import time

class Thread1(threading.Thread):
	'''a thread class'''
	v = 0
	vlock  = threading.Lock()
	def __init__(self,val):
		'''initialising the thread'''
		threading.Thread.__init__(self)
		self.param = val
		
	def run(self):
		'''body of the thread'''
		while 1:
			Thread1.vlock.acquire()
			Thread1.v += 1
			print "thread no",self.param,"val =",Thread1.v
			Thread1.vlock.release()
			time.sleep(1)
	
t1 = Thread1(1)
t2 = Thread1(2)

t1.start()
t2.start()
		
