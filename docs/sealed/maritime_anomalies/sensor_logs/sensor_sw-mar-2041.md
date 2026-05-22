# Sensor Log SW-MAR-2041

location: Rain Room 11
capture-date: 1984-06-10
device: manual tide staff

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
13:00,74,9,0.84,distant surf,wrong ceiling
13:15,64,18,25.12,muffled choir,footprints arrive
13:30,88,25,1.67,gull indoors,window shows sea
13:45,65,29,26.28,breathing drain,clear
14:00,92,33,33.27,static shaped like rain,clear
14:15,69,38,14.82,muffled choir,door reflected
14:30,85,46,21.11,muffled choir,wrong ceiling
14:45,85,52,10.81,gull indoors,clear
15:00,80,61,11.51,none,window shows sea
15:15,92,65,1.31,distant surf,window shows sea
15:30,95,69,7.55,static shaped like rain,door reflected
15:45,74,71,22.41,pipe hum,clear
16:00,78,72,22.87,static shaped like rain,clear
16:15,100,76,25.84,bell once,floor darkening
16:30,79,81,24.06,bell once,foam under desk
16:45,100,84,33.44,static shaped like rain,wrong ceiling
17:00,89,83,17.24,breathing drain,window shows sea
17:15,92,89,18.71,muffled choir,light below surface
17:30,79,95,29.26,gull indoors,light below surface
17:45,89,100,8.19,static shaped like rain,wrong ceiling
18:00,86,103,20.22,distant surf,door reflected
18:15,95,108,0.52,none,window shows sea
18:30,94,109,5.66,gull indoors,door reflected
18:45,93,113,3.23,gull indoors,foam under desk
19:00,88,118,34.2,bell once,clear
19:15,99,127,13.29,breathing drain,light below surface
19:30,100,131,29.45,distant surf,floor darkening
19:45,96,139,15.5,pipe hum,clear
20:00,100,148,33.7,static shaped like rain,floor darkening
20:15,100,152,10.33,gull indoors,window shows sea
20:30,100,150,8.45,breathing drain,clear
20:45,100,151,23.82,muffled choir,floor darkening
21:00,100,158,26.65,bell once,wrong ceiling
21:15,100,159,4.01,distant surf,light below surface
21:30,100,158,6.29,breathing drain,window shows sea
21:45,100,157,36.77,muffled choir,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
