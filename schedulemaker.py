import pandas as pd
import random




##data = [[3307, 'ANL-301', 'Kilinc', 'MW', 2.3, 3.45],[3308, 'ANL-301', 'Kilinc', 'MW', 4, 5.15],
##        [2409, 'ENG-210', 'Lund', 'TTH', 2.3, 3.45], [3462, 'ENG-210', 'Burns', 'TTH', 8.3, 9.15],
##        [3292, 'MGT-301', 'Mazza', 'MW', 1.0, 2.15], [3293, 'MGT-301', 'Mazza', 'MW', 2.3, 3.45],
##        [2714, 'REL-200', 'Reeder', 'MW', 4, 5.15],[2715, 'REL-200', 'Reeder', 'MW', 5.3, 6.45],
##        [3178, 'FIN-301', 'Bhuyan', 'MW', 4, 5.15]]

data = [[3307, 'ANL-301', 'Kilinc', 'MW', 2.3, 3.45],[3308, 'ANL-301', 'Kilinc', 'MW', 4, 5.15],
        [2409, 'ENG-210', 'Lund', 'TTH', 12, 1], [3462, 'ENG-210', 'Burns', 'TTH', 8.3, 9.15],
        [3292, 'MGT-301', 'Mazza', 'TTH', 1.0, 2.15], [3293, 'MGT-301', 'Mazza', 'TTH', 2.3, 3.45],
        [2714, 'REL-200', 'Reeder', 'MW', 4, 5.15],[2715, 'REL-200', 'Reeder', 'MW', 5.3, 6.45],
        [3178, 'FIN-301', 'Bhuyan', 'MW', 4, 5.15], [3207, 'MIS-201', 'Han', 'TTH', 1, 2.3],
        [3178, 'FIdN-301', 'Bhuyan', 'TTH', 4, 5.15]]

classes_df = pd.DataFrame(data, columns=['Syn', 'Class', 'Prof', 'Day', 'Start', 'End'], dtype=float)
##print(classes_df[0:1])

schedules = 0
classes_number = 0
##print(len(data))

##random_number = random.sample(range(8), 8)
random_number = random.sample(range(len(data)), len(data))
print(random_number)
c = classes_df[5:6]
print(c)




schedule = pd.DataFrame(columns=['Syn', 'Class', 'Prof', 'Day', 'Start', 'End'])

i = 0
counter = 0
classes = len(schedule)

##schedule = schedule.append(classes_df[random_number[0]:random_number[0]+1], ignore_index=True)
##print(schedule.head())

#make 3 schedules

    #use 5 classes
while len(schedule) <= 4:
    #random number list to pick classes 

##            print(random_number)
##            print(counter)
    if classes_number == len(data):
        break
    
    

    #if nothing in schedule
    if len(schedule) == 0:
        class_id = classes_df[random_number[classes_number]:random_number[classes_number]+1]
        schedule = schedule.append(class_id, ignore_index=True)
##                print(schedule.head())
        classes_number += 1

        continue

    #if 1 class in schedule
    if len(schedule) == 1:
        

        #get new class data
        class_id = classes_df[random_number[classes_number]:random_number[classes_number]+1]
        print('','classid',class_id, '')
        start = class_id.Start.item()
        end = class_id.End.item()
        day = class_id.Day.item()
        #get old classes data
        class1 = schedule[0:1]

##                print(class_id)
##                print(class1)

        #resort for errors
##                class1.reset_index(drop=True)
##                class_id.reset_index(drop=True)
        
        start1 = class1.Start.item()
        end1 = class1.End.item()
        day1 = class1.Day.item()
        
        if start < 7 :
            start+=12
        if end < 7:
            end+=12
            
        if start1 < 7:
            start1+=12
        if end1 < 7:
            end1+=12

##        print(day)
##        print(day1)
##        if day == day1:
##            print(day)
##            print(day1)
##            print('true')
##        else:
##            print('false')
            
        
        if class_id.Class.item() != class1.Class.item():
            if start1 > start and end1 >= start or start1 < start and end1 <= start or day != day1:
                
            
                schedule = schedule.append(class_id, ignore_index=True)
##                print(schedule.head())
                
                i += 1
##                print(class_id)
        classes_number+=1
        print('')
        print('schedule', schedule)
        print('')
        continue
        
    if len(schedule) == 2:

        #get new class data
        class_id = classes_df[random_number[classes_number]:random_number[classes_number]+1]
        print('','classid',class_id, '')
        start = class_id.Start.item()
        end = class_id.End.item()
        day = class_id.Day.item()
        #get old classes data
        class1 = schedule[0:1]
        class2 = schedule[1:2]

##                print(class_id)
##                print(class1)

        #resort for errors
##                class1.reset_index(drop=True)
##                class_id.reset_index(drop=True)
        
        start1 = class1.Start.item()
        end1 = class1.End.item()
        day1 = class1.Day.item()

        start2 = class2.Start.item()
        end2 = class2.End.item()
        day2 = class2.Day.item()

        
        if start < 7 :
            start+=12
        if end < 7:
            end+=12
            
        if start1 < 7:
            start1+=12
        if end1 < 7:
            end1+=12

        if start2 < 7:
            start2+=12
        if end2 < 7:
            end2+=12
            
        
        if class_id.Class.item() != class1.Class.item():
            if start1 > start and end1 > start or start1 < start and end1 < start or day != day1:
                
                    if class_id.Class.item() != class2.Class.item():
                        if start2 > start and end2 > start or start2 < start and end2 < start or day != day2:
                            
##                        if start1 < start and end1 < start:
                
                                schedule = schedule.append(class_id, ignore_index=True)
##                                print(schedule.head())
                    
                    
##                print(class_id)
        classes_number+=1
        print('')
        print('schedule', schedule)
        print('')
        continue


    if len(schedule) == 3:

        #get new class data
        class_id = classes_df[random_number[classes_number]:random_number[classes_number]+1]
        print('','classid',class_id, '')
        start = class_id.Start.item()
        end = class_id.End.item()
        day = class_id.Day.item()
        #get old classes data
        class1 = schedule[0:1]
        class2 = schedule[1:2]
        class3 = schedule[2:3]

##                print(class_id)
##                print(class1)

        #resort for errors
##                class1.reset_index(drop=True)
##                class_id.reset_index(drop=True)
        
        start1 = class1.Start.item()
        end1 = class1.End.item()
        day1 = class1.Day.item()

        start2 = class2.Start.item()
        end2 = class2.End.item()
        day2 = class2.Day.item()

        start3 = class3.Start.item()
        end3 = class3.End.item()
        day3 = class3.Day.item()
        
        if start < 7 :
            start+=12
        if end < 7:
            end+=12
            
        if start1 < 7:
            start1+=12
        if end1 < 7:
            end1+=12

        if start2 < 7:
            start2+=12
        if end2 < 7:
            end2+=12

        if start3 < 7:
            start3+=12
        if end3 < 7:
            end3+=12
            
        
        if class_id.Class.item() != class1.Class.item():
            if start1 > start and end1 > start or start1 < start and end1 < start or day != day1:
                
                    if class_id.Class.item() != class2.Class.item():
                        if class_id.Class.item() != class3.Class.item():
                            if start2 > start and end2 > start or start2 < start and end2 < start or day != day2:
                                
                                    if start3 > start and end3 > start or start3 < start and end3 < start or day != day3:
                                        
##                        if start1 < start and end1 < start:
                    
                                            schedule = schedule.append(class_id, ignore_index=True)
##                                            print(schedule.head())
                    
##                print(class_id)
        classes_number+=1
        print('')
        print('schedule', schedule)
        print('')
        continue

    if len(schedule) == 4:

            #get new class data
            class_id = classes_df[random_number[classes_number]:random_number[classes_number]+1]
            print('','classid',class_id, '')
            start = class_id.Start.item()
            end = class_id.End.item()
            day = class_id.Day.item()
            #get old classes data
            class1 = schedule[0:1]
            class2 = schedule[1:2]
            class3 = schedule[2:3]
            class4 = schedule[3:4]

##                print(class_id)
##                print(class1)

            #resort for errors
##                class1.reset_index(drop=True)
##                class_id.reset_index(drop=True)
            
            start1 = class1.Start.item()
            end1 = class1.End.item()
            day1 = class1.Day.item()

            start2 = class2.Start.item()
            end2 = class2.End.item()
            day2 = class2.Day.item()

            start3 = class3.Start.item()
            end3 = class3.End.item()
            day3 = class3.Day.item()

            start4 = class4.Start.item()
            end4 = class4.End.item()
            day4 = class4.Day.item()
            
            if start < 7 :
                start+=12
            if end < 7:
                end+=12
                
            if start1 < 7:
                start1+=12
            if end1 < 7:
                end1+=12

            if start2 < 7:
                start2+=12
            if end2 < 7:
                end2+=12

            if start3 < 7:
                start3+=12
            if end3 < 7:
                end3+=12

            if start4 < 7:
                start4+=12
            if end4 < 7:
                end4+=12
                
            
            if class_id.Class.item() != class1.Class.item():
                if start1 > start and end1 > start or start1 < start and end1 < start or day!=day1:
                    
                        if class_id.Class.item() != class2.Class.item():
                            if class_id.Class.item() != class3.Class.item():
                                if class_id.Class.item() != class4.Class.item():
                                    if start2 > start and end2 > start or start2 < start and end2 < start or day!=day2:
                                        
                                            if start3 > start and end3 > start or start3 < start and end3 < start or day!=day3:
                                                
                                                    if start4 > start and end4 > start or start4 < start and end4 < start or day!=day4:
                                                        
        ##                        if start1 < start and end1 < start:
                            
                                                            schedule = schedule.append(class_id, ignore_index=True)
##                                                            print(schedule.head())
                        
##                print(class_id)
            classes_number+=1
            print('')
            print('schedule', schedule)
            print('')
            continue
    
    print(classes_number)
    counter += 1
          
schedule = schedule.sort_values('Start', ascending=True)
schedule = schedule.sort_values('Day')

mw = schedule[schedule.Day != 'TTH']
mw = mw.reset_index(drop=True)
tth = schedule[schedule.Day != 'MW']
tth = tth.reset_index(drop=True)

mwAbove = pd.DataFrame(columns=['Syn', 'Class', 'Prof', 'Day', 'Start', 'End'])
mwBelow = pd.DataFrame(columns=['Syn', 'Class', 'Prof', 'Day', 'Start', 'End'])

tthAbove = pd.DataFrame(columns=['Syn', 'Class', 'Prof', 'Day', 'Start', 'End'])
tthBelow = pd.DataFrame(columns=['Syn', 'Class', 'Prof', 'Day', 'Start', 'End'])


##print(mwAbove)

##print(mw.index)schedule = schedule.append(class_id, ignore_index=True)

for index, row in mw.iterrows():
    if row.Start > 7:
        mwAbove = mwAbove.append(row)
    else:
        mwBelow = mwBelow.append(row)
        
mwAbove = mwAbove.sort_values('Start', ascending=True)
mwBelow = mwBelow.sort_values('Start', ascending=True)

for index, row in tth.iterrows():
    if row.Start > 7:
        tthAbove = tthAbove.append(row)
    else:
        tthBelow = tthBelow.append(row)
        
tthAbove = tthAbove.sort_values('Start', ascending=True)
tthBelow = tthBelow.sort_values('Start', ascending=True)


mwsorted = pd.concat([mwAbove, mwBelow])

tthsorted = pd.concat([tthAbove, tthBelow])

sortedSchedule = pd.concat([mwsorted, tthsorted])
sortedSchedule = sortedSchedule.reset_index(drop=True)
print('')
print('')
print('')
print('')
print(sortedSchedule)


##print('')
##print('')
##print('')
##print('')
##print(schedule)
           
  
