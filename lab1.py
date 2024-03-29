
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
       raise ValueError
   max = int_list[0]
   for i in int_list:
       if max < i:
           max = i
   return max
   pass

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
       raise ValueError
   if (len(int_list)==0):
       return []
   last = int_list[-1]
   return([last] + reverse_rec(int_list[:-1]))


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None:
       raise ValueError
   if not int_list:
       return None
   midPoint = (high+low)//2
   if low == high:
       return None
   if int_list[midPoint] == target:
       return midPoint
   if int_list[high] == target:
       return high
   if target < int_list[midPoint]:
       return bin_search(target,low,midPoint-1,int_list)
   if target > int_list[midPoint]:
       return bin_search(target,midPoint+1,high,int_list)
   else:
       return None


   pass
