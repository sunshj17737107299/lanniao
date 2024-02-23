import seaborn as sns
import pandas
import matplotlib.pyplot as plt

# plt.style.use('fivethirtyeight')
train_data = pandas.read_csv('train.tsv',sep='\t')
test_data = pandas.read_csv('dev.tsv',sep='\t')
# sns.countplot(x='label',data=train_data)
# # sns.countplot(data=train_data)
# plt.title("train_data")
# plt.show()
# sns.countplot(x='label',data=test_data)
# # sns.countplot(data=test_data)
# plt.title('valid_data')
# plt.show()


train_data['sentence_length'] = list(map(lambda x:len(x),train_data['sentence']))
# for i in train_data['sentence_length']:
#     print(i)
# sns.countplot(x='sentence_length',data=train_data)
# plt.xticks([])
# plt.show()
# sns.displot(train_data['sentence_length'])
# plt.yticks([])
# plt.show()


test_data['sentence_length'] = list(map(lambda x:len(x),test_data['sentence']))
sns.countplot(x='sentence_length',data=test_data)
plt.xticks([])
plt.show()
sns.displot(test_data['sentence_length'])
plt.yticks([])
plt.show()

# sns.stripplot(y='sentence_length',x='label',data=train_data)
# plt.show()
# sns.stripplot(y='sentence_length',x='label',data=test_data)
# plt.show()


