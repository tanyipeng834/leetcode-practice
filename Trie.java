
class Trie {

    public TrieNode root;


    private class TrieNode{
    // This is where we store the children of the current TrieNode
    private HashMap<Character,TrieNode> children;
    private boolean isWord;




   private TrieNode(HashMap<Character,TrieNode> children,boolean isWord){
    this.children = children;
    this.isWord = isWord;

    
    
   }
    }


    

    public Trie() {
        this.root = new TrieNode(new HashMap<>(),false);


    
    

        
    }
    
    public void insert(String word) {
        TrieNode current = root;
        for(char c : word.toCharArray()){
            if(current.children ==null || current.children.get(c) ==null ){
                current.children.put(c, new TrieNode(new HashMap<>(),false));
            }

            current = current.children.get(c);

            
            


        }
        current.isWord =true;
        

        
    }
    
    public boolean search(String word) {
        TrieNode current = root;
        for(char c : word.toCharArray())
        {
            if (current.children == null || current.children.get(c)==null){
                return false;
            }
            // Go to the next element in the Trie
            current = current.children.get(c);


        }
        if(current.isWord) return true;

        return false;
    }
    
    public boolean startsWith(String prefix) 
        TrieNode current = root;
        List<Character> charList = new ArrayList<Character>();
        for(char c: prefix.toCharArray())
        {
             if (current.children == null || current.children.get(c)==null){
                return false;
            }
            // Go to the next element in the Trie
            current = current.children.get(c);
            

        }

        if(dfs(current)){
            return true;
        }
        else{
            return false;
        }







       

        
        // Go through depth first seach to see when the first element would be an word


         
        
    }

    private boolean dfs(TrieNode node){
        if(node==null){
            return false;
        }
        else{
            if(node.isWord){
                return true;
            }

            for (TrieNode childNode : node.children.values()){
                if(dfs(childNode)){
                    return true;
                }
                

            }
            return false;




            }
        }
    }

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */