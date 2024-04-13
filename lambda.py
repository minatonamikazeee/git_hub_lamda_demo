import json

import pandas as pd
import requests
import pandas

def lambda_handler(event,context):
    print("Event-data->",event)
    response=requests.get("https://www.google.com")
    print(response.text)

    d={'co1l':[1,2],'col2':[3,4]}
    df=pd.DataFrame(data=d)
    print(df)