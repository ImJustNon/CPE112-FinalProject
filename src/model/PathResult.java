package model;

import java.util.List;

public class PathResult {
    private List<String> path;
    private List<Edge> edgesUsed;

    public PathResult(List<String> path, List<Edge> edgesUsed) {
        this.path = path;
        this.edgesUsed = edgesUsed;
    }

    public List<String> getPath() { return path; }
    public List<Edge> getEdgesUsed() { return edgesUsed; }
}
