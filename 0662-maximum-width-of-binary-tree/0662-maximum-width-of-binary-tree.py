class Solution:
     def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        max_width = 1
        queue = deque([root])
        index_queue = deque([1])
        
        while queue:
            level_size = len(queue)
            left_index, right_index = 0, 0
            
            for i in range(level_size):
                node = queue.popleft()
                index = index_queue.popleft()
                
                if i == 0:
                    left_index = index
                if i == level_size - 1:
                    right_index = index
                
                if node.left:
                    queue.append(node.left)
                    index_queue.append(index * 2)
                if node.right:
                    queue.append(node.right)
                    index_queue.append(index * 2 + 1)
            
            max_width = max(max_width, right_index - left_index + 1)
        
        return max_width