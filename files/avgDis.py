def readData():
    total = 0
    count = 0

    file = open("primary-time-series.csv" , 'r')
    column = file.readlines()
    for line in column[1:]:
        data = line.strip().split(',')
        readings = float(data[7])
        total = total + readings
        count += 1

        avg = total / count
    
    print("%.4f"%avg)
            

