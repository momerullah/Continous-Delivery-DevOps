import java.util.Scanner;

public class BMICalculator {

    // Method to calculate BMI
    public static double calculateBmi(double weight, double height) {
        if (height <= 0) {
            throw new IllegalArgumentException("Height must be greater than zero.");
        }
        if (weight <= 0) {
            throw new IllegalArgumentException("Weight must be greater than zero.");
        }
        return weight / (height * height);
    }

    // Method to determine weight target based on BMI and height
    public static Object[] determineWeightTarget(double bmi, double height) {
        if (bmi <= 0 || height <= 0) {
            throw new IllegalArgumentException("BMI and height must be greater than zero.");
        }
        double targetBmiLow = 18.5, targetBmiHigh = 24.9;
        if (bmi < targetBmiLow) {
            return new Object[]{targetBmiLow * (height * height), "gain"};
        } else if (bmi > targetBmiHigh) {
            return new Object[]{targetBmiHigh * (height * height), "lose"};
        } else {
            return new Object[]{null, "maintain"};
        }
    }

    // Main method
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter your weight in kg: ");
            double weight = scanner.nextDouble();

            System.out.print("Enter your height in meters: ");
            double height = scanner.nextDouble();

            double bmi = calculateBmi(weight, height);
            System.out.printf("Your BMI: %.1f%n", bmi);

            Object[] results = determineWeightTarget(bmi, height);
            Double targetWeight = (Double) results[0];
            String action = (String) results[1];

            if (targetWeight != null) {
                double difference = targetWeight - weight;
                System.out.printf("To reach a normal BMI, you need to %s %.1f kg.%n", action, Math.abs(difference));
            } else {
                System.out.println("Your weight is within the normal range.");
            }
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Invalid input.");
        } finally {
            scanner.close();
        }
    }
}
