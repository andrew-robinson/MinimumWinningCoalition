from Tkinter import*
import tkMessageBox
import math



def calculate():
    partyNames = partyNamesVar.get()
    partyFilter = partyFilterVar.get()
    size = sizeVar.get()
    quota = quotaVar.get()
    names = partyNames.split(",")
    copy = []
    boolsize = sizeCheckVar.get()
    boolweight = weightCheckVar.get()
    for name in names:
        copy += [name.strip()]
    names = []
    for name in copy: 
        names += [name]
    filters = partyFilter.split(",")
    copy = []
    for name in filters:
        copy += [name.strip()]
    filters = []
    for name in copy:
        filters += [name]
    sizes = size.split(",")
    copy = []
    for x in sizes:
        copy += [int(x)]
    sizes = copy
    
    winningCoalitions = mwc(len(sizes),sizes,quota,names)
    result = ""
    if(len(winningCoalitions) > 1):
        votes = []
        members = []
        result += "Minimum Winning Coalitions: \n"
        result += "Parties | Votes | Total \n"
        minimumSized = "Minimum Size Coalitions: \nParties | Votes | Total \n"
        minimumWeight = "Minimum Weight Coalitions: \nParties | Votes | Total \n"
        filteredOut = []
        filteredWinners = []
        if(not filters == ['']):
            for coalition in winningCoalitions:
                keep = True
                for party in filters:
                    if(not party in coalition[1]):
                        keep = False
                if (keep):
                    filteredWinners += [coalition]
            winningCoalitions = filteredWinners
        for coalition in winningCoalitions:
            result += str(coalition[1]) +  " | " + str(coalition[0]) + " | " + str(total(coalition)) + "\n" 
            votes += [total(coalition)]
            members += [len(coalition)]
        votes = [min(votes)]
        members = [min(members)]
        for coalition in winningCoalitions:
            if (total(coalition) == votes[0]):
                minimumWeight += str(coalition[1]) +  " | " + str(coalition[0]) + " | " + str(total(coalition)) + "\n" 
            if (len(coalition) == members[0]):
                minimumSized += str(coalition[1]) +  " | " + str(coalition[0]) + " | " + str(total(coalition)) + "\n" 
        if(boolsize):        
            result += "\n" +minimumSized 
        if(boolweight):
            result += "\n" + minimumWeight       
    else:
        result += "Minimum Winning Coalition: \n"
        result += "Parties | Votes | Total \n"
        result += str(winningCoalitions) + str(total(winningCoalitions[0]))
        
    tkMessageBox.showinfo( "Results", result)
    
def mwc(n, sizes,q,names) :   
    votesToWin = q
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
        partySizes = []
        partyNames = []
        for i in range(0,n):             
            if (coalition[i] == 1):         
                partySizes += [sizes[i]]
                partyNames += [names[i]]
        coalition = (partySizes, partyNames)
 
        if(hasWinningVotes(coalition,votesToWin)):
            winningCoalitions += [coalition]
    copy = []   
    for coalition in winningCoalitions: 
        copy = copy + [coalition]
          
    for coalition in winningCoalitions: 
        if(not allPivotal(coalition,q)):
            copy.remove(coalition)
     
    winningCoalitions = copy 
    
    return winningCoalitions

def allPivotal(coalition, q):
    sizes = coalition[0]
    size = sum(sizes)
    for num in sizes:
        if(size - num > q):
            return False        
    return True       
    
def hasWinningVotes(coalition,q):
    votes = sum(coalition[0])
    if votes >= q:
        return True
    return False
def total(coalition):
    total = 0
    total = sum(coalition[0])
    return total
def cleanup(coalition):
    copy = coalition
    sizes = copy[0]
    names = copy[1]
    indices = []
    for i in range(0,len(sizes)):
        if sizes[i] == (-1):
            indices += [i]
    indices.sort()
    indices.reverse()
    for i in indices:
        sizes.pop(i)
        names.pop(i)
    copy = (sizes,names)
    return copy
    

###MAIN###
root = Tk()
root.title("Minimum Winning Coalition Calculator by Andrew Robinson")
mainframe = Frame(root)
mainframe.grid()

partyNamesVar = StringVar()
partyNamesVar.set("Enter party names in a comma separated list")
sizeVar = StringVar()
sizeVar.set("Enter party sizes (in the same positions as names above) in a comma separated list" )
quotaVar = IntVar()
quotaVar.set(int(0))
partyFilterVar = StringVar()
partyFilterVar.set("Enter 0 or more party names in a coma separated list to see only coalitions which contain all parties in this list (clear this text and leave it blank to see all possible coalitions)")


titleLabel = Label (mainframe, text = "Minimum Winning Coalition Calculator", font = ("Arial", 20, "bold"), justify = CENTER)
titleLabel.grid(row = 1, column = 1, columnspan = 3, pady = 10, padx = 20)

nameLabel = Label (mainframe, text = "Party Names: ", font = ("Arial", 16), fg = "black")
nameLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)

sizeLabel = Label (mainframe, text = "Party Sizes: ", font = ("Arial", 16), fg = "black")
sizeLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)

nameEntry = Entry (mainframe, width = 100, bd = 5, textvariable = partyNamesVar)
nameEntry.grid(row = 2, column = 1, pady = 10, sticky = NW, padx = 160 )

sizeEntry = Entry (mainframe, width = 100, bd = 5, textvariable = sizeVar)
sizeEntry.grid(row = 3, column = 1, pady = 10, sticky = NW, padx = 160 )

quotaLabel = Label (mainframe, text = "Quota: ", font = ("Arial", 16), fg = "black")
quotaLabel.grid(row = 4, column = 1, pady = 10, sticky = NW)

quotaEntry = Entry (mainframe, width = 10, bd = 5, textvariable = quotaVar)
quotaEntry.grid(row = 4, column = 1, pady = 10, sticky = NW, padx = 160 )

filterLabel = Label (mainframe, text = "Filtered Parties: ", font = ("Arial", 16), fg = "black")
filterLabel.grid(row = 5, column = 1, pady = 10, sticky = NW)

filterEntry = Entry (mainframe, width = 150, bd = 5, textvariable = partyFilterVar)
filterEntry.grid(row = 5, column = 1, pady = 10, sticky = NW, padx = 160 )

sizeCheckVar = IntVar()
weightCheckVar = IntVar()

c1 = Checkbutton(root, text="Include Minimum Size Coalition Results", variable=sizeCheckVar,onvalue = 1, offvalue=0)
c1.grid(row=6, column=0)

c2 = Checkbutton(root, text="Include Minimum Weight Coalition Results", variable=weightCheckVar,onvalue = 1, offvalue=0)
c2.grid(row=7, column=0)

calculateButton =Button (mainframe, text = "Calculate", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = calculate)
calculateButton.grid(row = 8, column = 1, ipady = 8, ipadx = 12, pady = 5, padx = 55)


root.mainloop()