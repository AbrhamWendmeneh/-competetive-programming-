class Solution:
    def findComplement(self, num: int) -> int:
        # binarystr= bin(num)[2:]
        # complementint= ~int(binarystr,2)
        # complementbin=bin(complementint)[3:]
        # return int(complementbin,2)
        print(bin(39)[2:])
        mask = (1 << num.bit_length()) - 1
        print(mask)
        return num^mask
        
        
        
        