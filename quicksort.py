import random
import math
import time
import statistics

__verbose__=False
def vprint(*args, **kwargs):
        print(*args, **kwargs) if __verbose__ else lambda *a, **k: None

class QuickSort:
    def find_left_swap(self,list,left,pivot,num_ops):
        while list[left] <= list[pivot] and left < pivot:
            left+=1
            num_ops+=1

        vprint('find_left_swap() New left index is: ', left, ' with value: ',list[left])
        return left

    def find_right_swap(self,list,right,pivot,num_ops):
        while list[right] >= list[pivot] and right > pivot:
            right-=1
            num_ops+=1

        vprint('find_right_swap() New right index is: ', right, ' with value: ',list[right])
        return right

    def swap(self,list,l_index,r_index):
        tmp = list[l_index]
        list[l_index] = list[r_index]
        list[r_index] = tmp
        vprint('swap() Swapped ', tmp, ' with ', list[l_index])

    def sort(self,list):
        start = time.time()
        end = time.time()
        num_ops = 0

        print('\n\nsort() Unsorted list: ',list)
        if list == None or len(list)==0:
            return
        else:
            left = 0
            right = len(list)-1
            self.quicksort(list,left,right,num_ops)
        total = end - start
        print('sort() Total time of quicksort: ',total)
        print('sort() Sorted list: ',list)
        print('sort() Num ops: ',num_ops)
        return num_ops

    def quicksort(self,list,left,right,num_ops,pivot_index=None):

        #non-recusive cases
        if right-left < 1:
            return
        elif right-left == 1:
            if list[right] < list[left]:
                self.swap(list,left,right)
            return

        if pivot_index == None:
            pivot_index=self.get_pivot(list,left,right)

        vprint('quicksort() ', list[left:right+1],'/nleft: ', left, ', right: ',right, ', pindex: ',pivot_index)

        orig_left = left
        orig_right = right

        while left < right:
            left = self.find_left_swap(list,left,pivot_index,num_ops)
            right = self.find_right_swap(list,right,pivot_index,num_ops)
            if list[left] >= list[pivot_index] and list[right] <= list[pivot_index]:
                self.swap(list,left,right)
                num_ops+=1

        self.quicksort(list,orig_left,pivot_index-1,num_ops)
        self.quicksort(list,pivot_index,orig_right,num_ops)  

    def get_pivot(self,list,left,right):
        pindex=None
        if not list == None and not len(list)==0:
            pindex = int((left+right)/2)
            vprint('get_pivot() Pindex=',pindex)
            vprint('get_pivot() Pivot value is: ', list[pindex])
        else:
            vprint('get_pivot() Pindex=',pindex)
        return pindex


qs = QuickSort()
list=[0, 0, 0, 1, 2, 0, 5, 6, 5, 9]
#__verbose__ = True
num_ops = qs.sort(list)

list=[6,5,4,3,2,1]
num_ops = qs.sort(list)

size = 10
list = []
for i in range(size):
    list.append(i)
num_ops = qs.sort(list)

list = []
for i in reversed(range(size)):
    list.append(i)
num_ops = qs.sort(list)

list = []
for i in range(size):
    list.append(random.randint(0,i))
num_ops = qs.sort(list)