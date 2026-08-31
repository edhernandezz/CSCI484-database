import csv
with open('primary-time-series.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
    count= 0 
    tally= 0
    tallysq = 0
    measure =[]
    minVal = 100.0
    maxVal = 0.0
    first = True

    for row in spamreader:
        if count > 0:
            info=row[1].split(',')
            discharge=float(info[1])
            if first :
                minValue = discharge
                maxValue = discharge
                first = False
            if discharge < minValue:
                minValue = discharge
            if discharge > maxValue:
                maxValue = discharge
            measure.append(discharge)
            tally+=discharge
            tallysq+=discharge*discharge
            
        count+=1
    smeasure = sorted(measure)
    p25 = smeasure[int((count-1)*0.25)]
    p50 = smeasure[int((count-1)*0.5)]
    p75 = smeasure[int((count-1)*0.75)]
    average = tally/(count-1)
    variance = tallysq/(count-1)-average*average
    stdev = variance ** (1/2)
    print ("%.4f"%average, minValue, maxValue, "%.4f"%stdev)
    print(p25, p50, p75)