import pandas as pd
import numpy as np
data={
    'Name': ['Alice', 'Bob', 'Charlie','John','Sam'],
    'Age' : [21,32,24,23,34],
    'department':['IT','HR','finance','IT','finance'],
    'Salary':[20000,31000,45000,21000,32000]
}
#creating 1D array
a=pd.Series((1,2,3))
print("1D array using pd:",a)
#creating table
df=pd.DataFrame(data)
print("Original DataFrame:\n",df)
#load a csv file into pandas dataframe
d=pd.read_csv('example1.csv')
print("csv data:\n",d)
#extracting rows using head and tail
print("Frist 2 rows:\n",df.head(2))
print("Last 2 rows:\n",df.tail(2))
#shape of dataframe
print("Shape of dataframe:",df.shape)
#summary of dataframe
print(df.info())
#describe numerical columns
print("Descriptive of numerical columns statistics:\n",df.describe())
#print all the coloumn names
print("Column names:",df.columns)
#columns in list
print("columns are in list",df.columns.tolist())
# get index of dataframe
print("Index of dataframe:",df.index)
#show all the data types of columns
print("Data types of columns:\n",df.dtypes)
#Accesing a specific column
print("Accessing specific column 'Name':\n",df['Name'])
#Accesing multiple columns
print("Accessing multiple columns 'Name' and 'Age':\n",df[['Name', 'Age']])
#Accessing rows by index
print("Accesing row by index:\n",df.iloc[2])
#Aceessing roes by index range
print("Accessing rows by indexing range:\n",df.iloc[1:3])
#accesing rows by using label
print("Accessing rows by label:\n",df.loc[0])
#boolean filtering
print("all the names with salary greater than 25000:\n",df[df['Salary']>25000])
#sql query
print("Using sql:",df.query('Salary>25000'))
df['DA']=df['Salary']*0.2
print("modified dataframe after adding new column 'DA':\n",df)
#dropping a column
df.drop('Age',axis=1,inplace=True)
print("DataFrame after dropping 'Age' column:\n",df)
#dropping a row with index
df.drop(0, axis=0, inplace=True)
print("Dataframe after dropping row:\n",df)
#renaming the columns
df.rename(columns={'Name':'Emp name'},inplace=True)
print("Dataframe after renaming a coloumns\n",df)
#set a value to null
df.iloc[1, 2] = None
print("Dataframe after nulling values:\n",df)
#fill all the null values with a constant value
df.fillna(0, inplace=True)
print("Dataframe after filling null values with 'NA':\n",df)

#drop null values
df.dropna(inplace=True)
print("Dataframe after dropping null values:\n",df)
#sert the datatype of a column
df.astype({'Salary': 'int64'})
print("Dataframe after setting datatype of 'Salary' column:\n",df)
#sort the dataframe by a column
df.sort_values(by='Salary',inplace=True)
print("Dataframe after sorting by 'Salary':\n",df)
#sort by index
df.sort_index(inplace=True)
print("Dataframe after sorting by index:\n",df)
#rank of the dataframe
print("Rank of the dataframe:",df.rank())
#sum of the values in the dataframe
print("Total salary:",df['Salary'].sum())
#average salary of the employees
print("Average salary of the employees:",df['Salary'].mean())
#maximum salary of the employees
print("Maximum salary of the employees:",df['Salary'].max())
#minimum salary of the employees
print("Minimum salary of the employees:",df['Salary'].min())
#median salary of the employees
print("Median salary of the employees:",df['Salary'].median())
#standard deviation of the salary
print("Standard deviation of the salary:",df['Salary'].std())
#variance of the salary
print("Variance of the salary:",df['Salary'].var())
#count of the values in the dataframe
print("Count of the values in the dataframe:\n",df.count())
#unique values in a column
print("Unique values in 'department' column:\n",df['department'].unique())
#count of unique values in a column
print("Count of unique values in 'department' column:\n",df['department'].value_counts())
#correlation between columns
print("Correlation between columns:\n",df[['Salary','DA']].corr())
#grouping the data by a column
grouped_data = df.groupby('department')['Salary']
print("Grouped data by 'department':\n", grouped_data.mean())
#multiple aggregation group
grouped_data = df.groupby('department').agg({
    'Salary': ['mean', 'sum', 'max'],})
print("multiple aggregation:\n",grouped_data)
depart={
    'department': ['IT', 'HR', 'finance'],
    'location': ['New York', 'London', 'Tokyo']
}
#converting dictionary to dataframe
depart_df = pd.DataFrame(depart)
print("Department DataFrame:\n", depart_df)
#merging two dataframes
merged_df = pd.merge(df, depart_df)
print("Merged DataFrame:\n", merged_df)
#concatenating two dataframes
concat_df = pd.concat([df, depart_df])
print("Concatenated DataFrame:\n", concat_df)
#joing by index
joined_df = df.join(depart_df.set_index('department'), on='department', how='left')
print("Joined DataFrame:\n", joined_df)
df['joined_date'] = ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01']
print("DataFrame with joined date:\n", df)
#converting string to datetime
df['joined_date'] = pd.to_datetime(df['joined_date'])
print("DataFrame after converting 'joined_date' to datetime:\n", df)
#extracting year from datetime
df['joined_year'] = df['joined_date'].dt.year
print("DataFrame after extracting year from 'joined_date':\n", df)
#extracting month from datetime
df['joined_month'] = df['joined_date'].dt.month
print("DataFrame after extracting month from 'joined_date':\n", df)
#extracting day from datetime
df['joined_day'] = df['joined_date'].dt.day
print("DataFrame after extracting day from 'joined_date':\n", df)
df['Emp name']=df['Emp name'].str.upper()
print("DataFrame after converting 'Emp name' to uppercase:\n", df)
#string matching
df['contains_IT'] = df['department'].str.contains('IT')
print("DataFrame after checking if 'department' contains 'IT':\n", df)
#replace a string the values in a column
df['department'] = df['department'].str.replace('finance', 'Finance')
print("DataFrame after replacing 'finance' with 'Finance' in 'department':\n", df)
#split a string in a column
df['Name_split'] = df['Emp name'].str.split(' ')
print("DataFrame after splitting 'Emp name' into 'Name_split':\n", df)
#create pivot table with names and salaries
pivot_table = df.pivot_table(index='Emp name', values='Salary', aggfunc='sum')
print("Pivot table with names and salaries:\n", pivot_table)
#aggregate data using pivot table
aggregated_pivot=df.pivot_table(index='department', values='Salary', aggfunc=['mean', 'sum'])
print("Aggregate data using pivot table:\n", aggregated_pivot)
#unpivot the pivot table
unpivoted_df = aggregated_pivot.reset_index()
print("Unpivoted DataFrame:\n", unpivoted_df)
#melting the pivot table
melted_df = pd.melt(df, id_vars=['Emp name'], value_vars=['Salary', 'DA'])
print("Melted DataFrame:\n", melted_df)
#reshape indedx and colums
reshaped_df = df.set_index(['Emp name', 'department']).unstack()
print("Reshaped DataFrame with index and columns:\n", reshaped_df)
