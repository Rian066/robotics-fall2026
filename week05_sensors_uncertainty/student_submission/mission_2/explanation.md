# Mission 2

## comparison

For moving average windows 3, 7, and 11, the RMSE increased from 0.1395 to 0.1504 to 0.1601 m. All three had a delay of 1.10 seconds. The median window 3 had a slightly lower RMSE of 0.1389 m compared to 0.1395 m for moving average window 3. This shows the median performed slightly better.

## fusion_choice

With the median filter, weight 0.25 had an RMSE of 0.1389 m and a delay of 1.10 seconds. Weight 0.50 had an RMSE of 0.1270 m and a delay of 0.90 seconds. Weight 0.75 had an RMSE of 0.1335 m and a delay of 0.45 seconds. I would select 0.50 because it had the lowest RMSE. It balances noisy Sensor A with Sensor B, which is steadier but biased and slower.

## manual_average

4.17

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

I predict the median filter will handle outliers better than the moving average. A larger window will make readings smoother but may increase response delay. Changing the weight will change which sensor has more influence.

## responsiveness

Smoothing reduces noise but can slow down the robot's response. My three moving average windows all had a delay of 1.10 seconds, so larger windows did not increase the measured delay in this test. The fastest result was 0.45 seconds with median window 3 and weight 0.75. A longer delay could make the robot react too late when someone walks in front of it.

## selected

0
