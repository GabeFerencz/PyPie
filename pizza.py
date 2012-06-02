#!/usr/bin/env python
#Gabe Ferencz

class Pie(object):
    def __init__(self,length,rectangle=0,cost=0):
        self.cost = cost
        self.length = length
        self.rectangle = rectangle
        self.area = PizzaArea(length)
        
        self.avg_diam = 16.0
        self.avg_slices = 8.0
        # Calories based on average of NYC pizza places - see bottom of script
        self.avg_cals = 505
        self.cals_per_ounce = 68.748
        
        area_ratio = self.area / PizzaArea(self.avg_diam)
        self.calories = area_ratio*self.avg_slices*self.avg_cals
        
        avg_slice_area = PizzaArea(self.avg_diam)/self.avg_slices
        self.num_avg_slices = self.area/avg_slice_area
        
        #self.cost_per_sq_in = self.cost/self.area
            
        self.slices_per_person = 2
        self.CutPieInto(self.avg_slices)

        self.weight_in_oz = self.calories / float(self.cals_per_ounce)

    def __repr__(self):
        if self.rectangle == 0:
            size_str = "%d\" pizza"%self.length
            slice_str = "%d slices"%self.slices
        else:
            size_str = "%d\" x %d\" pizza"%(self.length,self.rectangle)
            slice_str = "%d pieces"%self.slices
        wcal_str = "%d calories"%self.calories
        scal_str = "%d calories each"%self.cals_per_slice

        str1 = size_str + " (%s)"%wcal_str
        str2 = slice_str + " (%s)"%scal_str
        return ', '.join([str1,str2]) + "."
    
    def CutPieInto(self, slices):
        self.slices = slices
        self.feeds = slices / float(self.slices_per_person)
        self.cals_per_slice = self.calories / float(slices)
        self.cost_per_slice = self.cost / float(slices)

    def UpdateCostByPie(self,cost):
        self.cost = cost
        self.cost_per_slice = cost / float(self.slices)
        self.cost_per_sq_in = cost / float(self.area)
    
    def UpdateCalsBySlice(self, cals):
        self.cals_per_slice = cals
        self.calories = cals*self.slices

    def UpdateCalsBySliceWeight(self,ounces):
        self.cals_per_slice = ounces * self.cals_per_ounce
        self.calories = self.cals_per_slice * self.slices
        self.weight_in_oz = ounces * self.slices
    
    def UpdateCalsByPie(self, cals):
        self.calories = cals
        self.cals_per_slice = cals / float(self.slices)
    
    def UpdateFromRoundSliceDim(self, chord):
        from math import asin, pi
        slice_angle = 2*asin((chord/2.0)/self.length)
        slice_frac = slice_angle / pi
        slice_area = self.area * slice_frac
        est_slices_in_pie = int(round(1.0/(2*slice_frac))*2)
        CutPieInto(est_slices_in_pie)
    
    def PrintNumAvgSlices(self):
        str = "(%d\" diameter / %d slices)"%(self.avg_diam,self.avg_slices)
        print("%.1f average-sized %s \"slices\"."%(self.num_avg_slices,str))
        print("$%.2f per average-sized \"slice\"."%(self.cost / float(self.num_avg_slices)))

    def PrintCostPerSlice(self):
        print("$%.2f per 1/%d slice."%(self.cost_per_slice,self.slices))
    
    def PrintNumPeopleFed(self):        
        feeds_str = "Feeds %.1f people "%self.feeds        
        cal_str = "(%d calories, "%(self.cals_per_slice*self.slices_per_person)
        portion_str = "%d slices each)."%self.slices_per_person
        print(feeds_str + cal_str + portion_str)
    
    def PrintCaloriesInPie(self):
        print("%d calories in whole pie."%self.calories)

    def PrintCaloriesInSlice(self):
        print("%d calories per %dth."%(self.cals_per_slice,self.slices))

    def PrintVarVals(self):
        for (k,v) in zip(vars(self).keys(),vars(self).values()):
            print '{0} = {1}'.format(k,v)
        
    def PrintStats(self):
        self.PrintNumAvgSlices()
        #self.PrintVarVals()
        self.PrintCostPerSlice()
        self.PrintNumPeopleFed()
        self.PrintCaloriesInPie()
        self.PrintCaloriesInSlice()
        
    
def PizzaArea(length,rectangle=0):
    from math import pi
    if rectangle == 0:
        r = length/2.0
        area = pi*r*r
    else:
        area = length*rectangle    
    return area

def DecodeInput(ins):
    if len(ins) == 3:
        l = int(ins[1])
        w = 0
        c = float(ins[2])
        print("%d\" pizza for $%.2f:"%(l,c))
    elif len(ins) == 4:
        l = int(ins[1])
        w = int(ins[2])
        c = float(ins[3])
        print("%d\" x %d\" sheet pizza for $%.2f:"%(l,w,c))
    else:
        size = map(int, raw_input("Pizza Size:  ").split())
        l = size[0]
        if len(size) == 1:
            w = 0
        else:
            w = size[1]
        c = float(raw_input("Pizza Cost:  "))
    return Pie(length=l,rectangle=w,cost=c)

if __name__ == "__main__":
    import sys
    pie = DecodeInput(sys.argv)
    pie.PrintStats()
    

# >>> cals = [613,552,577,539,610,482,485,502,462,392,366,481]
# >>> cals_per_ounce = [613/8.5,552/7.5,577/8.0,539/7.25,610/10.5,482/7.0,485/7.0,502/7.0,462/7.25,392/5.5,366/5.25,481/8.0]
# >>> def average(list):
# ... 	return float(sum(list))/len(list)
# ... 
# >>> average(cals)
# 505.08333333333331
# >>> average(cals_per_ounce)
# 68.748000542954898
# >>> 

# Calorie Info from 1994 NYTimes article
#http://www.nytimes.com/1994/09/14/garden/eating-well-fat-by-the-slice.html?sec=health

#cals = 505.08
#cals_per_ounce = 68.748

# Ray's of Greenwich Village 465 Avenue of the Americas (at 11th Street) 
# Weight in ounces -- 8 1/2 
# Calories -- 613 
# Fat in grams -- 25 

# Mama's Great Pan Pizza 2565 Broadway (near 96th Street) 
# Weight in ounces -- 7 1/2 
# Calories -- 552 
# Fat in grams -- 24 

# Famous Original Ray's Pizza 204 Ninth Avenue (at 23d Street) 
# Weight in ounces -- 8 
# Calories -- 577 
# Fat in grams -- 21 

# Famous Famiglia 876 Lexington Avenue (near 65th Street) 
# Weight in ounces -- 7 1/4 
# Calories -- 539 
# Fat in grams -- 18 

# Ray Bari 930 Third Avenue (at 56th Street) (pizza labeled "healthy") 
# Weight in ounces -- 10 1/2 
# Calories -- 610 
# Fat in grams -- 17 

# Two Boots to Go 36 Avenue A (near Third Street) 
# Weight in ounces -- 7 
# Calories -- 482 
# Fat in grams -- 17 

# Ray Bari 930 Third Avenue (at 56th Street) 
# Weight in ounces -- 7 
# Calories -- 485 
# Fat in grams -- 16 

# Sal and Carmine 2671 Broadway (between 101st and 102d streets) 
# Weight in ounces -- 7 
# Calories -- 502 
# Fat in grams -- 15 

# Ben's 123 Macdougal Street (at Third Street) 
# Weight in ounces -- 7 1/4 
# Calories -- 462 
# Fat in grams -- 14 

# California Pizza Oven 122 University Place (near 14th Street) 
# Weight in ounces -- 5 1/2 
# Calories -- 392 
# Fat in grams -- 12 

# Pintaile's Pizza 26 East 91st Street (near Madison Avenue) 
# Weight in ounces -- 5 1/4 
# Calories -- 366 
# Fat in grams -- 12 

# Famous Original Ray's 204 Ninth Avenue (at 23d Street) (Garden De-Lite pizza) 
# Weight in ounces -- 8 
# Calories -- 481 
# Fat in grams -- 11
