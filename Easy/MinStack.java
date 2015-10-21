class MinStack {
    LinkedList<Integer> list = new LinkedList<Integer>();

    LinkedList<Integer> minList = new LinkedList<Integer>();


    public void push(int x) {
        if(minList.isEmpty()){
            minList.addLast(x);
        }else if(x <= minList.getLast()){
            minList.addLast(x);
        }

        
        
        list.addLast(x);
    }

 
    public void pop() {
        int last = list.getLast();
        if (last == minList.getLast()) {
            minList.removeLast();
        }

        
        list.removeLast();
    }

    public int top() {
        return list.getLast();
    }

    public int getMin() {
        return minList.getLast();
    }
}
