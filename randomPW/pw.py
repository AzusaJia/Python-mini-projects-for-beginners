import string
import random
import math

# input the password's length
def len_input():
    asc = string.digits + string.ascii_letters + string.punctuation
    pw_len = int(input("please input the length of password: "))
    # di_le:50%    le_len:30%    pun_len:20%
    di_len = int(pw_len / 2)
    le_len = int(math.ceil(pw_len / 3))
    pun_len = pw_len - di_len - le_len
    return di_len, le_len, pun_len

password = []

# generate password
def password_generator(di_len, le_len, pun_len):
    di_pw = random.sample(string.digits,di_len)
    le_pw = random.sample(string.ascii_letters,le_len)
    pun_pw = random.sample(string.punctuation,pun_len)
    password = di_pw + le_pw + pun_pw
    random.shuffle(password)
    return ''.join(password)

if __name__=="__main__":
    di_len, le_len, pun_len = len_input()
    print(f'Your password is:{password_generator(di_len, le_len, pun_len)}, the length is: {di_len + le_len + pun_len}')