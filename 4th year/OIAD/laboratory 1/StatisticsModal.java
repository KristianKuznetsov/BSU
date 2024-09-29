package org.example.OIAD.lab1.solution;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class StatisticsModal {
    private double max;                // Максимальное значение
    private double min;                // Минимальное значение
    private double range;              // Размах распределения
    private double mean;               // Среднее значение
    private double median;             // Медиана
    private double mode;               // Мода
    private double variance;           // Дисперсия
    private double stdDeviation;       // Среднеквадратическое отклонение
    private double q1;                 // Первый квартиль
    private double q3;                 // Третий квартиль
    private double interquartileRange; // Интерквартильный размах
    private double skewness;           // Асимметрия
    private double kurtosis;           // Эксцесс
}
