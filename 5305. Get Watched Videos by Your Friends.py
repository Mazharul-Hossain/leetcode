class Solution:
    class FriendNode:
        def __init__(self, x, watched_Videos):
            self.id = x
            self.watched_Videos = set(watched_Videos)
            self.friends = []
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        Friend_List = []
        for index, watched_Videos in enumerate(watchedVideos):
            Friend_List.append(self.FriendNode(index, watched_Videos))
        for friend in friends:
            Friend_List[friend[0]].friends.append(friend[1])
            Friend_List[friend[1]].friends.append(friend[1])
        
        visited = [0 for i in range(len(Friend_List))]

        check_friend = set()
        