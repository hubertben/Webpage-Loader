import requests
import time
import threading

viewCount = 0

def view():
    in_file = 'links.txt'
  
    links = file_grab(in_file)

    for l in links:
      l = l.split('\n')[0]
 
    threads = []

    for l in links:
      new_thread = None
      new_thread = threading.Thread(target=return_request, args=(l,))
      threads.append(new_thread)

    for t in threads:
      t.start()


    print('Active Threads:', threading.active_count())
        

def return_request(link):
  for batch in range(viewCount):
    print('Running Thread at :', link, 'on Batch #:', batch)
    r = requests.get(link)  

def read_file(path):
  with open(path, "r+") as txt_file:
    lines = txt_file.readlines()
    return lines

def file_grab(path):
  return read_file(path)


if __name__ == '__main__':
  viewCount = int(input("How many views?: "))
  view()
