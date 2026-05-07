import algorithm.DijkstraOptimizer;
import graph.Graph;
import model.Edge;
import model.PathResult;
import parser.GraphParser;

import java.io.File;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    private static final Map<String, String> PROVINCE_CODES = new HashMap<>();
    private static final Map<String, String> CODE_TO_PROVINCE = new HashMap<>();

    static {
        String[][] codes = {
            {"กทม", "BKK"}, {"กระบี่", "KBI"}, {"กาญจนบุรี", "KAN"}, {"กาฬสินธุ์", "KAL"}, {"กำแพงเพชร", "KPT"}, 
            {"ขอนแก่น", "KKC"}, {"จันทบุรี", "CTI"}, {"ฉะเชิงเทรา", "CCO"}, {"ชลบุรี", "CHB"}, {"ชัยนาท", "CNT"}, 
            {"ชัยภูมิ", "CPM"}, {"ชุมพร", "CJM"}, {"เชียงราย", "CEI"}, {"เชียงใหม่", "CNX"}, {"ตรัง", "TST"}, 
            {"ตราด", "TDX"}, {"ตาก", "TAK"}, {"นครนายก", "NYK"}, {"นครปฐม", "NPT"}, {"นครพนม", "KOP"}, 
            {"นครราชสีมา", "NAK"}, {"นครศรีธรรมราช", "NST"}, {"นครสวรรค์", "NWN"}, {"นนทบุรี", "NBI"}, 
            {"นราธิวาส", "NAW"}, {"น่าน", "NNT"}, {"บึงกาฬ", "BKN"}, {"บุรีรัมย์", "BFV"}, {"ปทุมธานี", "PTE"}, 
            {"ประจวบคีรีขันธ์", "PKN"}, {"ปราจีนบุรี", "PRI"}, {"ปัตตานี", "PTN"}, {"พระนครศรีอยุธยา", "AYA"}, 
            {"พะเยา", "PYO"}, {"พังงา", "PNA"}, {"พัทลุง", "PLG"}, {"พิจิตร", "PCT"}, {"พิษณุโลก", "PHS"}, 
            {"เพชรบุรี", "PBI"}, {"เพชรบูรณ์", "PHY"}, {"แพร่", "PRH"}, {"ภูเก็ต", "HKT"}, {"มหาสารคาม", "MKM"}, 
            {"มุกดาหาร", "MDH"}, {"แม่ฮ่องสอน", "HGN"}, {"ยโสธร", "YST"}, {"ยะลา", "YLA"}, {"ร้อยเอ็ด", "ROI"}, 
            {"ระนอง", "UNN"}, {"ระยอง", "RYG"}, {"ราชบุรี", "RBR"}, {"ลพบุรี", "LRI"}, {"ลำปาง", "LPT"}, 
            {"ลำพูน", "LPN"}, {"เลย", "LOE"}, {"ศรีสะเกษ", "SSK"}, {"สกลนคร", "SNO"}, {"สงขลา", "SGZ"}, 
            {"สตูล", "SAT"}, {"สมุทรปราการ", "SPK"}, {"สมุทรสงคราม", "SKM"}, {"สมุทรสาคร", "SKN"}, 
            {"สระแก้ว", "SKW"}, {"สระบุรี", "SRI"}, {"สิงห์บุรี", "SBR"}, {"สุโขทัย", "THS"}, 
            {"สุพรรณบุรี", "SPB"}, {"สุราษฎร์ธานี", "URT"}, {"สุรินทร์", "SRN"}, {"หนองคาย", "NKI"}, 
            {"หนองบัวลำภู", "NBP"}, {"อ่างทอง", "ATG"}, {"อำนาจเจริญ", "ACR"}, {"อุดรธานี", "UTH"}, 
            {"อุตรดิตถ์", "UTD"}, {"อุทัยธานี", "UTI"}, {"อุบลราชธานี", "UBP"}
        };
        for (String[] pair : codes) {
            PROVINCE_CODES.put(pair[0], pair[1]);
            CODE_TO_PROVINCE.put(pair[1].toUpperCase(), pair[0]);
        }
    }

    public static void main(String[] args) {
        Graph graph = initializeGraph();
        if (graph == null) return;

        Scanner scanner = new Scanner(System.in);
        
        boolean[] preferences = getOptimizationPreferences(scanner);
        if (preferences == null) {
            scanner.close();
            return;
        }

        java.util.Set<String> validSources = new java.util.TreeSet<>();
        java.util.Set<String> validDestinations = new java.util.TreeSet<>();
        extractValidLocations(graph, validSources, validDestinations);

        String source = promptLocation(scanner, "source", validSources);
        if (source == null) {
            scanner.close();
            return;
        }

        String destination = promptLocation(scanner, "destination", validDestinations);
        if (destination == null) {
            scanner.close();
            return;
        }

        optimizeAndPrintRoute(graph, source, destination, preferences[0], preferences[1], preferences[2]);
        
        scanner.close();
    }

    private static Graph initializeGraph() {
        String jsonFile = "src/weight/travel_weight.json";
        if (!new File(jsonFile).exists()) {
            jsonFile = "travel_weight.json";
            if (!new File(jsonFile).exists()) {
                System.out.println("Could not find JSON data file.");
                return null;
            }
        }

        System.out.println("Loading graph data...");
        Graph graph = GraphParser.loadGraph(jsonFile);
        System.out.println("Loaded " + graph.getVertices().size() + " vertices.\n");
        return graph;
    }

    private static boolean[] getOptimizationPreferences(Scanner scanner) {
        System.out.println("=== Route Optimization ===");
        System.out.println("What do you want to save the most? (Minimize)");
        System.out.println("You can choose multiple separated by commas (e.g., 1,3 or 1,2,3)");
        System.out.println("1. Distance (km)");
        System.out.println("2. Time (minutes)");
        System.out.println("3. Price (Baht)");
        System.out.print("Enter your choice(s) (1-3): ");
        
        String choiceInput = scanner.nextLine().trim();
        boolean useDist = choiceInput.contains("1");
        boolean useTime = choiceInput.contains("2");
        boolean usePrice = choiceInput.contains("3");

        if (!useDist && !useTime && !usePrice) {
            System.out.println("Invalid choice. Exiting.");
            return null;
        }
        return new boolean[]{useDist, useTime, usePrice};
    }

    private static void extractValidLocations(Graph graph, java.util.Set<String> validSources, java.util.Set<String> validDestinations) {
        for (String v : graph.getVertices()) {
            if (!graph.getNeighbors(v).isEmpty()) validSources.add(v);
            for (Edge e : graph.getNeighbors(v)) validDestinations.add(e.getDestination());
        }
    }

    private static void displayLocations(java.util.Set<String> locations) {
        java.util.List<String> displayList = new java.util.ArrayList<>();
        for (String loc : locations) {
            String code = PROVINCE_CODES.getOrDefault(loc, "N/A");
            displayList.add(loc + " (" + code + ")");
        }
        for (int i = 0; i < displayList.size(); i++) {
            System.out.printf("%-32s", displayList.get(i));
            if ((i + 1) % 3 == 0) System.out.println();
        }
        if (displayList.size() % 3 != 0) System.out.println();
    }

    private static String promptLocation(Scanner scanner, String locationType, java.util.Set<String> validLocations) {
        System.out.println("\nAvailable " + locationType + " province(s):");
        displayLocations(validLocations);
        
        System.out.print("\nEnter " + locationType + " province (Name or Code): ");
        String input = scanner.nextLine().trim();
        String location = CODE_TO_PROVINCE.getOrDefault(input.toUpperCase(), input);
        
        if (!validLocations.contains(location)) {
            System.out.println("Error: '" + input + "' is not a valid " + locationType + " location in the data.");
            return null;
        }
        return location;
    }

    private static void optimizeAndPrintRoute(Graph graph, String source, String destination, 
                                              boolean useDist, boolean useTime, boolean usePrice) {
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
    }
}
