class Solution:
    def trap(self, height: List[int]) -> int:
        rain_water = 0
        if height is None or len(height) == 0:
            return rain_water
        left_wall, right_wall = 0, 1
        # find the first high wall in the left
        while(right_wall < len(height) and height[left_wall] <= height[right_wall]):
            left_wall, right_wall = left_wall + 1, right_wall + 1
        
        while(right_wall < len(height)):
            # find the high wall in the right to block
            if((left_wall + 1 == right_wall) and  height[left_wall] == height[right_wall]):
                left_wall, right_wall = left_wall + 1, right_wall + 1
                continue
            if(height[left_wall] > height[right_wall]):
                right_wall += 1
                continue
            wall_height = min(height[left_wall], height[right_wall])
            for i in range(left_wall + 1, right_wall):
                rain_water += ( wall_height - height[i] ) 
            left_wall, right_wall = right_wall, right_wall + 1
        
        # finding local maximum
        if left_wall + 1 != right_wall:
            left_boundary = left_wall
            left_wall, right_wall = right_wall - 2, right_wall - 1
            while((left_boundary < left_wall) and (height[right_wall] <= height[left_wall])):
                    left_wall, right_wall = left_wall - 1, right_wall - 1
            
            while(left_boundary <= left_wall):
                if((left_wall + 1 == right_wall) and height[right_wall] == height[left_wall]):
                    left_wall, right_wall = left_wall - 1, right_wall - 1
                if(height[right_wall] > height[left_wall]):
                    left_wall = left_wall - 1
                    continue
                wall_height = min(height[left_wall], height[right_wall])
                for i in range(left_wall + 1, right_wall):
                    rain_water += ( wall_height - height[i] ) 
                left_wall, right_wall = left_wall - 1, left_wall
        return rain_water
