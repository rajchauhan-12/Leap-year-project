def valid_date(d):
    import datetime
    date_string = d
    date_format = '%Y-%m-%d'
    try:
        dateObject = datetime.datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False
    
    
    
date1=(input("Enter the start Date\nIn (YYYY-MM-DD): "))
date2=(input("Enter the end Date\nIn (YYYY-MM-DD): "))
if valid_date(date1) and valid_date(date2):
    a=int(date1[0:4])
    b=int(date2[0:4])
    print("\nStart Year:",a)
    print("End Year:",b,"\n")
    print("Leap Years Are:")
    l=[]
    if a>b:
        for i in range(b,a+1):
            if (i % 400 == 0) and (i % 100 == 0):
                l.append(i)
            elif (i % 4 ==0) and (i % 100 != 0):
                l.append(i)
            else:
                continue
    else:
        for i in range(a,b+1):
            if (i % 400 == 0) and (i % 100 == 0):
                l.append(i)
            elif (i % 4 ==0) and (i % 100 != 0):
                l.append(i)
            else:
                continue
    print(l)
    m=[]
    if a<b:
        for i in range(a,b):
            if i not in l:
                m.append(i)
    else:
        for i in range(b,a):
            if i not in l:
                m.append(i)
    print("Non Leap Years Are:")
    print(m)
else:
    print("Enter Date in correct manner")