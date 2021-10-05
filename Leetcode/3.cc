class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> hash;
        int n = s.size();
        int longest = 0;
        int cur = 0;
        for(int i = 0; i < n; i++) {
            if (hash.find(s[i]) != hash.end()) {
                longest = cur > longest ? cur : longest;
                int prev_ind = hash[s[i]];
                for (int j = i - cur; j <= prev_ind; j++) {
                    hash.erase(s[j]);
                }
                cur = i - prev_ind;
            } else {
                cur++;
            }
            hash[s[i]] = i;
        }
        longest = cur > longest ? cur : longest;
        return longest;
    }
};