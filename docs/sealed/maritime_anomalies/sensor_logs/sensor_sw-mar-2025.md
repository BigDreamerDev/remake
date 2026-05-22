# Sensor Log SW-MAR-2025

location: The Pool That Was Not Built
capture-date: 2023-11-15
device: manual tide staff

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
08:00,61,8,28.4,bell once,wrong ceiling
08:15,81,16,15.15,static shaped like rain,clear
08:30,86,14,21.16,bell once,clear
08:45,57,12,2.19,gull indoors,clear
09:00,76,12,24.6,distant surf,wrong ceiling
09:15,69,18,9.68,breathing drain,window shows sea
09:30,63,26,5.85,muffled choir,window shows sea
09:45,83,31,28.33,pipe hum,foam under desk
10:00,75,38,18.58,gull indoors,door reflected
10:15,97,43,27.83,pipe hum,light below surface
10:30,98,49,35.4,pipe hum,door reflected
10:45,70,48,6.8,static shaped like rain,wrong ceiling
11:00,69,52,32.62,breathing drain,clear
11:15,79,50,11.71,distant surf,footprints arrive
11:30,78,56,25.31,muffled choir,foam under desk
11:45,70,62,11.71,bell once,window shows sea
12:00,81,68,26.1,none,door reflected
12:15,73,69,24.45,distant surf,window shows sea
12:30,100,70,0.39,static shaped like rain,wrong ceiling
12:45,78,68,19.15,gull indoors,wrong ceiling
13:00,77,67,21.94,breathing drain,floor darkening
13:15,73,70,30.73,none,clear
13:30,92,74,12.59,gull indoors,door reflected
13:45,92,74,20.82,distant surf,light below surface
14:00,78,79,27.25,none,foam under desk
14:15,82,84,13.25,none,clear
14:30,90,92,20.32,distant surf,window shows sea
14:45,100,91,20.64,bell once,footprints arrive
15:00,80,95,30.24,muffled choir,foam under desk
15:15,100,94,34.7,pipe hum,door reflected
15:30,100,94,25.56,muffled choir,floor darkening
15:45,83,93,29.02,gull indoors,door reflected
16:00,100,99,9.78,gull indoors,floor darkening
16:15,100,101,24.41,none,clear
16:30,99,110,6.37,gull indoors,footprints arrive
16:45,100,110,29.31,static shaped like rain,floor darkening
17:00,100,116,13.65,bell once,window shows sea
17:15,86,115,11.79,distant surf,door reflected
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
