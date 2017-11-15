
import threading
import time

def worker():
	while True:
		print "this is a long string"
		time.sleep(0.2)

def mainline():
	for i in range(3):
		t = threading.Thread(target=worker)
		t.start()

if __name__ == "__main__":
	mainline()


