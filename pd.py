import pandas as pd

#Form a dataframe
df = pd.read_csv("Cars_Data.csv")
print(df)
print()

#Check the first n rows with df.head(n)
#Equivalent to df.iloc[0:n]
df.head(5)
print(df)
print()

#Check the last n rows with df.tail(n)
#Equivalent to df.iloc[len(df)-n:len(df)]
df.tail(5)
print(df)
print()

#Clean CSV data and update the file
df.drop_duplicates(subset= ['index','brand','body-style','wheel-base','length','engine-type','num-of-cylinders','horsepower','mileage','price'], keep = 'first')
df = df.drop('index', axis=1)
df = df.dropna() 
print(df)
print()


#Which car brand price is maximum
maxprice= max(df.price)
car = df[(df.price==maxprice)]
print (car[["brand", "price"]])
print()

#find All "Nissan" Car information
df.loc[df['brand'] == 'nissan']
print()


#Calculate the total no. of cars per firm
for brand in df['brand'].unique():
    car_count=len(df[df.brand==brand])
    print(f'{brand} has {car_count} cars')
print()


#Each brand’s Highest price car
for brand in df['brand'].unique():
    car = df.loc[df[df.brand==brand]['price'].idxmax()]
    highest_value = car.price
    print(f'{brand} has {highest_value} priced car')
print()


#The average mileage of each car brand
for brand in df['brand'].unique():
    milage = df[df.brand==brand]['mileage'].mean()
    print(f'Average milage of {brand} is {milage}')
print()

#Sorting all cars by Price
sort_car = df.sort_values('price')
print(sort_car)
print()

#Concatenating two data frames and make a key for each data frame
G_Comp = {'Firm': ['Hyundai', 'Mazda', 'jaguar', 'Porsche'], 'Price': [18752, 127850, 356982 , 56892]}
J_Comp = {'Firm': ['Porsche', 'Honda', 'Nissan', 'volkswagen'], 'Price': [41781, 25841, 83256 , 56781]}

G_df = pd.DataFrame(list(G_Comp.items()))
G_df = pd.DataFrame(G_Comp, columns = ['Firm', 'Price'])
G_df['key']='G_Comp'
print(G_df)


J_df = pd.DataFrame(list(J_Comp.items()))
J_df = pd.DataFrame(J_Comp, columns = ['Firm', 'Price'])
J_df['key']='J_Comp'
print(J_df)
print()




#Merging two data frames using the given condition
Price = {'Firm': ['Hyundai', 'Honda', 'Chevrolet', 'Porsche'], 'Price': [18752, 17995, 356982 , 56892]}
Hpower = {'Firm': ['Hyundai', 'Honda', 'Chevrolet', 'Porsche'], 'horsepower': [141, 80, 182 , 160]}

price_df = pd.DataFrame(list(Price.items()))
price_df = pd.DataFrame(Price, columns = ['Firm', 'Price'])
print(price_df)

hpower_df = pd.DataFrame(list(Hpower.items()))
hpower_df = pd.DataFrame(Hpower, columns = ['Firm', 'horsepower'])
print(hpower_df)

merged_data=pd.merge(price_df,hpower_df,on='Firm')
print(merged_data)