# Sensor Log SW-MAR-2006

location: The Pool That Was Not Built
capture-date: 2021-12-25
device: floorline acoustic monitor

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
19:00,52,1,16.48,none,wrong ceiling
19:15,57,1,3.07,gull indoors,footprints arrive
19:30,82,7,29.35,gull indoors,footprints arrive
19:45,79,14,4.72,none,foam under desk
20:00,69,15,32.64,static shaped like rain,door reflected
20:15,81,23,29.17,gull indoors,window shows sea
20:30,62,30,30.19,static shaped like rain,light below surface
20:45,66,36,15.12,distant surf,footprints arrive
21:00,92,38,25.67,muffled choir,footprints arrive
21:15,80,47,14.89,gull indoors,footprints arrive
21:30,80,54,17.06,none,door reflected
21:45,88,53,21.64,bell once,wrong ceiling
22:00,90,59,26.58,static shaped like rain,floor darkening
22:15,100,62,22.98,bell once,foam under desk
22:30,82,64,23.66,pipe hum,foam under desk
22:45,80,70,9.75,none,footprints arrive
23:00,100,74,36.25,bell once,foam under desk
23:15,83,77,16.6,pipe hum,floor darkening
23:30,100,83,30.49,bell once,footprints arrive
23:45,100,87,8.42,static shaped like rain,window shows sea
00:00,99,92,34.75,bell once,floor darkening
00:15,100,93,1.93,gull indoors,footprints arrive
00:30,100,91,2.66,gull indoors,wrong ceiling
00:45,85,89,7.17,pipe hum,clear
01:00,100,90,9.07,distant surf,light below surface
01:15,80,90,0.43,gull indoors,clear
01:30,80,98,27.58,pipe hum,door reflected
01:45,96,101,23.19,bell once,clear
02:00,100,103,0.96,gull indoors,foam under desk
02:15,100,110,13.22,muffled choir,floor darkening
02:30,98,114,8.04,gull indoors,floor darkening
02:45,95,119,21.18,static shaped like rain,door reflected
03:00,100,125,5.17,muffled choir,door reflected
03:15,100,133,1.62,bell once,light below surface
03:30,100,136,28.03,bell once,clear
03:45,100,138,11.43,distant surf,door reflected
04:00,100,136,18.06,pipe hum,clear
04:15,100,141,23.31,muffled choir,wrong ceiling
04:30,100,143,13.27,bell once,clear
04:45,100,149,27.44,static shaped like rain,window shows sea
05:00,100,156,24.07,static shaped like rain,clear
05:15,100,164,32.07,static shaped like rain,door reflected
05:30,100,163,15.79,pipe hum,footprints arrive
05:45,100,171,4.7,muffled choir,foam under desk
06:00,100,173,16.76,none,floor darkening
06:15,100,181,12.79,gull indoors,footprints arrive
06:30,100,184,22.1,breathing drain,window shows sea
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
