package parser;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import graph.Graph;

import java.io.FileReader;

public class GraphParser {

    public static Graph loadGraph(String filePath) {
        Graph graph = new Graph();
        
        try (FileReader reader = new FileReader(filePath)) {
            JsonObject jsonObject = JsonParser.parseReader(reader).getAsJsonObject();
            
            // Extract vertices
            if (jsonObject.has("vertices")) {
                JsonArray verticesArray = jsonObject.getAsJsonArray("vertices");
                for (JsonElement vElement : verticesArray) {
                    graph.addVertex(vElement.getAsString());
                }
            }

            // Extract edges
            if (jsonObject.has("edges")) {
                JsonArray edgesArray = jsonObject.getAsJsonArray("edges");
                for (JsonElement eElement : edgesArray) {
                    JsonObject eObj = eElement.getAsJsonObject();
                    
                    String source = eObj.has("source") ? eObj.get("source").getAsString() : null;
                    String destination = eObj.has("destination") ? eObj.get("destination").getAsString() : null;
                    String transport = eObj.has("transport") ? eObj.get("transport").getAsString() : "Unknown";
                    
                    double distance = eObj.has("distance") ? eObj.get("distance").getAsDouble() : Double.POSITIVE_INFINITY;
                    double time = eObj.has("time") ? eObj.get("time").getAsDouble() : Double.POSITIVE_INFINITY;
                    double price = eObj.has("price") ? eObj.get("price").getAsDouble() : Double.POSITIVE_INFINITY;
                    
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
