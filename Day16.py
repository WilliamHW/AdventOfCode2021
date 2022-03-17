from get_aoc import get_input

raw_hex_input = get_input(16)
#raw_hex_input = "D2FE28"
#raw_hex_input = "38006F45291200"
#raw_hex_input = "EE00D40C823060"
#raw_hex_input = "8A004A801A8002F478"
#raw_hex_input = "620080001611562C8802118E34"
#raw_hex_input = "C0015000016115A2E0802F182340"
#raw_hex_input = "A0016C880162017C3686B18A3D4780"
#raw_int_input = int(raw_hex_input, 16)
#raw_int_input = int(raw_hex_input, base=16)

#raw_hex_input = "C200B40A82"
#raw_hex_input = "04005AC33890"
#raw_hex_input = "880086C3E88112"
#raw_hex_input = "CE00C43D881120"
#raw_hex_input = "D8005AC2A8F0"
#raw_hex_input = "F600BC2D8F"
#raw_hex_input = "9C005AC2F8F0"
#raw_hex_input = "9C0141080250320F1802104A08"

raw_bin_input = ""
for x in raw_hex_input:
    raw_bin_input += str(bin(int(x,16)))[2:].zfill(4)  

#version = int(raw_bin_input[0:3], 2)
#type_ID = int(raw_bin_input[3:6], 2)
#rest = raw_bin_input[6::]
#len_rest = len(rest)

def get_parameters(remaining_binary):
    version = int(remaining_binary[0:3], 2)
    print("The version is " + str(version))
    type_ID = int(remaining_binary[3:6], 2)
    print("The type_ID is " + str(type_ID))
    rest = remaining_binary[6::]
    len_rest = len(rest)
    return version, type_ID, rest

stuff_left = True
place = 0
version_total_count = 0

rest = raw_bin_input

def get_version_subtotal (binary_string):
    if len(binary_string) < 11 :
        print("The string is too short, of length : " + str(len(binary_string)))
        return 0
    version, type_ID, rest = get_parameters(binary_string)
    #version_total_count += version
    version_subtotal = version
    #print("The version total is " + str(version_total_count))
    if type_ID == 4:
        print("ID 4")
        literal_value = ""
        while rest[0] == "1":
            literal_value += rest[1:5]
            #if rest[0] == "1" : break
            #print("why didn't this work?")
            temp_rest = rest[5::]
            rest = temp_rest
        literal_value += rest[1:5]
        #if rest[0] == "1" : break
        #print("last loop, only once")
        temp_rest = rest[5::]
        rest = temp_rest
        int_literal_value = int(literal_value, 2)
        print("The literal value is " + str(int_literal_value))
    elif type_ID != 4:
        if rest[0] == "0": # Length Type ID
            total_length_in_bits = int(rest[1:16],2)
            temp_rest = rest[16::]
            rest = temp_rest
            #print("I don't know how to interprete this") # How come the string is 11 and 16 long
        elif rest [0] == "1":
            number_of_sub_packets = int(rest[1:12],2)
            print("There are x sub-packets : " + str(number_of_sub_packets))
            temp_rest = rest[12::]
            rest = temp_rest
            #print("so I got here")
        else:
            print("Something's fucked2")
    else:
        print("Something's fucked")
    return version + get_version_subtotal(rest)

total = get_version_subtotal(raw_bin_input)
print("Part 1: The running total of version numbers is : " + str(total)) #Answer = 908

#Part Two
print("PART TWO")

def literal_value (rest): #Type ID 4
    literal_value = ""
    while rest[0] == "1":
        literal_value += rest[1:5]
        #if rest[0] == "1" : break
        print("why didn't this work?")
        temp_rest = rest[5::]
        rest = temp_rest
    literal_value += rest[1:5]
    #if rest[0] == "1" : break
    print("last loop, only once")
    temp_rest = rest[5::]
    rest = temp_rest
    int_literal_value = int(literal_value, 2)
    print("The literal value is " + str(int_literal_value))
    return int_literal_value, rest

def type_ID_0 (rest, number_of_sub_packets): # Sums values
    print("so I got here")
    running_loop = 0
    sub_packet_counter = 0
    while sub_packet_counter < number_of_sub_packets :
        print("Keep it running") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        running_loop += packet_value                
        print("Running loop has this value : " +str(running_loop))
        sub_packet_counter += 1
    return running_loop, rest

def type_ID_0b (rest): # Sums values
    print("so I got hereB")
    running_loop = 0
    while len(rest) >= 11:
        print("Keep it runningB") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        running_loop += packet_value                
        print("Running loop has this value : " +str(running_loop))
    return running_loop #, rest

def type_ID_1 (rest, number_of_sub_packets): # Sums values
    print("so NOW I got here")
    running_loop = 1
    sub_packet_counter = 0
    while sub_packet_counter < number_of_sub_packets :
        print("Keep NOW it running") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        running_loop = running_loop * packet_value                
        print("Running NOW loop has this value : " +str(running_loop))
        sub_packet_counter += 1
    return running_loop, rest

def type_ID_1b (rest): # Sums values
    print("so NOW I got hereB")
    running_loop = 1
    while len(rest) >= 11:
        print("Keep Now it runningB") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        running_loop = running_loop * packet_value                
        print("Running loopB has this value : " +str(running_loop))
    return running_loop #, rest

def type_ID_2 (rest, number_of_sub_packets): # Gives min value
    print("so NOW I got hereC")
    #running_loop = 1
    sub_packet_counter = 0
    packet_min_array = []
    while sub_packet_counter < number_of_sub_packets :
        print("Keep NOW it runningC") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        packet_min_array.append(packet_value)
        #running_loop = running_loop * packet_value                
        print("Array for min has these values : ")
        print(packet_min_array)
        sub_packet_counter += 1
    return min(packet_min_array), rest

def type_ID_2b (rest): # gives min value
    print("so NOW I got hereCc")
    packet_min_array = []
    while len(rest) >= 11:
        print("Keep Now it runningC") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        packet_min_array.append(packet_value)             
        print("Array for minB has these values : ")
        print(packet_min_array)
    return min(packet_min_array) #, rest

def type_ID_3 (rest, number_of_sub_packets): # Gives MAX value
    print("so NOW I got hereC")
    #running_loop = 1
    sub_packet_counter = 0
    packet_max_array = []
    while sub_packet_counter < number_of_sub_packets :
        print("Keep NOW it runningC") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        packet_max_array.append(packet_value)
        #running_loop = running_loop * packet_value                
        print("Array for max has these values : ")
        print(packet_max_array)
        sub_packet_counter += 1
    return max(packet_max_array), rest

def type_ID_3b (rest): # gives max value
    print("so NOW I got hereCc")
    packet_max_array = []
    while len(rest) >= 11:
        print("Keep Now it runningC") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        packet_max_array.append(packet_value)             
        print("Array for maxB has these values : ")
        print(packet_max_array)
    return min(packet_max_array) #, rest

def type_ID_5 (rest, number_of_sub_packets): # Gives 1 or 0 value
    print("so NOW I got hereD")
    #running_loop = 1
    sub_packet_counter = 0
    packet_array = []
    while sub_packet_counter < number_of_sub_packets :
        print("Keep NOW it runningD") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        packet_array.append(packet_value)
        #running_loop = running_loop * packet_value                
        print("Array for greater than has these values : ")
        print(packet_array)
        sub_packet_counter += 1
    if packet_array[0] > packet_array[1] : return 1, rest
    if packet_array[0] <= packet_array[1] : return 0, rest # How to combine this in 1 line?

def type_ID_5b (rest): # gives max value
    print("so NOW I got hereDd")
    packet_array = []
    while len(rest) >= 11:
        print("Keep Now it runningD") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        packet_array.append(packet_value)             
        print("Array for greater than has these values : ")
        print(packet_array)
    if packet_array[0] > packet_array[1] : return 1
    if packet_array[0] <= packet_array[1] : return 0

def type_ID_6 (rest, number_of_sub_packets): # Gives 1 or 0 value
    print("so NOW I got hereE")
    #running_loop = 1
    sub_packet_counter = 0
    packet_array = []
    while sub_packet_counter < number_of_sub_packets :
        print("Keep NOW it runningE") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        packet_array.append(packet_value)
        #running_loop = running_loop * packet_value                
        print("Array for less than has these values : ")
        print(packet_array)
        sub_packet_counter += 1
    if packet_array[0] < packet_array[1] : return 1, rest
    if packet_array[0] >= packet_array[1] : return 0, rest # How to combine this in 1 line?

def type_ID_6b (rest): # gives max value
    print("so NOW I got hereEe")
    packet_array = []
    while len(rest) >= 11:
        print("Keep Now it runningE") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        packet_array.append(packet_value)             
        print("Array for less than has these values : ")
        print(packet_array)
    if packet_array[0] < packet_array[1] : return 1
    if packet_array[0] >= packet_array[1] : return 0

def type_ID_7 (rest, number_of_sub_packets): # Gives 1 or 0 value
    print("so NOW I got hereF")
    #running_loop = 1
    sub_packet_counter = 0
    packet_array = []
    while sub_packet_counter < number_of_sub_packets :
        print("Keep NOW it runningF") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        packet_array.append(packet_value)
        #running_loop = running_loop * packet_value                
        print("Array for equals has these values : ")
        print(packet_array)
        sub_packet_counter += 1
    if packet_array[0] < packet_array[1] : return 1, rest
    if packet_array[0] >= packet_array[1] : return 0, rest # How to combine this in 1 line?

def type_ID_7b (rest): # gives max value
    print("so NOW I got hereFf")
    packet_array = []
    while len(rest) >= 11:
        print("Keep Now it runningF") # : " + str(len(binary_string)))
        packet_value, rest = get_packet_value(rest)
        packet_array.append(packet_value)             
        print("Array for equals has these values : ")
        print(packet_array)
    if packet_array[0] == packet_array[1] : return 1
    if packet_array[0] != packet_array[1] : return 0

def get_packet_value (binary_string):
    print("NEW ANALYSIS")
    int_literal_value = 0
    if len(binary_string) < 11 :
        print("The string is too short, of length : " + str(len(binary_string)))
        return 0
    version, type_ID, rest = get_parameters(binary_string)
    version_subtotal = version
    if type_ID == 4:
        print("ID 4")
        return literal_value (rest)   
    elif rest[0] == "0": # Length Type ID, 15 bits
        print("hEer")
        total_length_in_bits = int(rest[1:16],2)
        temp_rest = rest[16::]
        this_rest = temp_rest[:total_length_in_bits:]
        remaining_rest = temp_rest[total_length_in_bits::]
        if type_ID == 0 : sub_packet_valueB = type_ID_0b (this_rest)
        if type_ID == 1 : sub_packet_valueB = type_ID_1b (this_rest)
        if type_ID == 2 : sub_packet_valueB = type_ID_2b (this_rest)
        if type_ID == 3 : sub_packet_valueB = type_ID_3b (this_rest)
        #if type_ID == 4 : sub_packet_valueB = type_ID_4b (this_rest)
        if type_ID == 5 : sub_packet_valueB = type_ID_5b (this_rest)
        if type_ID == 6 : sub_packet_valueB = type_ID_6b (this_rest)
        if type_ID == 7 : sub_packet_valueB = type_ID_7b (this_rest)
        return sub_packet_valueB, remaining_rest
        print("then here")
        return this_call, remaining_rest
        #print("I don't know how to interprete this") # How come the string is 11 and 16 long
    elif rest[0] == "1": # Number of sub-packets, 11 bits
        number_of_sub_packets = int(rest[1:12],2)
        print("There are x sub-packets : " + str(number_of_sub_packets))
        temp_rest = rest[12::]
        rest = temp_rest
        if type_ID == 0 : return type_ID_0 (rest, number_of_sub_packets)
        if type_ID == 1 : return type_ID_1 (rest, number_of_sub_packets)
        if type_ID == 2 : return type_ID_2 (rest, number_of_sub_packets)
        if type_ID == 3 : return type_ID_3 (rest, number_of_sub_packets)
        #if type_ID == 4 : return type_ID_4 (rest, number_of_sub_packets)
        if type_ID == 5 : return type_ID_5 (rest, number_of_sub_packets)
        if type_ID == 6 : return type_ID_6 (rest, number_of_sub_packets)
        if type_ID == 7 : return type_ID_7 (rest, number_of_sub_packets)
    else:
        print("Something's fucked")
    return int_literal_value + get_packet_value(rest)

total_value, remaining_rest = get_packet_value(raw_bin_input)
print("The remaining rest is : " + str(remaining_rest))
print("Part 2: The value of the othermost packet is : " + str(total_value))
#Answer != 10626194228227


"""
while stuff_left == True:
    print("first time here")
    version, type_ID, rest = get_parameters(rest)
    version_total_count += version
    print("The version total is " + str(version_total_count))
    if type_ID == 4:
        print("ID 4")
        literal_value = ""
        while rest[0] == "1":
            literal_value += rest[1:5]
            #if rest[0] == "1" : break
            print("why didn't this work?")
            temp_rest = rest[5::]
            rest = temp_rest
        literal_value += rest[1:5]
        #if rest[0] == "1" : break
        print("last loop, only once")
        temp_rest = rest[5::]
        rest = temp_rest
        int_literal_value = int(literal_value, 2)
        print("The literal value is " + str(int_literal_value))
    elif type_ID != 4:
        if rest[0] == "0": # Length Type ID
            total_length_in_bits = int(rest[1:16],2)
            temp_rest = rest[(16 + total_length_in_bits)::]
            rest = temp_rest
            print("I don't know how to interprete this") # How come the string is 11 and 16 long
        elif rest [0] == "1":
            number_of_sub_packets = int(rest[1:12],2)
            print("There are x sub-packets : " + str(number_of_sub_packets))
            temp_rest = rest[(12 + 11*number_of_sub_packets)::]
            rest = temp_rest
            print("so I got here")
        elif rest [0] == "1":
            number_of_sub_packets = int(rest[1:12],2)
            print("There are x sub-packets : " + str(number_of_sub_packets))
            temp_rest = rest[(12 + 11*number_of_sub_packets)::]
            rest = temp_rest
            print("so I got here")
        elif rest [0] == "1":
            number_of_sub_packets = int(rest[1:12],2)
            print("There are x sub-packets : " + str(number_of_sub_packets))
            temp_rest = rest[(12 + 11*number_of_sub_packets)::]
            rest = temp_rest
            print("so I got here")
        elif rest [0] == "1":
            number_of_sub_packets = int(rest[1:12],2)
            print("There are x sub-packets : " + str(number_of_sub_packets))
            temp_rest = rest[(12 + 11*number_of_sub_packets)::]
            rest = temp_rest
            print("so I got here")
        elif rest [0] == "1":
            number_of_sub_packets = int(rest[1:12],2)
            print("There are x sub-packets : " + str(number_of_sub_packets))
            temp_rest = rest[(12 + 11*number_of_sub_packets)::]
            rest = temp_rest
            print("so I got here")
        elif rest [0] == "1":
            number_of_sub_packets = int(rest[1:12],2)
            print("There are x sub-packets : " + str(number_of_sub_packets))
            temp_rest = rest[(12 + 11*number_of_sub_packets)::]
            rest = temp_rest
            print("so I got here")
        elif rest [0] == "1":
            number_of_sub_packets = int(rest[1:12],2)
            print("There are x sub-packets : " + str(number_of_sub_packets))
            temp_rest = rest[(12 + 11*number_of_sub_packets)::]
            rest = temp_rest
            print("so I got here")
        elif rest [0] == "1":
            number_of_sub_packets = int(rest[1:12],2)
            print("There are x sub-packets : " + str(number_of_sub_packets))
            temp_rest = rest[(12 + 11*number_of_sub_packets)::]
            rest = temp_rest
            print("so I got here")
        else:
            print("Something's fucked2")
    else:
        print("Something's fucked")
    if len(rest) <= 10:
        stuff_left = False
        print("The string left is only this long : " + str(len(rest)))
"""
"""
hex_value = "1f"
print(len(hex_value))
int_value = int(hex_value, base=16)
print(bin(int_value))
binary_value = str(bin(int_value))[2:].zfill(4*2)
print(binary_value)
test = "D2FE28"
int_test = int(test, base=16)
print(int_test)
print(type(int_test))
bin_test = str(bin(int_test))[2:].zfill(len(test)*4)
print(bin_test)
print(type(bin_test))
#print(bin(test))
"""