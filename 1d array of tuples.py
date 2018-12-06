import numpy as np

all_data = np.genfromtxt(open("./adult.data","r"), dtype=[ 
                      ('age', 'i4'),
                      ('workclass', 'S16'),
                      ('fnlwgt', 'i8'),
                      ('education', 'S12'),
                      ('education_num', 'i4'),
                      ('marital_status', 'S22'),
                      ('occupation', 'S17'),
                      ('relationship', 'S14'),
                      ('race', 'S18'),
                      ('sex', 'S6'),
                      ('capital_gain', 'i8'),
                      ('capital_loss', 'i8'),
                      ('hours_per_week', 'i4'),
                      ('native_country', 'S26'),
                      ('income', 'S5')
                      ],
                      delimiter=",", autostrip=True,
                      missing_values=('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'))

# load class labels from column 15
y_adult_labels = all_data['income']

# load the 14 features
X_adult = all_data[:][0:-1]
