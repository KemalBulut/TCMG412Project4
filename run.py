import requests

## Logfile URL 
url = "https://s3.amazonaws.com/tcmg476/http_access_log"

r = requests.get(url, stream = True)

## Open and copy to new local file
with open("python.txt","wb") as textfile:
   for chunk in r.iter_content(chunk_size=1024):

       if chunk:
           textfile.write(chunk)

## Open and work off of the new local file
file = open ("python.txt")

## Defining variables for final results desired including formatting for output data
result1 = {"day data": {}}
result2 = {"week data": {}}
result3 = {"month data": {}}
result4 = {"request not successful": 0}
result5 = {"request redirected elsewhere": 0}
result6 = {"filetime request frequency": {}}

## still need to be established so that they actually output what they're supposed to
result7 = {"most requested file"}
result8 = {"least requested file"}

fileMost = None
fileLeast = None
countMost = 0
countLeast = 0

date_day = None
days = 0
week = None
months_done = []

for line in file:
    
    if len(line) >= 56:
        data = line.split()
        date = data[3][1::].split(':')
        if not (date_day == date[0]):
            date_day = date[0]
            days += 1
            if days % 7 == 0:
                week = date_day
       
        ## Count file requests per day
        if date[0] in result1["day data"]:
            result1["day data"][date[0]] += 1
        else:
            result1["day data"][date[0]] = 0
        
        ## Count file requests per week
        if week in result2["week data"]:
            result2["week data"][week] += 1
        else:
            result2["week data"][week] = 0
        month = date[0][3::]
        
        ## Create a new file for the new month data
        if month not in months_done:
            file_name = month[:3:] + month[4::]
            if (len(file_name)) == 7:
                month_file = open(month[:3:] + month[4::] + ".txt", 'w')
                print(file_name)
            months_done.append(month)
        month_file.write(line)
        
        ## Count file requests per month
        if month in result3["month data"]:
            result3["month data"][month] += 1
        else:
            result3["month data"][month] = 0
        
        ## 400 level requests, unsuccessful count
        if data[-2][0] == "4":
            result4["request not successful"] += 1
            if data[-2][0] == "3":
                result5["requests redirected elsewhere"] += 1
        
        ## 300 level requests, unsuccessful count
        
        
        ## File request frequency count
        if data[6] in result6["filetime request frequency"]:
            result6["filetime request frequency"][data[6]] += 1
        else:
            result6["filetime request frequency"][data[6]] = 1

max = result6
min = result6
maxName = " "
maxValue = 0
minName = " "
minValue = 0
for i in result6:
   if result6[i] > max:
       max = result6[i]
       maxlist=[i]
       maxValue = max
   if result6[i] < min:
       min = result6[i]
       minlist=[i]
       minValue = min

   if result6[i] == max:
       maxlist.append(i)

   if result6[i] == min:
       minlist.append(i)

result7=[max,maxlist]
result8=[min,minlist]

## Nested within the loops to print for each day, week, month before increasing to next
print(result1)
print(result2)
print(result3)

## Printed at the end?
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)



