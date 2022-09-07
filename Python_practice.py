# counties = ["Arapahoe","Denver","Jefferson"]
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# # print(f'Arapahoe county has {counties_dict["Arapahoe"]} registered voters.')
# # print(f'Denver county has {counties_dict["Denver"]} registered voters.')
# # print(f'Jefferson county has {counties_dict["Jefferson"]} registered voters.')
# for county, voters in counties_dict.items():
#     print(f'{county} county has {voters} registered voters')
#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
# the following is to retrieve only the counties from the voting_data dictionary
# for i in range(len(voting_data)):
#     print(voting_data[i]["county"])
#The following is to retrieve only the values from the voting_data dictionary
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
#the following is to retrieve the number of registered voters (be sure you are using underscores and being consistent)
# for county_dict in voting_data:
#      print(county_dict['registered_voters'])
#the following is used to retrieve the counties from the voting_data dictionary
# for county_dict in voting_data:
#     print(county_dict['county'])
#the following prints what each county has.
# for county_dict in voting_data:
#         print(f'{county_dict["county"]} county has {county_dict["registered_voters"]} registered voters.')
