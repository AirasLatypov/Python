# my_list = [123, "Airas", 32.2]
# print(my_list[2])
# print(type(my_list[2]))
#
            # my_dict = {"ключ": 'значение'}
# print(my_dict)
#
#
#
#
# my_cars = ["Dodge", "Honda", "Nissan", "Ford"]
# data = {"cars": my_cars}
# print(data["cars"][2])

example = [{"id":"5005","type":"Sugar"},{"id":"5007","type":"Powdered Sugar"},{"id":"5006","type":"Chocolate with Sprinkles"},{"id":"5003","type":"Chocolate"},{"id":"5004","type":"Maple"}]
count = len(example)
# print(count)
# print(example[3]["type"])


nsa_list = [{"ключ": 'значение1'}, {"ключ": 'значение2'}, {"ключ": 'значение3'}, {"ключ": 'значение4'}]
nsa_dict = {"ключ1": 'значение1', "ключ2": 'значени2е', "ключ3": 'значение3'}
nsa_combination = {"ключ": nsa_list}

test = {"Working": True}
test2 = {"Working": true}
print(type(nsa_combination))
print(type(nsa_combination["ключ"]))


print(type(test))