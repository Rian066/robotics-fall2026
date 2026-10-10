# Mission 3

## Assistive.prediction_draft

I predict the revised policy will be more careful around people and avoid moving with missing sensor data. However, it may stop more often.

## Warehouse.prediction_draft

I predict this policy will stop the robot near obstacles, but sensor errors and delays could cause unsafe movement. It may also stop unnecessarily.

## context_comparison

I increased the warehouse caution margin from 0.10 to 0.20 m and Sensor A's weight from 0.35 to 0.50. Delay improved from 0.10 to 0 seconds, while the false-safe rate stayed at 0.62%. Assistive robots need extra caution because they work closely with people.

## error_costs

In warehouses, unsafe movement can hurt workers, while unnecessary stops slow down work. My false-safe rate was 0.62%, and unnecessary stops were 5.61%. The revised policy reduced delay from 0.10 to 0 seconds. For assistive robots, unsafe movement could hurt users or limit their independence.

## limitations

The seven tests show how the robot handles obstacles, sensor errors, and missing readings. My warehouse policy had zero dangerous events, but simulations cannot guarantee real-world safety. I would ask workers for feedback and test the robot with real obstacles before using it.
