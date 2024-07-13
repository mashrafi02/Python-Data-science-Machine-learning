import numpy as np
import matplotlib.pyplot as plt

years = [2012 + x for x in range(9)]
incomes = [55,57,61,59,65,70,73,77,68]

income_ticks = list(range(50,80,2))

plt.plot(years, incomes)
plt.title("Jannat's income in USD", fontsize = 20, fontname = "Serif")
plt.xlabel("Years")
plt.ylabel("Yearly income in USD")
plt.yticks(income_ticks, [f"${x}k" for x in income_ticks])
plt.grid()

plt.show()