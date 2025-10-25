#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_SENSORS 5
#define NUM_READINGS 1000

// Function to simulate reading sensor data
int read_sensor(int sensor_id) {
    // Random integer between 20 and 100 as sensor value
    return 20 + rand() % 81;
}

// Simple processing: compute the average of sensor readings
double process_data(int readings[], int size) {
    int sum = 0;
    for(int i = 0; i < size; i++) {
        sum += readings[i];
    }
    return (double)sum / size;
}

int main() {
    srand(time(NULL));

    int sensor_readings[NUM_SENSORS];
    double averages[NUM_SENSORS];
    for(int reading = 0; reading < NUM_READINGS; reading++) {
        // Simulate reading each sensor
        for(int s = 0; s < NUM_SENSORS; s++) {
            sensor_readings[s] = read_sensor(s);
        }

        // Process the data: compute average for each sensor
        for(int s = 0; s < NUM_SENSORS; s++) {
            averages[s] = process_data(sensor_readings, 1); // per-sensor average
        }

        // Output results every 100 readings
        if (reading % 100 == 0) {
            printf("Reading %d:\n", reading);
            for(int s = 0; s < NUM_SENSORS; s++) {
                printf("  Sensor %d average: %.2f\n", s, averages[s]);
            }
        }
    }

    return 0;
}

