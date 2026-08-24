class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        fleet=0
        prev_time=0
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(reverse=True)
        for positions,speeds in cars:
            time=(target-positions)/speeds
            if prev_time<time:
                fleet+=1
                prev_time=time
        return fleet