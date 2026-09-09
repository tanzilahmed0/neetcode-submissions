class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We care about arrival times, if arrival time of car behind <= car ahead,
        # it will catch up and join fleet. So we store the arrival times by zipping
        # list. We also need to sort by position descending because cars can't pass 
        # cars ahead, so the one closest to the target is the primary blocker 
        # We can store a latest_arrival_time and fleet_count both initialized at 0
        # if the closest car's arrival time is greater than the arrival time, it forms 
        # new fleet, and becomes new latest arrival time 
        # if car behind <= latest_arrival_time, it joins the fleet 
        
        arr_times = [(target - pos) / spd for pos, spd in zip(position, speed)]

        cars = sorted(zip(position, arr_times), reverse=True) 

        stack = [] 
        fleet = 0 
        latest_arrival_time = 0 

        for car in cars: 
            if car[1] > latest_arrival_time: 
                fleet += 1 
                latest_arrival_time = car[1] 

            elif car[1] <= latest_arrival_time: 
                continue

        return fleet 


