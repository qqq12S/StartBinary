import random 
"""
Simple algorithms
BinarySearch
Sort bubble 
"""
def binarySearch(alias,seek):
    start=0
    last=len(alias)-1
    fount=False
    while start <=last and not fount:
        masher=(start+last)//2
        if alias[masher]==seek:
            fount=True
            
        if alias[masher] > seek:
            last = last - 1
        elif alias[masher] < seek:
            last =last+1
            
    return fount

def bubbleSort(alias):
    for i in range(len(alias)-1,0,-1):
        for j in range(i):
            if alias[i]<alias[j]:
                temp = alias[j]
                alias[j] = alias[j+1]
                alias[j+1]= temp
    return alias
         
def demo_input_seek():
    a=int(input('enter number for research:'))
    return a

if __name__ == "__main__":
    list_new=random.sample(range(30),6)
    print("Random list = {}".format(list_new))
    bubbleSort(list_new)
    print("Sorted list = {}".format(list_new))
    seek=demo_input_seek()
    print("number for research = {}".format(seek))
    print('Yor number is = ')
    print(binarySearch(list_new,seek))
