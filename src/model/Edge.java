package model;

public class Edge {
    private String destination;
    private String transport;
    private double distance;
    private double time;
    private double price;

    public Edge(String destination, String transport, double distance, double time, double price) {
        this.destination = destination;
        this.transport = transport;
        this.distance = distance;
        this.time = time;
        this.price = price;
    }

    public String getDestination() { return destination; }
    public String getTransport() { return transport; }
    public double getDistance() { return distance; }
    public double getTime() { return time; }
    public double getPrice() { return price; }

    public double getWeight(boolean useDistance, boolean useTime, boolean usePrice) {
        double weight = 0;
        if (useDistance) weight += distance;
        if (useTime) weight += time;
        if (usePrice) weight += price;
        return weight;
    }
}
