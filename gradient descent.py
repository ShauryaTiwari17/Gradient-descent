import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([2,4,3,1,5])

theta_0=0 #intercept
theta_1=0 #slope
n_iterations=1000
learning_rate=0.1
m=len(x)

# prediction 

for iteration in range(n_iterations):
    
    y_pred = theta_0+theta_1*x
    
    gradient_theta_0=(2/m)*np.sum(y_pred-y)
    gradient_theta_1=(2/m)*np.sum((y_pred-y)*x)
    
    theta_0-=learning_rate*gradient_theta_0
    theta_1-=learning_rate*gradient_theta_1
    
print(f"The Inercept is:{theta_0}")
print(f"The Slope is:{theta_1}")