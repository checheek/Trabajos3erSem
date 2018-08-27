import math

def hIzq (i):
	return 2*i
	
def hDer (i):
	return 2*i+1

def intercambio (A,x,y):
		tmp= A[x]
		A[x]=A[y]
		A[y]=tmp
		
def MaxHeapify (A, i, tamanoHeap):
			L=hIzq(i)
			R=hDer(i)
			if (L <= tamanoHeap and A[L]>A[i]):
				posMax=L
			else:
				posMax=i
				
			if (R <= tamanoHeap and A[R]>A[posMax]):
				posMax=R
			if (posMax != i):
				intercambio (A, i, posMax)
				MaxHeapify(A,posMax,tamanoHeap)
				
def ConstruirHeapMaxIni (A,tamanoHeap):
	for i in range (math.ceil(tamanoHeap/2) -1, 0, -1):
		MaxHeapify(A,i,tamanoHeap)
		
def OrdenacionHeapSort(A,tamanoHeap):
		ConstruirHeapMaxIni(A,tamanoHeap)
		for i in range (len (A[1:]),1,-1):
			intercambio(A,1,i)
			tamanoHeap=tamanoHeap-1
			MaxHeapify(A,1,tamanoHeap)
            
            
Lista= [0,1,2,3,5,7,17,8,20]
OrdenacionHeapSort (Lista,10 )            