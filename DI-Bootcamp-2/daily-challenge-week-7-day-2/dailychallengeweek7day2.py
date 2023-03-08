
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Daily Challenge
# Seaborn
# Seaborn is a Python data visualization library based on Matplotlib.
# It is used to make useful statistical plots with high level commands.
# The point is that all these commands could be done with Matplotlib, but it’s
# much easier to write and understand in Seaborn.
# A video is available on the course content

# Take the following example:

# data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
# data = pd.DataFrame(data, columns=['x', 'y'])
# for col in 'xy':
#     plt.hist(data[col], normed=True, alpha=0.5)
# plt.title("Matplotlib histogram")
# plt.show()

# import seaborn as sns
# for col in 'xy':
#     sns.kdeplot(data[col], shade=True)
# plt.title("Seaborn kdeplot")
# plt.show()

# sns.distplot(data['x'])
# sns.distplot(data['y']);
# plt.title("Seaborn distplot")
# plt.show()
# plt17
# plt18
# plt19

# Your Task
# Use Seaborn functions to make more interesting plots from the Titanic data.
# An example of a Box plot of the gender distribution by age is shown:

# df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# sns.catplot( "Sex", "Age", data=df, kind="box")
# plt.show()
# plt20

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival distributions plot')
plt.show()

sns.stripplot(x='Pclass', y='Age', hue='Sex', data=df)
plt.title('Age Distribution Plot')
plt.show()

sns.boxplot(x='Pclass', y='Fare', data=df)
plt.title('Fare Distribution Plot')
plt.show()





# 