
import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures 
import numpy as np
import matplotlib
import pandas as pd




    
def calc_isf(data):

    time=[i for i in range (0,235,5)]  
    x=np.array(time).reshape((-1,1))
    y=[]
     
    #calculating bg change
    for i in range(len(data)-1):
        change=int(data[i+1][0])-int(data[i][0])
        y.append(change)
    isf=abs(sum(y))/3
    poly_features = PolynomialFeatures(degree =3, include_bias = False)

    x_poly = poly_features.fit_transform(x)
    lin_reg = LinearRegression() 
    lin_reg.fit(x_poly, y)
    score=lin_reg.score(x_poly,y)
    print(score)
    y_pred= lin_reg.predict(x_poly)

    predict(y_pred,time)

    
    return y_pred,time,isf






    
    

   
def predict(change,timelist):
    bg=int(input("Current blood glucose"))
    prediction=[]
    for val in change:
        bg=val+bg
        prediction.append(bg)
    data={'Time in minutes':timelist, 'Blood sugar in mg/dl':prediction}
    prediction = pd.DataFrame(data)
    

  
 
       

with open('day.csv') as csvfile:
    reader= csv.reader(csvfile)
    data=list(reader)
    y_pred,time,isf_val=calc_isf(data)
    plt.plot(time, y_pred,'b',label ="Day")

 
        
with open('morning.csv') as csvfile:
    reader= csv.reader(csvfile)
    data=list(reader)
    y_pred,time,isf_val=calc_isf(data)
    plt.plot(time, y_pred,'r', label ="Morning")



 
with open('night.csv') as csvfile:
    reader= csv.reader(csvfile)
    data=list(reader)
    y_pred,time,isf_val=calc_isf(data)
    plt.plot(time, y_pred,'g', label ="Night")






plt.xlabel('Time in minutes')
plt.ylabel('Change in Blood sugar in mg/dl')
plt.legend()
plt.show()


















  

