# Sensor Log SW-MAR-2009

location: Below-Stairs Reservoir
capture-date: 2022-04-15
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
18:00,60,0,0.13,bell once,footprints arrive
18:15,76,9,25.69,static shaped like rain,wrong ceiling
18:30,60,13,23.45,muffled choir,clear
18:45,82,20,31.93,muffled choir,wrong ceiling
19:00,60,21,8.91,pipe hum,clear
19:15,81,26,8.12,pipe hum,floor darkening
19:30,61,25,23.6,muffled choir,floor darkening
19:45,68,31,10.41,gull indoors,light below surface
20:00,81,32,27.82,breathing drain,floor darkening
20:15,63,32,21.91,distant surf,window shows sea
20:30,93,33,5.61,breathing drain,light below surface
20:45,79,32,30.36,breathing drain,wrong ceiling
21:00,91,31,33.38,pipe hum,wrong ceiling
21:15,69,36,14.99,gull indoors,door reflected
21:30,80,39,16.49,pipe hum,wrong ceiling
21:45,70,43,8.03,pipe hum,foam under desk
22:00,97,46,5.9,pipe hum,window shows sea
22:15,62,44,13.11,gull indoors,footprints arrive
22:30,86,44,10.44,static shaped like rain,light below surface
22:45,92,49,11.53,gull indoors,foam under desk
23:00,67,53,28.14,gull indoors,floor darkening
23:15,95,60,14.4,static shaped like rain,floor darkening
23:30,78,63,5.07,static shaped like rain,foam under desk
23:45,97,69,16.26,none,door reflected
00:00,73,72,25.59,distant surf,clear
00:15,97,78,5.59,gull indoors,door reflected
00:30,100,79,33.29,bell once,door reflected
00:45,88,80,16.51,static shaped like rain,footprints arrive
01:00,95,80,33.25,gull indoors,clear
01:15,86,87,10.32,none,footprints arrive
01:30,92,88,4.24,bell once,light below surface
01:45,79,88,7.36,static shaped like rain,door reflected
02:00,92,91,3.31,muffled choir,clear
02:15,98,89,15.13,static shaped like rain,light below surface
02:30,100,90,3.97,none,floor darkening
02:45,87,92,7.15,static shaped like rain,floor darkening
03:00,97,98,15.17,muffled choir,wrong ceiling
03:15,100,107,31.09,breathing drain,window shows sea
03:30,97,109,25.12,muffled choir,clear
03:45,100,116,22.58,none,clear
04:00,100,123,22.83,pipe hum,wrong ceiling
04:15,96,121,24.3,muffled choir,clear
04:30,100,122,9.67,none,floor darkening
04:45,100,125,12.19,breathing drain,foam under desk
05:00,91,127,19.87,none,light below surface
05:15,100,135,19.42,breathing drain,window shows sea
05:30,100,140,22.15,none,wrong ceiling
05:45,100,149,10.27,gull indoors,clear
06:00,100,147,4.94,none,footprints arrive
06:15,100,146,26.62,pipe hum,window shows sea
06:30,100,153,16.94,breathing drain,window shows sea
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
