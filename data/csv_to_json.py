import csv
import json
import os
import glob

result = dict()

for filename in os.listdir('./csv/'):
    if filename.endswith('.csv'):

        with open(os.path.join('./csv/', filename)) as f:
            reader = csv.DictReader(f)
            category = filename.split('.')[0]
            print(category)
            result[category] = []
            for row in reader:
                result[category].append(row)

# for filepath in glob.glob(os.path.join('./csv/', '*.csv')):
#     with open(filepath) as csvfile:
#         reader = csv.DictReader(csvfile)
#         print(filepath)
#         for row in reader:
#             # result['data'].append(row)
#             result.append(row)

with open('./data.json', 'w') as output:
    json.dump(result, output, indent=4)

# with open('./places.js', 'w') as output:
#     output.write('export default [')