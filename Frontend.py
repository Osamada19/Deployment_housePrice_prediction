import streamlit as st 
import pandas as pd 
import numpy as np
import requests

# st.title('House price prediction')
# st.write('start predicting with the linear Regression Model ')


features_values=[]
#to enter a ready list : 
raw=st.text_input('Enter features as a list ')



# features_name=['crime_rate','resid_area','air_qual','room_num','age','teachers','poor_prop','n_hos_beds','n_hot_rooms'	,'rainfall'	,'avg_dist','airport_YES','waterbody_Lake',	'waterbody_Lake and River',	'waterbody_River']

# for feature in features_name :
#     features_values.append(st.number_input(feature ,value=0.0))

print(features_values)


if st.button('predict') :
    features_values=[float(feature.strip()) for feature in raw.split(',')]

    inputs={'features' :features_values} 

    response= requests.post('http://localhost:8000/predict',
                            json=inputs 
    )


    if response.status_code == 200:
        st.success(f"Prediction: {response.json()['prediction']}")
    else:
        st.error("Prediction failed")
    st.write(response.json())



    # st.success(f"Prediction: {response.json()['prediction']}")