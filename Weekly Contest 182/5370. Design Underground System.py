class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.total_time = {}         

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customers:
            self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.customers:
            temp_station, temp_time  = self.customers[id]
            del self.customers[id]

            if ( temp_station, stationName ) not in self.total_time:
                self.total_time[ ( temp_station, stationName )  ] = (0, 0)
                
            temp_total_time, temp_total_customer = self.total_time[ ( temp_station, stationName )  ]
            
            temp_total_time += ( t - temp_time )            
            temp_total_customer += 1
            self.total_time[ ( temp_station, stationName )  ] = ( temp_total_time, temp_total_customer)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # print(self.total_time)
        temp_score = self.total_time[ ( startStation, endStation )  ]
        return temp_score[0] / temp_score[1]
        


# Your UndergroundSystem object will be instantiated and called as such:
undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
print( undergroundSystem.getAverageTime("Paradise", "Cambridge") )       
print('return 14.0. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)') 
print( undergroundSystem.getAverageTime("Leyton", "Waterloo") )          
print('return 11.0. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.0') 
undergroundSystem.checkIn(10, "Leyton", 24)
print( undergroundSystem.getAverageTime("Leyton", "Waterloo") )          
print("return 11.0") 
undergroundSystem.checkOut(10, "Waterloo", 38)
print( undergroundSystem.getAverageTime("Leyton", "Waterloo") )      
print("return 12.0") 