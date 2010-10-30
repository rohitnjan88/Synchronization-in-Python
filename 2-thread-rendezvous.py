import threading
import time

class Thread1(threading.Thread):
	'''a thread class'''
	vlock1= threading.Lock()
	vlock1.acquire();
	vlock2= threading.Lock()
	vlock2.acquire();
	def __init__(self,val):
		'''initialising the thread'''
		threading.Thread.__init__(self)
		self.param = val

	def run(self):
		'''body of the thread'''
		if self.param == 1:
			self.thread1()
		else :
			self.thread2()

	def thread1(self):
		'''body of the first thread'''
		print " a1 arrived"
		Thread1.vlock1.release()
		Thread1.vlock2.acquire()
		print "a2 arrived"

	def thread2(self):
		'''body of the second thread'''
		print " b1 arrived"
		Thread1.vlock2.release()
		Thread1.vlock1.acquire()
		print "b2 arrived"


t1 = Thread1(1)
t2 = Thread1(2)

t1.start()
t2.start()
