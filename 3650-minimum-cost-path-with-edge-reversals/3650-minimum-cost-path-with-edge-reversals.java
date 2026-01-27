import java.util.*;

class Solution {

    static class Node {
        int v;
        long cost;
        Node(int v, long cost) {
            this.v = v;
            this.cost = cost;
        }
    }

    public int minCost(int n, int[][] edges) {

        List<Node>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();

        // Build graph
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].add(new Node(v, w));       // normal edge
            graph[v].add(new Node(u, 2L * w));  // reversed edge
        }

        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);

        PriorityQueue<Node> pq =
            new PriorityQueue<>(Comparator.comparingLong(a -> a.cost));

        dist[0] = 0;
        pq.offer(new Node(0, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            int u = cur.v;
            long cost = cur.cost;

            if (cost > dist[u]) continue;

            for (Node next : graph[u]) {
                if (dist[next.v] > cost + next.cost) {
                    dist[next.v] = cost + next.cost;
                    pq.offer(new Node(next.v, dist[next.v]));
                }
            }
        }

        return dist[n - 1] == Long.MAX_VALUE ? -1 : (int) dist[n - 1];
    }
}

