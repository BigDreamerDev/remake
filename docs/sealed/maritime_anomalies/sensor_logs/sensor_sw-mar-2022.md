# Sensor Log SW-MAR-2022

location: Old Bathing Pavilion
capture-date: 2023-07-28
device: manual tide staff

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
13:00,55,8,2.47,none,footprints arrive
13:15,56,12,16.25,bell once,footprints arrive
13:30,59,20,35.25,static shaped like rain,light below surface
13:45,58,22,19.24,static shaped like rain,light below surface
14:00,72,26,11.21,distant surf,footprints arrive
14:15,93,34,33.85,distant surf,door reflected
14:30,77,37,14.82,distant surf,wrong ceiling
14:45,63,43,2.77,gull indoors,light below surface
15:00,94,52,21.18,bell once,window shows sea
15:15,77,59,16.05,muffled choir,foam under desk
15:30,84,60,11.51,static shaped like rain,window shows sea
15:45,70,61,14.11,breathing drain,wrong ceiling
16:00,88,69,12.05,breathing drain,window shows sea
16:15,83,69,4.16,static shaped like rain,clear
16:30,100,67,32.2,distant surf,wrong ceiling
16:45,82,67,4.53,static shaped like rain,floor darkening
17:00,74,76,6.02,pipe hum,light below surface
17:15,100,80,30.96,muffled choir,window shows sea
17:30,86,82,31.08,none,floor darkening
17:45,96,85,26.49,bell once,wrong ceiling
18:00,87,89,13.29,pipe hum,footprints arrive
18:15,92,89,34.08,breathing drain,door reflected
18:30,84,93,5.31,static shaped like rain,clear
18:45,100,94,31.78,pipe hum,door reflected
19:00,81,93,9.28,gull indoors,floor darkening
19:15,79,91,9.39,muffled choir,door reflected
19:30,79,92,22.39,breathing drain,window shows sea
19:45,100,94,9.51,static shaped like rain,floor darkening
20:00,100,100,2.77,distant surf,foam under desk
20:15,100,107,20.77,distant surf,footprints arrive
20:30,85,109,31.2,pipe hum,floor darkening
20:45,89,113,11.8,pipe hum,light below surface
21:00,92,113,31.18,pipe hum,footprints arrive
21:15,100,111,18.48,breathing drain,foam under desk
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
