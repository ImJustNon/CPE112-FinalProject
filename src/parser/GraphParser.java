package parser;

import graph.Graph;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;

public class GraphParser {

    /**
     * Parses the graph data from a JSON file using Jackson.
     */
    public static Graph loadGraph(String filePath) {
        Graph graph = new Graph();
        
        try {
            ObjectMapper mapper = new ObjectMapper();
            JsonNode rootNode = mapper.readTree(new File(filePath));

            // Extract vertices
            JsonNode verticesNode = rootNode.get("vertices");
            if (verticesNode != null && verticesNode.isArray()) {
                for (JsonNode vNode : verticesNode) {
                    graph.addVertex(vNode.asText());
                }
            }

            // Extract edges
            JsonNode edgesNode = rootNode.get("edges");
            if (edgesNode != null && edgesNode.isArray()) {
                for (JsonNode eNode : edgesNode) {
                    String source = eNode.has("source") ? eNode.get("source").asText() : null;
                    String destination = eNode.has("destination") ? eNode.get("destination").asText() : null;
                    String transport = eNode.has("transport") ? eNode.get("transport").asText() : "Unknown";
                    
                    double distance = eNode.has("distance") ? eNode.get("distance").asDouble(Double.POSITIVE_INFINITY) : Double.POSITIVE_INFINITY;
                    double time = eNode.has("time") ? eNode.get("time").asDouble(Double.POSITIVE_INFINITY) : Double.POSITIVE_INFINITY;
                    double price = eNode.has("price") ? eNode.get("price").asDouble(Double.POSITIVE_INFINITY) : Double.POSITIVE_INFINITY;
                    
                    if (source != null && destination != null) {
                        graph.addEdge(source, destination, transport, distance, time, price);
                    }
                }
            }
            
        } catch (Exception e) {
            System.err.println("Error reading JSON: " + e.getMessage());
        }

        return graph;
    }
}
