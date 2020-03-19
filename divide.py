import csv
import re
times=20000

all_list=[]

empty_list=[]

noneEmp_list=[]
noneEmp_list_mid=[]
noneEmp_list_big=[]



#with open('testCsv.csv',newline='') as csvfile:
with open('email.csv',newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        
        if(times<=0):
            break
        times-=1
        
        
        if('@' in row[1]):
            #print(row[1])
            all_list.append(row)

            if(('{' in row[1])):
# =============================================================================
#                 noneEmp_list_big.append(row)
# =============================================================================

                tempList=re.findall(r'([{\,\w\.-}]+@[a-z\.-]+)', row[1])
                for eachEmail in tempList:
                    noneEmp_list_big.append([row[0],eachEmail])
                
            else:
                if(('(' in row[1]) ):
                    
# =============================================================================
#                     noneEmp_list_mid.append(row)
# =============================================================================
                    
                    tempList=re.findall(r'([\w\.-]+@[\w\.-]+)', row[1])
                    for eachEmail in tempList:
                        noneEmp_list_mid.append([row[0],eachEmail])
    # =============================================================================
    #                 tempList=re.findall(r'([\w\.-]+@[\w\.-]+)', row[1])
    #                 for eachEmail in tempList:
    #                     noneEmp_list_mid.append([row[0],eachEmail])
    # =============================================================================
                else:
                    tempList=re.findall(r'[\w\.-]+@[\w\.-]+', row[1])
                    for eachEmail in tempList:
                        noneEmp_list.append([row[0],eachEmail])
        else:
            empty_list.append(row)



        #if(row[1]== None): print('NULL')

print('\nempty_list:\n')
for item in empty_list:
    print(item)

print('\nnoneEmp_list:\n')
for item in noneEmp_list:
    print(item)

print('\nnoneEmp_list_big:\n')
for item in noneEmp_list_big:
    print(item)

print('\nnoneEmp_list_mid:\n')
for item in noneEmp_list_mid:
    print(item)

with open('noneEmp_list.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in noneEmp_list:
        try:
            writer.writerow(row)  
        except:
            pass

with open('noneEmp_list_big.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in noneEmp_list_big:
        try:
            writer.writerow(row)  
        except:
            pass

with open('noneEmp_list_mid.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in noneEmp_list_mid:
        try:
            writer.writerow(row)  
        except:
            pass



#    print(len(rows))
# =============================================================================
#     print(rows[0])
#     print(rows[1])
# =============================================================================
