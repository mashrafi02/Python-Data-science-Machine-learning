import numpy as np
import matplotlib.pyplot as plt

years = [2012 + x for x in range(9)]
incomes1 = [55,57,61,59,65,70,73,77,68]
incomes2 = [53,56,65,59,69,70,75,71,74]
incomes3 = [58,62,65,55,69,63,73,77,79]

income_ticks = list(range(50,80,2))

plt.plot(years, incomes1, label="Jannat")
plt.plot(years, incomes2, label="Arafat")
plt.plot(years, incomes3, label="Mashrafi")
plt.title("Our incomes in USD", fontsize = 20, fontname = "Serif")
plt.xlabel("Years")
plt.ylabel("Yearly income in USD")
plt.yticks(income_ticks, [f"${x}k" for x in income_ticks])
plt.grid()
plt.legend(loc="lower right", fontsize = 10)

plt.show()