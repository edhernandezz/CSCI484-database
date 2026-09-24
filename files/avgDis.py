import math

def openFile():

        file = open("primary-time-series.csv" , 'r')
        column = file.readlines()
        file.close()

        return column

def avgDis(column):
        total = 0
        count = 0
        for line in column[1:]:
                data = line.strip().split(',')
                readings = float(data[7])

                total += readings
                count += 1

                avg = total / count

        return avg
        
def minMax(column):
        first = True

        for line in column[1:]:
                data = line.strip().split(',')
                readings = float(data[7])
        
                if first :
                        min = readings
                        max = readings
                        first = False
                if readings < min:
                        min = readings
                if readings > max:
                        max = readings
                

        return min, max

def stdDev(column, avg):
        count = 0
        total = 0
        
        for line in column[1:]:
                data = line.strip().split(',')
                readings = float(data[7])
        
                diff = readings - avg
                sqr = diff * diff
                total += sqr
                count += 1

                
        result = math.sqrt(total / (count - 1))
        
        return result

def main():

        column = openFile()
        avg = avgDis(column)
        min, max = minMax(column)
        std_dev = stdDev(column, avg)

        print("Avg = " "%.4f"%avg)
        print("Min = " "%.2f"%min)
        print("Max = " "%.2f"%max)
        print("Standard Deviation = " "%.4f"%std_dev)

        return 0


if __name__ == "__main__":
        main()