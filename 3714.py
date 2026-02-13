class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = b = c = 0
        res = 0
        
        # Maps to store first occurrence of specific states
        # 3-char case: state is (a-b, a-c)
        map3 = {(0, 0): -1}
        
        # 2-char cases: state is (diff, forbidden_count)
        # We need the "forbidden" char count to be constant (delta c == 0)
        # and the pair diff to be constant (delta a == delta b)
        mapAB = {(0, 0): -1}  # key: (a-b, c) -> finds equal a, b with 0 c's
        mapAC = {(0, 0): -1}  # key: (a-c, b) -> finds equal a, c with 0 b's
        mapBC = {(0, 0): -1}  # key: (b-c, a) -> finds equal b, c with 0 a's
        
        # 1-char case: simple counter
        current_run = 0
        
        for i, ch in enumerate(s):
            # 1. Update counts
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            
            # 2. Handle 1-character case (consecutive run)
            if i > 0 and s[i] == s[i-1]:
                current_run += 1
            else:
                current_run = 1
            res = max(res, current_run)
            
            # 3. Handle 3-character case ({a,b,c})
            # We want count(a)==count(b)==count(c)
            key3 = (a - b, a - c)
            if key3 in map3:
                res = max(res, i - map3[key3])
            else:
                map3[key3] = i
            
            # 4. Handle 2-character cases
            # Case {a, b}: a==b, c count must not change
            keyAB = (a - b, c)
            if keyAB in mapAB:
                res = max(res, i - mapAB[keyAB])
            else:
                mapAB[keyAB] = i
                
            # Case {a, c}: a==c, b count must not change
            keyAC = (a - c, b)
            if keyAC in mapAC:
                res = max(res, i - mapAC[keyAC])
            else:
                mapAC[keyAC] = i
                
            # Case {b, c}: b==c, a count must not change
            keyBC = (b - c, a)
            if keyBC in mapBC:
                res = max(res, i - mapBC[keyBC])
            else:
                mapBC[keyBC] = i
        
        return res