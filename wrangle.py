
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def get_zillow():

    import env
    import os
    import pandas as pd
    """
    Acquire bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, and fips 
    from the zillow database for all 'Single Family Residential' properties.
    """
    filename = 'Zillow.csv'
    
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        #read from csv
        df = pd.read_csv(filename, index_col=0) #wont make the index a new column
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
        #read from sql
        url = env.get_db_url(db = 'zillow', user=env.user, password=env.password, host=env.host)
        df = pd.read_sql(
'''
select properties_2017.bedroomcnt,
properties_2017.bathroomcnt,
properties_2017.calculatedfinishedsquarefeet,
properties_2017.taxvaluedollarcnt,
properties_2017.yearbuilt,
properties_2017.taxamount,
properties_2017.fips,
propertylandusetype.propertylandusedesc
from properties_2017
join propertylandusetype using(propertylandusetypeid)
'''
, url)

        #save to csv
        df.to_csv(filename)
        
    return df 



def prep_zillow(zillow):
    new_column_names = {
    'bedroomcnt': 'Bedroom Count',
    'bathroomcnt': 'Bathroom Count',
    'calculatedfinishedsquarefeet': 'Finished Square Feet',
    'taxvaluedollarcnt': 'Tax Value',
    'yearbuilt': 'Year Built',
    'taxamount': 'Tax Amount',
    'fips': 'FIPS',
    'propertylandusedesc':'Property Land Use',
}

# Rename the columns
    zillow.rename(columns=new_column_names, inplace=True)
    zillow = zillow.dropna()
    class_mapping = {6037: 'LA County', 6059: 'Orange County', 6111: 'Ventura County'}
    zillow['FIPS'] = zillow['FIPS'].replace(class_mapping)
    
    return zillow



def split_zillow(zillow):

# First split
    train, validate_test = train_test_split(zillow, 
                                        train_size=0.60,
                                        random_state=123,
                                        )

# Second split
    validate, test = train_test_split(validate_test,
                                  test_size=0.50,
                                  random_state=123,
                                 )
    
    return train, validate, test