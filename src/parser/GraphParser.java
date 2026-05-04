package parser;

import graph.Graph;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class GraphParser {

    /**
     * A very basic JSON parser using Regex (since standard Java doesn't have a built-in JSON library).
     * For production, please use Jackson or Google Gson.
     */
    public static Graph loadGraph(String filePath) {
        Graph graph = new Graph();
        
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            StringBuilder sb = new StringBuilder();
            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line);
            }
            String content = sb.toString();

            // Extract vertices (assuming "vertices": ["A", "B", ...])
            Pattern vertexPattern = Pattern.compile("\"vertices\"\\s*:\\s*\\[(.*?)\\]");
            Matcher vertexMatcher = vertexPattern.matcher(content);
            if (vertexMatcher.find()) {
                String verticesStr = vertexMatcher.group(1);
                Matcher vMatch = Pattern.compile("\"([^\"]+)\"").matcher(verticesStr);
                while (vMatch.find()) {
                    graph.addVertex(vMatch.group(1));
                }
            }

            // Extract edges
            Pattern edgeArrayPattern = Pattern.compile("\"edges\"\\s*:\\s*\\[(.*)\\]");
            Matcher edgeArrayMatcher = edgeArrayPattern.matcher(content);
            if (edgeArrayMatcher.find()) {
                String edgesStr = edgeArrayMatcher.group(1);
                
                // Matches individual edge objects { ... }
                Pattern edgeObjPattern = Pattern.compile("\\{(.*?)\\}", Pattern.DOTALL);
                Matcher edgeMatch = edgeObjPattern.matcher(edgesStr);
                
                while (edgeMatch.find()) {
                    String eStr = edgeMatch.group(1);
                    
                    String source = extractStringField(eStr, "source");
                    String destination = extractStringField(eStr, "destination");
                    String transport = extractStringField(eStr, "transport");
                    
                    double distance = extractDoubleField(eStr, "distance");
                    double time = extractDoubleField(eStr, "time");
                    double price = extractDoubleField(eStr, "price");
                    
                    if (source != null && destination != null) {
                        if (transport == null) transport = "Unknown";
                        graph.addEdge(source, destination, transport, distance, time, price);
                    }
                }
            }
            
        } catch (Exception e) {
            System.err.println("Error reading JSON: " + e.getMessage());
        }

        return graph;
    }
    
    private static String extractStringField(String data, String field) {
        Pattern p = Pattern.compile("\"" + field + "\"\\s*:\\s*\"([^\"]+)\"");
        Matcher m = p.matcher(data);
        if (m.find()) {
            return m.group(1);
        }
        return null;
    }
    
    private static double extractDoubleField(String data, String field) {
        Pattern p = Pattern.compile("\"" + field + "\"\\s*:\\s*([0-9]+\\.?[0-9]*)");
        Matcher m = p.matcher(data);
        if (m.find()) {
            return Double.parseDouble(m.group(1));
        }
        return Double.POSITIVE_INFINITY;
    }
}
