class Solution(object):
    def initialize_map(self, str):
        map = {}
        for ch in str:
            if ch in map:
                map[ch] = map[ch] + 1
            else:
                map[ch] = 1
        return map
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False
            
        if len(s) == 0 and len(t) == 0:
            return True
        
        if len(s) != len(t):
            return False
        
        map_s = self.initialize_map(s)
        map_t = self.initialize_map(t)
        
        set_s = set(map_s.items())
        set_t = set(map_t.items())
        
        if len(set_s) != len(set_t):
            return False
        
        shared_items = set_s & set_t
        
        if len(shared_items) != len(set_s):
            return False
        else:
            return True

        

solution = Solution()
print(solution.isAnagram("abcc", "cbca"))