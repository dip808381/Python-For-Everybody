import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
data = urllib.request.urlopen(url).read()
info = json.loads(data)

print('User count:', len(info))
info = info['comments']
# print(info)
count = 0
sm = 0
for num in info:
    item = num['count']
    count += 1
    sm += int(item)
print(count, sm)
