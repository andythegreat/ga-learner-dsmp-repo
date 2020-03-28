# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
data = pd.read_csv(path)
z_critical = stats.norm.ppf(q = 0.95)  

data_sample=data.sample(n=sample_size,random_state=0)

sample_mean=data_sample['installment'].mean()
sample_std=data_sample['installment'].std()

margin_of_error=(z_critical*sample_std)/math.sqrt(sample_size)
print(margin_of_error)

confidence_interval=(round(sample_mean - margin_of_error,2),round(sample_mean + margin_of_error,2))
print(confidence_interval)    

true_mean = round(data['installment'].mean(),2)
print(true_mean)     



# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])
print(sample_size)

fig,axes=plt.subplots(3,1, figsize=(10,20))
for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        m.append(data['installment'].sample(sample_size[i]).mean())
    mean_series=pd.Series(m)  
    axes[i].hist(mean_series, normed=True)
    
plt.show()

#Code starts here



# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['int.rate'] = data['int.rate'].map(lambda x:float(x.replace('%', ''))/100)
print(data['int.rate'])

z_statistic, p_value = ztest(data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative='larger')

print('z_statistic is ' + format(z_statistic))
print('pval is ' + format(p_value ))

if (p_value <0.05):
    inference='Reject'
else:
    inference='Accept'
print(inference)    


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here

z_statistic, p_value = ztest(x1=data[data['paid.back.loan']=='No']['installment'],x2=data[data['paid.back.loan']=='Yes']['installment'])

print('z_statistic is ' + format(z_statistic))
print('pval is ' + format(p_value ))

if (p_value <0.05):
    inference='Reject'
else:
    inference='Accept'
print(inference)      
    



# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
 

yes= data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
print(yes)

no= data[data['paid.back.loan']=='No']['purpose'].value_counts()
print(yes)   
observed = pd.concat([yes.transpose(),no.transpose()], 1,keys=['Yes','No'])

#observed=pd.concat( yes.transpose(),no.transpose(),axis=1,['Yes','No'] )
print(observed)
chi2, p, dof, ex  =  chi2_contingency(observed)
print(chi2)
print(critical_value)   

if (chi2 > critical_value):
    inference='Reject'
else:
    inference='Accept'
print(inference)    
    



