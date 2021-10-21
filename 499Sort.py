names = list()
filename = "Sort Me.txt"

with open(filename) as fin:#accept the file as input for the system
    for line in fin:
        if len(line.strip()) != 0 :
            names.append(line.strip())
  
names.sort(key=len)# we can use the built in python sort for length


for element in range(0,len(names) - 1):
    for element in range(0,len(names) - 1):# Bubble sort for the alphabet order

        if len(names[element]) != len(names[element+1]):# dont let names of different lengths interact with each other
          continue
                    
        elif names[element] > names[element + 1]:# simple bubble sort swap mechanism
                hold = names[element + 1]
                names[element + 1] = names[element]
                names[element] = hold

                
            
print(names)#print out the list of sorted names