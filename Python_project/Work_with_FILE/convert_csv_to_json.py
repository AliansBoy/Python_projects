import json

file_csv = open('csv_file.txt', 'r')
csv_data = [line.strip() for line in file_csv]
file_csv.close()

json_data = []
for line in csv_data:
    club_data = line.split(',')
    json_data.append({"club": club_data[0], "city": club_data[1], "country": club_data[2]})

file_json = open('json_file.txt', 'w')
json.dump(json_data, file_json)
file_json.close()
