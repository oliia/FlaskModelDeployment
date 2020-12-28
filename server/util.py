import pickle
import json
import numpy as np
import os

__data_columns = None
__model = None


def get_estimated_price(applicantincome, coapplicantincome, loanamount, loan_amount_term,
                        married_yes, property_area, credit_history=1, gender_male=0, dependents_1=0, dependents_2=0,
                        dependents_3=0,
                        education_not=0, self_employed_yes=0):
    try:
        dep_index = __data_columns.index(__dependants.lower())
        prop_index = __data_columns.index(__property_area.lower())
    except:
        loc_index = -1



    x = np.zeros(len(__data_columns))
    x[0] = credit_history
    x[1] = gender_male
    x[2] = married_yes
    x[3] = dependents_1
    x[4] = dependents_2
    x[5] = dependents_3
    x[6] = education_not
    x[7] = self_employed_yes

    # property_area
    if property_area > 0:
        x[8:10][property_area-1] = 1

    # numerical features
    x[10] = applicantincome
    x[11] = coapplicantincome
    x[12] = loanamount
    x[13] = loan_amount_term

    # if loc_index>=0:
    #     x[loc_index] = 1

    p = int(__model.predict([x]))
    poss = ['Rejected', 'Accepted']
    prediction = poss[p]

    return str(prediction)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __dependants
    global __property_area

    path = os.path.dirname(os.path.abspath(__file__))
    artifacts = os.path.join(path, "artifacts")

    with open(artifacts + "/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __dependants = __data_columns[3:6]  # 1, 2, 3+, columns 3,4 and 5
        __property_area = __data_columns[8:10]  # semiurban, urban, (dropped rural)

    global __model
    if __model is None:
        with open(artifacts + "/rf_model.pkl", 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_property_area():
    return __property_area


def get_dependant_numbers():
    return __dependants


def get_data_columns():
    return __data_columns


load_saved_artifacts()
