class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    public MinStack(){
        stack = new Stack<>();
        minStack = new Stack<>();
    }  
    
    
    public void push(int val) {
        stack.push(val);
        // for minStack condition
        if( minStack.isEmpty() || val <= minStack.peek() ){
            minStack.push(val);
        }
    }
    
    public void pop() {
        if (stack.isEmpty()) {
        throw new RuntimeException("Stack is empty");
        }
    
        int removedElem = stack.pop();
        if( removedElem == minStack.peek()){
            minStack.pop();
        }
    }
    
    public int top() {
        if (stack.isEmpty()) {
        throw new RuntimeException("Stack is empty");
        }
        return stack.peek();
    }
    

    public int getMin() {
        if (stack.isEmpty()) {
        throw new RuntimeException("Stack is empty");
        }
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */