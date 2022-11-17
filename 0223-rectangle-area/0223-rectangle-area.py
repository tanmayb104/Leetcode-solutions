class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        return (C-A)*(D-B)+(G-E)*(H-F)-max(min(C,G)-max(A, E),0)*max(min(D,H)-max(B,F),0)