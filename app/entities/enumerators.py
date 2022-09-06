from enum import Enum,Flag, auto
import numpy as np
import pandas as pd

class EnumBase(Flag): 
    @classmethod
    def random_by_dist(cls, proba:list):
        # weight a selection so if need to randomly select can do so
        return np.random.choice(np.array(list(cls)), p = proba)

    @classmethod
    def clean_str(cls,selection):
        # strips underscores based on numeric enum value to return key name 
        return cls(selection).name.replace("_","")

class BinaryBase(EnumBase): 
    """ 
    use for : 
    - slow_ship_state 
    - wismo_complaint
    - site down
    - SaleAccept
    - CodeException
    - rma
    - exchange offered
    - exchange accepted
    - gift
    - refund

    """
    yes = 1
    no = 0

class ContactType(EnumBase): 
    Defect = 1
    Promo = 2 
    Return = 3
    Sales_Order = 4
    WISMO = 5

class ProductFamily(EnumBase):
    uncategorized = 1
    clothing = 2
    pack = 3 
    sleeping_bag = 4
    tent = 5

class Product(EnumBase):
    Charlatan_sleeping_bag = (2,4)
    Hoax_Max_sleeping_bag = (3,4)
    Fiction_sleeping_bag = (5,4)

    CudaFooledMe_backpack = (7,3)
    Faux_backpack = (11,3)
    Illusion_camp_bag = (13,3)

    Fiction_jacket = (17,2)
    Sham_sweatshirt = (19,2)
    UltraSham_heavy_jacket = (23,2)
    Heavy_Deception_jacket = (29,2)
    Mountbank_vest = (31,2)

    Fiction_tent = (37,5)
    Illusion_tent = (41,5)
    Mirage_tent = (43,5)
    NeverThere_tent = (47,5)
    Pretender_Canvas_tent = (53,5)

    Likely_Story_camp_chair = (59,1)
    Pretender_solar_camp_shower = (61,1)
    Unreal_kettle_mess_kit = (67,1)

    @classmethod
    def family(cls,product): 
        return ProductFamily(product.value[1]).name # return

class SiteDownSentiment(EnumBase): 
    Negative = 1
    Neutral = 2
    Positive = 3

class Carrier(EnumBase): 
    FedEx = 1 
    UPS = 2
    USPS = 3

class State(EnumBase):
    Alabama = 1
    Alaska = 2
    Arizona = 3
    Arkansas = 4
    California = 5
    Colorado = 6
    Connecticut = 7
    Delaware = 8
    District_of_Columbia = 9
    Florida = 10
    Georgia = 11
    Hawaii = 12
    Idaho = 13
    Illinois = 14
    Indiana = 15
    Iowa = 16
    Kansas = 17
    Kentucky = 18
    Louisiana = 19
    Maine = 20
    Maryland = 21
    Massachusetts = 22
    Michigan = 23
    Minnesota = 24
    Mississippi = 25
    Missouri = 26
    Montana = 27
    Nebraska = 28
    Nevada = 29
    New_Hampshire = 30
    New_Jersey = 31
    New_Mexico = 32
    New_York = 33
    North_Carolina = 34
    North_Dakota = 35
    Ohio = 36
    Oklahoma = 37
    Oregon = 38
    Pennsylvania = 39
    Rhode_Island = 40
    South_Carolina = 41
    South_Dakota = 42
    Tennessee = 43
    Texas = 44
    Utah = 45
    Vermont = 46
    Virginia = 47
    Washington = 48
    West_Virginia = 49
    Wisconsin = 50
    Wyoming = 51

class PromoFailReason(EnumBase): 
    exclusion = 1
    expiration = 2

class ReturnReason(EnumBase):
    color = 1 
    quality = 2
    size = 3
    style = 4

class SurveyScore(EnumBase):
    one =1 
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9 
    ten = 10

class whatever:
    # again cuz lazy create any enum from dict with class methods 
    # since enums are immudtable this was easier for dynamic creations 
    def __init__(self, **kwargs):
        for (key,value) in kwargs.items():
            self.__dict__[key] = value
    
    def random_by_dist(cls, proba:list):
        # weight a selection so if need to randomly select can do so
        return np.random.choice(np.array(list(cls.__dict__)), p = proba)


class DateDim:
    def __init__(self): 
        self.calendar = None

    def create_date_table (self, start,end): 
        df = pd.DataFrame({"Date": pd.date_range(start, end)})
        df["Day"] = df.Date.dt.weekday_name
        df["Week"] = df.Date.dt.weekofyear
        df["Quarter"] = df.Date.dt.quarter
        df["Year"] = df.Date.dt.year
        df["Year_half"] = (df.Quarter + 1) // 2
        df.insert(0, 'Id', range(0, 0 + len(df)))
        self.calendar = df
        return self

    def random_by_dist(self, proba:list):
        # weight a selection so if need to randomly select can do so
        # in this case use date id's = in order to weight probability of things happening on certain day
        return np.random.choice(np.array(self.calendar.Id.tolist()), p = proba)

    def create_probability_dist(self, probabilities=None, start=None, end=None,date_list:list=None): 
        # create probability distribution for user based on start and end date or list of dates

        if np.sum(probabilities)!=100: 
            raise Exception("probabilities must add to 1.0")

        dist = [0]*(len(self.calendar)-1)
        if date_list is None: 
            # use the date range
            # blank range
            ids = self.calendar[(self.calendar.Date >=start) & (self.calendar.Date <=end)].Id.copy()
            
        else: 
            # if random days provided instead 
            ids = self.calendar(self.calendar.Date.isin(date_list)).copy()
        
        for i in ids:
            dist.insert(i,probabilities[i])
        return dist