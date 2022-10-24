#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sıralanacakarray(k):
    for i in range(1,len(k)):    #since we want to swap an item with previous one, we start from 1
        j = i                    #create i's copy (or not)
        temp = k[j]              #temp will be used for comparison with previous items, and sent to the place it belongs
        while j > 0 and temp < k[j-1]: #j>0 bcoz no point going till k[0] since there is no seat available on its left, for temp
            k[j] = k[j-1] #Move the bigger item 1 step right to make room for temp
            j=j-1 #take k[j] all the way left to the place where it has a smaller/no value to its left.
        k[j] = temp
    return k


# In[2]:


A = [4,6,8,3,2,5,7,9,0]
print(sıralanacakarray(A))


# In[ ]:


array k
   arrayın ilk elemanını al ve ikinci elemanıyla karşışaltır 
         eğer ilk eleman büyük ise ikinci elemanı üçüncü eleman ile karşışaltır.
             üçüncü büyük ise 
         eğer ikinci eleman büyükse üçüncü ile birinciyi karşıaştır.???????????????????????????
            
    


# In[ ]:





# In[4]:


#ilk elemanı min seçiyor elemanları sırayla karşılaştırıyor eğer minimimdan daha küçük bir minimim bulursa onu yeni minimum
  #olarak atıyor. 

arr = [4,3,5,2,7,0]
min = arr[0]
for i in range (len(arr)):
    if arr[i] < min:
        min = arr[i]
print(min)


# In[ ]:


Python İle Programlamaya Giriş pg145

