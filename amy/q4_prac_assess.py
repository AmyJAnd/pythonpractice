# given an integer, add 5 so the number is as big as possible.
# for example 6730 becomes 67530 but 2367 becomes 52367
# minus numbers -234 becomes -2345. -654 becomes -5654

n = 26
n_str = str(n)
count = 0
# print(type(n_str))
if n == 0:
    n_str = "50"
    print(int(n_str))
if n > 0:
    for x in n_str:
            if int(x) <= 5:
                if count == 0:  #ie at beginning of string
                    n_str = "5" + n_str[0:] # put 5 at the beginning
                    print(int(n_str))
                    break
                elif count > 0 and count < len(n_str): # somewhere in the middle
                    n_str = n_str[0:count] + "5" + n_str[count:]
                    print(int(n_str))
                    break
            elif int(x) > 5 and count == len(n_str) - 1:     # all digits are over 5 - put at end
                n_str = n_str + "5"
                print(int(n_str))
                break
            count +=1
if n < 0:
    n_st = str(n)
    n_str = n_st[1:] # removes minus sign
    # print(n_str)
    for x in n_str:
        if int(x) >= 5:
            if count == 0:
                n_str = "5" + n_str[0:]
                print(int(n_str))
                break
            elif count > 0 and count < len(n_str): # think this is right now puts 5 in middle inc one before end
                n_str = n_str[0:count] + "5" + n_str[count:]
                n_str2 = "-" + n_str
                print(int(n_str2))
                break
        elif int(x) < 5 and count == len(n_str) - 1:
            n_str = "-" + n_str + "5"
            print(int(n_str))
            break
        count += 1