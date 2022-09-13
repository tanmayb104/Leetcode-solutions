class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        k = 0
        while k < len(data):
            if data[k] >> 7 == 0:
                k += 1
            elif data[k] >> 5 == 0b110:
                if k+1 == len(data) or data[k+1] >> 6 != 0b10:
                    return False
                k += 2
            elif data[k] >> 4 == 0b1110:
                if k+2 >= len(data) or data[k+1] >> 6 != 0b10 or data[k+2] >> 6 != 0b10:
                    return False
                k += 3
            elif data[k] >> 3 == 0b11110:
                if k+3 >= len(data) or data[k+1] >> 6 != 0b10 or data[k+2] >> 6 != 0b10 or data[k+3] >> 6 != 0b10:
                    return False
                k += 4
            else:
                return False
        return True