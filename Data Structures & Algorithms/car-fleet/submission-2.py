class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #time_arrival=(target-position)/speed
        #if time of arrival of next car <= prev car -> merge them

        stack=[]    #stack of time of arrival
        cardata = sorted(zip(position, speed), reverse=True)
        for carpos, carspeed in cardata:
            time_arrival=(target-carpos)/carspeed
            if stack:
                if time_arrival > stack[-1]:
                    stack.append(time_arrival)
            else: 
                stack.append(time_arrival)


        return len(stack)