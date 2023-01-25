class Solution:
    def closestMeetingNode(self, e: List[int], n1: int, n2: int) -> int:
        g=defaultdict(list)
        for i in range(len(e)):
            if(e[i]!=-1):
                g[i].append(e[i])
        # print(g)
        dis1={}
        dis2={}
        for i in range(len(e)):
            dis1[i]=999999999999999999
            dis2[i]=999999999999999999
        vis=set()
        q=deque([n1,-1])
        dis=0
        while(q):
            a=q.popleft()
            # print(a)
            if(a==-1):
                if(len(q)):
                    q.append(-1)
                dis+=1
            else:
                dis1[a]=dis
                vis.add(a)
                for i in g[a]:
                    if i not in vis:
                        q.append(i)
        # print(dis1)
        vis=set()
        q=deque([n2,-1])
        dis=0
        while(q):
            a=q.popleft()
            if(a==-1):
                if(len(q)):
                    q.append(-1)
                dis+=1
            else:
                dis2[a]=dis
                vis.add(a)
                for i in g[a]:
                    if i not in vis:
                        q.append(i)
        # print(dis2)
        ans=99999999999999999
        j=99999999999999999
        for i in range(len(e)):
            if(ans>max(dis1[i],dis2[i])):
                ans=max(dis1[i],dis2[i])
                j=i
            elif(ans==max(dis1[i],dis2[i])):
                j=min(j,i)
            # print(i,ans,j)
        if(ans==99999999999999999):
            return -1
        return j
        
        