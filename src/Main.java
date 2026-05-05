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

        java.util.Set<String> validSources = new java.util.TreeSet<>();
        java.util.Set<String> validDestinations = new java.util.TreeSet<>();
        for (String v : graph.getVertices()) {
            if (!graph.getNeighbors(v).isEmpty()) validSources.add(v);
            for (Edge e : graph.getNeighbors(v)) validDestinations.add(e.getDestination());
        }

        System.out.println("\nAvailable source province(s):");
        java.util.List<String> sourceDisplayList = new java.util.ArrayList<>();
        for (String s : validSources) {
            String code = PROVINCE_CODES.getOrDefault(s, "N/A");
            sourceDisplayList.add(s + "(" + code + ")");
        }
        System.out.println(String.join(", ", sourceDisplayList));
        System.out.print("Enter source province (Name or Code): ");
        String sourceInput = scanner.nextLine().trim();
        String source = CODE_TO_PROVINCE.getOrDefault(sourceInput.toUpperCase(), sourceInput);
        if (!validSources.contains(source)) {
            System.out.println("Error: '" + sourceInput + "' is not a valid source location in the data.");
            return;
        }

        System.out.println("\nAvailable destination province(s):");
        java.util.List<String> destDisplayList = new java.util.ArrayList<>();
        for (String d : validDestinations) {
            String code = PROVINCE_CODES.getOrDefault(d, "N/A");
            destDisplayList.add(d + " (" + code + ")");
        }
        System.out.println(String.join(", ", destDisplayList));
        System.out.print("Enter destination province (Name or Code): ");
        String destInput = scanner.nextLine().trim();
        String destination = CODE_TO_PROVINCE.getOrDefault(destInput.toUpperCase(), destInput);
        if (!validDestinations.contains(destination)) {
            System.out.println("Error: '" + destInput + "' is not a valid destination location in the data.");
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
