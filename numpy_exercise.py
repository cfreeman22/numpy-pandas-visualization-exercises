#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

import scipy.stats as stats


# In[2]:


a = np.array([4,10,12,23,-2,-1,0,0,0,-6,3,-7])


# ### 1 - How many negative numbers are there?

# In[3]:


neg_num = len(a[a<0])

# There are 4 negative numbers

neg_num


# ### 2 -How many positive numbers are there?

# In[4]:


pos_num = len(a[a>0])
#There are 5 positive numbers
pos_num


# ### 3 - How many even positive numbers are there?
# 

# In[5]:


pos_numbers = a[a>0]

pos_even_num = pos_numbers[pos_numbers % 2 ==0]

pos_even_num

len(pos_even_num)

# There are 3 positive even numbers


# ### 4 - If you were to add 3 to each data point, how many positive numbers would there be?

# In[6]:


updated_a = a + 3

updated_a


# In[7]:


new_pos_num = updated_a[updated_a >0]

new_pos_num

len(updated_a)

# There are 12 positive numbers with updated array


# ### 5 - If you squared each number, what would the new mean and standard deviation be?

# In[8]:


# assuming we are working now with the original array
original_mean = np.mean(a)
original_mean


# In[9]:


standard_dev = np.std(a)
standard_dev


# In[10]:


a_squared = a ** 2

a_squared


# In[11]:


new_mean = np.mean(a_squared)

new_mean
#New mean will be 74.0


# In[12]:


new_stdv = np.std(a_squared)

new_stdv
# New stdv will be 144.024


# ### 6 - Center the data set

# In[13]:


data_centered = a - a.mean()

data_centered


# ### - 7 Calculate the z-score for each data point.

# In[14]:


z_score = stats.zscore(a)

z_score


# ### 8 - Copy the setup and exercise directions from More Numpy Practice 

# ### Setup 1
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# #### Use python's built in functionality/operators to determine the following:
# #### Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
# 
# #### Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
# 
# #### Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
# 
# #### Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
# 
# #### Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
# 
# #### Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
# 
# #### Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
# 
# #### Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
# 
# ##### What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# 
# 
# 

# In[15]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[16]:


#Exercise 1 - 
sum_of_a = np.sum(a)

sum_of_a


# In[17]:


#Exercise 2
min_of_a = np.min(a)

min_of_a


# In[18]:


#Exercise 3
max_of_a = np.max(a)

max_of_a


# In[19]:


#Exercise 4
mean_of_a = np.mean(a)

mean_of_a


# In[20]:


#Exercise 5
product_of_a = np.prod(a)

product_of_a


# In[21]:


#Exercise 6
squares_of_a = np.square(a)

squares_of_a


# In[22]:


#Exercise 7
odds_in_a = np.array(a)


odds_of_a = odds_in_a[odds_in_a %2 !=0]
odds_of_a


# In[23]:


#Exercise 8
evens_in_a = np.array(a)


evens_of_a = evens_in_a[evens_in_a %2 ==0]
evens_of_a


#  ### What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# ## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
# 

# In[24]:


b = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[25]:


b = np.array(b)


# In[26]:


sum_of_b =0 
for row in b:
    sum_of_b += sum(row)


# In[27]:


sum_of_b


# In[28]:


#refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  


# In[29]:


min_of_b


# In[30]:


#refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])


# In[31]:


max_of_b


# In[32]:


#refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))


# In[33]:


mean_of_b


# In[34]:


#refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number


# In[35]:


product_of_b


# In[36]:


#refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)


# In[37]:


squares_of_b


# In[38]:


#refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)


# In[39]:


odds_in_b


# In[40]:


#refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)


# In[41]:


evens_in_b


# In[42]:


# Exercise 9 - print out the shape of the array b.
b.shape


# In[43]:


# Exercise 10 - transpose the array b.
b.T


# In[ ]:




