names = list()
filename = "Sort Me.txt"
Sorted1 = open("Sorted.txt","w")
Sorted2 = open("Sorted2.txt","w")
with open(filename) as fin:#accept the file as input for the system
    for line in fin:
        if len(line.strip()) != 0 :
            names.append(line.strip()+" \n")
            
            
namesOC = list()
  
names.sort(key=len)# we can use the built in python sort for length


for element in range(0,len(names) - 1):
    for element in range(0,len(names) - 1):# Bubble sort for the alphabet order

        if len(names[element]) != len(names[element+1]):# dont let names of different lengths interact with each other
          continue
                    
        elif names[element] > names[element + 1]:# simple bubble sort swap mechanism
                hold = names[element + 1]
                names[element + 1] = names[element]
                names[element] = hold

                
count=0
for r in reversed(names):
        namesOC.append(r) 
        count+=1
Sorted1.writelines(names)
Sorted2.writelines(namesOC)
Sorted1.close()
Sorted2.close()

        

    

    