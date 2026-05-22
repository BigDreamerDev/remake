# Sensor Log SW-MAR-2060

location: Tide Elevator
capture-date: 1986-05-23
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
18:00,52,0,0.69,pipe hum,light below surface
18:15,82,7,20.69,static shaped like rain,wrong ceiling
18:30,60,7,30.62,muffled choir,clear
18:45,72,16,16.03,gull indoors,footprints arrive
19:00,81,18,22.98,gull indoors,foam under desk
19:15,86,26,26.45,distant surf,footprints arrive
19:30,60,29,14.1,gull indoors,door reflected
19:45,58,28,19.72,static shaped like rain,wrong ceiling
20:00,81,30,25.03,distant surf,foam under desk
20:15,77,28,26.43,pipe hum,door reflected
20:30,79,37,2.41,gull indoors,footprints arrive
20:45,62,44,4.01,distant surf,light below surface
21:00,76,48,26.29,static shaped like rain,wrong ceiling
21:15,88,52,24.72,none,wrong ceiling
21:30,98,59,20.64,distant surf,wrong ceiling
21:45,100,68,7.89,breathing drain,clear
22:00,72,74,19.71,breathing drain,door reflected
22:15,96,80,16.13,breathing drain,foam under desk
22:30,100,89,23.66,bell once,clear
22:45,100,89,23.56,distant surf,wrong ceiling
23:00,96,93,35.06,none,window shows sea
23:15,100,96,34.57,muffled choir,footprints arrive
23:30,85,103,22.64,static shaped like rain,floor darkening
23:45,92,108,1.4,bell once,door reflected
00:00,100,113,24.78,distant surf,wrong ceiling
00:15,100,112,15.95,muffled choir,clear
00:30,100,114,16.18,static shaped like rain,light below surface
00:45,100,114,25.63,breathing drain,clear
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
