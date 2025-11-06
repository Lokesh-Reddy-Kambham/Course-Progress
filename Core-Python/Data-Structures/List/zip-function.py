# names = ["Rohit","Virat","Dhoni","Rahul"]
# runs = [1000,12000,7000,8000]
# states = ["MH","DL","JK","KA"]
# ipl_team = ["MI","RCB","CSK","DC"]
#
# c_info = list(zip(names,runs,states,ipl_team))
# print(c_info)
# info = [(n1,r1,s1,i1) for n1,r1,s1,i1 in (names,runs,states,ipl_team)]
# print(info)

names = ["Rohit","Virat","Dhoni","Rahul"]
runs = [1000,12000,7000,8000]
states = ["MH","DL","JK","KA"]
ipl_team = ["MI","RCB"]
c_info_1 = list(zip(names,runs,states,ipl_team))
print(c_info_1)

from itertools import zip_longest
c_info_2 = list(zip_longest(names,runs,states,ipl_team))
print(c_info_2)
c_info_3 = list(zip_longest(names,runs,states,ipl_team,fillvalue="###"))
print(c_info_3)

c_info_4 = dict(zip_longest(names,runs,states,ipl_team,fillvalue="###"))

print(c_info_4)


