import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[10,11,12,13,14]
# plt.plot(x,y)
# plt.show()

# categories=["A","B","C","D","E"]
# values=[10,12,14,16,18]
# plt.bar(categories,values,color="purple")
# plt.title("My Bar Diagram")
# plt.show()

# data=[1,2,2,3,3,3,4,4,4,5,5,5,5,5]
# plt.hist(data,bins=5,color="purple",edgecolor="black")
# plt.show()

import seaborn as sns
df=sns.load_dataset("tips")
print(df.head())

