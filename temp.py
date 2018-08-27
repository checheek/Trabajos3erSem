def swap(i, j):                    
    Lista[i], Lista[j] = Lista[j], Lista[i] 
    
   
def heapify(Ult,i):   
    l=2 * i + 1  
        
    r=2 * (i + 1) 
    
    max=i   
    if l < Ult and Lista[i] < Lista[l]:   
        max = l
    print ("rama izquierda: " + str(Lista[i]))
    if r < Ult and Lista[max] < Lista[r]:   
        max = r 
    print ("rama derecha: " + str(Lista[max]))
    if max != i:   
        swap(i, max)   
        heapify(Ult, max)   

def heap_sort():     
    Ult = len(Lista)   
    start = Ult // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):   
        heapify(Ult, i)   
    for i in range(Ult-1, 0, -1):
        swap(i, 0)   
        heapify(i, 0)   
        
List = []        
Cuantos= int(input ("Cuantos valores ingresara? "))
for k in range(Cuantos): 
    print("Ingresa el valor numero " + str(k) + " de la lista ")
    tmp=int(input())
    List.insert(k,tmp)
    
    
Lista=List
#Lista = [1, 8, 12, 20, -5, 2, 3, 32, 101,54,9]
heap_sort()

print(Lista)