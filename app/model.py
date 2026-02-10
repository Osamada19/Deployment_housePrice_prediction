
import joblib

model = joblib.load(r"linear_regression_housing.joblib") 

feature_order=['crime_rate','resid_area','air_qual','room_num','age','teachers','poor_prop','n_hos_beds','n_hot_rooms'	,'rainfall'	,'avg_dist','airport_YES','waterbody_Lake',	'waterbody_Lake and River',	'waterbody_River']
