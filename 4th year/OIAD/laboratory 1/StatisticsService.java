package org.example.OIAD.lab1.solution;

import org.apache.commons.math3.stat.descriptive.DescriptiveStatistics;

import java.util.ArrayList;
import java.util.Collections;

public class StatisticsService {
    public StatisticsModal calculateParameters(PlantStorage storage) {
        StatisticsModal modal = new StatisticsModal();


        ArrayList<Double> dbHtValues = new ArrayList<>();
        for (PlantModal m : storage.getList()) {
            dbHtValues.add(m.getHt());
        }

        // Расчет статистических значений
        DescriptiveStatistics stats = new DescriptiveStatistics();
        for (double value : dbHtValues) {
            stats.addValue(value);
        }

        modal.setMax(stats.getMax());
        modal.setMin(stats.getMin());
        modal.setRange(modal.getMax() - modal.getMin());
        modal.setMean(stats.getMean());
        modal.setVariance(stats.getVariance());
        modal.setStdDeviation(Math.sqrt(modal.getVariance()));
        modal.setMedian(calculateMedian(dbHtValues));
        modal.setMode(calculateMode(dbHtValues));
        modal.setQ1(calculatePercentile(dbHtValues, 25));
        modal.setQ3(calculatePercentile(dbHtValues, 75));
        modal.setInterquartileRange(modal.getQ3() - modal.getQ1());
        modal.setSkewness(stats.getSkewness());
        modal.setKurtosis(stats.getKurtosis());

        return modal;
    }

    private static double calculateMedian(ArrayList<Double> values) {
        Collections.sort(values);
        int size = values.size();
        if (size % 2 == 0) {
            return (values.get(size / 2 - 1) + values.get(size / 2)) / 2.0;
        } else {
            return values.get(size / 2);
        }
    }

    private static double calculateMode(ArrayList<Double> values) {
        java.util.Map<Double, Integer> frequencyMap = new java.util.HashMap<>();
        for (double value : values) {
            frequencyMap.put(value, frequencyMap.getOrDefault(value, 0) + 1);
        }
        return frequencyMap.entrySet()
                .stream()
                .max(java.util.Map.Entry.comparingByValue())
                .get().getKey();
    }

    private static double calculatePercentile(ArrayList<Double> values, double percentile) {
        Collections.sort(values);
        int index = (int) Math.ceil(percentile / 100 * values.size()) - 1;
        return values.get(index);
    }
}
