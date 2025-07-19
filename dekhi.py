'''import matplotlib.pyplot as plt

students=['rahim','karim','jasim','jesmine','bobby','robi','nita']
marks=[80,90,84,70,77,98,73]

plt.plot(students,marks)
plt.title('result graph')
plt.xlabel('students')
plt.ylabel('marks')
plt.show()

plt.bar(students,marks)
plt.title('bar diagram')
plt.xlabel('students')
plt.ylabel('marks')
plt.show()'''
import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('titanic')
sns.barplot(x='who',y='fare',data=df)
plt.show()