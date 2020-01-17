#takes a list and returns the list sans an duplicates.
sample = [ 1, 1, 'hi', 'hi', 23, 'eight hundred', 800, 60, 12345, 12345, 1, "1"]
new_list = []
i = 0
while i < len(sample):
    if (sample[i] not in new_list):
         new_list.append(sample[i])
    i += 1

print(new_list)