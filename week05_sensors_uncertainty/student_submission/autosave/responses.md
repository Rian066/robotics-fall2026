# Week 5: Sensors, Noise, and Uncertainty

- course_id: CSCI 39536 
- email: Rian.Alif58@login.cuny.edu
- name: Rian M Alif

## concepts.observation

The bias changes where the median is, and the noise increases the total number of data for the graphs.

## final.course_reflection

This activity helped me understand how robots use sensor information to make decisions. I found it interesting that even small sensor errors can affect how a robot moves.

I also learned that making a robot work correctly is not enough. We must think about the safety of people around it. For example, a robot that reacts too slowly could hurt someone, while a robot that stops too often could cause problems.

The most interesting part was testing different filters and seeing how the results changed. This activity made me more interested in robotics and how programming can solve real-world problems. I would like to learn more about making robots safer and more reliable in the future.

## final.synthesis

In this lab, I learned how sensor errors affect robot decisions and safety. In Mission 1, I studied 240 sensor readings and found that the sensor had a bias of -0.0141 m, a variance of 0.00431 m², 6 missing readings, and 1 outlier. This showed me that sensors are not always accurate, even when the object is not moving.

In Mission 2, I tested different filters and sensor weights. The median filter worked slightly better than the moving average because it handled outliers better. Using a median filter with window 3 and weight 0.50 gave the lowest RMSE of 0.1270 m. I also learned that smoother readings can sometimes make the robot respond more slowly.

In Mission 3, I tested how sensor estimates affect robot movement. My revised warehouse policy reduced the maximum delay from 0.10 seconds to 0 seconds. However, the false-safe rate stayed at 0.62%. This showed that faster responses do not always remove safety risks.

Overall, I learned that robot safety depends on accurate sensors, good filtering, and careful decisions. Different environments need different safety settings, especially when robots work near people.

## mission_1.bias

-0.0141

## mission_1.bias_vs_variance

Bias shows how far the average reading is from the true distance. Variance shows how much the readings change. My sensor has a small bias of -0.0141 m and a variance of 0.00431 m^2.

## mission_1.dropouts

6

## mission_1.mean

1.99

## mission_1.median

2

## mission_1.more_samples

No, more samples would not fix the main problem. Most readings are rounded to 2.0 m or 1.9 m, which shows quantization. More samples cannot remove this rounding.

## mission_1.outliers

1

## mission_1.prediction

A biased sensor will consistently give readings above or below 2.00 m. A noisy sensor will give readings that randomly change around 2.00 m. I would check the average and how spread out the 240 readings are to tell the difference.

## mission_1.prediction_draft

A biased sensor will consistently give readings above or below 2.00 m. A noisy sensor will give readings that randomly change around 2.00 m. I would check the average and how spread out the 240 readings are to tell the difference.

## mission_1.profile

quantized

## mission_1.robot_consequence

The robot might think an obstacle is closer or farther than it really is because the readings are rounded. This could cause it to stop unnecessarily or move too close to a person.

## mission_1.variance

0.00431

## mission_2.comparison

For moving average windows 3, 7, and 11, the RMSE increased from 0.1395 to 0.1504 to 0.1601 m. All three had a delay of 1.10 seconds. The median window 3 had a slightly lower RMSE of 0.1389 m compared to 0.1395 m for moving average window 3. This shows the median performed slightly better.

## mission_2.fusion_choice

With the median filter, weight 0.25 had an RMSE of 0.1389 m and a delay of 1.10 seconds. Weight 0.50 had an RMSE of 0.1270 m and a delay of 0.90 seconds. Weight 0.75 had an RMSE of 0.1335 m and a delay of 0.45 seconds. I would select 0.50 because it had the lowest RMSE. It balances noisy Sensor A with Sensor B, which is steadier but biased and slower.

## mission_2.manual_average

4.17

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

I predict the median filter will handle outliers better than the moving average. A larger window will make readings smoother but may increase response delay. Changing the weight will change which sensor has more influence.

## mission_2.responsiveness

Smoothing reduces noise but can slow down the robot's response. My three moving average windows all had a delay of 1.10 seconds, so larger windows did not increase the measured delay in this test. The fastest result was 0.45 seconds with median window 3 and weight 0.75. A longer delay could make the robot react too late when someone walks in front of it.

## mission_2.selected

0

## mission_3.Assistive.prediction_draft

I predict the revised policy will be more careful around people and avoid moving with missing sensor data. However, it may stop more often.

## mission_3.Warehouse.prediction_draft

I predict this policy will stop the robot near obstacles, but sensor errors and delays could cause unsafe movement. It may also stop unnecessarily.

## mission_3.context_comparison

I increased the warehouse caution margin from 0.10 to 0.20 m and Sensor A's weight from 0.35 to 0.50. Delay improved from 0.10 to 0 seconds, while the false-safe rate stayed at 0.62%. Assistive robots need extra caution because they work closely with people.

## mission_3.error_costs

In warehouses, unsafe movement can hurt workers, while unnecessary stops slow down work. My false-safe rate was 0.62%, and unnecessary stops were 5.61%. The revised policy reduced delay from 0.10 to 0 seconds. For assistive robots, unsafe movement could hurt users or limit their independence.

## mission_3.limitations

The seven tests show how the robot handles obstacles, sensor errors, and missing readings. My warehouse policy had zero dangerous events, but simulations cannot guarantee real-world safety. I would ask workers for feedback and test the robot with real obstacles before using it.
