import sys
import heapq

sys.stdin = open('test.txt','r')
input = sys.stdin.readline


def main():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        s, e, d, don = map(int, input().split())
        graph[s].append((e, d, don))
        graph[e].append((s, d, don))

    def dijkstra(start, end):
        dist = [float('inf')] * (V + 1)
        dist[start] = 0
        max_donation_so_far = 0

        heap = [(0, start, max_donation_so_far)]

        while heap:
            total_dist, node, max_donation = heapq.heappop(heap)

            if node == end:
                return total_dist - max_donation

            if total_dist > dist[node]:
                continue

            for neighbor, neighbor_dist, neighbor_don in graph[node]:
                new_dist = total_dist + neighbor_dist
                new_max_donation = max(max_donation, neighbor_don)

                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor, new_max_donation))

        return float('inf')

    for x in range(2, V + 1):
        result = dijkstra(1, x)
        print(result)

if __name__ == '__main__':
    main()

