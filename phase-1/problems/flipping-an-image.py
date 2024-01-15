class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for im in image:
            print(im)
            im.reverse()
            print(im)
            for i in range(len(im)):
                if im[i]==0: im[i]=1
                else: im[i]=0
                
        return image