package graph;

import model.Edge;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Set;

public class Graph {
    // Adjacency list using a Map where the value is a LinkedList, 
    // to strictly adhere to standard graph linked-list mappings.
    private Map<String, LinkedList<Edge>> adjList;

    public Graph() {
        this.adjList = new HashMap<>();
    }

    public void addVertex(String vertex) {
        adjList.putIfAbsent(vertex, new LinkedList<>());
    }

    public void addEdge(String source, String destination, String transport, double distance, double time, double price) {
        addVertex(source);
        addVertex(destination);
        LinkedList<Edge> edges = adjList.get(source);
        edges.add(new Edge(destination, transport, distance, time, price));
    }

    public LinkedList<Edge> getNeighbors(String vertex) {
        return adjList.getOrDefault(vertex, new LinkedList<>());
    }

    public Set<String> getVertices() {
        return adjList.keySet();
    }
}
