import algorithm.DijkstraOptimizer;
import graph.Graph;
import model.Edge;
import model.PathResult;
import parser.GraphParser;

import java.io.File;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String jsonFile = "data/weight_data.json";
        if (!new File(jsonFile).exists()) {
            jsonFile = "weight_data.json";
            if (!new File(jsonFile).exists()) {
                System.out.println("Could not find JSON data file.");
                return;
            }
        }

        System.out.println("Loading graph data...");
        Graph graph = GraphParser.loadGraph(jsonFile);
        
        System.out.println("Loaded " + graph.getVertices().size() + " vertices.\n");

        System.out.println("=== Route Optimization ===");
        System.out.println("What do you want to save the most? (Minimize)");
        System.out.println("You can choose multiple separated by commas (e.g., 1,3 or 1,2,3)");
        System.out.println("1. Distance (km)");
        System.out.println("2. Time (minutes)");
        System.out.println("3. Price (Baht)");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your choice(s) (1-3): ");
        String choiceInput = scanner.nextLine().trim();

        boolean useDist = choiceInput.contains("1");
        boolean useTime = choiceInput.contains("2");
        boolean usePrice = choiceInput.contains("3");

        if (!useDist && !useTime && !usePrice) {
            System.out.println("Invalid choice. Exiting.");
            return;
        }

        System.out.print("Enter source province: ");
        String source = scanner.nextLine().trim();
        if (!graph.getVertices().contains(source)) {
            System.out.println("Error: '" + source + "' is not a valid location in the data.");
            return;
        }

        System.out.print("Enter destination province: ");
        String destination = scanner.nextLine().trim();
        if (!graph.getVertices().contains(destination)) {
            System.out.println("Error: '" + destination + "' is not a valid location in the data.");
            return;
        }

        try {
            DijkstraOptimizer optimizer = new DijkstraOptimizer();
            PathResult result = optimizer.findShortestPath(graph, source, destination, useDist, useTime, usePrice);

            if (result == null) {
                System.out.println("\nNo path found between '" + source + "' and '" + destination + "'.");
                return;
            }

            System.out.println("\n=== Best Route Found ===");
            System.out.println("Path: " + String.join(" -> ", result.getPath()) + "\n");

            System.out.println("Detailed steps:");
            double totalDist = 0, totalTime = 0, totalPrice = 0;

            for (int i = 0; i < result.getEdgesUsed().size(); i++) {
                Edge edge = result.getEdgesUsed().get(i);
                String from = result.getPath().get(i);
                String to = result.getPath().get(i + 1);

                totalDist += edge.getDistance();
                totalTime += edge.getTime();
                totalPrice += edge.getPrice();

                System.out.println((i + 1) + ". " + from + " -> " + to + " (via " + edge.getTransport() + ")");
                System.out.printf("   Distance: %.1fkm, Time: %.1fm, Price: %.1f฿\n", 
                                  edge.getDistance(), edge.getTime(), edge.getPrice());
            }

            System.out.println("----------------------------------------");
            System.out.printf("Totals -> Distance: %.1fkm | Time: %.1fm | Price: %.1f฿\n", 
                              totalDist, totalTime, totalPrice);
                              
        } catch (Exception e) {
            System.out.println("\nAn error occurred: " + e.getMessage());
            e.printStackTrace();
        }
        
        scanner.close();
    }
}
