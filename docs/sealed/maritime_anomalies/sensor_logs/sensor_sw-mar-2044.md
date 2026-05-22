# Sensor Log SW-MAR-2044

location: Tide Elevator
capture-date: 1984-10-07
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
13:00,80,8,32.1,breathing drain,light below surface
13:15,52,10,10.16,pipe hum,light below surface
13:30,72,17,11.9,pipe hum,wrong ceiling
13:45,78,25,22.37,muffled choir,door reflected
14:00,93,31,29.04,gull indoors,footprints arrive
14:15,87,38,34.41,breathing drain,window shows sea
14:30,83,41,19.88,distant surf,wrong ceiling
14:45,82,39,28.46,distant surf,wrong ceiling
15:00,81,37,6.2,breathing drain,clear
15:15,80,42,35.81,muffled choir,floor darkening
15:30,81,42,7.23,distant surf,foam under desk
15:45,82,49,1.89,muffled choir,footprints arrive
16:00,68,48,34.19,distant surf,clear
16:15,79,46,18.07,breathing drain,window shows sea
16:30,86,49,17.4,static shaped like rain,window shows sea
16:45,71,49,10.56,pipe hum,door reflected
17:00,84,58,1.85,gull indoors,clear
17:15,90,60,28.04,pipe hum,floor darkening
17:30,95,60,14.33,muffled choir,footprints arrive
17:45,98,67,28.17,static shaped like rain,floor darkening
18:00,97,73,10.43,static shaped like rain,footprints arrive
18:15,94,80,0.97,breathing drain,clear
18:30,94,89,30.59,breathing drain,window shows sea
18:45,100,89,34.24,breathing drain,clear
19:00,100,95,31.01,pipe hum,clear
19:15,100,96,32.39,distant surf,door reflected
19:30,100,95,26.42,gull indoors,wrong ceiling
19:45,100,100,5.79,pipe hum,door reflected
20:00,87,103,25.3,muffled choir,light below surface
20:15,100,109,22.63,pipe hum,clear
20:30,100,116,5.53,pipe hum,foam under desk
20:45,100,120,3.88,static shaped like rain,wrong ceiling
21:00,100,126,1.32,breathing drain,door reflected
21:15,100,128,3.1,breathing drain,foam under desk
21:30,100,128,21.02,pipe hum,floor darkening
21:45,100,134,32.86,gull indoors,foam under desk
22:00,100,139,18.77,gull indoors,floor darkening
22:15,100,141,2.15,breathing drain,door reflected
22:30,100,149,5.7,muffled choir,door reflected
22:45,100,158,29.13,bell once,light below surface
23:00,100,160,28.38,pipe hum,footprints arrive
23:15,100,163,20.54,none,wrong ceiling
23:30,100,166,26.01,bell once,light below surface
23:45,100,169,15.38,distant surf,clear
00:00,100,169,14.15,pipe hum,floor darkening
00:15,100,173,16.01,none,window shows sea
00:30,100,180,13.36,pipe hum,window shows sea
00:45,100,189,35.21,none,door reflected
01:00,100,198,26.75,none,clear
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
