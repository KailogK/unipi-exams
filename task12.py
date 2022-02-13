from urllib.request import Request, urlopen
import json

print ()
print ("Description: getting 100 latest numbers from: 'https://drand.cloudflare.com/public/latest'")
print ("Merging all numbers together (converted from hex to binary);")
print ("Showing the length of most consecutive 0's and the length of most consecutive 1's.")
print ("Before we continue choose an option: 1) show just the results | 2) show numbers with details")\

option=str(input("Option: "))
while (option != "1" and option != "2"):
    option=str(input("Please give an option between 1 and 2: "))

if (option == "2"):
    print ()
    print ("By default consecutive 0's and 1's would be marked red. \n But depending how you run the program, it could show you something such as '←[1;31m' and '←[0m'")
    print ("If you want a different way of finding 0's and 1's, type something like '|||||'. \n If you want to keep default just press enter.")
    option2=str(input("Option: "))

    if (option2 == ""):
        start = "\033[1;31m"
        end = "\x1b[0m"
    else:
        start = option2
        end = option2

print ()
print ("Getting numbers...")
print ()

numbers = ""
numbersHEX = ""
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
page = urlopen(req).read()
data = page.decode()
data = json.loads(data)
numbers += (bin(int(data["randomness"], 16))[2:]) #appending bin number
numbersHEX += data["randomness"]
counter = 1
print (counter,"", data["randomness"])

#reading and appending the rest 99 of the numbers
for round in range(int(data["round"])-1, int(data["round"])-100, -1): #range: latest - latest-100
    url = 'https://drand.cloudflare.com/public/' + str(round)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    page = urlopen(req).read()
    data = page.decode()
    data = json.loads(data)
    numbers += (bin(int(data["randomness"], 16))[2:])
    numbersHEX += data["randomness"]
    counter += 1
    print (counter, "", data["randomness"])

#counting 1's and 0's
counter = 0
count0 = 0
max0count = 0
max0start = 0
max0end = 0
count1 = 0
max1count = 0
max1start = 0
max1end = 0
for i in numbers:
    if (i == "0"):
        count1 = 0
        count0 += 1
        if (count0 > max0count):
            max0count = count0
            max0end = counter
            max0start = max0end - count0
    else:
        count0 = 0
        count1 += 1
        if (count1 > max1count):
            max1count = count1
            max1end = counter
            max1start = max1end - count1
    counter += 1

print ()
print ()
print ("===== RESULTS =====")
print ()
if (option == "2"):                                        # \
    newnumbers = ""                                        #  \
    counter = 0                                            #   \
    for i in numbers:                                      #    \
        if (counter == max1start or counter == max0start): #     \
            newnumbers += i                                #      \
            newnumbers += start                            #       } showing location of consecutive 0's and 1's if option 2 is selected
        elif (counter == max1end or counter == max0end):   #      /
            newnumbers += i                                #     /
            newnumbers += end                              #    /
        else:                                              #   /
            newnumbers += i                                #  /
        counter += 1                                       # /
    print ("all of 100 numbers in hex:", numbersHEX)
    print ()
    print ("in binary:", newnumbers)
    print ("Note: if you went with the default option for marking and didn't see any red, \n make sure to try with something such as '|||||'")
    print ()

print ("counted:", max0count, "consecutive 0's   |  ", max1count, "consecutive 1's")
print ()
x=str(input("Type anything to quit: "))
