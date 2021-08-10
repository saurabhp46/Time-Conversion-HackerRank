def timeConversion(s):
    dict1={}
    j=1
    for i in range(13,24):
        while (j):
            dict1[str(j)]=str(i)
            j+=1
            break
    keys=list(dict1.keys())
    list1=s.split(":")
    if list1[-1].endswith("PM"):
        list1[-1]=list1[-1].replace("PM","")
        if list1[0]=="12":
            list1[0]="12"
        if list1[0][0]=="0":
            list1[0]=list1[0].replace("0","")
        for i in keys:
            if list1[0]==i:
                list1[0]=dict1[i]
    if list1[-1].endswith("AM"):
        list1[-1]=list1[-1].replace("AM","")
        if list1[0][0]=="0":
            list1[0]=list1[0].replace("0","")
        if list1[0]=="12":
            list1[0]="00"
    opDate = ':'.join([elem for elem in list1])
    return opDate

if __name__ == '__main__':
    s = input('Enter Time in "hh:mm:ssAM/PM" format: ')   #e.g "07:40:03AM"

    result = timeConversion(s)
    print("Time in 24Hr Format:", result)
