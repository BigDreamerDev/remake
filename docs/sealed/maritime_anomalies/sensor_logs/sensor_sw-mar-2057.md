# Sensor Log SW-MAR-2057

location: West Sluice Door
capture-date: 1986-02-02
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
12:00,86,9,2.53,muffled choir,footprints arrive
12:15,63,9,0.55,gull indoors,window shows sea
12:30,84,9,16.93,static shaped like rain,clear
12:45,53,12,29.83,bell once,light below surface
13:00,85,15,32.92,bell once,wrong ceiling
13:15,75,23,17.72,gull indoors,door reflected
13:30,58,25,35.42,pipe hum,clear
13:45,83,26,6.59,pipe hum,window shows sea
14:00,85,33,24.46,none,footprints arrive
14:15,93,32,28.15,breathing drain,foam under desk
14:30,65,36,17.44,static shaped like rain,door reflected
14:45,94,42,15.32,muffled choir,floor darkening
15:00,97,46,17.01,pipe hum,light below surface
15:15,100,52,31.85,distant surf,wrong ceiling
15:30,71,50,13.45,bell once,light below surface
15:45,99,52,14.31,pipe hum,floor darkening
16:00,66,56,28.18,bell once,clear
16:15,85,64,35.63,bell once,footprints arrive
16:30,100,65,17.14,pipe hum,wrong ceiling
16:45,81,70,26.9,muffled choir,clear
17:00,84,77,36.61,static shaped like rain,wrong ceiling
17:15,94,82,26.34,none,footprints arrive
17:30,100,83,7.68,muffled choir,window shows sea
17:45,86,92,17.55,muffled choir,footprints arrive
18:00,87,97,7.97,bell once,floor darkening
18:15,97,99,30.42,pipe hum,light below surface
18:30,82,102,33.15,none,door reflected
18:45,95,107,18.35,bell once,light below surface
19:00,97,107,35.41,bell once,window shows sea
19:15,100,108,22.02,breathing drain,light below surface
19:30,100,113,16.87,bell once,door reflected
19:45,100,112,2.19,pipe hum,foam under desk
20:00,94,117,10.27,distant surf,foam under desk
20:15,94,118,5.13,breathing drain,door reflected
20:30,100,116,29.27,none,window shows sea
20:45,100,121,2.13,distant surf,foam under desk
21:00,98,128,17.8,breathing drain,foam under desk
21:15,100,129,28.54,none,wrong ceiling
21:30,100,135,19.9,bell once,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
