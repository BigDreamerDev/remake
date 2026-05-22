# Sensor Log SW-MAR-2015

location: Tide Elevator
capture-date: 2022-11-24
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
09:00,75,3,26.92,pipe hum,window shows sea
09:15,63,4,14.41,distant surf,door reflected
09:30,69,11,19.91,gull indoors,clear
09:45,72,12,26.77,pipe hum,door reflected
10:00,70,14,31.04,distant surf,door reflected
10:15,76,18,19.9,breathing drain,wrong ceiling
10:30,89,25,18.88,static shaped like rain,footprints arrive
10:45,79,34,13.0,none,light below surface
11:00,70,39,7.12,none,floor darkening
11:15,88,43,25.57,pipe hum,foam under desk
11:30,67,48,28.03,pipe hum,window shows sea
11:45,68,54,19.44,pipe hum,window shows sea
12:00,100,63,22.15,static shaped like rain,foam under desk
12:15,75,70,35.13,breathing drain,wrong ceiling
12:30,95,73,33.18,breathing drain,wrong ceiling
12:45,71,71,21.26,breathing drain,footprints arrive
13:00,100,72,21.34,none,window shows sea
13:15,94,78,15.88,breathing drain,wrong ceiling
13:30,100,86,6.68,distant surf,door reflected
13:45,100,92,22.45,muffled choir,door reflected
14:00,99,94,24.12,gull indoors,window shows sea
14:15,87,95,29.73,gull indoors,foam under desk
14:30,92,95,3.64,breathing drain,floor darkening
14:45,100,101,29.27,distant surf,floor darkening
15:00,99,109,34.01,muffled choir,light below surface
15:15,100,117,28.1,bell once,foam under desk
15:30,100,116,1.26,gull indoors,window shows sea
15:45,100,125,15.58,gull indoors,wrong ceiling
16:00,100,127,36.32,gull indoors,floor darkening
16:15,99,135,29.99,muffled choir,window shows sea
16:30,100,144,31.24,bell once,door reflected
16:45,99,146,34.25,static shaped like rain,floor darkening
17:00,100,153,0.54,none,floor darkening
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
