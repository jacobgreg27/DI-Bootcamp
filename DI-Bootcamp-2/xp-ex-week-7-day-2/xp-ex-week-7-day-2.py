import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

#data
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

#drop
df.drop(['PassengerId'], axis=1, inplace=True)

#summary printing
print(df.describe())


df[['Age', 'Fare']].hist(bins=20)
plt.show()


for col in ['Survived', 'Pclass', 'Sex', 'Embarked']:
    sns.countplot(x=col, data=df)
    plt.show()


for col in ['Pclass', 'Sex', 'Embarked']:
    sns.barplot(x=col, y='Survived', data=df)
    plt.show()




df['Age'].fillna(df['Age'].median(), inplace=True)


df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)


df.drop(['Cabin'], axis=1, inplace=True)


le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])


df = pd.get_dummies(df, columns=['Embarked'])


scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])


df = df[(df['Age'] >= -3) & (df['Age'] <= 3)]
df = df[(df['Fare'] >= -3) & (df['Fare'] <= 3)]


X_train, X_test, y_train, y_test = train_test_split(df.drop(['Survived'], axis=1), df['Survived'], random_state=42)


X_train = df[df['Pclass'] != 3].drop(['Survived'], axis=1)
y_train = df[df['Pclass'] != 3]['Survived']
X_test = df[df['Pclass'] == 3].drop(['Survived'], axis=1)
y_test = df[df['Pclass'] == 3]['Survived']
