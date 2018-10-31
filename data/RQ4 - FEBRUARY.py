
# coding: utf-8

# **[RQ4] What is the most common way of payments? Discover the way payments are executed in each borough and visualize the number of payments for any possible means. Then run the Chi-squared test to see whether the method of payment is correlated to the borough. Then, comment the results.**

# In[1]:


###month of FEBRUARY

#We imported only the columns useful to answer our Rquestion.
#NB:Payment_type represented by a numeric code signifying how the passenger paid for the trip.  
#1= Credit card; 2= Cash; 3= No charge; 4= Dispute; 5= Unknown; 6= Voided trip.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

data=pd.read_csv('/Users/Enzopc/Desktop/yellow_tripdata_2018-02.csv', usecols=['passenger_count','PULocationID', 'DOLocationID','payment_type','total_amount'])
zone=pd.read_csv('/Users/Enzopc/Desktop/taxi _zone_lookup.csv', usecols=['LocationID', 'Borough'])
datazone=pd.merge(data, zone, how='left', left_on=['PULocationID'],right_on=['LocationID'])

print("Number of rows:", datazone.shape[0])
print("Number of columns: ", datazone.shape[1])
datazone.head()


# In[2]:


# What is the most common way of payments? #
datazone['payment_type'].value_counts()


# As we can see from an initial count, it seems that the most common way of payments is by credit card
# 
# 
# 1: 5990799   2: 2446989    3: 42675    4: 11613

# In[3]:


#But now let's see more deeply: 
#Discover the way payments are executed in each borough and visualize the number of payments for any possible means.

contingency_table = pd.crosstab(datazone['payment_type'], datazone['Borough'])
contingency_table


# **Chi-squared test to see whether the method of payment is correlated to the borough.**
# 
# H0 (Null Hypothesis): There is no relationship between variable one and variable two.
# 
# H1 (Alternative Hypothesis): There is a relationship between variable 1 and variable 2.
# 
# If the p-value is significant, you can reject the null hypothesis and claim that the findings support the alternative hypothesis.
# 
# 
# Chi-square Assumptions that need to be met in order for the results of the Chi-square test to be trusted:
# 
#  -When testing the data, the cells should be frequencies or counts of cases and not percentages. It is okay to convert to percentages after testing the data
#  
#  -The levels (categories) of the variables being tested are mutually exclusive
#  
#  -Each participant contributes to only one cell within the Chi-square table
#  
#  -The groups being tested must be independent
#  
#  -The value of expected cells should be greater than 5
# 
# If all of these assumptions are met, then Chi-square is the correct test to use.

# In[4]:


from scipy import stats

stats.chi2_contingency(contingency_table)


# The first value (12698.78) is the Chi-square value, followed by the p-value ~ 0, then comes the degrees of freedom (18), and lastly it outputs the expected frequencies as an array. 
# Since all of the expected frequencies are greater than 5, the Chi-square test results can be trusted.
# We can reject the null hypothesis as the p-value is less than 0.05. 
# Thus, the results indicate that there is a correlation/some sort of relationship between payment type and borough. For sure we do know that these two variables are not independent of each other.
# 
# We could relate this result to the "industrialization" of boroughs. Focusing on Manhattan, Brooklyn, EWR and Queens we can see that the most common way of payment is with credit card. Fos Staten Island there's no big difference and in Bronx most of the people pay with cash.

# In[ ]:


###Grafico per visualizzare il numero di pagamenti per ogni mezzo###

#contingency_table = pd.crosstab(datazone['payment_type'], datazone['Borough'])
#Assigns the frequency values
#creditcard = contingency_table.iloc[0][0:6].values
#cash = contingency_table.iloc[1][0:6].values
#Plots the bar chart
#fig = plt.figure(figsize=(10, 5))
#sns.set(font_scale=1.5)
#categories = ["Bronx","Brooklyn","Manhattan","Queens","Staten Island","Unknown"]
#p1 = plt.bar(categories, creditcard, color='#d62728')
#p2 = plt.bar(categories, cash, bottom=creditcard)
#plt.legend((p2[0], p1[0]), ('Cash', 'Credit Card'))
#plt.xlabel('Borough')
#plt.ylabel('Count')
#plt.show()

