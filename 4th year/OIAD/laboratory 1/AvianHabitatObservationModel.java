package org.example.OIAD.lab1.solution;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class AvianHabitatObservationModel {

        @JsonProperty("Site")
        private String site;

        @JsonProperty("Observer")
        private String observer;

        @JsonProperty("Subpoint")
        private int subpoint;

        @JsonProperty("VOR")
        private double vor;

        @JsonProperty("PDB")
        private double pdb;

        @JsonProperty("DBHt")
        private double dbHt;

        @JsonProperty("PW")
        private double pw;

        @JsonProperty("WHt")
        private double wht;

        @JsonProperty("PE")
        private int pe;

        @JsonProperty("EHt")
        private double eht;

        @JsonProperty("PA")
        private int pa;

        @JsonProperty("AHt")
        private double aht;

        @JsonProperty("PH")
        private double ph;

        @JsonProperty("HHt")
        private double hht;

        @JsonProperty("PL")
        private double pl;

        @JsonProperty("LHt")
        private double lht;

        @JsonProperty("PB")
        private double pb;
}
