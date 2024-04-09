
import pandas as pd
import math
import plotly.express as px
import datapackage

data_url = 'https://datahub.io/core/global-temp/datapackage.json'
new_data_url_prefix = 'https://r2.datahub.io/clt98lqg6000el708ja5zbtz0/master/raw/' 

# to load Data Package into storage
package = datapackage.Package(data_url)

# to load only tabular data
resources = package.resources
for resource in resources:
    print("Resource")
    desc = resource.descriptor
    for key in desc.keys():
        if (True):
          print(key, ":", desc[key])
        if (key == 'description' or key == 'name'):
          print(key, ":", desc[key])
    if resource.tabular and resource.name == "monthly":
        prefixed_data_url = new_data_url_prefix + resource.descriptor['path']
        df = pd.read_csv(prefixed_data_url)
        print(df)
        # convert to date
        print("Converting to date type...")
        df['Date'] = pd.to_datetime(df['Date'])
        print(df)
        print(df.dtypes)
    print('---------------------------------------------', "\n")
    
    
