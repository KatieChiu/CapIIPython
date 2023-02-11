import Array
maxSize = 10 
arr = Array.Array(maxSize) 
arr.insert(77) 
arr.insert(44)
arr.insert(5)
arr.insert(9)
arr.insert(44)
arr.insert(555)
arr.insert(12.34)
arr.insert(0)
arr.insert(2)
arr.insert(-17)
#print("Array containing", len(arr), "items")
#arr.traverse()
#print("Search for 12.34 returns", arr.search(12.34))
#print("Deleting 0 returns", arr.delete(0))
#print("Deleting 17 returns", arr.delete(17))
#print("Setting item at index 3 to 33")
#arr.set(3, 33)
#print("Array after deletions has", len(arr), "items")

                ########TAREA########
arr.traverse()
print("numero mayor es ", arr.getMaxNum())
print("Sin duplicar")
arr.removeDups()
arr.deleteMaxNum()     #solo se puede un deleteMaxNum a la vez
#arr.deleteMaxNumOrdenados()
arr.traverse()






