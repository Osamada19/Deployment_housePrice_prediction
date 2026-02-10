from pydantic import BaseModel


class HouseInput(BaseModel):
    # crime_rate:float
    # resid_area : float
    # air_qual:float
    # room_num:float
    # age:float
    # teachers:float
    # poor_prop:float
    # n_hos_beds:float
    # n_hot_rooms:float
    # rainfall:float
    # avg_dist:float
    # airport_YES:float
    # waterbody_Lake:float
    # waterbody_Lake_and_River :float
    # waterbody_River:float
    
    features:list[float]
    

