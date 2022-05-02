# Party in Town
## Medium 
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">Geek town has <strong>N </strong>Houses numbered from <strong>1</strong> to <strong>N</strong>. They are connected with each other via <strong>N-1</strong> bidirectional roads&nbsp;and an adjacency list <strong>adj</strong> is used to represent the connections</span><span style="font-size:18px">. To host the optimal party, you need to identify&nbsp;the house from which the distance to the farthest house is&nbsp;minimum. Find this&nbsp;distance.</span></p>

<p><br>
<strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input: </strong>
N = 4
adj = {{2},{1,3,4},{2},{2}} </span>
<span style="font-size:18px"><strong>Output:</strong> 1</span>
<span style="font-size:18px"><strong>Explaination:</strong> 
<img alt="" src="https://media.geeksforgeeks.org/img-practice/ScreenShot2022-05-02at4-1651489722.png" class="img-responsive">
Party should take place at house number 2. 
Maximum distance from house number 2 is 1.</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:
</span></strong><span style="font-size:18px">N = 4
adj = {{2},{1,3},{2,4},{3}}</span><strong><span style="font-size:18px">
Output:
</span></strong><span style="font-size:18px">2</span><strong><span style="font-size:18px">
Explanation:
</span></strong><span style="font-size:18px">Party should take place at house number 2 or 3.
So, the minimum distance between the farthest
house and the party house is 2.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function <strong>partyHouse() </strong>which takes N and adj as input parameters and returns the minimum possible distance to the farthest house from the house where the party is happening.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N*N)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;=&nbsp;N &lt;=&nbsp;1000<br>
1 &lt;= adj[i][j] &lt;= N</span></p>
 <p></p>
            </div>