import math
#mwc takes an integer n (number of parties)
#a list ([integer]) of party size
#e.g. [1,2,3,4,5]
#and a quota, q, which is the number
#of votes needed to pass a measure
def mwc(n, sizes,q) :   
     votesToWin = q
     first = True
     coalitions = []                       
     winningCoalitions =[]                 
     minSizes = []                         
     for i in range(0,int(math.pow(2,n))): 
          coalitions = coalitions + [[0]*n]          
     for j in range(0,n ):                 
          switch = len(coalitions) / (math.pow(2,j + 1))  
          num = 1                         
          counter = 0                      
          for i in range(0,len(coalitions)) : 
               if (counter < switch):      
                    coalitions[i][j] = num
                    counter +=1
                    
               else:                      
                    num = num * (-1)
                    coalitions[i][j] = num
                    counter = 1
                    
     for coalition in coalitions:   
          size = 0
          for i in range(0,n):             
               if (coalition[i] == 1):         
                    coalition[i] = sizes[i]
 
          coalition = filter(lambda x: x != (-1),coalition)
          if(sum(coalition) >= votesToWin):
               winningCoalitions = winningCoalitions + [coalition]
     copy = []   
     for coalition in winningCoalitions: 
          copy = copy + [coalition]
          
     for coalition in winningCoalitions: 
          if(not allPivotal(coalition,q)):
               copy.remove(coalition)
     
     winningCoalitions = copy 

          
     if(len(winningCoalitions) > 1):
          votes = []
          members = []
          print "Multiple Minimum Winning Coalitions: "
          for coalition in winningCoalitions:
               print"Coalition, votes, size : ", coalition , sum(coalition), len(coalition)
               votes += [sum(coalition)]
               members += [len(coalition)]
          votes = [min(votes)]
          members = [min(members)]
          for coalition in winningCoalitions:
               if (sum(coalition) == votes[0]):
                    print "Minimum weight coalition : " , coalition, sum(coalition)
               if (len(coalition) == members[0]):
                    print "Minimum size coalition : " , coalition, len(coalition)
                    
     else:
          print"Minimum winning coalition, votes, size: ", winningCoalitions, sum(coalition), len(coalition)


def allPivotal(coalition, q):
     size = sum(coalition)
     for num in coalition:
          if(size - num > q):
               return False        
     return True
     