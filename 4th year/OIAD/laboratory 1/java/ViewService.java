package org.example.OIAD.lab1.solution;

public class ViewService {


    public String getDataToTask3And4(PlantStorage storage){

        StringBuilder builder = new StringBuilder();
        builder.append("np.array([");

        for (PlantModal modal : storage.getList()){
            builder.append(modal.getHt());
            builder.append(", ");
        }
        builder.setLength(builder.length() - 2);
        builder.append("])");
        return builder.toString();
    }


}
