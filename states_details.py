import pandas as pd
states_details = {'Andhra Pradesh': [53903393,27], 'Assam': [35607039, 41],
                  'Arunachal Pradesh': [35607039, 153], 'Bihar': [124799926, 12],
                  'Gujarat': [63872399, 23], 'Jammu and Kashmir': [13606320, 75],
                  'Jharkhand': [38593948, 37], 'West Bengal': [99609303, 15],
                  'Karnataka': [67562686, 21], 'Kerala': [38593948, 37],
                  'Madhya Pradesh': [85358965, 17], 'Maharashtra': [123144223, 12],
                  'Manipur': [3091545, 137], 'Meghalaya': [3366710, 135],
                  'Mizoram': [1239244, 158], 'Nagaland': [2249695, 146],
                  'Odisha': [46356334, 31], 'Punjab': [30141373, 48],
                  'Rajasthan': [81032689, 20], 'Sikkim': [690251, 166],
                  'Tamil Nadu': [77841267, 20], 'Tripura': [4169794, 130],
                  'Uttarakhand': [13606320, 75], 'Uttar Pradesh': [237882725, 5],
                  'Haryana': [28204692, 51], 'Himachal Pradesh':[7451955, 104],
                  'Goa': [1586250, 153], 'Chhattisgarh': [29436231, 48], 'Telangana': [39362732, 36]}

#calling pandas module dataframe to create the dataframe from the dictionary
state = pd.DataFrame.from_dict(states_details, orient='index')
print(state)
state.to_csv('state')  #storing the read values into the state csv file