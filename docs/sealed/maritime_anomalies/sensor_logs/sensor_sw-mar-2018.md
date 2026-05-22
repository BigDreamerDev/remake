# Sensor Log SW-MAR-2018

location: Oyster Stair
capture-date: 2023-03-08
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
10:00,49,5,19.57,distant surf,foam under desk
10:15,55,5,4.83,none,foam under desk
10:30,85,14,4.96,pipe hum,foam under desk
10:45,67,13,24.38,none,clear
11:00,62,22,23.96,pipe hum,foam under desk
11:15,82,29,13.34,muffled choir,floor darkening
11:30,76,29,19.02,distant surf,door reflected
11:45,91,32,5.36,static shaped like rain,footprints arrive
12:00,71,36,13.31,gull indoors,clear
12:15,77,41,12.55,none,window shows sea
12:30,82,39,27.6,none,footprints arrive
12:45,78,37,6.75,gull indoors,window shows sea
13:00,95,38,4.56,static shaped like rain,window shows sea
13:15,82,44,9.18,distant surf,floor darkening
13:30,82,49,19.21,muffled choir,door reflected
13:45,98,48,9.37,pipe hum,light below surface
14:00,89,51,28.74,distant surf,light below surface
14:15,97,57,22.17,gull indoors,floor darkening
14:30,75,55,20.75,none,window shows sea
14:45,77,64,2.41,breathing drain,light below surface
15:00,80,64,23.87,none,floor darkening
15:15,100,65,3.0,distant surf,footprints arrive
15:30,74,70,12.83,none,door reflected
15:45,100,79,11.06,bell once,clear
16:00,80,79,34.89,static shaped like rain,clear
16:15,84,82,0.7,static shaped like rain,door reflected
16:30,91,83,15.65,breathing drain,window shows sea
16:45,83,82,20.66,gull indoors,window shows sea
17:00,82,85,1.82,bell once,foam under desk
17:15,80,90,17.89,distant surf,floor darkening
17:30,98,94,21.64,static shaped like rain,window shows sea
17:45,88,93,15.47,pipe hum,foam under desk
18:00,83,100,19.05,static shaped like rain,floor darkening
18:15,100,108,20.64,none,wrong ceiling
18:30,100,111,19.96,bell once,wrong ceiling
18:45,100,111,24.63,breathing drain,foam under desk
19:00,93,110,3.62,none,footprints arrive
19:15,100,112,15.02,bell once,footprints arrive
19:30,96,117,36.71,distant surf,door reflected
19:45,100,126,30.63,bell once,light below surface
20:00,100,125,35.22,gull indoors,foam under desk
20:15,100,128,19.45,gull indoors,window shows sea
20:30,100,127,18.42,breathing drain,wrong ceiling
20:45,100,127,35.26,gull indoors,light below surface
21:00,100,132,31.24,distant surf,footprints arrive
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
