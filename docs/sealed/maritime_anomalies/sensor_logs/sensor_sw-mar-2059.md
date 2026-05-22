# Sensor Log SW-MAR-2059

location: Crescent Breakwater
capture-date: 1986-04-14
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
11:00,79,0,0.3,muffled choir,clear
11:15,66,5,0.21,breathing drain,light below surface
11:30,64,11,9.72,bell once,footprints arrive
11:45,68,12,6.17,bell once,floor darkening
12:00,66,16,30.74,distant surf,window shows sea
12:15,86,25,19.48,breathing drain,window shows sea
12:30,92,32,34.59,muffled choir,foam under desk
12:45,87,41,7.08,static shaped like rain,footprints arrive
13:00,76,41,27.09,gull indoors,wrong ceiling
13:15,74,39,5.38,none,window shows sea
13:30,76,42,9.04,pipe hum,door reflected
13:45,85,50,14.6,pipe hum,clear
14:00,94,59,4.93,bell once,window shows sea
14:15,95,65,16.98,muffled choir,light below surface
14:30,78,71,8.09,breathing drain,light below surface
14:45,96,75,7.32,none,window shows sea
15:00,77,75,23.9,muffled choir,window shows sea
15:15,76,74,12.91,muffled choir,window shows sea
15:30,87,79,9.07,muffled choir,wrong ceiling
15:45,97,81,10.43,none,light below surface
16:00,100,79,34.15,static shaped like rain,door reflected
16:15,100,88,2.68,muffled choir,window shows sea
16:30,89,96,26.31,distant surf,window shows sea
16:45,100,103,21.72,breathing drain,light below surface
17:00,100,103,20.11,muffled choir,door reflected
17:15,100,112,27.98,gull indoors,clear
17:30,100,114,33.12,gull indoors,floor darkening
17:45,100,119,3.38,gull indoors,window shows sea
18:00,100,128,10.98,gull indoors,floor darkening
18:15,100,129,11.09,bell once,light below surface
18:30,100,134,36.18,muffled choir,foam under desk
18:45,100,134,24.01,gull indoors,floor darkening
19:00,100,137,14.45,bell once,clear
19:15,100,135,2.18,static shaped like rain,foam under desk
19:30,100,135,17.86,bell once,window shows sea
19:45,96,136,34.09,distant surf,wrong ceiling
20:00,100,145,35.81,muffled choir,foam under desk
20:15,100,145,16.85,static shaped like rain,clear
20:30,100,153,22.95,gull indoors,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
