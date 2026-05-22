# Sensor Log SW-MAR-2024

location: Tide Elevator
capture-date: 2023-10-07
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
04:00,78,5,34.79,muffled choir,floor darkening
04:15,84,13,14.6,bell once,light below surface
04:30,87,15,33.3,distant surf,floor darkening
04:45,69,22,19.32,pipe hum,door reflected
05:00,73,28,7.03,static shaped like rain,footprints arrive
05:15,77,26,22.34,pipe hum,footprints arrive
05:30,83,27,6.77,bell once,foam under desk
05:45,92,30,35.62,static shaped like rain,floor darkening
06:00,76,39,15.44,muffled choir,floor darkening
06:15,86,42,31.42,gull indoors,wrong ceiling
06:30,98,51,29.94,none,light below surface
06:45,95,57,12.79,none,wrong ceiling
07:00,78,55,29.01,none,foam under desk
07:15,90,55,18.52,static shaped like rain,wrong ceiling
07:30,73,53,26.06,distant surf,door reflected
07:45,86,62,25.02,static shaped like rain,wrong ceiling
08:00,82,67,14.68,gull indoors,clear
08:15,85,71,20.12,muffled choir,door reflected
08:30,99,72,29.23,none,door reflected
08:45,77,70,12.35,static shaped like rain,door reflected
09:00,94,79,20.89,none,window shows sea
09:15,86,87,9.26,pipe hum,footprints arrive
09:30,98,92,21.16,none,clear
09:45,100,93,11.3,distant surf,clear
10:00,99,100,1.0,none,wrong ceiling
10:15,100,106,18.46,distant surf,window shows sea
10:30,100,111,28.04,gull indoors,wrong ceiling
10:45,100,114,16.07,distant surf,wrong ceiling
11:00,100,123,12.32,pipe hum,wrong ceiling
11:15,100,123,28.15,none,window shows sea
11:30,100,123,3.35,bell once,foam under desk
11:45,100,127,28.93,static shaped like rain,floor darkening
12:00,100,136,6.41,breathing drain,clear
12:15,100,141,25.55,pipe hum,wrong ceiling
12:30,100,141,29.47,breathing drain,door reflected
12:45,100,140,35.69,gull indoors,door reflected
13:00,100,143,13.23,pipe hum,foam under desk
13:15,100,145,7.17,gull indoors,foam under desk
13:30,100,153,21.25,none,window shows sea
13:45,100,161,4.96,none,window shows sea
14:00,100,167,11.29,static shaped like rain,door reflected
14:15,100,175,24.79,distant surf,floor darkening
14:30,100,183,25.73,none,light below surface
14:45,100,186,32.09,muffled choir,wrong ceiling
15:00,100,191,12.56,distant surf,footprints arrive
15:15,100,189,19.8,distant surf,foam under desk
15:30,100,191,2.85,gull indoors,light below surface
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
