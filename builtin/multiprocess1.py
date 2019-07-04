import multiprocessing
def spawn():
#  print('test!')
   while True:
       pass

if __name__ == '__main__':
  for i in range(5):
    p1 = multiprocessing.Process(target=spawn)
    p2 = multiprocessing.Process(target=spawn)
    p1.start()
    p2.start()
    #p.join()