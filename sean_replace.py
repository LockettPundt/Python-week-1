staff_list = ["Sean", "David", "Mary Ella", "Liz", "Sean"]
print(staff_list)
i = 0
while i < len(staff_list):
    if staff_list[i] == "Sean":
        staff_list[i] = "Ranger"
    elif staff_list[i] == "David":
        staff_list[i] = "Not David"
        
    i += 1

print(staff_list)

# print(staff_list)
# for x in staff_list:
#     if x == "Sean":
#         sean_index = staff_list.index("Sean")
#         staff_list[sean_index] = "Ranger"
#     elif x == "David":
#         david_index = staff_list.index("David")
#         staff_list[david_index] = "Not David"


# print(staff_list)
