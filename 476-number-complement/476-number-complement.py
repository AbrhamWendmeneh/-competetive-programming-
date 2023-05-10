class Solution:
    def findComplement(self, num: int) -> int:
        
        # complementint= ~int(binarystr,2)
        # complementbin=bin(complementint)[3:]
        # return int(complementbin,2)
        # print(bin(39)[2:])
        # mask = (1 << num.bit_length()) - 1
        # print(mask)
        # return num^mask
        
        
        binarystr= bin(num)[2:]
        val=''.join(['0' if i=='1' else '1' for i in binarystr])
        if val:
            return int(val,2)
        return 1
        
        
        