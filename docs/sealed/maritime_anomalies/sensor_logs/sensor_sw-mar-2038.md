# Sensor Log SW-MAR-2038

location: The Pool That Was Not Built
capture-date: 1984-03-01
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
11:00,61,8,35.64,breathing drain,light below surface
11:15,56,11,26.27,none,footprints arrive
11:30,52,11,13.73,pipe hum,footprints arrive
11:45,68,19,9.28,pipe hum,floor darkening
12:00,58,18,5.85,gull indoors,clear
12:15,89,22,22.57,pipe hum,clear
12:30,68,30,6.02,none,footprints arrive
12:45,77,38,26.17,bell once,footprints arrive
13:00,76,47,32.69,none,clear
13:15,71,48,22.16,muffled choir,window shows sea
13:30,100,52,23.36,gull indoors,footprints arrive
13:45,95,54,6.09,none,door reflected
14:00,92,59,23.98,none,foam under desk
14:15,74,58,10.63,none,clear
14:30,72,60,20.29,breathing drain,foam under desk
14:45,73,62,16.45,pipe hum,wrong ceiling
15:00,91,71,24.94,none,wrong ceiling
15:15,83,78,14.56,static shaped like rain,foam under desk
15:30,100,76,26.98,muffled choir,window shows sea
15:45,90,79,2.17,breathing drain,wrong ceiling
16:00,100,79,3.21,bell once,floor darkening
16:15,98,82,4.23,gull indoors,door reflected
16:30,83,82,2.26,distant surf,floor darkening
16:45,82,88,14.41,static shaped like rain,door reflected
17:00,83,96,23.5,distant surf,floor darkening
17:15,88,105,22.05,gull indoors,floor darkening
17:30,97,106,23.42,static shaped like rain,floor darkening
17:45,95,111,22.18,pipe hum,floor darkening
18:00,100,109,9.0,distant surf,door reflected
18:15,95,113,8.64,muffled choir,door reflected
18:30,100,115,10.65,distant surf,wrong ceiling
18:45,95,120,4.37,static shaped like rain,clear
19:00,93,121,9.12,muffled choir,light below surface
19:15,93,126,22.88,gull indoors,footprints arrive
19:30,100,135,11.75,bell once,light below surface
19:45,100,135,10.17,bell once,foam under desk
20:00,99,136,30.52,static shaped like rain,floor darkening
20:15,100,142,6.15,gull indoors,wrong ceiling
20:30,98,143,13.3,bell once,wrong ceiling
20:45,100,144,18.69,bell once,window shows sea
21:00,100,147,22.78,distant surf,wrong ceiling
21:15,100,151,24.03,muffled choir,footprints arrive
21:30,100,152,1.52,bell once,door reflected
21:45,100,150,20.46,gull indoors,clear
22:00,100,159,22.65,muffled choir,footprints arrive
22:15,100,159,5.44,breathing drain,foam under desk
22:30,100,163,15.26,distant surf,foam under desk
22:45,100,167,0.45,distant surf,light below surface
23:00,100,174,3.81,static shaped like rain,clear
23:15,100,172,21.9,gull indoors,clear
23:30,100,175,32.23,bell once,light below surface
23:45,100,177,30.6,distant surf,foam under desk
00:00,100,177,35.41,static shaped like rain,light below surface
00:15,100,176,27.23,distant surf,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
