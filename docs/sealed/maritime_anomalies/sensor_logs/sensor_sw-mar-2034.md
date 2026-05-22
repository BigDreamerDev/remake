# Sensor Log SW-MAR-2034

location: Rain Room 11
capture-date: 1983-09-29
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
10:00,64,0,0.49,bell once,door reflected
10:15,74,0,0.56,muffled choir,wrong ceiling
10:30,73,1,2.16,distant surf,wrong ceiling
10:45,54,1,12.35,pipe hum,clear
11:00,65,2,35.23,gull indoors,footprints arrive
11:15,77,1,15.4,pipe hum,wrong ceiling
11:30,52,2,33.44,muffled choir,light below surface
11:45,57,4,5.63,static shaped like rain,door reflected
12:00,57,4,1.13,gull indoors,foam under desk
12:15,80,2,21.51,bell once,light below surface
12:30,54,7,35.17,pipe hum,light below surface
12:45,72,14,6.56,breathing drain,footprints arrive
13:00,84,23,24.62,none,floor darkening
13:15,73,29,29.99,muffled choir,door reflected
13:30,76,29,32.94,none,wrong ceiling
13:45,65,38,5.84,muffled choir,light below surface
14:00,85,38,21.75,none,footprints arrive
14:15,66,38,9.71,breathing drain,window shows sea
14:30,74,46,13.55,none,window shows sea
14:45,89,55,10.55,pipe hum,foam under desk
15:00,85,60,1.49,gull indoors,door reflected
15:15,83,58,26.8,muffled choir,door reflected
15:30,94,60,23.31,breathing drain,foam under desk
15:45,75,65,24.38,gull indoors,wrong ceiling
16:00,97,63,36.64,breathing drain,floor darkening
16:15,92,68,13.88,static shaped like rain,foam under desk
16:30,100,68,33.67,none,footprints arrive
16:45,100,76,19.65,pipe hum,clear
17:00,84,83,18.91,pipe hum,door reflected
17:15,75,81,34.68,none,window shows sea
17:30,100,80,29.3,breathing drain,floor darkening
17:45,100,83,16.1,breathing drain,light below surface
18:00,100,84,24.62,pipe hum,wrong ceiling
18:15,89,90,17.59,muffled choir,light below surface
18:30,85,94,17.9,static shaped like rain,wrong ceiling
18:45,100,102,33.68,gull indoors,foam under desk
19:00,100,103,20.34,gull indoors,door reflected
19:15,100,110,30.08,pipe hum,footprints arrive
19:30,100,113,14.95,breathing drain,window shows sea
19:45,100,112,4.39,muffled choir,foam under desk
20:00,95,119,29.31,distant surf,wrong ceiling
20:15,100,121,25.58,pipe hum,door reflected
20:30,100,120,36.29,muffled choir,floor darkening
20:45,100,128,25.75,distant surf,door reflected
21:00,100,133,29.39,muffled choir,light below surface
21:15,98,133,2.74,breathing drain,footprints arrive
21:30,100,136,13.8,muffled choir,wrong ceiling
21:45,100,144,9.55,bell once,door reflected
22:00,100,146,1.79,breathing drain,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
