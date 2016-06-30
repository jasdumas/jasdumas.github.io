
#from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LassoLarsCV
 
#Load the dataset
data = pd.read_csv("C:/Users/JD87417/Desktop/python work/Coursera/forest_fires.csv")

#upper-case all DataFrame column names
data.columns = map(str.upper, data.columns)

# Data Management - remove missing values
data_clean = data.dropna()

#select predictor variables and target variable as separate data sets  
predvar= data_clean[["X", "Y", "MONTHAUG", "MONTHDEC", "MONTHFEB", 
"MONTHJAN", "MONTHJUL", "MONTHJUN", "MONTHMAR", "MONTHMAY", "MONTHNOV", 
"MONTHOCT", "MONTHSEP", "DAYMON", "DAYSAT", "DAYSUN", "DAYTHU", 
"DAYTUE", "DAYWED", "FFMC", "DMC", "DC", "ISI", "TEMP", "RH", 
"WIND", "RAIN"]]

target = data_clean.AREA
 
# standardize predictors to have mean=0 and sd=1
predictors=predvar.copy()
from sklearn import preprocessing
predictors['X']=preprocessing.scale(predictors['X'].astype('float64'))
predictors['Y']=preprocessing.scale(predictors['Y'].astype('float64'))
predictors['MONTHAUG']=preprocessing.scale(predictors['MONTHAUG'].astype('float64'))
predictors['MONTHDEC']=preprocessing.scale(predictors['MONTHDEC'].astype('float64'))
predictors['MONTHFEB']=preprocessing.scale(predictors['MONTHFEB'].astype('float64'))
predictors['MONTHJAN']=preprocessing.scale(predictors['MONTHJAN'].astype('float64'))
predictors['MONTHJUL']=preprocessing.scale(predictors['MONTHJUL'].astype('float64'))
predictors['MONTHJUN']=preprocessing.scale(predictors['MONTHJUN'].astype('float64'))
predictors['MONTHMAR']=preprocessing.scale(predictors['MONTHMAR'].astype('float64'))
predictors['MONTHMAY']=preprocessing.scale(predictors['MONTHMAY'].astype('float64'))
predictors['MONTHNOV']=preprocessing.scale(predictors['MONTHNOV'].astype('float64'))
predictors['MONTHOCT']=preprocessing.scale(predictors['MONTHOCT'].astype('float64'))
predictors['MONTHSEP']=preprocessing.scale(predictors['MONTHSEP'].astype('float64'))
predictors['DAYMON']=preprocessing.scale(predictors['DAYMON'].astype('float64'))
predictors['DAYSAT']=preprocessing.scale(predictors['DAYSAT'].astype('float64'))
predictors['DAYSUN']=preprocessing.scale(predictors['DAYSUN'].astype('float64'))
predictors['DAYTHU']=preprocessing.scale(predictors['DAYTHU'].astype('float64'))
predictors['DAYTUE']=preprocessing.scale(predictors['DAYTUE'].astype('float64'))
predictors['DAYWED']=preprocessing.scale(predictors['DAYWED'].astype('float64'))
predictors['FFMC']=preprocessing.scale(predictors['FFMC'].astype('float64'))
predictors['DMC']=preprocessing.scale(predictors['DMC'].astype('float64'))
predictors['DC']=preprocessing.scale(predictors['DC'].astype('float64'))
predictors['ISI']=preprocessing.scale(predictors['ISI'].astype('float64'))
predictors['TEMP']=preprocessing.scale(predictors['TEMP'].astype('float64'))
predictors['RH']=preprocessing.scale(predictors['RH'].astype('float64'))
predictors['WIND']=preprocessing.scale(predictors['WIND'].astype('float64'))
predictors['RAIN']=preprocessing.scale(predictors['RAIN'].astype('float64'))

# split data into train and test sets
pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, target, 
                                                              test_size=.3, random_state=123)

# specify the lasso regression model
model=LassoLarsCV(cv=10, precompute=False).fit(pred_train,tar_train)

# print variable names and regression coefficients
dict(zip(predictors.columns, model.coef_))

# plot coefficient progression
m_log_alphas = -np.log10(model.alphas_)
ax = plt.gca()
plt.plot(m_log_alphas, model.coef_path_.T)
plt.axvline(-np.log10(model.alpha_), linestyle='--', color='k',
            label='alpha CV')
plt.ylabel('Regression Coefficients')
plt.xlabel('-log(alpha)')
plt.title('Regression Coefficients Progression for Lasso Paths')

# plot mean square error for each fold
m_log_alphascv = -np.log10(model.cv_alphas_)
plt.figure()
plt.plot(m_log_alphascv, model.cv_mse_path_, ':')
plt.plot(m_log_alphascv, model.cv_mse_path_.mean(axis=-1), 'k',
         label='Average across the folds', linewidth=2)
plt.axvline(-np.log10(model.alpha_), linestyle='--', color='k',
            label='alpha CV')
plt.legend()
plt.xlabel('-log(alpha)')
plt.ylabel('Mean squared error')
plt.title('Mean squared error on each fold')
         

# MSE from training and test data
from sklearn.metrics import mean_squared_error
train_error = mean_squared_error(tar_train, model.predict(pred_train))
test_error = mean_squared_error(tar_test, model.predict(pred_test))
print ('training data MSE')
print(train_error)
print ('test data MSE')
print(test_error)

# R-square from training and test data
rsquared_train=model.score(pred_train,tar_train)
rsquared_test=model.score(pred_test,tar_test)
print ('training data R-square')
print(rsquared_train)
print ('test data R-square')
print(rsquared_test)