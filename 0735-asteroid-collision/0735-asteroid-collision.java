import java.util.Stack;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();

        for (int asteroid : asteroids) {

            // Case 1: moving right → no immediate collision
            if (asteroid > 0) {
                stack.push(asteroid);
            } 
            // Case 2: moving left → handle collisions
            else {
                // Destroy smaller right-moving asteroids
                while (!stack.isEmpty() && stack.peek() > 0 
                       && stack.peek() < Math.abs(asteroid)) {
                    stack.pop();
                }

                // Equal size → both destroyed
                if (!stack.isEmpty() && stack.peek() == Math.abs(asteroid)) {
                    stack.pop();
                }
                // No collision → asteroid survives
                else if (stack.isEmpty() || stack.peek() < 0) {
                    stack.push(asteroid);
                }
            }
        }

        // Convert stack to array
        int[] result = new int[stack.size()];
        for (int i = 0; i < stack.size(); i++) {
            result[i] = stack.get(i);
        }
        return result;
    }
}
