from urllib.request import Request, urlopen
from math import log
import json

print ()
print ("Description: getting 20 latest numbers from: 'https://drand.cloudflare.com/public/latest'")
print ("For each number (hex) we count every character and calculate the entropy;")
x=str(input("Type anything to continue: "))
print ()
print ("Getting numbers...")
print ()
numbers = ""
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
page = urlopen(req).read()
data = page.decode()
data = json.loads(data)
numbers += data["randomness"] #appending hex number
counter = 1
print (counter,"", data["randomness"])

#reading and appending the rest 19 of the numbers
for round in range(int(data["round"])-1, int(data["round"])-20, -1): #range: latest - latest-20
    url = 'https://drand.cloudflare.com/public/' + str(round)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    page = urlopen(req).read()
    data = page.decode()
    data = json.loads(data)
    numbers += data["randomness"]
    counter += 1
    print (counter, "", data["randomness"])

#print (numbers) #TESTING PURPOSES
#calculating probability and entropy for each character
percentage = 0.0
ent = 0
print ()
print ("===== RESULTS =====")
for i in range(16):                                  # \
    sum=0                                            #  \
    for number in numbers:                           #   \
        if (number==hex(i)[2:]):                     #    \
            sum+=1                                   #     | counting appereances for every
    percentage=sum/len(numbers)*100                  #     | number and calculating its
    print ()                                         #     | probability of appearing and entropy
    print ("for the char '",hex(i)[2:],"' we have:") #    /
    print ("counted in total:",sum)                  #   /
    print ("probability:",percentage,"%")            #  /
    ent += -percentage*log(percentage)               # /

print ()
print ("entropy:", ent)
print ()
x=str(input("Type anything to quit: "))
