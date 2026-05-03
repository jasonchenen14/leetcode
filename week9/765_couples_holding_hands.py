class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0
        
        for i in range(0, n, 2):
            first_person = row[i]
            partner = first_person ^ 1
            
            if row[i + 1] != partner:
                swaps += 1
                partner_pos = pos[partner]
                wrong_person = row[i + 1]
                
                row[i + 1], row[partner_pos] = row[partner_pos], row[i + 1]
                pos[wrong_person] = partner_pos
                
        return swaps
