'''
Exercise 3:

From the below string extract, IP DATE PICS URL , and print it
Input String:
'123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
'''

string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'


# IP ----------------

ip = string.split()[0] #Since IP is the first element, we split it by space and we get the first element at index [0]
print(ip)

#DATE ---------------

#Ver. 1

#Using split
date = string.split('[')[1].split(']')[0].split(':')[0] #At the end, we split the timestamp by ":" and take the first part
print(date)

#Ver. 2

#Using partition
start = string.partition('[')[2]
end = start.partition(']')[0]
date = end.split(':')[0]
print(date)

# PICS ------------------
picsPathStart = string.split('"')[1] #We split by ", and we get the element at the first index, meaning 'GET /pics/wpaper.gif HTTP/1.0',
pics = picsPathStart.split()[1] #We split again by empty space and we get the element at the first index, the pics path
print(pics)

# URL ------------------
url = string.split('"')[3] #Since the URL is wrapped around doble quotes, we can use the same method as with the PICS, but changing the index
print(url)
