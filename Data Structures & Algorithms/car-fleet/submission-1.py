class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        #Sort by position
        for i in range(len(position)):
            car={
                "pos":0,
                "spid":0
            }
            car["pos"] = position[i]
            car["spid"]=speed[i]
            car["time_to"] = (target - car["pos"])/car["spid"]
            cars.append(car)
        cars: list[dict] = sorted(cars,key=lambda x: x["pos"],)

        #monotonic stack descending order

        stack = []
        fleet_number = 0
        for i, num in enumerate(reversed(cars)):
            if not stack:
                stack.append(num["time_to"])

            else:
                if num["time_to"] > stack[-1]:
                    stack.append(num["time_to"])
        return len(stack)