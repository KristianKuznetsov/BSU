package org.example.OIAD.lab1.solution;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;


public class SolverLab1 {
    public static void solve(){
        //Для сериализации объектов
        Gson gson = new GsonBuilder().setPrettyPrinting().create();

        //Для статистики
        StatisticsService statisticsService = new StatisticsService();

        //Для построения графиков
        ViewService viewService = new ViewService();

        //Вычитываем все данные из файла
        AvianHabitatObservationStorage avianHabitatObservationStorage = new AvianHabitatObservationStorage();
        avianHabitatObservationStorage.uploadData();

        //Выбираем данные для своего варианта
        PlantStorage dbStorage = new PlantStorage();
        dbStorage.convertToDbPlant(avianHabitatObservationStorage);

        //Выбираем данные для соседнего варианта + убираем нулевые
        PlantStorage wStorage = new PlantStorage();
        wStorage.convertToWPlant(avianHabitatObservationStorage);
        wStorage.removeZeroValues();
        wStorage.removeZeroVor();

        System.out.println("Первоночальное количество наблюдений -> " + dbStorage.getList().size());

        //Чистим по параметрам p и ht
        dbStorage.removeZeroValues();
        System.out.println("Количество наблюдений после удаление наблюдений где 0 в параметре p или ht -> " + dbStorage.getList().size());

        //Чистим по параметру vor
        dbStorage.removeZeroVor();
        System.out.println("Количество наблюдений после удаление наблюдений где 0 в параметре vor -> " + dbStorage.getList().size());

        //Вычисляем статистики для нашего вырианта по Ht
        StatisticsModal statisticsModal = (statisticsService.calculateParameters(dbStorage));

        System.out.println("Статистические праметры для DB (карликовая берёза)");
        System.out.println(gson.toJson(statisticsModal));

        //Данные для Python
        //Ибо к сожалению строить нормально графики в java я не научился
        System.out.println(viewService.getDataToTask3And4(dbStorage));
        System.out.println(viewService.getDataToTask3And4(wStorage));


    }


}
