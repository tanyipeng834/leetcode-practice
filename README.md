<div align="center">
  <h1>Leetcode Practice</h1>
  <img src="./images/leetcode.png" alt="Practing my leetcode" />

  <div>
  <h2>Union Find Algoirthm</h2>

  <h3>Quick Find</h3>
  <p> p  and q are connected if they have the same entry in the array</p>
  
 
  <p>
  Union(4,3)
  <br>
  Change the id of the 2nd element to the 1st element in the funciton call
  <br>
  Go Through the entire array and change all entries with the 2nd id to the 1st id to show that they are connected
  
  </p>

  <h3>Union Find</h3>

  <p>
<pre class="code-block">
  private int root(int i){
  while (int [i] != i){i = int[i]}
  return i}
</pre>

<h3>Code Improvements</h3>

Keep note of the size of the tree to make sure that the smaller tree is connected to the bigger tree

<h3>Make the child connect to the grandparent  to flatten out the tree</h3>
<pre class="code-block">
  private int root(int i){
  while (int [i] != i){
  int[i] = int[int[i]]
  i = int[i]}
  return i}
</pre>

<h3>Itearing over a Linked List</h3>
<pre class="code-block">
  while (current is not None):
    current = current.next
</pre>

<h2>Binary Tree</h2>

<h3>Pre-Order Traversal</h3>
<p>Visit the parent node before visiting left children and right children</p>
<pre class="code-block">
  def pre_order_traversal(root):
    if root:
        print(root.val, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
</pre>

<h3>In-Order Traversal</h3>
<p>Visit the left Node before visiting the parent and then the right node</p>
<pre class="code-block">
  def in_order_traversal(root):
    if root:
        pre_order_traversal(root.left)
        print(root.val, end=" ")
        pre_order_traversal(root.right)
</pre>

<h3>Post-Order Traversal</h3>
<p>Visit the left Node and Right Node before visiting the parent</p>
<pre class="code-block">
  def post_order_traversal(root):
    if root:
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
        print(root.val, end=" ")
</pre>



    
  </p>

    
  </div>
</div>
