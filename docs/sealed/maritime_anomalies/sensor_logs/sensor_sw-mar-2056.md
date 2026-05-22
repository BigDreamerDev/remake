# Sensor Log SW-MAR-2056

location: Rain Room 11
capture-date: 1985-12-21
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
10:00,70,4,12.17,muffled choir,door reflected
10:15,84,5,17.36,pipe hum,window shows sea
10:30,70,12,30.69,static shaped like rain,clear
10:45,58,13,25.38,pipe hum,light below surface
11:00,68,19,19.85,breathing drain,door reflected
11:15,59,26,34.86,muffled choir,footprints arrive
11:30,60,31,2.32,breathing drain,clear
11:45,80,39,28.15,breathing drain,wrong ceiling
12:00,75,46,28.46,gull indoors,floor darkening
12:15,100,54,7.94,pipe hum,floor darkening
12:30,98,63,17.82,gull indoors,clear
12:45,82,66,25.05,distant surf,window shows sea
13:00,81,73,19.52,distant surf,window shows sea
13:15,73,74,25.66,pipe hum,floor darkening
13:30,100,82,26.46,pipe hum,clear
13:45,95,80,4.69,bell once,door reflected
14:00,100,85,17.73,breathing drain,floor darkening
14:15,84,94,19.03,bell once,light below surface
14:30,100,99,33.31,pipe hum,wrong ceiling
14:45,100,98,18.05,gull indoors,window shows sea
15:00,97,104,30.09,breathing drain,light below surface
15:15,100,112,2.34,bell once,floor darkening
15:30,100,113,35.24,muffled choir,wrong ceiling
15:45,100,119,4.04,distant surf,door reflected
16:00,100,121,34.26,bell once,door reflected
16:15,100,123,4.33,breathing drain,wrong ceiling
16:30,100,128,11.93,breathing drain,floor darkening
16:45,97,133,5.1,gull indoors,wrong ceiling
17:00,100,139,32.4,bell once,footprints arrive
17:15,100,144,29.88,gull indoors,footprints arrive
17:30,100,152,16.52,static shaped like rain,door reflected
17:45,100,157,18.95,breathing drain,wrong ceiling
18:00,100,163,21.56,gull indoors,light below surface
18:15,100,162,25.9,breathing drain,footprints arrive
18:30,100,170,7.55,bell once,window shows sea
18:45,100,172,10.21,bell once,window shows sea
19:00,100,181,19.24,bell once,footprints arrive
19:15,100,179,18.73,distant surf,floor darkening
19:30,100,187,25.89,distant surf,clear
19:45,100,194,29.06,breathing drain,light below surface
20:00,100,201,36.52,muffled choir,floor darkening
20:15,100,201,24.08,breathing drain,foam under desk
20:30,100,200,36.49,pipe hum,light below surface
20:45,100,202,30.05,breathing drain,floor darkening
21:00,100,203,1.19,gull indoors,floor darkening
21:15,100,202,14.49,distant surf,foam under desk
21:30,100,207,18.75,gull indoors,floor darkening
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
