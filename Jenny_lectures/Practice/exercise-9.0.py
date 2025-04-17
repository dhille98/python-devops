# write program for avg height 

height = input("Enter heights separated by a sapce:")

height_list = height.split()
count = 0
# using for user enter how many values 
for height in height_list:
    count += 1
print(count)
# this is using for converting to string to int
for i in range(count):
    height_list[i] = int(height_list[i])
    
print(height_list)
# calculate the avg height 
total = 0

for persion in height_list:
    total += persion
print(f"for total height is:, {total}")

avg = total / count

print(f"total avg is height is: {avg}")

