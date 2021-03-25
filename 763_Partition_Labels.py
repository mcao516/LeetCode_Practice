class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        """
        S = ["ababcbaca", "defegde", "hijhklij"]
        
        """
        positions = {}
        for i, c in enumerate(S):
            positions[c] = max(i, positions[c] if c in positions else 0)
        
        max_pos, length = -1, 0
        part_sizes = []
        
        for i, c in enumerate(S):
            length += 1
            if positions[c] > max_pos:
                max_pos = positions[c]
                
            # check if cuttable
            if i == max_pos:
                part_sizes.append(length)
                length = 0
        
        return part_sizes