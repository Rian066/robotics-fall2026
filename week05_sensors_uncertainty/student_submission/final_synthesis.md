# Final synthesis

In this lab, I learned how sensor errors affect robot decisions and safety. In Mission 1, I studied 240 sensor readings and found that the sensor had a bias of -0.0141 m, a variance of 0.00431 m², 6 missing readings, and 1 outlier. This showed me that sensors are not always accurate, even when the object is not moving.

In Mission 2, I tested different filters and sensor weights. The median filter worked slightly better than the moving average because it handled outliers better. Using a median filter with window 3 and weight 0.50 gave the lowest RMSE of 0.1270 m. I also learned that smoother readings can sometimes make the robot respond more slowly.

In Mission 3, I tested how sensor estimates affect robot movement. My revised warehouse policy reduced the maximum delay from 0.10 seconds to 0 seconds. However, the false-safe rate stayed at 0.62%. This showed that faster responses do not always remove safety risks.

Overall, I learned that robot safety depends on accurate sensors, good filtering, and careful decisions. Different environments need different safety settings, especially when robots work near people.