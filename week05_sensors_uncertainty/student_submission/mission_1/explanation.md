# Mission 1

## bias

-0.0141

## bias_vs_variance

Bias shows how far the average reading is from the true distance. Variance shows how much the readings change. My sensor has a small bias of -0.0141 m and a variance of 0.00431 m^2.

## dropouts

6

## mean

1.99

## median

2

## more_samples

No, more samples would not fix the main problem. Most readings are rounded to 2.0 m or 1.9 m, which shows quantization. More samples cannot remove this rounding.

## outliers

1

## prediction

A biased sensor will consistently give readings above or below 2.00 m. A noisy sensor will give readings that randomly change around 2.00 m. I would check the average and how spread out the 240 readings are to tell the difference.

## prediction_draft

A biased sensor will consistently give readings above or below 2.00 m. A noisy sensor will give readings that randomly change around 2.00 m. I would check the average and how spread out the 240 readings are to tell the difference.

## profile

quantized

## robot_consequence

The robot might think an obstacle is closer or farther than it really is because the readings are rounded. This could cause it to stop unnecessarily or move too close to a person.

## variance

0.00431
