from typing import List
class ContainsDublicate:
    def contains_dublicate(self, nums:List[int]) -> bool:
        # hashSet = set()
        hashmap = {}

        # for num in nums:
        #     if num in hashSet:
        #         return True
        #     hashSet.add(num)

        for num in nums:
            if num in hashmap:
                return True
            
            else:
                hashmap[num] = True
        
        return False

if __name__ == "__main__":
    list_ = [1,2,3,4,6]
    cdObj = ContainsDublicate();
    result = cdObj.contains_dublicate(list_);
    print(result)


