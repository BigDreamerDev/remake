# Sensor Log SW-MAR-2013

location: Mirrorpool Basin
capture-date: 2022-08-26
device: floorline acoustic monitor

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
18:00,55,5,5.7,pipe hum,footprints arrive
18:15,59,7,22.71,breathing drain,light below surface
18:30,81,15,1.8,static shaped like rain,clear
18:45,71,22,34.35,pipe hum,clear
19:00,75,29,7.69,pipe hum,light below surface
19:15,77,31,30.53,muffled choir,foam under desk
19:30,81,31,11.89,breathing drain,light below surface
19:45,64,38,4.47,muffled choir,door reflected
20:00,62,39,31.61,pipe hum,clear
20:15,66,39,1.24,muffled choir,foam under desk
20:30,92,39,7.04,muffled choir,foam under desk
20:45,71,40,30.26,pipe hum,wrong ceiling
21:00,70,44,1.5,distant surf,floor darkening
21:15,97,48,23.18,static shaped like rain,wrong ceiling
21:30,73,57,0.85,none,wrong ceiling
21:45,70,66,31.85,breathing drain,clear
22:00,86,64,22.53,none,light below surface
22:15,73,68,0.36,muffled choir,footprints arrive
22:30,73,68,24.15,gull indoors,wrong ceiling
22:45,79,70,13.57,gull indoors,foam under desk
23:00,98,70,35.09,none,window shows sea
23:15,100,78,30.3,pipe hum,door reflected
23:30,100,76,32.45,gull indoors,floor darkening
23:45,83,75,3.12,gull indoors,door reflected
00:00,96,74,11.79,bell once,wrong ceiling
00:15,100,73,1.46,distant surf,window shows sea
00:30,100,82,32.19,gull indoors,light below surface
00:45,90,86,10.78,breathing drain,floor darkening
01:00,77,84,12.58,muffled choir,window shows sea
01:15,100,90,21.55,muffled choir,door reflected
01:30,95,90,23.14,pipe hum,window shows sea
01:45,100,90,18.34,muffled choir,wrong ceiling
02:00,81,95,26.87,static shaped like rain,foam under desk
02:15,100,98,21.32,breathing drain,clear
02:30,100,100,7.17,gull indoors,footprints arrive
02:45,100,101,16.74,distant surf,foam under desk
03:00,100,109,32.79,breathing drain,door reflected
03:15,100,107,16.37,breathing drain,door reflected
03:30,100,110,31.85,static shaped like rain,door reflected
03:45,100,119,11.62,distant surf,floor darkening
04:00,100,119,34.72,static shaped like rain,floor darkening
04:15,96,119,0.59,breathing drain,floor darkening
04:30,100,127,3.64,none,floor darkening
04:45,100,128,15.24,static shaped like rain,floor darkening
05:00,100,134,19.64,bell once,door reflected
05:15,100,138,5.95,none,window shows sea
05:30,100,138,26.28,none,footprints arrive
05:45,95,140,15.75,pipe hum,light below surface
06:00,100,145,31.15,pipe hum,floor darkening
06:15,100,150,12.99,breathing drain,wrong ceiling
06:30,100,152,16.05,gull indoors,door reflected
06:45,100,161,27.29,muffled choir,door reflected
07:00,100,167,16.87,muffled choir,floor darkening
07:15,100,166,25.79,bell once,window shows sea
07:30,100,165,2.92,muffled choir,footprints arrive
07:45,100,165,2.96,muffled choir,door reflected
08:00,100,167,15.31,gull indoors,clear
08:15,100,169,33.73,gull indoors,floor darkening
08:30,100,169,7.62,none,footprints arrive
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
