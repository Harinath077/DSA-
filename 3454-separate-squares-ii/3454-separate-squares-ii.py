class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        from collections import defaultdict

        events = defaultdict(list)
        ys = set()
        xs = set()

        for x, y, l in squares:
            events[y].append((x, x + l, 1))
            events[y + l].append((x, x + l, -1))
            ys.add(y)
            ys.add(y + l)
            xs.add(x)
            xs.add(x + l)

        ys = sorted(ys)
        xs = sorted(xs)

        # compress x
        idx = {v: i for i, v in enumerate(xs)}
        m = len(xs)
        seg = [0] * (4 * m)
        cnt = [0] * (4 * m)

        # precompute x lengths
        length = [0] * (m - 1)
        for i in range(m - 1):
            length[i] = xs[i + 1] - xs[i]

        def update(node, l, r, ql, qr, val):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                cnt[node] += val
            else:
                mid = (l + r) // 2
                update(node * 2 + 1, l, mid, ql, qr, val)
                update(node * 2 + 2, mid, r, ql, qr, val)

            if cnt[node] > 0:
                seg[node] = xs[r] - xs[l]
            else:
                if r - l == 1:
                    seg[node] = 0
                else:
                    seg[node] = seg[node * 2 + 1] + seg[node * 2 + 2]

        area = 0
        total_area = 0
        prev_y = ys[0]

        for y in ys:
            dy = y - prev_y
            if dy > 0:
                total_area += seg[0] * dy
            for x1, x2, sgn in events[y]:
                update(0, 0, m - 1, idx[x1], idx[x2], sgn)
            prev_y = y

        target = total_area / 2
        area = 0
        seg = [0] * (4 * m)
        cnt = [0] * (4 * m)
        prev_y = ys[0]

        for y in ys:
            dy = y - prev_y
            if dy > 0:
                if area + seg[0] * dy >= target:
                    return prev_y + (target - area) / seg[0]
                area += seg[0] * dy
            for x1, x2, sgn in events[y]:
                update(0, 0, m - 1, idx[x1], idx[x2], sgn)
            prev_y = y

        return float(ys[-1])
