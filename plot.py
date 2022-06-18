import matplotlib.pyplot as plt
  
# x axis values
x = [0,0,50,83,125]
# corresponding y axis values
y = [0,0,33,66,163]


plt.plot(x, y, color='green', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='blue', markersize=8)
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('z1')
# naming the y axis
plt.ylabel('z2')
  
# giving a title to my graph
plt.title('Le front de pareto')
  
# function to show the plot
plt.show()
