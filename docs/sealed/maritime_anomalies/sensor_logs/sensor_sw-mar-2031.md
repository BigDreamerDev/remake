# Sensor Log SW-MAR-2031

location: The Dry Dock With Water In It
capture-date: 1983-06-06
device: floorline acoustic monitor

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
13:00,82,0,0.95,none,foam under desk
13:15,55,2,7.11,distant surf,light below surface
13:30,62,6,10.43,distant surf,door reflected
13:45,83,10,9.76,pipe hum,foam under desk
14:00,64,15,22.86,distant surf,footprints arrive
14:15,74,23,16.46,muffled choir,clear
14:30,59,22,4.11,pipe hum,window shows sea
14:45,65,29,35.27,none,window shows sea
15:00,67,27,35.26,muffled choir,floor darkening
15:15,65,25,22.07,distant surf,window shows sea
15:30,77,32,30.05,muffled choir,foam under desk
15:45,92,32,7.1,pipe hum,door reflected
16:00,64,39,13.23,gull indoors,light below surface
16:15,67,37,14.64,breathing drain,foam under desk
16:30,95,45,1.26,breathing drain,foam under desk
16:45,76,53,19.74,gull indoors,foam under desk
17:00,94,51,25.53,bell once,window shows sea
17:15,87,53,3.62,gull indoors,footprints arrive
17:30,68,57,18.38,muffled choir,door reflected
17:45,73,57,34.55,distant surf,door reflected
18:00,87,62,9.04,pipe hum,wrong ceiling
18:15,77,67,24.92,bell once,footprints arrive
18:30,100,68,32.37,bell once,clear
18:45,75,77,0.97,gull indoors,foam under desk
19:00,89,83,2.56,none,wrong ceiling
19:15,99,83,28.86,distant surf,door reflected
19:30,79,82,20.71,none,footprints arrive
19:45,99,83,31.47,bell once,footprints arrive
20:00,91,89,9.01,gull indoors,clear
20:15,78,90,1.63,breathing drain,footprints arrive
20:30,84,94,8.2,muffled choir,light below surface
20:45,83,100,9.11,muffled choir,door reflected
21:00,100,102,0.82,pipe hum,foam under desk
21:15,91,105,33.63,static shaped like rain,wrong ceiling
21:30,100,111,22.27,gull indoors,clear
21:45,100,111,5.45,gull indoors,footprints arrive
22:00,100,113,32.24,pipe hum,foam under desk
22:15,100,121,35.83,gull indoors,window shows sea
22:30,100,121,35.12,gull indoors,clear
22:45,93,119,18.72,bell once,clear
23:00,100,128,36.21,distant surf,foam under desk
23:15,92,129,10.13,distant surf,floor darkening
23:30,95,131,16.63,distant surf,floor darkening
23:45,100,136,18.74,breathing drain,clear
00:00,100,135,8.41,pipe hum,footprints arrive
00:15,100,143,35.62,static shaped like rain,footprints arrive
00:30,100,151,13.28,gull indoors,wrong ceiling
00:45,100,160,17.87,static shaped like rain,floor darkening
01:00,100,163,21.82,gull indoors,wrong ceiling
01:15,100,172,4.75,none,floor darkening
01:30,100,181,7.39,static shaped like rain,foam under desk
01:45,100,185,9.59,distant surf,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
