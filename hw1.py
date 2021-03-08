# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061135.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

for i in range(len(data)):
   if data[i]['TEMP'] == -99 or data[i]['TEMP'] == -999:
      data[i]['TEMP'] = 'NONE'



data_C0X260 = list(filter(lambda item: item['station_id'] == 'C0X260', data))
data_C0A880 = list(filter(lambda item: item['station_id'] == 'C0A880', data))
data_C0F9A0 = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
data_C0G640 = list(filter(lambda item: item['station_id'] == 'C0G640', data))
data_C0R190 = list(filter(lambda item: item['station_id'] == 'C0R190', data))

data_C0X260.sort(key = lambda item : item['TEMP'])
data_C0A880.sort(key = lambda item : item['TEMP'])
data_C0F9A0.sort(key = lambda item : item['TEMP'])
data_C0G640.sort(key = lambda item : item['TEMP'])
data_C0R190.sort(key = lambda item : item['TEMP'])

# Retrive ten data points from the beginning.
target_data = [['C0A880',data_C0A880[-1]['TEMP']],['C0F9A0',data_C0F9A0[-1]['TEMP']],['C0G640',data_C0G640[-1]['TEMP']],['C0R190',data_C0R190[-1]['TEMP']],['C0X260',data_C0X260[-1]['TEMP']]]

#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#print(data_C0X260)
#print(data[0]['TEMP'])
#========================================