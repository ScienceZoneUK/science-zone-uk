# RGB list
COLOUR_LIST = ["R", "G", "B"]
rgb = [1,2,3]

#8 bit Binary values
BIN_VALUES = [128,64,32,16,8,4,2,1]

#A string of 3 binary lists
binary_nums = "11111111 11111111 11111111"
#Split string in a list by 'space'
bin_list = binary_nums.split(" ")

print(f'List of binary values : {binary_nums}')
#Set colour at 0
colour = 0

#Alogrithm to turn binary into a value 0-255
for col_count, colour in enumerate(rgb):
    print(f'{COLOUR_LIST[col_count]} = {colour}')
    colour = 0 # reset colour value
    for count, value in enumerate(bin_list[col_count]):
        print(count, value)
        if value == '1':
            colour += BIN_VALUES[count]
    print(colour)
              
    
            
print(f'Final RGB value : {rgb}')
            




