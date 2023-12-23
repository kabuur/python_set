
# list of coutries
List_couters = ["somali","gana","kenya", "ethopia","djbuti"]
# list of countries change into set
coutry_set = set(List_couters)
print("Set of countries is ",coutry_set)

#create set with default values
fruits = {"apple","banana","mango"}
# check if the watermelon in the set 
print("watermelon" in fruits)
# add watermelon in the set 
fruits.add("watermelon")
print(fruits)
#removing rendom elemant
print(fruits.pop())
print(fruits)