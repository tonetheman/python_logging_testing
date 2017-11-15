import threading
import time

class Log:
	def log(self, *args):
		for a in args:
			print str(a),
		print

dbg = Log()

def worker():
	while True:
		dbg.log("this is a long string")
		time.sleep(0.2)

def mainline():
	for i in range(3):
		t = threading.Thread(target=worker)
		t.start()

if __name__ == "__main__":
	mainline()



