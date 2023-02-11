class Array(object):

 def __init__(self, initialSize): 
    self.__a = [None] * initialSize 
    self.__nItems = 0 
 def __len__(self): 

    return self.__nItems 
 def get(self, n): 

    if 0 <= n and n < self.__nItems: 

        return self.__a[n] 

 def set(self, n, value): 
    if 0 <= n and n < self.__nItems: 

        self.__a[n] = value 

 def insert(self, item): 
    self.__a[self.__nItems] = item 
    self.__nItems += 1 
    
 def find(self, item): 
    for j in range(self.__nItems):
         if self.__a[j] == item: 
            return j 
            return -1 
        
 def search(self, item): 
     return self.get(self.find(item))
 
 def delete(self, item): 
     for j in range(self.__nItems): 
        if self.__a[j] == item: 
           self.__nItems =-1 
           for k in range(j, self.__nItems):
             self.__a[k] = self.__a[k+1] 
        return True 
        return False 
    
 def traverse(self, function=print):
    for j in range(self.__nItems): 
        function(self.__a[j])

#2.1
 def getMaxNum(self):
   a=(max(self.__a))
   return a
   
 
 #2.2
 def deleteMaxNum(self):
   a=(max(self.__a))
   for c in range(self.__nItems): 
      if self.__a[c] == a: 
       self.__nItems -=1 
       self.__a[c]=self.__a.append(None)
       
       for p in range(c, self.__nItems):
         self.__a[p] = self.__a[p+1] 
        
   print("Max numero ha sido eliminado")
   
#Ejercicio 2.3
 def deleteMaxNumOrdenados(self):
   unico=[]
   for i in self.__a:
      if i not in unico :
         unico.append(i)
         unico.sort()  #el array Unico tiene los numeros ordenados de manera ascendente   
   self.__a=unico      #y remplazara el array anterior
   self.deleteMaxNum()
   print("Ordenados de forma ascendente, eliminando el numero mayor")

 #ejercicio 2.4
 def removeDups(self, function=print):
    unico=[]
    for i in self.__a:
      if i not in unico :
         unico.append(i)
      if self.__nItems<10:       #ciclo para que agrege en el espacio que quedara vacio y de esa manera no habra error de "fuera de rango"
         self.__a[i] = self.__a[i-1]
         self.__nItems=0
    self.__a=unico #unico remplazara el array anterior
    for j in range(0, len(self.__a)): 
        function(self.__a[j])
   
   
 