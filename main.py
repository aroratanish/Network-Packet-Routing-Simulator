from graph import Graph
from dijkstra import dijkstra

def main():
    g = Graph()

    # Sample network
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'E', 3)
    g.add_edge('E', 'D', 4)
    g.add_edge('D', 'F', 11)

    print("Network Graph:")
    g.display()

    start = input("\nEnter source node: ").upper()
    distances = dijkstra(g.graph, start)

    print("\nShortest distances from", start)
    for node, dist in distances.items():
        print(f"{node}: {dist}")

if __name__ == "__main__":
    main()
