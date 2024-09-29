package org.example.OIAD.lab1.solution;

import com.fasterxml.jackson.dataformat.csv.CsvMapper;
import com.fasterxml.jackson.dataformat.csv.CsvSchema;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class AvianHabitatObservationStorage {
    private final String FILE_PATH = "src\\main\\java\\org\\example\\OIAD\\lab1\\resource\\avianHabitat.csv";

    private ArrayList<AvianHabitatObservationModel> list;

    public AvianHabitatObservationStorage() {
        list = new ArrayList<>();
    }

    public ArrayList<AvianHabitatObservationModel> getList() {
        return list;
    }

    public void uploadData() {

        CsvMapper csvMapper = new CsvMapper();
        CsvSchema schema = CsvSchema.emptySchema().withHeader();

        try {
            List<Object> data = csvMapper.readerFor(AvianHabitatObservationModel.class)
                    .with(schema)
                    .readValues(new File(FILE_PATH))
                    .readAll();

            for (Object observation : data) {
                    list.add((AvianHabitatObservationModel) observation);
            }

        } catch (IOException e) {
            System.out.println("yps.... " + e.getMessage());
        }

    }

}
