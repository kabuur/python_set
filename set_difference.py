# creating set_num1 start with 1 end with 999
set_num1 = set(range(1000))
# creating set_num2 start with 500 end with 1499
set_num2 = set(range(500,1500))

# difference set_num1 to set_num2
difference_set = set_num1.difference(set_num2)
print ("difference set_num1 to set_num2", difference_set)

print("///////////////////////////")

# set of days 
set_days1 = {"monday","tuesday","wednesday",}
set_days2 = {"thursday","friday","saturday","wednesday"}

difference_days = set_days1.difference(set_days2)
print ("the difference of the days", difference_days)