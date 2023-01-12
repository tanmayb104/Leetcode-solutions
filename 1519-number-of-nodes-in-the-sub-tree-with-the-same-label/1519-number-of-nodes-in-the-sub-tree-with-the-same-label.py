class Solution:
    def countSubTrees(self, n: int, e: List[List[int]], l: str) -> List[int]:
        g={}
        for i in e:
            if(i[0] in g):
                g[i[0]].append(i[1])
            else:
                g[i[0]]=[i[1]]
            if(i[1] in g):
                g[i[1]].append(i[0])
            else:
                g[i[1]]=[i[0]]
        ans=[1 for i in range(n)]
        def dfs(node,par):
            val=1
            dic={}
            for i in g[node]:
                if(i!=par):
                    d=dfs(i,node)
                    for j in d:
                        if(j in dic):
                            dic[j]+=d[j]
                        else:
                            dic[j]=d[j]
            if(l[node] in dic):
                val+=dic[l[node]]
            ans[node]=val
            if(l[node] in dic):
                dic[l[node]]+=1
            else:
                dic[l[node]]=1
            # print(dic,node)
            return dic
        dfs(0,-1)
        return ans