import pandas as pd 

filename = 'Sample_data_approved.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:7].as_matrix()
y = data.iloc[:,7].as_matrix()
x2 = data.iloc[:,[1,4,5,6,10,12]].as_matrix()
x3 = data.iloc[:,[4]].as_matrix()

# filename2 = 'Sample_data_approved_2.xls'
# data2 = pd.read_excel(filename2)
# x3 = data.iloc[:,:7].as_matrix()
# y3 = data.iloc[:,7].as_matrix()


from sklearn.linear_model import LogisticRegression as LR 
# # from sklearn.stability_selection.randomized_lasso import RandomizedLogisticRegression as RLR 
# from stability_selection.randomized_lasso import RandomizedLogisticRegression as RLR
# # from sklearn.linear_model import RandomizedLogisticRegression as RLR



# rlr = RLR()
# rlr.fit(x,y)
# # rlr.get_support()
# # print sorted(zip(map(lambda x: round(x,r), rlr.scores_)),reserve=true)
# print(u'Random_select_features_finished')
# print(u'effective features: %s' % ','.join(data.columns[rlr.get_support()]))
# x = data[data.columns[rlr.get_support()]].as_matrix()

lr = LR()
lr.fit(x,y)

# x2 = data[3,5,7,8].as_matrix()
lr2 = LR()
lr2.fit(x2,y)

lr3 = LR()
lr3.fit(x3,y)
print(u'LogicRegression Finished')

print(u'Dataset1 method 1 average accurate is: %s' % lr.score(x,y))
print(u'Dataset1 method 2 average accurate is: %s' % lr2.score(x2,y))
print(u'Dataset2 method 1 average accurate is: %s' % lr3.score(x3,y))

