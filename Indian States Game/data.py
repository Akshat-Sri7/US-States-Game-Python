import pandas

states_data = {
    "state": ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat',
              'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra',
              'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
              'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal'],

    "x": [-100, 278, 239, 83, -25, -215, -249, -136, -108, 69, -192, -181, -110, -182, 278, 203, 252, 290, 41,
          -145, -199, 148, -108, -7, 222, -89, -60, 129],

    "y": [-176, 168, 113, 86, -15, -166, 35, 179, 260, 37, -183, -292, 36, -56, 74, 83, 33, 109, -47, 227, 122,
          140, -280, -117, 39, 203, 110, 23]
}

data = pandas.DataFrame(states_data)

data.to_csv('Indian_States.csv')
