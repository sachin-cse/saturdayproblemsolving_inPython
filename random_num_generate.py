import random
def random_num_generate(a,b):
    return random.randint(int(a),int(b))

x,y = input('Enter the values').split()

print(random_num_generate(x,y))