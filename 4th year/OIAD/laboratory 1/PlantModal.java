package org.example.OIAD.lab1.solution;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PlantModal {
    private String site;
    private String observer;
    private int subpoint;
    private double vor;
    private double p;
    private double ht;
}
