import json

dictionaries = []
with open("task7.txt","r") as f: # | reading from a
    data = f.read()              # | file (task7.txt)

dictionaries = data.split("\n")               # \
if (dictionaries[len(dictionaries)-1] == ""): #  } removing "\n" from data and "" at the end | (data type - string)
    dictionaries.pop()                        # /

for i in range(len(dictionaries)):                # | converting
    dictionaries[i] = json.loads(dictionaries[i]) # | to dictionary

keys = list(dictionaries[0].keys()) # | making list out of keys
print ()
print ("Description: reading dictionaries from local txt file;")
print ("1 dictionary per line, all dictionaries have the same keys;")
print ("type at any time 'KILL' to quit.")
print ()
print ("Keys found in file:", keys)
key = str(input("Give a key: "))
while (key != "KILL"):
    while (key not in keys and key != "KILL"):
        print ("keys:", keys)
        key = str(input("Give a key listed from above: "))
    if (key != "KILL"):
        temp = []
        for dict in dictionaries:
            temp.append(dict[key])
        print ()
        print ("For key '",key,"' the following values have been found:", temp)
        mintmp = temp[0]
        if (type(temp[0]) == type("")): #type str ?      # \
            maxtmp = ""                                  #  \
            popular = ""                                 #   | checking whether values within
        elif (type(temp[0]) == type(0)): #type int ?     #   | selected key are int or string
            maxtmp = 0                                   #  /
            popular = 0                                  # /
        popularcounter = 0
        for tmp in temp:                           # \
            if (tmp > maxtmp):                     #  \
                maxtmp = tmp                       #   \
            elif (tmp < mintmp):                   #    | finding biggest, smallest
                mintmp = tmp                       #    | and most popular values
            if (popularcounter < temp.count(tmp)): #   /
                popular = tmp                      #  /
                popularcounter = temp.count(tmp)   # /
        print ("biggest value:", maxtmp)
        print ("type:", str(type(maxtmp))[8:-2])
        print ()
        print ("smallest value:", mintmp)
        print ("type:", str(type(mintmp))[8:-2])
        print ()
        if (popularcounter <= 1):
            print ("most popular value: none")
        else:
            print ("most popular value:", popular)
            print ("type:", str(type(popular))[8:-2])
        print ()
        key=str(input("Give a key: "))
