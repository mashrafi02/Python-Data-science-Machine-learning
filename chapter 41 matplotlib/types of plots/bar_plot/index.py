import matplotlib.pyplot as plt


x = ["C", "C++", "C#", "Java", "Python", "Go", "Flutter"]
y = [20,45,60,30,210,50,110]


plt.bar(x,y, color="aqua", align="center", width=0.7, edgecolor="blue", lw=2)
plt.show()