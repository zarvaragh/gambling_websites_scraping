import pandas as pd
import json
import sys
#Q2 PART1

#inserting the file manually
# df = pd.read_json('data.json').T.reset_index().rename(columns = {'index': 'fullname'})

#inserting the file with an external input argument 
df = pd.read_json((sys.argv[1])).T.reset_index().rename(columns = {'index': 'fullname'})
df.to_csv('q2-part1.csv', index=False)

df['lastname']=  df['fullname'].str.split().str[-1]
groupby_lastName_count = df.groupby(['lastname'])["lastname"].count()
groupby_lastName_age = dict(df.groupby(['lastname', 'age'])["lastname"].count())
groupby_lastName_address = dict(df.groupby(['lastname', 'address'])["lastname"].count())
groupby_lastName_occupation = dict(df.groupby(['lastname', 'occupation'])["lastname"].count())

last_name_unique = sorted(list(set(df['lastname'])))


dic = {}
for i in range(len(last_name_unique)):  
    dic.update({str(last_name_unique[i]): {'count': groupby_lastName_count[i],
                                           'age':[{key2:(groupby_lastName_age[key1, key2])} for key1, key2 in  groupby_lastName_age.keys() if (key1 in last_name_unique[i])],
                                           'address':[{key2:(groupby_lastName_address[key1, key2])} for key1, key2 in  groupby_lastName_address.keys() if (key1 in last_name_unique[i])],
                                           'occupation':[{key2:(groupby_lastName_occupation[key1, key2])} for key1, key2 in  groupby_lastName_occupation.keys() if (key1 in last_name_unique[i])]}})
print(dic)

df = pd.DataFrame(dic)
df.to_json(path_or_buf='dic_names.json')





