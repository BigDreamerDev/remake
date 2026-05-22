# Sensor Log SW-MAR-2027

location: South Intake Tunnel
capture-date: 1983-01-11
device: floorline acoustic monitor

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
18:00,51,1,35.5,breathing drain,footprints arrive
18:15,58,1,32.09,none,window shows sea
18:30,50,0,0.86,muffled choir,light below surface
18:45,60,0,0.58,muffled choir,footprints arrive
19:00,62,5,12.19,bell once,light below surface
19:15,63,10,20.41,static shaped like rain,foam under desk
19:30,86,15,7.9,pipe hum,light below surface
19:45,59,22,29.82,breathing drain,window shows sea
20:00,75,30,26.73,distant surf,floor darkening
20:15,84,39,29.88,breathing drain,clear
20:30,95,47,22.56,bell once,clear
20:45,66,54,28.35,none,footprints arrive
21:00,75,60,2.85,static shaped like rain,window shows sea
21:15,98,62,26.06,breathing drain,wrong ceiling
21:30,84,62,21.59,distant surf,light below surface
21:45,94,61,1.9,pipe hum,light below surface
22:00,74,60,15.67,breathing drain,light below surface
22:15,81,65,26.23,breathing drain,wrong ceiling
22:30,100,68,11.73,breathing drain,window shows sea
22:45,73,68,20.23,none,door reflected
23:00,85,68,13.66,static shaped like rain,footprints arrive
23:15,88,68,3.64,distant surf,footprints arrive
23:30,95,72,16.12,muffled choir,footprints arrive
23:45,78,80,18.18,static shaped like rain,clear
00:00,92,80,5.7,bell once,foam under desk
00:15,100,87,16.76,breathing drain,door reflected
00:30,96,87,29.52,none,foam under desk
00:45,91,90,6.33,muffled choir,clear
01:00,87,90,21.43,muffled choir,light below surface
01:15,100,94,20.45,none,window shows sea
01:30,90,95,7.4,none,clear
01:45,100,97,9.38,static shaped like rain,door reflected
02:00,89,95,17.25,distant surf,clear
02:15,85,94,8.61,muffled choir,footprints arrive
02:30,96,94,36.49,gull indoors,door reflected
02:45,99,97,21.61,muffled choir,clear
03:00,100,100,15.39,breathing drain,floor darkening
03:15,100,108,30.83,none,footprints arrive
03:30,92,116,23.95,static shaped like rain,light below surface
03:45,100,121,19.01,pipe hum,wrong ceiling
04:00,100,124,28.11,distant surf,window shows sea
04:15,100,124,35.26,distant surf,door reflected
04:30,92,132,34.14,none,light below surface
04:45,95,137,14.65,static shaped like rain,foam under desk
05:00,100,136,22.11,breathing drain,door reflected
05:15,93,134,16.59,pipe hum,wrong ceiling
05:30,98,139,5.88,muffled choir,footprints arrive
05:45,100,141,14.41,none,light below surface
06:00,100,150,5.89,breathing drain,door reflected
06:15,100,149,33.45,distant surf,light below surface
06:30,100,158,35.13,pipe hum,light below surface
06:45,100,163,30.07,breathing drain,door reflected
07:00,100,163,3.92,muffled choir,window shows sea
07:15,100,164,13.77,pipe hum,door reflected
07:30,100,166,2.44,bell once,door reflected
07:45,100,166,14.55,pipe hum,door reflected
08:00,100,165,6.45,gull indoors,light below surface
08:15,100,172,31.82,none,footprints arrive
08:30,100,174,15.33,none,window shows sea
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
