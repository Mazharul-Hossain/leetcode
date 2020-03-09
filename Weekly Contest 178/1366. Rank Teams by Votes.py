class Solution:
    def rankTeams(self, votes: [str]) -> str:
        # if len(votes) == 1 or len(votes[0]) == 1:
        #     return votes[0]

        # team_list = sorted(votes[0])
        # vote_count = {}
        # for team in team_list:
        #     vote_count_list = [0 for i in range( len(votes[0]) ) ] 
        #     vote_count[team] = vote_count_list

        # for vote in votes:
        #     for place in range( len(vote) ):
        #         vote_count[ vote[place] ][ place ] += 1

        # from queue import PriorityQueue
        # vote_score_priority_queue = PriorityQueue()
        
        # for key, item in vote_count.items():
        #     score, weight = 0, 1
        #     for i in range( len(item)-1, -1, -1):
        #         score += weight * item[i]
        #         weight += 1
        #     vote_score_priority_queue.put( (-1*score, key) )
        
        # result = []
        # while vote_score_priority_queue.qsize() > 0:
        #     vote_score = vote_score_priority_queue.get()
        #     print(vote_score)
        #     result.append(vote_score[1])

        # return "".join(result)

        count = {v: [0] * len(votes[0]) + [v] for v in votes[0]}
        # print(count)
        
        for vote in votes:
            for i, v in enumerate(vote):
                count[v][i] -= 1
        # print(count)

        return ''.join(sorted(votes[0], key=count.get))

obj = Solution()
votes = ["ABC","ACB","ABC","ACB","ACB"]
print("ACB", obj.rankTeams(votes) )

votes = ["WXYZ","XYZW"]
print("XWYZ", obj.rankTeams(votes) )

votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
print("ZMNAGUEDSJYLBOPHRQICWFXTVK", obj.rankTeams(votes) )

votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
print("ABC", obj.rankTeams(votes) )

votes = ["M","M","M","M"]
print("M", obj.rankTeams(votes) )

votes = ["FVSHJIEMNGYPTQOURLWCZKAX","AITFQORCEHPVJMXGKSLNZWUY","OTERVXFZUMHNIYSCQAWGPKJL","VMSERIJYLZNWCPQTOKFUHAXG","VNHOZWKQCEFYPSGLAMXJIUTR","ANPHQIJMXCWOSKTYGULFVERZ","RFYUXJEWCKQOMGATHZVILNSP","SCPYUMQJTVEXKRNLIOWGHAFZ","VIKTSJCEYQGLOMPZWAHFXURN","SVJICLXKHQZTFWNPYRGMEUAO","JRCTHYKIGSXPOZLUQAVNEWFM","NGMSWJITREHFZVQCUKXYAPOL","WUXJOQKGNSYLHEZAFIPMRCVT","PKYQIOLXFCRGHZNAMJVUTWES","FERSGNMJVZXWAYLIKCPUQHTO","HPLRIUQMTSGYJVAXWNOCZEKF","JUVWPTEGCOFYSKXNRMHQALIZ","MWPIAZCNSLEYRTHFKQXUOVGJ","EZXLUNFVCMORSIWKTYHJAQPG","HRQNLTKJFIEGMCSXAZPYOVUW","LOHXVYGWRIJMCPSQENUAKTZF","XKUTWPRGHOAQFLVYMJSNEIZC","WTCRQMVKPHOSLGAXZUEFYNJI"]
print("VWFHSJARNPEMOXLTUKICZGYQ", obj.rankTeams(votes) )