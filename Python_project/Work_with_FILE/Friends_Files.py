#friends = input("input 3 friends name separated by space: ").split(',')
friends = ['Anna', 'Jose', 'Mitchal']

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()] #[Line1, Line2, Line3, Line4]
people.close()

nearby_friends_set = set(friends).intersection(set(people_nearby))

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in nearby_friends_set:
    print(f"{friend} is nearby friend")
    nearby_friends_file.write(f"{friend}\n")

nearby_friends_file.close()

temp = []
temp.append()

