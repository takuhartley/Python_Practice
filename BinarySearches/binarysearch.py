random_array_with_num = [1,3,9,7,5,2,8,4,6]


class Binary_Search_And_Say:
    def __init__(self, test_array, number_in_question, found=False):
        self.test_array = test_array
        self.number_in_question = number_in_question

    def binary_search_dis_shit(self):
        start_point = 0
        end_point = len(self.test_array) -1
        while(start_point <= end_point and not self.found):
            mid = (start_point + end_point)//2
            print('The current mid point is ', mid)
            if self.test_array[mid] == self.number_in_question:
                found = True
            else:
                if self.number_in_question < self.test_array[mid]:
                    end_point = mid - 1
                    print('The new end point is ', end_point)
                else:
                    start_point = mid + 1
                    print('The new end point is ', start_point)
        return found

    def coolwords(self):
        if self.found == True:
            print('THE ITEM WAS FOUND CONGRATS')
        else:
            print('WHERE IS THE ITEM!?')

Binary_Search_And_Say.test_array = random_array_with_num
print(Binary_Search_And_Say.test_array)
