package org.example.OIAD.lab1.solution;

import lombok.Getter;

import java.util.ArrayList;

@Getter
public class PlantStorage {
    private final ArrayList<PlantModal> list;

    public PlantStorage() {
        this.list = new ArrayList<>();
    }

    public void add(PlantModal modal) {
        this.list.add(modal);
    }

    public void convertToDbPlant(AvianHabitatObservationStorage storage){
        for (AvianHabitatObservationModel modal : storage.getList()) {
            add(new PlantModal(modal.getSite(),
                    modal.getObserver(),
                    modal.getSubpoint(),
                    modal.getVor(),
                    modal.getPdb(),
                    modal.getDbHt()));
        }
    }

    public void convertToWPlant(AvianHabitatObservationStorage storage){
        for (AvianHabitatObservationModel modal : storage.getList()) {
            add(new PlantModal(modal.getSite(),
                    modal.getObserver(),
                    modal.getSubpoint(),
                    modal.getVor(),
                    modal.getPw(),
                    modal.getWht()));
        }
    }

    public void removeZeroValues(){
        list.removeIf(modal -> modal.getP() == 0.0 || modal.getHt() == 0.0);
    }

    public void removeZeroVor(){
        list.removeIf(modal -> modal.getVor() == 0.0);
    }

}
