# Sensor Log SW-MAR-2017

location: The Third Jetty
capture-date: 2023-02-02
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
07:00,51,8,33.86,gull indoors,wrong ceiling
07:15,68,14,29.85,distant surf,foam under desk
07:30,64,23,11.99,static shaped like rain,clear
07:45,68,29,23.46,static shaped like rain,floor darkening
08:00,87,28,23.38,gull indoors,window shows sea
08:15,89,32,6.92,pipe hum,foam under desk
08:30,58,32,1.48,breathing drain,foam under desk
08:45,68,39,14.78,distant surf,light below surface
09:00,79,45,20.8,none,light below surface
09:15,78,46,5.9,none,door reflected
09:30,89,45,28.78,bell once,wrong ceiling
09:45,77,49,33.07,pipe hum,light below surface
10:00,91,53,35.32,none,wrong ceiling
10:15,73,57,25.23,distant surf,foam under desk
10:30,74,55,28.88,static shaped like rain,wrong ceiling
10:45,73,62,8.39,breathing drain,door reflected
11:00,86,62,3.91,static shaped like rain,window shows sea
11:15,88,68,34.3,pipe hum,foam under desk
11:30,91,66,6.19,distant surf,window shows sea
11:45,94,67,4.09,distant surf,floor darkening
12:00,71,70,15.95,bell once,clear
12:15,73,77,27.29,pipe hum,light below surface
12:30,80,78,11.19,none,wrong ceiling
12:45,96,78,30.78,pipe hum,light below surface
13:00,82,80,17.82,static shaped like rain,floor darkening
13:15,100,87,24.77,gull indoors,door reflected
13:30,92,96,8.51,static shaped like rain,floor darkening
13:45,82,94,18.07,distant surf,clear
14:00,100,97,16.28,static shaped like rain,window shows sea
14:15,96,105,21.13,none,window shows sea
14:30,97,113,11.87,muffled choir,footprints arrive
14:45,100,111,20.36,gull indoors,light below surface
15:00,100,119,24.26,bell once,foam under desk
15:15,100,127,14.62,muffled choir,light below surface
15:30,100,132,1.66,distant surf,door reflected
15:45,99,139,33.64,breathing drain,light below surface
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
