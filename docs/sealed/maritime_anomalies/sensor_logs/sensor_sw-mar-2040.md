# Sensor Log SW-MAR-2040

location: North Glass Shoal
capture-date: 1984-05-01
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
16:00,70,9,12.46,distant surf,footprints arrive
16:15,83,16,30.5,gull indoors,window shows sea
16:30,85,24,6.6,muffled choir,wrong ceiling
16:45,76,23,32.87,static shaped like rain,light below surface
17:00,64,27,29.0,breathing drain,light below surface
17:15,92,32,27.82,static shaped like rain,foam under desk
17:30,68,35,30.13,static shaped like rain,clear
17:45,73,38,35.45,distant surf,clear
18:00,69,38,35.65,gull indoors,door reflected
18:15,97,44,17.86,bell once,floor darkening
18:30,73,43,12.33,breathing drain,wrong ceiling
18:45,93,45,16.37,bell once,light below surface
19:00,80,46,10.07,breathing drain,wrong ceiling
19:15,67,55,25.61,static shaped like rain,wrong ceiling
19:30,89,59,13.15,pipe hum,foam under desk
19:45,74,57,9.38,static shaped like rain,light below surface
20:00,69,60,10.88,gull indoors,wrong ceiling
20:15,96,60,32.89,pipe hum,light below surface
20:30,79,67,14.53,distant surf,foam under desk
20:45,98,68,9.55,pipe hum,wrong ceiling
21:00,84,75,13.53,bell once,footprints arrive
21:15,100,83,34.5,muffled choir,wrong ceiling
21:30,91,90,5.6,static shaped like rain,light below surface
21:45,100,91,33.19,pipe hum,foam under desk
22:00,100,97,36.71,static shaped like rain,footprints arrive
22:15,100,103,31.31,distant surf,clear
22:30,100,102,16.2,muffled choir,clear
22:45,100,106,2.24,bell once,foam under desk
23:00,100,115,12.5,distant surf,clear
23:15,96,120,8.59,gull indoors,footprints arrive
23:30,95,123,16.22,none,clear
23:45,93,129,21.99,distant surf,footprints arrive
00:00,100,138,27.32,muffled choir,clear
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
