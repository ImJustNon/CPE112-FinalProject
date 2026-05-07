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
    private static final Map<String, String> PROVINCE_TO_REGION = new HashMap<>();

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

        // Region categorization
        String[] north = {"เชียงราย", "เชียงใหม่", "น่าน", "พะเยา", "แพร่", "แม่ฮ่องสอน", "ลำปาง", "ลำพูน", "อุตรดิตถ์"};
        String[] northEast = {"กาฬสินธุ์", "ขอนแก่น", "ชัยภูมิ", "นครพนม", "นครราชสีมา", "บึงกาฬ", "บุรีรัมย์", "มหาสารคาม", "มุกดาหาร", "ยโสธร", "ร้อยเอ็ด", "เลย", "ศรีสะเกษ", "สกลนคร", "สุรินทร์", "หนองคาย", "หนองบัวลำภู", "อำนาจเจริญ", "อุดรธานี", "อุบลราชธานี"};
        String[] west = {"กาญจนบุรี", "ตาก", "ประจวบคีรีขันธ์", "เพชรบุรี", "ราชบุรี"};
        String[] east = {"จันทบุรี", "ฉะเชิงเทรา", "ชลบุรี", "ตราด", "ปราจีนบุรี", "ระยอง", "สระแก้ว"};
        String[] south = {"กระบี่", "ชุมพร", "ตรัง", "นครศรีธรรมราช", "นราธิวาส", "ปัตตานี", "พังงา", "พัทลุง", "ภูเก็ต", "ยะลา", "ระนอง", "สงขลา", "สตูล", "สุราษฎร์ธานี"};
        // Everything else will default to Central ("ภาคกลาง")
        
        for (String p : north) PROVINCE_TO_REGION.put(p, "ภาคเหนือ");
        for (String p : northEast) PROVINCE_TO_REGION.put(p, "ภาคตะวันออกเฉียงเหนือ");
        for (String p : west) PROVINCE_TO_REGION.put(p, "ภาคตะวันตก");
        for (String p : east) PROVINCE_TO_REGION.put(p, "ภาคตะวันออก");
        for (String p : south) PROVINCE_TO_REGION.put(p, "ภาคใต้");
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
        String[] regions = {"ภาคเหนือ", "ภาคตะวันออกเฉียงเหนือ", "ภาคกลาง", "ภาคตะวันออก", "ภาคตะวันตก", "ภาคใต้"};
        Map<String, java.util.List<String>> byRegion = new java.util.LinkedHashMap<>();
        for (String r : regions) {
            byRegion.put(r, new java.util.ArrayList<>());
        }

        for (String loc : locations) {
            String region = PROVINCE_TO_REGION.getOrDefault(loc, "ภาคกลาง");
            String code = PROVINCE_CODES.getOrDefault(loc, "N/A");
            byRegion.get(region).add(" " + loc + " (" + code + ")");
        }

        for (String region : regions) {
            java.util.List<String> list = byRegion.get(region);
            if (list.isEmpty()) continue;

            System.out.println("┌────────────────────────────────────────────────────────────────────────┐");
            System.out.println("│ " + padRightCenter(region, 70) + " │");
            System.out.println("├────────────────────────────────────────────────────────────────────────┤");

            for (int i = 0; i < list.size(); i += 3) {
                String col1 = list.get(i);
                String col2 = (i + 1 < list.size()) ? list.get(i + 1) : "";
                String col3 = (i + 2 < list.size()) ? list.get(i + 2) : "";

                System.out.println("│" + padRightThai(col1, 24) + padRightThai(col2, 24) + padRightThai(col3, 24) + "│");
            }
            System.out.println("└────────────────────────────────────────────────────────────────────────┘");
        }
    }

    private static int getDisplayLength(String str) {
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            // Ignore Thai upper/lower combining characters for display width calculation
            if ((c >= '\u0E31' && c <= '\u0E31') || 
                (c >= '\u0E34' && c <= '\u0E3A') || 
                (c >= '\u0E47' && c <= '\u0E4E')) {
                continue;
            }
            count++;
        }
        return count;
    }

    private static String padRightThai(String s, int n) {
        int pad = n - getDisplayLength(s);
        if (pad <= 0) return s;
        StringBuilder sb = new StringBuilder(s);
        for (int i = 0; i < pad; i++) sb.append(" ");
        return sb.toString();
    }

    private static String padRightCenter(String s, int n) {
        int len = getDisplayLength(s);
        int pad = n - len;
        if (pad <= 0) return s;
        int leftPad = pad / 2;
        int rightPad = pad - leftPad;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < leftPad; i++) sb.append(" ");
        sb.append(s);
        for (int i = 0; i < rightPad; i++) sb.append(" ");
        return sb.toString();
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
