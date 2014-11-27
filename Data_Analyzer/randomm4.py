# Note exponential and exponential1 functions are used to generate random % of time difference between actual and estimated time required.  changing expval and expval1 will increase or decrease the deviation of random generation of actual time taken from estimated time required.   
import math
import re
#import scipy as sc
print ""
from random import randint
expval=24
expval1=5
f = open ("IN.txt","r")                           #IN.txt contains the database of locations in India
data = f.read()
strr=str(data)
strr=strr.split('\n')
strrr=[]
j=[]
k=0
for i in strr:
    b=i.split('\t')
    strrr.append(b)
    k=k+1
strrr.pop(-1)
fd=open("test.txt");                               # The file where transit time extreme cases(Exceptions) are added
rec1=fd.read()
rec1=rec1.split("\n")
rec=[]
for i in rec1:
    rec.append(i.split("\t"))
rec.pop(-1)
newrec={}                                          # A dictionary of transit time exceptions with a string '[Pune,Mumbai]' i.e. '[Source,Destin                                                   #ation]' as the key
for i in rec:
    if str([i[0],i[1]]) not in newrec:
        newrec[str([i[0],i[1]])]=1
    else:
        newrec[str([i[0],i[1]])]=newrec[str([i[0],i[1]])]+1

rdictt={}                                          # Dictionary with all the locations in IN.txt

for i in strrr:
    if i[2] not in rdictt:
        rdictt[i[2]]=[]
        rdictt[i[2]].append(i)
    else:
        rdictt[i[2]].append(i)
#print rdictt
latlon={}                                          # Dictionary with latitude as the key
for i in strrr:
    nos=int(float(i[4][:2]))
    if nos not in latlon:
        latlon[nos]=[]
        latlon[nos].append(i)
    else:
        latlon[nos].append(i)

def popul(people):                                 # List of locations above 10000 Population
    n=[]
    for i in strrr:
        if int(i[14])>people:
            n.append(i)
   # print len(strrr)-len(n)
    return n

newlist=popul(10000)

lonlat={}                                          # Dictionary of locations with longitudes as keys
for i in strrr:
    nos=int(float(i[5][:2]))
    if nos not in lonlat:
        lonlat[nos]=[]
        lonlat[nos].append(i)
    else:
        lonlat[nos].append(i)

latlon1={}                                         # Dictionary of locations above 10000 population with latitudes as keys 
for i in newlist:
    nos=int(float(i[4][:2]))
    if nos not in latlon1:
        latlon1[nos]=[]
        latlon1[nos].append(i)
    else:
        latlon1[nos].append(i)

lonlat1={}                                         # Dictionary of locations above 10000 population with longitudes as keys
for i in newlist:
    nos=int(float(i[5][:2]))
    if nos not in lonlat1:
        lonlat1[nos]=[]
        lonlat1[nos].append(i)
    else:
        lonlat[nos].append(i)



States={'Andhra Pradesh':'Hyderabad','Manipur':'Imphal','Meghalaya':'Shillong','Mizoram':'Aizawl','West Bengal':'Kolkata','Uttarakhand':'Dehradun','Uttar Pradesh':'Lucknow','Tripura':'Agartala','Tamil Nadu':'Chennai','Rajasthan':'Jaipur','Punjab':'Chandigarh','Odisha':'Bhubaneswar','Nagaland':'Kohima','Madhya Pradesh':'Bhopal','Andaman and Nicobar':'Port Blair','Chhattisgarh':'Raipur','Goa':'Panaji','Bihar':'Patna','Kerala':'Thiruvananthapuram','Jharkhand':'Ranchi','Jammu and Kashmir':'Srinagar','Himachal Pradesh':'Shimla','Haryana':'Chandigarh','Lakshadweep':'Kavaratti','Karnataka':'Bangalore','Assam':'Dispur','Arunachal Pradesh':'Itanagar','Maharashtra':'Mumbai','Gujrat':'Gandhinagar',"Delhi":"New Delhi"}                                                  # Dictionary of States in India and their capitals

Capitals={'Hyderabad':'Andhra Pradesh','Imphal':'Manipur','Shillong':'Meghalaya','Aizawl':'Mizoram','Kolkata':'West Bengal','Dehradun':'Uttarakhand','Lucknow':'Uttar Pradesh','Agartala':'Tripura','Chennai':'Tamil Nadu','Jaipur':'Rajasthan','Chandigarh':'Punjab','Bhubaneswar':'Odisha','Kohima':'Nagaland','Bhopal':'Madhya Pradesh','Port Blair':'Andaman and Nicobar','Raipur':'Chhattisgarh','Panaji':'Goa','Patna':'Bihar','Thiruvananthapuram':'Kerala','Ranchi':'Jharkhand','Srinagar':'Jammu and Kashmir','Shimla':'Himachal Pradesh','Chandigarh':'Haryana','Kavaratti':'Lakshadweep','Bangalore':'Karnataka','Dispur':'Assam','Itanagar':'Arunachal Pradesh','Mumbai':'Maharashtra','Gandhinagar':'Gujrat',"New Delhi":"Delhi"}                                                # Capitals=Keys to States

randomsource=[]                                    # list of locations random source locations
randomdest=[]                                      # list of locations random destination locations
for i in range(0,1000):
    rs=randint(0,53050)                            # 53050 is the no of records in IN.txt i.e #locations
    randomsource.append([strrr[rs][2],rs])         # [name of location,index of location]
    rd=randint(0,53050)
    randomdest.append([strrr[rd][2],rd])           # [name of location,index of location]


def distance1(lat1,lon1,lat2,lon2):                # returns distance between two locations with latitude and longitudes passed to the funcion                                                    # as parameters i.e straight line distance (Great Circle Distance) 
    from math import sin, cos, sqrt, atan2, radians
    
    R = 6373.0
    lat1=radians(float(lat1))
    lon1 = radians(float(lon1))
    lon2 = radians(float(lon2))
    lat2 = radians(float(lat2))
   
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance

def nearestst1(lat,lon):                         #Gives the Probable State where the location lies.This is used to provide a list of states the route goes through in function distance4
    dist=9999
    for i in Capitals.keys():
        temp=distance1(rdictt[i][0][4],rdictt[i][0][5],lat,lon)
        if(temp<dist):
            dist=temp
            st=Capitals[i]
    return st


def nearestst(city):                                #Gives the Probable State where the location lies.This is done to remove duplicate locations
    dist=9999
    for i in Capitals.keys():
        temp=distance1(rdictt[i][0][4],rdictt[i][0][5],city[4],city[5])
        if(temp<dist):
            dist=temp
            st=Capitals[i]
    return st

randomsrc=[]                                        # contains random records with [name of location,Name of State,index no in all the records]
randomdst=[]                                        # contains random records with [name of location,Name of State,index no in all the records]

for i in randomsource: 
    state=nearestst(strrr[i[1]])
    randomsrc.append([i[0],state,i[1]])
for i in randomdest:
    state1=nearestst(strrr[i[1]])
    randomdst.append([i[0],state1,i[1]])

def areClockwise(v1, v2):                                # check whether pt v1 lies clockwise or anti clockwise w.r.t pt v2
    return ((((-1*v1[0])*v2[1]) + v1[1]*v2[0]) > 0)

def isWithinRadius(v,radiusSquared):                     # check point lies within the limits of the radius of the sector
    return (((v[0]*v[0]) + (v[1]*v[1])) <= radiusSquared)

def isInsideSector(point, center, sectorStart, sectorEnd, radius): #Checks whether point lies inside the Sector with Sector Start and Sector end marking the start and end
    x = point[0] - center[0]
    y= point[1] - center[1]
    relPoint=[x,y]
    return (not(areClockwise(sectorStart, relPoint)))and(areClockwise(sectorEnd, relPoint))and((distance1(center[0],center[1],point[0],point[1])-radius)<0)
#(isWithinRadius(relPoint,radiusSquared))

def angle1(lat1,lon1,lat2,lon2):                        # Finds the angle formed between two locations
    from math import sin, cos, sqrt, atan2, radians, degrees 
    lat1 = radians(float(lat1))
    lon1 = radians(float(lon1))
    lon2 = radians(float(lon2))
    lat2 = radians(float(lat2))
    dlong=lon2-lon1
    thetaa = atan2(sin(dlong)*cos(lat2), cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(dlong))
    return math.degrees(thetaa)


def angle(point1,point2):                               # angle formed between pts on Graph (not used)
    from math import sin, cos, sqrt, atan2, radians ,degrees
    delx=point2[0]-point1[0]
    dely=point2[1]-point1[1]
    return math.degrees(atan2(radians(delx),radians(dely)))


#print math.degrees(angle([0,0],[100,100]))

def pts(theta,r):                                       # Used to find the pts showing start and end of the sector
    return [round(r*math.cos(math.radians(theta))),round(r*math.sin(math.radians(theta)))]

                                                        #ptinsec finds whether point lies in a sector with theta as angle on either side of the                                                        # line drawn between pointc and pointe i.e source and destination with r=radius of the                                                         # sector

def ptinsec(point,pointc,pointe,r,theta):               #point=location to be checked wheter inside the sector, pointc=source location from whe                                                        #re we need to search the next location in our route, pointe= destination location, r=                                                         #radius in which the next location in route must lie, theta = angle on either side of #                                                         route
    point0=float(point[0])
    point1=float(point[1])
    pointc0=float(pointc[0])
    pointc1=float(pointc[1])
    pointe0=float(pointe[0])
    pointe1=float(pointe[1])
    point=[point0,point1]
    pointc=[pointc0,pointc1]
    pointe=[pointe0,pointe1]
    thet=angle1(pointc[0],pointc[1],pointe[0],pointe[1]) #finds angle between pts
    if ((thet-theta)>0):
        ptstart=pts(thet-theta,r)                      #Start pt of sector
    else :
        ptstart=pts(360+thet-theta,r)
    if ((thet+theta) < 360):
        ptend=pts(thet+theta,r)                        #End pt of sector
    else:
        ptend=pts(thet+theta-360,r)
   # print "Angle",thet
 #   print "Pt end",ptend
  #  print "Pt start",ptstart
    return isInsideSector(point,pointc,ptstart,ptend,r) #check whether inside sector


def distance4(src,dst,r,theta):                        #Finds the distance between source and destination for an approximate possible road route between source and destination, Also calculates connectivity and altitude travelled
    alt=[]
    connectivity=0
    countt=1
    city1=strrr[src[2]]
    city2=strrr[dst[2]]
    ptc=[city1[4],city1[5]]
    pte=[city2[4],city2[5]]
    fli=0
    fl0=0
    distan=0
    temp=0
    lat1=float(city1[4])
    lon1=float(city1[5])
    if(len(city1[16])>0):
        alt.append(city1[16])
    lat2=float(city2[4])
    lon2=float(city2[5])
#   print city1
    store=[]
    stlist=[]                                          # List of States the route goes through. It is useful to predict the Locations in the                                                          # route which may be affected by Holidays 
    temp=0
    flgr=0
    latkm=float(r)/111;
    inc=50
    tempr=r
    tinc=50
    while((ptc[0]!=pte[0])and(ptc[1]!=pte[1])):         # while source != Destination
        countt=countt+1                                 #countt is the no of locations in route
        distan=distan+temp
        if(fl0==1):
            if int(locatn[14])>50000:                   # population > 20000 increases count of connectivity
                connectivity=connectivity+1
            if(len(locatn[16])>0): 
                alt.append(locatn[16])                  # generating list of altitudes for all locations in route
            ptc=[locatn[4],locatn[5]]                   #sector center latitude longitude
            lat1=float(locatn[4])
            lat2=float(city2[4])
            lon1=float(locatn[5])
            lon2=float(city2[5])
        thet=angle1(ptc[0],ptc[1],pte[0],pte[1])        # Angle between current pt ptc and destination
        ptstart=pts(thet-theta,r)                       # Sector start pt
        ptend=pts(thet+theta,r)                         # Sector end pt
        ptss=[]
        latflag=0
        lonflag=0
        if lat1<lat2:                                   # to get a range of latitudes to check for location i.e src to destination
            s=lat1
            e=lat2
        else:
            s=lat2
            e=lat1

        if lon1<lon2:                                   # to get a range of longitudes to check for location i.e src to destination
            sl=lon1
            el=lon2
        else:
            sl=lon2
            el=lon1

        ang=angle1(ptc[0],ptc[1],pte[0],pte[1])         
        # for i in range(int(s),int(e)+1):                      
        #     if i in latlon1:       
        #         for j in latlon1[i]:
        #             pt=[j[4],j[5]]
        #             if ptinsec(pt,ptc,pte,r,theta):     # Check all points between lat1 and lat2 and append them in a list if the location lies                                                        # within the sector
        #                 ptss.append(j)    
        rangelats=int(s)
        rangelate=int(e)+1
        rangelons=int(sl)
        rangelone=int(el)+1
        latcounter=rangelats
	

        while(latcounter<=(rangelate)):
            if latcounter not in latlon1:
                latcounter+=1
                continue
            for i in latlon1[latcounter]:
                if(((int(float(i[5])))>=(rangelons-1))and((int(float(i[5])))<=rangelone)):
                    pt=[i[4],i[5]]
                    if ptinsec(pt,ptc,pte,r,theta):
                        ptss.append(i)
            latcounter+=1
       
        anglee=0
        distt=9999
        for i in ptss:                                  
            if i[2]==city2:                             # if location == destination and within sector 
                locatn=i
                break;
            if (int(i[14])>anglee) and (i[2] not in store) and not(i[2].find("State")!=-1): #and (abs(distance1(i[4],i[5],pte[0],pte[1],dictt)-temp)<distt):
                anglee=int(i[14])
                locatn=i
                if fli==0:
                    fli=1
                    r=tempr
    
                #distt=(distance1(i[4],i[5],pte[0],pte[1],dictt)-temp)
              
        if fli==0 and flgr!=1:
            r=r+inc
#           latkm=float(r)/111;
            flgr=1
            continue;
        else:
            if fli==0:
                r=r+inc
                continue;
        if(flgr==1) and (locatn[2] not in store) :
            r=tempr
            latkm=float(r)/111;
            flgr=0
            
        if locatn[2] in store:
           # tempr=r
            r=r+inc
#            latkm=float(r)/111;
            flgr=1
                
        temp=distance1(ptc[0],ptc[1],locatn[4],locatn[5])
        tempe=distance1(pte[0],pte[1],locatn[4],locatn[5])
        if tempe<(r/2):
            distan=distan+temp+tempe
            return [distan,alt,[connectivity,countt],stlist]    

        fl0=1
        store.append(locatn[2])
        sts=nearestst1(locatn[4],locatn[5])
        if sts not in stlist:                          # Appends the States the route goes through.
            stlist.append(sts)
#        if(len(store)>7):
#           store.pop(0)
     #   print locatn
      #  print distan

    return [distan,alt,[connectivity,countt],stlist]


#print len(strrr)  53051
rfloat=[]

for i in range(0,100):                                  # list of 100 random float values to calculate percentages
    rfloat.append(float(randint(0,999999))/1000000)
#print rfloat

def exponential(u):                                     # exponential distribution for generating realistic random values
    m=expval #16
    x=-m*math.log(u)
    return x

def exponential1(u):                                    # different lambda parameter used for -ve time differences (-ve side exponential)
    m=expval1
    x=-m*math.log(u)
    return -x


def loglogistic(u):
    Beta=1.0/2
    Alpha=36
    x=Beta*((1-u)/u)
    return x

def largefreq(array,maxx):
    val=sum(array)
    csum=0
    prev=0
    for i in array:
        if csum<=maxx:
            prev=csum
            csum=csum+i
        else:
            return prev
expo=[]                                                 # final list of values of transit time differences in percentage than the values generated by this program
interval=[]
frequency=[]
for i in rfloat: 
    rad=float(randint(0,999999))/1000000
    if(rad<0.09):                                        #Bernoulli Dist to provide few such values with -ve percentage i.e less time required
        expo.append(exponential1(i))
    else:
        expo.append(exponential(i))

x1=min(expo)
y1=max(expo)

def freq():                                             # just checks the frequency of percentages for approximation of m value
    # intr=10
    # table={}
    # for i in range(0,14):
    #     table[i*10]=[]
    # for i in array:
    #     if i<10:
    #         table[
    interval.append(x1)
    #for i in range(0,20):
    temp=0
    i=0
    while(temp<y1):
        temp=interval[i]+10
        interval.append(temp)
        i=i+1
    interval.append(temp+10)
    for i in range(0,len(interval)):
        temp1=0
        for j in range(0,len(expo)):
            if i==0:
                if expo[j]<interval[i]:
                    temp1=temp1+1
            else:
                if expo[j]<interval[i] and expo[j]>=interval[i-1]:
                    temp1=temp1+1
        frequency.append(temp1)
            
        
    
freq()
# print "intervals",interval 
# print "expo ",expo
# print "Length expo",len(expo)
# print "Frequency",frequency
# print "SUM Of FREQUENCY",sum(frequency)
# print "Large Freq",largefreq(frequency,75)                 # where does large amount of frequency of difference lie 
# print "MAX",max(expo)
# print "MIN",min(expo)
rdata=[]
speed=60

print "Please wait for 15-20 seconds"
import datetime, time
import random

Capitals1={'AP':'Andhra Pradesh','MN':'Manipur','ML':'Meghalaya','MZ':'Mizoram','WB':'West Bengal','UK':'Uttarakhand','UP':'Uttar Pradesh','TR':'Tripura','TN':'Tamil Nadu','RJ':'Rajasthan','PB':'Punjab','OR':'Odisha','NL':'Nagaland','MP':'Madhya Pradesh','AN':'Andaman and Nicobar','CH':'Chhattisgarh','GA':'Goa','BR':'Bihar','KL':'Kerala','JH':'Jharkhand','JK':'Jammu and Kashmir','HP':'Himachal Pradesh','HR':'Haryana','LD':'Lakshadweep','KA':'Karnataka','AS':'Assam','AR':'Arunachal Pradesh','MH':'Maharashtra','GJ':'Gujrat',"DL":"Delhi","CG":"Chandigarh","PY":"Puducherry","SK":"Sikkim","National":"ALL","DN":"Dadra and Nagar Haveli","DD":"Daman and Diu"}

Months={"January":"1","February":"2","March":"3","April":"4","May":"5","June":"6","July":"7","August":"8","September":"9","October":"10","November":"11","December":"12"}

fdx=open("HolidayList.txt"); #publicholidays.in
rec4=fdx.read()                                         
rec4=rec4.split("\n")
rec5=[]
for i in rec4:
    rec5.append(i.split("\t"))
rec5.pop(-1)
rec6=[]
for i in rec5:
    tareek=(i[0].split(" "))                             
    Month=Months[tareek[1]]
    Day=tareek[0]
    Year="2014"
    Datee=Year+"-"+Month+"-"+Day
    temp0=[]
    temp0.append(Datee)
    for j in range(1,len(i)):
        temp0.append(i[j])
    rec6.append(temp0)                            # The code above reads a list of Holidays and processes each according to required format.
#print rec6

Hol=Capitals1.keys()


rec7=[]
lenrec=len(rec6)
for i in range(0,lenrec):
    sta=rec6[i][3].split(" ")
    sta1=[]
    lensta=len(sta)
    for k in range(0,lensta):
        if sta[k]=="":
            sta.pop(k)
            #lensta=lensta-1
            k=k-1
    if rec6[i][3]=="National":
        for w in Hol:
            if w not in sta:
                sta.append(w)
    for j in sta:
#        print j
        if j== "Bank" or j=="Holiday":
            continue
        sta1.append(Capitals1[j])
    rec7.append([rec6[i][0],rec6[i][2],rec6[i][1],sta1])
#print rec7

def year_start(year):
    return time.mktime((datetime.date(year, 1, 1).timetuple()))

def rand_day(year):#yyyy-mm-dd
    stamp = random.randrange(year_start(year), year_start(year + 1))
    return datetime.date.fromtimestamp(stamp)

hundreddays=[]
for i in range(0,100):
    hundreddays.append(rand_day(2014))


def checkdate(tareekh):
    for i in rec7:
        if i[0]==tareekh:
            return i
    return -1

def disaltitude(array):                                     # Calculates the altitude travel by summing differences in altitude in route 
    travelalt=0
    differ=[]
    for i in range(0,len(array)):
        if i==0:
            differ.append(0)
        else:
            differ.append(abs(float(array[i])-float(array[i-1])))
    return sum(differ)

#def probability():
def percentage1(var,ref): 
    return (float(var)/ref)*100
def percentage(var,ref):                                    #gets the time equivalent for a percentage difference
    return ((float(var)/100)*ref)

reasdecision={"Good Road Connectivity, Free Road":0, "Within Time":24,"Altitude Travel":800,"Less road connectivity":35}

def reason(ti):                                             # Generates a reason for time difference
    
    reasonn=""
    flag9=0
    flag99=0
    if ti[0]<reasdecision["Within Time"]:                                            #if less than 1 and half day within time. Safe assumption of 1 and half day
        if ti[0]<reasdecision["Good Road Connectivity, Free Road"]:                                         # if less than approx time generated for src to dst reason given below 
            return "Good Road Connectivity, Free Road"
        else:                                                 
            return "Within Time"
    else:                                                   # if above 36 hrs possible reasons for time required
        if ti[1]>reasdecision["Altitude Travel"]:                                       # if altitude travelled i.e sum of alt differences > 800m
            reasonn=reasonn+"Altitude Travel"
            flag9=1
        if ((float(ti[2][0])/ti[2][1])*100)<reasdecision["Less road connectivity"]:             #If connectivity < 35 %
            if flag9==0:
                reasonn=reasonn+"Less road connectivity"
                flag99=1
            else:
                reasonn=reasonn+", Less road connectivity"
                flag99=1
        if (checkdate(ti[3])!=-1):
            tar=checkdate(ti[3])
            holidaystates=tar[3]
            newflag=0
            for s in holidaystates:
                if s in ti[4]:
                    newflag=1
                    break
            if newflag==1:
                tar=tar[1]
                if flag99==1 or flag9==1:
                    reasonn=reasonn+", "+tar                #Reason given is a particular Holiday affecting States which lie in the route
                else:
                    reasonn=reasonn+", "+tar                #Reason given is a particular Holiday affecting States which lie in the route 
        else:                                               #Unable to predict reason
            if flag9!=1:
                reasonn=reasonn+"Unable to predict a reason" 
    return reasonn

for i in range(0,len(randomsrc)):                           # for hundred random src,dst values generate reasons
    flagd=0
    tareekh=hundreddays[i]
    dal=distance4(randomsrc[i],randomdst[i],100,45)         # 100 is the radius of the sector, 45 is the theta on either side of the line forme                                                            #d joining source and destination points
    distanc=dal[0]
    alt=dal[1]
    alttravel=disaltitude(alt)
    randint(0,6*24)
    time=distanc/speed
    reas=reason([percentage(expo[i],time),abs(alttravel),dal[2],tareekh,dal[3]])
    if reas=="Unable to predict a reason" and str([randomsrc[i][0],randomdst[i][0]]) in newrec: 
        if newrec[str([randomsrc[0],randomdst[0]])]>20:     # 20 is the frequency of occuring of that exception in the file which is appended w                                                            #ith records showing exceptions. So all records with > frequency have the foll. rea                                                            # son
            reas="Exception frequency is high, so it may not be an exception"
            flagd=1
    if flagd==0:
        reas=reason([percentage(expo[i],time),abs(alttravel),dal[2],tareekh,dal[3]])
        #reas=reason([expo[i],abs(alttravel),dal[2]])
    else:
        flagd=0
    if reas=="Unable to predict a reason":
        newstr=""+str(randomsrc[i][0])+"\t"+str(randomdst[i][0])+"\t"+str(expo[i])+"\n"
        with open("test.txt", "a") as myfile:
            myfile.write(newstr)
    rdata.append([randomsrc[i],randomdst[i],distanc,abs(alttravel),time,percentage(expo[i],time)+time,reas,tareekh])
    #rdata.append([randomsrc[i],randomdst[i],distanc,abs(alttravel),time,percentage(expo[i],time)+time,reas])
    if i==99:
        break

def roundd(val):
    return (float(int(val*100))/100)

#print rdata
print '{: ^10}'.format("Date"),'{: ^20}'.format("SOURCE CITY"),'{: ^18}'.format("SOURCE STATE"),'{: ^20}'.format("DEST CITY"),'{: ^18}'.format("DEST STATE"),'{: ^8}'.format("DISTANCE"),'{: ^8}'.format("ALT TRAV"),'{: ^8}'.format("EST TIME"),'{: ^8}'.format("ACT TIME"),'{: ^20}'.format("REASON")
for i in rdata:
    print '{: ^10}'.format(str(i[7])),'{: ^20}'.format(str(i[0][0])), '{: ^18}'.format(str(i[0][1])),'{: ^20}'.format(str(i[1][0])),'{: ^18}'.format(str(i[1][1])),'{: ^8}'.format(str(roundd(i[2]))),'{: ^8}'.format(str(roundd(i[3]))),'{: ^8}'.format(str(roundd(i[4]))),'{: ^8}'.format(str(roundd(i[5]))),'{: ^20}'.format(str(i[6]))
