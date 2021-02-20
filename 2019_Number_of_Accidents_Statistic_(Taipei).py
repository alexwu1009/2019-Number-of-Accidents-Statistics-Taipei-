import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

df = pd.read_csv('http://163.29.157.32:8080/es/dataset/2f238b4f-1b27-4085-93e9-d684ef0e2735/resource/f47c1289-9e2f-49aa-a328-37708402a9ac/download/20201223105235.csv', encoding='big5')
df['區序'] = df['區序'].apply(lambda x:''.join([i for i in x if not i.isdigit()])) 
df['性別'] = df['性別'].apply(lambda x: 'Male' if x == 1 else 'Female')
df = df.groupby(['區序', '性別'])[['死亡人數', '受傷人數']].sum().reset_index().sort_values('受傷人數')
df = df.reset_index(drop=True)
df.columns = ['District', 'Sex', 'Death', 'Injury']

df['District'] = df['District'].str.replace('南港區', 'Nangang District')
df['District'] = df['District'].str.replace('松山區', 'Songshan District')
df['District'] = df['District'].str.replace('萬華區', 'Wanhua District')
df['District'] = df['District'].str.replace('大同區', 'Datong District')
df['District'] = df['District'].str.replace('士林區', 'Shilin District')
df['District'] = df['District'].str.replace('中正區', 'Zhongzheng District')
df['District'] = df['District'].str.replace('信義區', 'Xinyi District')
df['District'] = df['District'].str.replace('文山區', 'Wenshan District')
df['District'] = df['District'].str.replace('北投區', 'Beitou District')
df['District'] = df['District'].str.replace('中山區', 'Zhongshan District')
df['District'] = df['District'].str.replace('內湖區', 'Neihu District')
df['District'] = df['District'].str.replace('大安區', 'Daan District')

df = df.sort_values(['District', 'Sex'], ascending=False)
df = df.reset_index(drop=True)

n_cols = len(df['District'])
index = np.arange(n_cols)

x = df['Death']
y = df['Injury']

plt.subplots(figsize=(60, 15))
plt.title('2019 Number of accidents (Taipei City)', fontsize=40, color='g')

plt.xlabel('District', fontsize=30, color='g')
plt.xticks(index, ('Zhongzhen\nM', 'Zhongzhen\nF', 'Zhongshan\nM', 'Zhongshan\nF', 'Xinyi\nM', 'Xinyi\nF', 'Wenshan\nM', 'Wenshan\nF',
                  'Wanhua\nM', 'Wanhua\nF', 'Songshan\nM', 'Songshan\nF', 'Shilin\nM', 'Shilin\nF', 'Neihu\nM', 'Neihu\nF', 'Nangang\nM', 'Nangang\nF', 
                  'Datong\nM', 'Datong\nF', 'Daan\nM', 'Daan\nF', 'Beitou\nM', 'Beitou\nF'), fontsize=20)

plt.ylabel('Population Statistics', fontsize=30, color='g')
plt.yticks(fontsize=40)

plt.bar(index, df['Injury'], label='Injury')
plt.bar(index, df['Death'], color='orange', label='Death')
plt.plot(index, df['Injury'], '-o', color='r')
plt.grid()
plt.legend(fontsize=48)
for xx, yy in enumerate(y):  #為了更容易觀看長條圖，使用enumerate日數字顯示在各個長條圖上方
    plt.text(xx, yy, '{:,}'.format(int(yy)), ha='center', va='bottom', fontsize=40)
for xx, yy in enumerate(x):
    plt.text(xx, yy, '{:,}'.format(int(yy)), ha='center', va='bottom', fontsize=40)

plt.show()
