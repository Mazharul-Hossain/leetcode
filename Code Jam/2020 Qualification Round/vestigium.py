def main():
    T = int( input() )
    for case in range(1, T + 1):
        N = int( input() )
        M = []
        for i in range(N):
            temp_string = input()
            temp_list = list( map(int, temp_string.rstrip().split() ) )
            M.append(temp_list)
        
        k, r, c = 0, 0, 0
        for i in range(N):
            temp_list = M[i]
            k += temp_list[i]
            
            temp_set = list( set(temp_list) )
            if len(temp_list) != len(temp_set):
                r += 1 
            
            temp_list = [row[i] for row in M]
            temp_set = list( set(temp_list) )
            if len(temp_list) != len(temp_set):
                c += 1

        print("Case #{}:".format(case), k, r, c)

if __name__ == '__main__':
    main()