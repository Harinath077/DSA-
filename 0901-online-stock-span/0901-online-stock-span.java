import java.util.ArrayDeque;
import java.util.Deque;

class StockSpanner {

    private Deque<int[]> stack;
    private int index;

    public StockSpanner() {
        stack = new ArrayDeque<>();
        index = -1;
    }

    public int next(int price) {
        index++;

        // Pop all smaller or equal prices
        while (!stack.isEmpty() && stack.peek()[0] <= price) {
            stack.pop();
        }

        int span;
        if (stack.isEmpty()) {
            span = index + 1;
        } else {
            span = index - stack.peek()[1];
        }

        // Push {price, index}
        stack.push(new int[]{price, index});
        return span;
    }
}