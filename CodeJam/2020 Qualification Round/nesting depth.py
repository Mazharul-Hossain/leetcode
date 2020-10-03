def main():
    T = int( input() )
    for case in range(1, T + 1):
        temp_list = input()
        
        temp_string, depth = "", 0
        for s in temp_list:
            i = int(s)
            if i > depth:                
                for _ in range(depth, i):
                    temp_string = temp_string + "("
                depth = i
            elif i < depth:
                for _ in range(depth, i, -1):
                    temp_string = temp_string + ")"                
                depth = i
            temp_string = temp_string + s
        if depth > 0:
            for _ in range(depth, 0, -1):
                temp_string = temp_string + ")"
        print("Case #{}:".format(case), temp_string)

if __name__ == '__main__':
    main()