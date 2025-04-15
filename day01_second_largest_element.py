class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr) # finding the length of the array
        if n<2:
            return -1 # because for only single or no element how can a largest be present
        first = second = float('-inf') # storing the min largest value of negative infinity
        for num in arr: # iterating through the array
            if num > first: # if the current index num is greater then than than - infinity or prestored no here initially, we will do following two operations 
                second = first
                first = num
            elif num>second and num!=first: # if current index number is greater than secnd and should be not equal to the first as no identical number can be first and second. Also its very obvious num cannot be greater than first if elif is executing
                second = num
        
        if second == float('-inf'): # after complete loop execution if second is equal to - infinity that means no second largest no exist thus we return -1
            return -1
        else :  return second # otherwise we return second if it exists
