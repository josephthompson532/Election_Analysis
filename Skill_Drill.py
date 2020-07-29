voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for dis_dic in voting_data:
    print(f"{dis_dic['county']} county has {dis_dic['registered_voters']:,} registered voters")