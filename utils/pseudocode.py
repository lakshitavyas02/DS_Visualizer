"""
Pseudocode definitions for data structure operations
"""

STACK_PSEUDOCODE = {
    "push": """
ALGORITHM Push(stack, element)
BEGIN
    1. IF stack is full THEN
        PRINT "Stack Overflow"
        RETURN
    2. top = top + 1
    3. stack[top] = element
    4. PRINT "Element pushed successfully"
END
    """,

    "pop": """
ALGORITHM Pop(stack)
BEGIN
    1. IF stack is empty THEN
        PRINT "Stack Underflow"
        RETURN NULL
    2. element = stack[top]
    3. top = top - 1
    4. RETURN element
END
    """,

    "peek": """
ALGORITHM Peek(stack)
BEGIN
    1. IF stack is empty THEN
        PRINT "Stack is empty"
        RETURN NULL
    2. RETURN stack[top]
END
    """
}

QUEUE_PSEUDOCODE = {
    "enqueue": """
ALGORITHM Enqueue(queue, element)
BEGIN
    1. IF queue is full THEN
        PRINT "Queue Overflow"
        RETURN
    2. rear = (rear + 1) % MAX_SIZE
    3. queue[rear] = element
    4. size = size + 1
    5. PRINT "Element enqueued successfully"
END
    """,

    "dequeue": """
ALGORITHM Dequeue(queue)
BEGIN
    1. IF queue is empty THEN
        PRINT "Queue Underflow"
        RETURN NULL
    2. element = queue[front]
    3. front = (front + 1) % MAX_SIZE
    4. size = size - 1
    5. RETURN element
END
    """
}

LINKED_LIST_PSEUDOCODE = {
    "insert_beginning": """
ALGORITHM InsertAtBeginning(head, data)
BEGIN
    1. newNode = CREATE_NODE(data)
    2. newNode.next = head
    3. head = newNode
    4. PRINT "Node inserted at beginning"
END
    """,

    "insert_end": """
ALGORITHM InsertAtEnd(head, data)
BEGIN
    1. newNode = CREATE_NODE(data)
    2. IF head is NULL THEN
        head = newNode
        RETURN
    3. current = head
    4. WHILE current.next != NULL DO
        current = current.next
    5. current.next = newNode
END
    """,

    "delete": """
ALGORITHM Delete(head, data)
BEGIN
    1. IF head is NULL THEN
        PRINT "List is empty"
        RETURN
    2. IF head.data == data THEN
        head = head.next
        RETURN
    3. current = head
    4. WHILE current.next != NULL AND current.next.data != data DO
        current = current.next
    5. IF current.next != NULL THEN
        current.next = current.next.next
END
    """
}

BINARY_TREE_PSEUDOCODE = {
    "insert": """
ALGORITHM Insert(root, data)
BEGIN
    1. IF root is NULL THEN
        root = CREATE_NODE(data)
        RETURN root
    2. IF data < root.data THEN
        root.left = Insert(root.left, data)
    3. ELSE
        root.right = Insert(root.right, data)
    4. RETURN root
END
    """,

    "inorder": """
ALGORITHM InorderTraversal(root)
BEGIN
    1. IF root is not NULL THEN
        InorderTraversal(root.left)
        PRINT root.data
        InorderTraversal(root.right)
END
    """,

    "preorder": """
ALGORITHM PreorderTraversal(root)
BEGIN
    1. IF root is not NULL THEN
        PRINT root.data
        PreorderTraversal(root.left)
        PreorderTraversal(root.right)
END
    """,

    "postorder": """
ALGORITHM PostorderTraversal(root)
BEGIN
    1. IF root is not NULL THEN
        PostorderTraversal(root.left)
        PostorderTraversal(root.right)
        PRINT root.data
END
    """
}

HASH_TABLE_PSEUDOCODE = {
    "hash_function": """
ALGORITHM Hash(key, table_size)
BEGIN
    1. IF key is string THEN
        hash_value = 0
        FOR each character in key DO
            hash_value = hash_value + ASCII(character)
        RETURN hash_value MOD table_size
    2. ELSE
        RETURN hash(key) MOD table_size
END
    """,

    "insert": """
ALGORITHM Insert(hash_table, key, value)
BEGIN
    1. index = Hash(key, table_size)
    2. bucket = hash_table[index]
    3. FOR each (k, v) in bucket DO
        IF k == key THEN
            UPDATE (k, v) to (key, value)
            RETURN "Updated"
    4. APPEND (key, value) to bucket
    5. RETURN "Inserted"
END
    """,

    "search": """
ALGORITHM Search(hash_table, key)
BEGIN
    1. index = Hash(key, table_size)
    2. bucket = hash_table[index]
    3. FOR each (k, v) in bucket DO
        IF k == key THEN
            RETURN v
    4. RETURN "Not Found"
END
    """
}

HEAP_PSEUDOCODE = {
    "insert": """
ALGORITHM Insert(heap, value)
BEGIN
    1. ADD value to end of heap array
    2. index = length(heap) - 1
    3. HeapifyUp(heap, index)
END
    """,

    "extract": """
ALGORITHM Extract(heap)
BEGIN
    1. IF heap is empty THEN
        RETURN null
    2. root = heap[0]
    3. heap[0] = heap[last_index]
    4. REMOVE last element
    5. HeapifyDown(heap, 0)
    6. RETURN root
END
    """,

    "heapify_up": """
ALGORITHM HeapifyUp(heap, index)
BEGIN
    1. WHILE index > 0 DO
        parent_index = (index - 1) / 2
        IF heap[index] satisfies_heap_property_with heap[parent_index] THEN
            SWAP heap[index] and heap[parent_index]
            index = parent_index
        ELSE
            BREAK
END
    """
}

GRAPH_PSEUDOCODE = {
    "add_edge": """
ALGORITHM AddEdge(graph, vertex1, vertex2, weight)
BEGIN
    1. ADD vertex1 to graph if not exists
    2. ADD vertex2 to graph if not exists
    3. ADD (vertex2, weight) to adjacency_list[vertex1]
    4. IF graph is undirected THEN
        ADD (vertex1, weight) to adjacency_list[vertex2]
END
    """,

    "bfs": """
ALGORITHM BFS(graph, start_vertex)
BEGIN
    1. CREATE empty queue
    2. CREATE empty visited set
    3. ENQUEUE start_vertex to queue
    4. WHILE queue is not empty DO
        vertex = DEQUEUE from queue
        IF vertex not in visited THEN
            ADD vertex to visited
            PRINT vertex
            FOR each neighbor of vertex DO
                IF neighbor not in visited THEN
                    ENQUEUE neighbor to queue
END
    """,

    "dfs": """
ALGORITHM DFS(graph, start_vertex)
BEGIN
    1. CREATE empty visited set
    2. DFS_Recursive(start_vertex, visited)
END

ALGORITHM DFS_Recursive(vertex, visited)
BEGIN
    1. ADD vertex to visited
    2. PRINT vertex
    3. FOR each neighbor of vertex DO
        IF neighbor not in visited THEN
            DFS_Recursive(neighbor, visited)
END
    """
}
