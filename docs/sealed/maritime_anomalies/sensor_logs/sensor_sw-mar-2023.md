# Sensor Log SW-MAR-2023

location: Old Bathing Pavilion
capture-date: 2023-08-30
device: floorline acoustic monitor

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
22:00,82,0,0.6,breathing drain,clear
22:15,55,8,18.79,none,light below surface
22:30,74,17,16.76,distant surf,window shows sea
22:45,60,18,13.03,breathing drain,floor darkening
23:00,62,17,21.86,bell once,floor darkening
23:15,68,22,34.12,static shaped like rain,clear
23:30,81,23,4.77,none,clear
23:45,91,30,2.36,pipe hum,clear
00:00,74,30,2.27,breathing drain,footprints arrive
00:15,85,30,13.81,none,floor darkening
00:30,78,37,22.18,breathing drain,window shows sea
00:45,68,35,33.02,static shaped like rain,wrong ceiling
01:00,63,43,23.29,distant surf,clear
01:15,82,41,11.32,none,clear
01:30,82,49,12.39,pipe hum,wrong ceiling
01:45,77,50,9.35,muffled choir,foam under desk
02:00,67,48,19.73,breathing drain,light below surface
02:15,69,57,17.0,static shaped like rain,door reflected
02:30,72,63,17.74,muffled choir,window shows sea
02:45,98,68,4.71,distant surf,clear
03:00,75,77,22.72,static shaped like rain,light below surface
03:15,92,83,1.68,breathing drain,clear
03:30,86,87,5.91,gull indoors,foam under desk
03:45,89,96,12.73,gull indoors,floor darkening
04:00,100,100,10.6,pipe hum,floor darkening
04:15,85,108,17.91,distant surf,door reflected
04:30,100,116,35.81,muffled choir,foam under desk
04:45,100,117,1.54,gull indoors,light below surface
05:00,100,115,4.25,distant surf,wrong ceiling
05:15,100,116,11.37,pipe hum,footprints arrive
05:30,100,120,26.02,distant surf,light below surface
05:45,100,128,31.61,gull indoors,clear
06:00,100,131,10.38,muffled choir,footprints arrive
06:15,100,136,11.87,gull indoors,footprints arrive
06:30,97,136,4.18,breathing drain,footprints arrive
06:45,98,143,8.47,bell once,light below surface
07:00,100,145,5.22,breathing drain,footprints arrive
07:15,100,149,5.67,static shaped like rain,door reflected
07:30,100,148,23.27,none,wrong ceiling
07:45,100,156,16.87,gull indoors,window shows sea
08:00,100,164,28.3,bell once,foam under desk
08:15,100,162,16.06,pipe hum,wrong ceiling
08:30,100,166,2.28,muffled choir,window shows sea
08:45,100,172,13.2,gull indoors,door reflected
09:00,100,172,22.78,distant surf,foam under desk
09:15,100,177,27.86,static shaped like rain,floor darkening
09:30,100,184,1.01,none,foam under desk
09:45,100,191,18.92,bell once,floor darkening
10:00,100,198,4.96,muffled choir,footprints arrive
10:15,100,199,2.4,bell once,footprints arrive
10:30,100,202,21.84,distant surf,door reflected
10:45,100,208,31.6,none,door reflected
11:00,100,206,16.51,bell once,clear
11:15,100,206,18.6,static shaped like rain,wrong ceiling
11:30,100,207,10.33,pipe hum,wrong ceiling
11:45,100,214,31.43,breathing drain,foam under desk
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
