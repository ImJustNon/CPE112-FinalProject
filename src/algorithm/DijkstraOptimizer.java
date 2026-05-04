package algorithm;

import graph.Graph;
import model.Edge;
import model.PathResult;

import java.util.*;

public class DijkstraOptimizer {
    
    private static class NodeRecord implements Comparable<NodeRecord> {
        String node;
        double weight;

        NodeRecord(String node, double weight) {
            this.node = node;
            this.weight = weight;
        }

        @Override
        public int compareTo(NodeRecord other) {
            return Double.compare(this.weight, other.weight);
        }
    }

    private static class Predecessor {
        String prevNode;
        Edge edgeUsed;
        
        Predecessor(String prevNode, Edge edgeUsed) {
            this.prevNode = prevNode;
            this.edgeUsed = edgeUsed;
        }
    }

    public PathResult findShortestPath(Graph graph, String startNode, String endNode, 
                                       boolean useDistance, boolean useTime, boolean usePrice) {
        
        PriorityQueue<NodeRecord> pq = new PriorityQueue<>();
        Map<String, Double> minWeights = new HashMap<>();
        Map<String, Predecessor> predecessors = new HashMap<>();

        for (String vertex : graph.getVertices()) {
            minWeights.put(vertex, Double.POSITIVE_INFINITY);
        }
        
        minWeights.put(startNode, 0.0);
        pq.add(new NodeRecord(startNode, 0.0));

        while (!pq.isEmpty()) {
            NodeRecord current = pq.poll();

            if (current.node.equals(endNode)) break;

            if (current.weight > minWeights.getOrDefault(current.node, Double.POSITIVE_INFINITY)) {
                continue;
            }

            // Linked List traversal behavior
            for (Edge edge : graph.getNeighbors(current.node)) {
                String neighbor = edge.getDestination();
                double edgeWeight = edge.getWeight(useDistance, useTime, usePrice);
                double newWeight = current.weight + edgeWeight;

                if (newWeight < minWeights.getOrDefault(neighbor, Double.POSITIVE_INFINITY)) {
                    minWeights.put(neighbor, newWeight);
                    predecessors.put(neighbor, new Predecessor(current.node, edge));
                    pq.add(new NodeRecord(neighbor, newWeight));
                }
            }
        }

        if (!predecessors.containsKey(endNode) && !startNode.equals(endNode)) {
            return null; // Path not found
        }

        // Reconstruct Path
        List<String> path = new ArrayList<>();
        List<Edge> edgesUsed = new ArrayList<>();
        String current = endNode;

        while (predecessors.containsKey(current)) {
            path.add(current);
            Predecessor p = predecessors.get(current);
            edgesUsed.add(p.edgeUsed);
            current = p.prevNode;
        }
        
        path.add(startNode);
        Collections.reverse(path);
        Collections.reverse(edgesUsed);

        return new PathResult(path, edgesUsed);
    }
}
