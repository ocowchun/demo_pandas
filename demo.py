#%%
import pandas as pd
import numpy as np

#%%
## read data from json
user_df = pd.read_json('users.json')
user_df.head()

#%%
# read data from csv
quiz_df = pd.read_csv('quiz.csv')
quiz_df.head()
[1,2,3]
#%%
# find max year in quiz data
max_years = quiz_df['years'].max()
print(max_years)
#%%
# find data with max year in quiz data
# quiz_user_with_max_years = 
quiz_df['years']==max_years
quiz_df[quiz_df['years']==max_years]
#%%
# aggregate average years in quiz data
mean_years = quiz_df['years'].mean()
print(mean_years)
#%%
# agregate familiar language count
result = quiz_df["familiar language"].value_counts()
print(result)
#%%
# find user using the most popular language
popular_language = result.index[0]
quiz_user_with_popular_language = quiz_df[quiz_df['familiar language']==popular_language]
print(quiz_user_with_popular_language)

# join quiz with user using right join
#%%
quiz_with_user = pd.merge(user_df, quiz_df, how='right', left_on = 'email', right_on = 'email')
print(quiz_with_user)
# drop na user data
#%%
result = quiz_with_user.dropna()
print(result)
# find user willing to use code editor
result = result[result['will you want to use code editor']=='T']
