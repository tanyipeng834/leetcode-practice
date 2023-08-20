class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count =0
        if len(flowerbed) ==1:
            if flowerbed[0] == 0:
                count =1
            else: 
                count =0
            
        else:
            for i in range(len(flowerbed)):
                if i==0:
                    if flowerbed[i]==0 and flowerbed[i+1]==0:
                        flowerbed[i]=1
                        count+=1
                elif i == len(flowerbed)-1:
                    if flowerbed[i-1] ==0 and flowerbed[i]==0:
                        flowerbed[i]=1
                        count+=1
                else:
                    if flowerbed[i-1]==0 and flowerbed[i+1] ==0 and flowerbed[i] ==0:
                        flowerbed[i]=1
                        count +=1
        print(count)
        if count >= n:
            return True
        else:
            return False