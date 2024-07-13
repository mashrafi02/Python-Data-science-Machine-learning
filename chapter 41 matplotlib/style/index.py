import matplotlib.pyplot as plt
import matplotlib.style as stl


# stl.use("ggplot")
stl.use("dark_background")

votes = [5,16,7,8,12,9,14]
persons = ["A","B","C","D","E","F","G"]

plt.pie(votes, labels=None, autopct="%.2f%%")
plt.legend(labels=persons)

plt.show()