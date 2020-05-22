class Solution:
    def displayTable(self, orders: [[str]]) -> [[str]]:
        food_menu, return_table, food_items = {}, [], set()

        for order in orders:
            _, tableNumber, foodItem = order
            food_items.add( foodItem )
            
            if tableNumber not in food_menu:                
                food_menu[ tableNumber ] = {}

            if foodItem  not in food_menu[ tableNumber ]:
                food_menu[ tableNumber ][ foodItem ] = 0

            food_menu[ tableNumber ][ foodItem ] += 1
        
        food_items = list(food_items)  
        food_items.sort()      
        
        row = ["Table"]
        for foodItem in food_items:
            row.append(foodItem)
        return_table.append(row)

        keylist = list( map(int, food_menu.keys()) )
        keylist.sort()
        for tableNumber in keylist:
            tableNumber = str(tableNumber)

            foodItems = food_menu[ tableNumber ]
            row = [tableNumber]
            for foodItem in food_items:
                if foodItem  not in foodItems:
                    row.append( str(0) )
                else:
                    row.append( str( foodItems[ foodItem ] ) )
            return_table.append(row)

        return return_table


obj = Solution()

print( obj.displayTable( orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]] ) )

print( obj.displayTable( orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]] ) )

print( obj.displayTable( orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]] ) )