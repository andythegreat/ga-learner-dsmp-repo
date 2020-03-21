# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
#basicExploration(df) 
m=df[df['fico'].astype(float)>700]
p_a=len(m)/len(df)
print(p_a)

df1=df[df['purpose'] == 'debt_consolidation']
p_b=len(df1)/len(df)
print(p_b)


g=df1[df1['fico'].astype(float)>700]
p_a_b=len(g)/len(df1)
print(p_a_b)

result = p_a_b == p_a
print(result)



# code ends here


# --------------
# code starts here
new_df=df[df['paid.back.loan'] == 'Yes']
prob_lp=len(new_df)/len(df)
print(prob_lp)


n=df[df['credit.policy'] == 'Yes']
prob_cs=len(n)/len(df)
print(prob_cs)    


n=new_df[new_df['credit.policy'] == 'Yes']
prob_pd_cs=len(n)/len(new_df)
print(prob_pd_cs)        

bayes=prob_pd_cs*prob_lp/prob_cs
print(bayes)




# code ends here


# --------------
# code starts here

df['purpose'].value_counts().plot(kind="bar")
plt.show()    

df1=df[df['paid.back.loan'] == 'No']
df1['purpose'].value_counts().plot(kind="bar")
plt.show()  

# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()  
inst_mean=df['installment'].mean()  

print('In Draw Histogram ' + 'installment')
bin=int(len(df['installment'])**(1/3)*2)
df.hist(column='installment', bins=bin, figsize=(10,10))
plt.title("Show " + format('installment'))
plt.xlabel('installment')
plt.ylabel('Frequency')  
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.show()



bin=int(len(df['log.annual.inc'])**(1/3)*2)
df.hist(column='log.annual.inc', bins=bin, figsize=(10,10))
plt.title("Show " + format('log annual income'))
plt.xlabel('log annual income')
plt.ylabel('Frequency')  
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.show()    



# code ends here


