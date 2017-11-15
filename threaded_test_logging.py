import logging
import threading
import time

logging.basicConfig()
logger = logging.getLogger()

def worker():
	while True:
		logger.warning("this is a long string")
		time.sleep(0.2)

def mainline():
	for i in range(3):
		t = threading.Thread(target=worker)
		t.start()

if __name__ == "__main__":
	mainline()



