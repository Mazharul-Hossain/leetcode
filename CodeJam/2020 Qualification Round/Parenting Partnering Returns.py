from queue import PriorityQueue

def maxEvents(events, N) -> str:
    return_string = ["" for _ in range(N)]
    Cameron, Jamie = 0, 0
    while events.qsize() > 0 :
        event, event_id = events.get()
        start, end = event
        # print(event_id, "#", start, end)

        if Cameron <= start:
            Cameron = end
            return_string[event_id] = "C"
        
        elif Jamie <= start:
            Jamie = end
            return_string[event_id] = "J"

        else:
            return "IMPOSSIBLE"    
    
    return "".join( return_string )

def main():
    T = int( input() )
    for case in range(1, T + 1):
        N = int( input() )

        events = PriorityQueue()
        for i in range(N):
            temp_string = input()
            temp_list = list( map(int, temp_string.rstrip().split() ) )
            events.put( ( (temp_list[0], temp_list[1] ) , i) )

        print("Case #{}:".format(case), maxEvents(events, N))

if __name__ == '__main__':
    main()