import threading
import time

class Thread1(threading.Thread):
	'''a thread class'''
	v=[]
	v.append(threading.Lock())
	v.append(threading.Lock())
	v.append(threading.Lock())
	v.append(threading.Lock())
	v.append(threading.Lock())

	def __init__(self,val):
		'''initialising the thread'''
		threading.Thread.__init__(self)
		self.param = val

	def run(self):
		''' body of the thread'''
		if self.param == 4:
			self.phil5()
		else:
			self.phil()
	
	def phil(self):
		'''body of the philosopher'''
		while 1:
			Thread1.v[ self.param ].acquire()
			Thread1.v[ ( self.param + 1 ) % 5 ].acquire()
			print "thread",self.param,"eating"
			time.sleep(2)		
			print "thread",self.param,"leaving"
			Thread1.v[ ( self.param + 1 ) % 5 ].release() 
			Thread1.v[ self.param ].release()
			time.sleep(6)		

	def phil5(self):
		'''body of the fifth philosopher'''
		while 1:
			Thread1.v[ ( self.param + 1 ) % 5 ].acquire()
			Thread1.v[ self.param ].acquire()
			print "thread",self.param,"eating"
			time.sleep(2)		
			print "thread",self.param,"leaving"
			Thread1.v[ self.param ].release()
			Thread1.v[ ( self.param + 1 ) % 5 ].release() 
			time.sleep(6)		

		
threads = []
for i in range (0 , 5):
	threads.append(Thread1(i))

for i in threads:
	i.start()
