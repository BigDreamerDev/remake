# Sensor Log SW-MAR-2047

location: Undertow Corridor
capture-date: 1985-01-22
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
08:00,54,5,29.58,none,wrong ceiling
08:15,79,7,13.22,breathing drain,floor darkening
08:30,82,13,1.69,breathing drain,light below surface
08:45,70,16,20.05,static shaped like rain,wrong ceiling
09:00,56,19,8.63,bell once,foam under desk
09:15,87,23,10.24,none,light below surface
09:30,72,31,5.21,breathing drain,window shows sea
09:45,60,37,1.66,bell once,clear
10:00,69,35,10.06,none,wrong ceiling
10:15,84,37,7.66,static shaped like rain,clear
10:30,82,36,25.88,distant surf,foam under desk
10:45,91,42,4.15,gull indoors,footprints arrive
11:00,72,41,16.3,distant surf,light below surface
11:15,88,49,22.43,gull indoors,wrong ceiling
11:30,88,51,9.8,bell once,door reflected
11:45,84,57,7.29,bell once,foam under desk
12:00,90,57,1.45,distant surf,clear
12:15,86,55,28.07,breathing drain,door reflected
12:30,73,61,12.56,gull indoors,light below surface
12:45,69,64,11.05,gull indoors,door reflected
13:00,86,73,34.95,muffled choir,window shows sea
13:15,80,76,17.76,muffled choir,door reflected
13:30,100,74,5.67,muffled choir,floor darkening
13:45,91,83,4.26,gull indoors,wrong ceiling
14:00,100,83,13.94,pipe hum,door reflected
14:15,81,84,11.39,static shaped like rain,wrong ceiling
14:30,100,93,28.45,muffled choir,foam under desk
14:45,93,101,15.95,distant surf,clear
15:00,100,106,33.2,bell once,door reflected
15:15,86,110,27.04,breathing drain,light below surface
15:30,100,111,21.2,none,floor darkening
15:45,100,114,19.38,pipe hum,clear
16:00,100,123,5.53,breathing drain,window shows sea
16:15,100,129,17.75,distant surf,clear
16:30,100,138,21.94,pipe hum,footprints arrive
16:45,98,137,17.26,bell once,window shows sea
17:00,100,135,12.6,gull indoors,clear
17:15,100,138,15.82,distant surf,light below surface
17:30,97,146,18.7,pipe hum,foam under desk
17:45,100,150,28.16,muffled choir,light below surface
18:00,100,151,29.04,muffled choir,clear
18:15,100,155,14.47,pipe hum,clear
18:30,100,163,29.08,static shaped like rain,footprints arrive
18:45,100,170,21.54,none,clear
19:00,100,171,11.41,none,floor darkening
19:15,100,172,26.85,none,floor darkening
19:30,100,176,26.35,none,floor darkening
19:45,100,175,2.48,distant surf,window shows sea
20:00,100,184,14.92,muffled choir,foam under desk
20:15,100,184,27.85,pipe hum,light below surface
20:30,100,190,2.71,distant surf,window shows sea
20:45,100,197,20.43,breathing drain,footprints arrive
21:00,100,204,34.41,distant surf,footprints arrive
21:15,100,203,27.93,gull indoors,wrong ceiling
21:30,100,206,19.54,distant surf,light below surface
21:45,100,208,34.36,distant surf,floor darkening
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
