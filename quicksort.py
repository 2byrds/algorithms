import random
import math
import time
import statistics

class QuickSort:
    def find_left_swap(self,list,left,pivot,max,num_ops):
        while list[left] < pivot:
            if left+1 == max:
                return None 
            left+=1
            num_ops+=1

        print('New left is: ', left)
        return left

    def find_right_swap(self,list,right,pivot,min,num_ops):
        while list[right] >= pivot:
            if right-1 == min:
                return None 
            right-=1
            num_ops+=1

        print('New right is: ', right)
        return right

    def swap(self,list,l_index,r_index):
        tmp = list[l_index]
        list[l_index] = list[r_index]
        list[r_index] = tmp
        print('Swapped ', tmp, ' with ', list[l_index])

    def sort(self,list):
        start = time.time()
        end = time.time()
        num_ops = 0
        if list == None or len(list)==0:
            return
        else:
            left = 0
            right = len(list)-1
            self.quicksort(list,left,right,num_ops,self.get_pivot(list))
        total = end - start
        print('Total time of quicksort: ',total)
        print('New list: ',list)
        return num_ops

    def quicksort(self,list,left,right,num_ops,pivot):
        print(list,'/nleft: ', left, ', right: ',right)
        orig_left = left
        orig_right = right
        while right != None and left != None:
            if list[left] < pivot and list[right] >= pivot:
                self.swap(list,left,right)
                num_ops+=1
            left = self.find_left_swap(list,left,pivot,right-1,num_ops)
            right = self.find_right_swap(list,right,pivot,left+1,num_ops)

        left_half = int((orig_left+left)/2)
        if orig_left < left_half:
            self.quicksort(list,orig_left,left_half,num_ops,pivot)
        if left_half < left:
            self.quicksort(list,left_half,left,num_ops,pivot)
            
        right_half = int((orig_right+right)/2)
        if orig_right > right_half:
            self.quicksort(list,right_half,orig_right,num_ops,pivot)
        if right_half < right:
            self.quicksort(list,right,right_half,num_ops,pivot)

    def get_pivot(self,list):
        pivot=None
        if not list == None and not len(list)==0:
            sample = []
            for _ in range(10):
                sample.append(list[random.randint(0,len(list)-1)])
            pivot = statistics.mean(sample)
        print('pivot is: ', pivot)
        return pivot

list = []
qs = QuickSort()
num_ops = qs.sort(list)

size = 10
for i in range(size):
    list.append(random.randint(0,size))
print(list)

num_ops = qs.sort(list)
