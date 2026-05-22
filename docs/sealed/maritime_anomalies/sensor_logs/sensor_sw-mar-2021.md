# Sensor Log SW-MAR-2021

location: Undertow Corridor
capture-date: 2023-07-07
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
09:00,73,0,0.69,muffled choir,window shows sea
09:15,80,9,1.79,distant surf,floor darkening
09:30,71,15,2.73,breathing drain,foam under desk
09:45,53,14,31.66,gull indoors,footprints arrive
10:00,53,12,2.44,none,foam under desk
10:15,74,14,10.91,pipe hum,clear
10:30,70,15,3.8,none,light below surface
10:45,69,23,13.0,distant surf,clear
11:00,83,26,27.03,none,floor darkening
11:15,76,27,22.66,bell once,wrong ceiling
11:30,57,27,16.8,muffled choir,door reflected
11:45,93,35,9.3,pipe hum,floor darkening
12:00,80,39,32.25,bell once,foam under desk
12:15,86,40,14.92,muffled choir,floor darkening
12:30,73,47,34.73,none,clear
12:45,68,52,15.69,gull indoors,light below surface
13:00,91,55,27.59,none,window shows sea
13:15,86,61,32.38,gull indoors,door reflected
13:30,98,64,2.16,none,footprints arrive
13:45,100,66,8.09,bell once,foam under desk
14:00,89,71,12.19,gull indoors,clear
14:15,100,77,36.12,gull indoors,footprints arrive
14:30,100,80,13.8,bell once,window shows sea
14:45,100,85,30.32,none,light below surface
15:00,99,93,32.55,pipe hum,clear
15:15,100,96,1.57,muffled choir,foam under desk
15:30,100,103,19.67,gull indoors,clear
15:45,85,111,12.38,none,door reflected
16:00,100,110,26.11,static shaped like rain,light below surface
16:15,100,116,31.84,gull indoors,clear
16:30,95,124,29.46,breathing drain,light below surface
16:45,100,128,6.16,bell once,footprints arrive
17:00,97,127,31.89,static shaped like rain,footprints arrive
17:15,100,125,7.72,bell once,clear
17:30,100,131,22.16,distant surf,clear
17:45,100,131,19.67,none,floor darkening
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
