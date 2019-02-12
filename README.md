# My data storage and compressing lib
 `example.py`
 
```python
from CompressedStorage import StackStorage
    
    
# | Put values to StackStorage
storage = StackStorage()
    
storage.put(14, 20)
storage.put(17, 21)
storage.put(12, 15)
storage.put(1, 10)
    
    
# | Pull all data from storage to file
with open('file.stor', 'wb') as f:
   data = storage.pullDataBytes() # it kill data from storage (see storage.getDataBytes() to save it)
    f.write(data)


# | Put data from file
with open('file.stor', 'rb') as f:
   data = f.read()

storage.putBytes(data)
    
    
# | Print storaged values from stack (LIFO organisation)
print(storage.pull(10)) # 1
print(storage.pull(15)) # 12
print(storage.pull(21)) # 17
print(storage.pull(20)) # 14
```
