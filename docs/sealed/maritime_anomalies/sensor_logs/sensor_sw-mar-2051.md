# Sensor Log SW-MAR-2051

location: Rain Room 11
capture-date: 1985-06-17
device: floorline acoustic monitor

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
18:00,74,5,16.25,static shaped like rain,light below surface
18:15,76,9,34.63,breathing drain,light below surface
18:30,70,13,28.82,pipe hum,footprints arrive
18:45,69,21,9.74,breathing drain,window shows sea
19:00,73,23,22.69,gull indoors,clear
19:15,91,31,30.96,none,clear
19:30,84,35,29.86,gull indoors,window shows sea
19:45,67,43,6.8,pipe hum,door reflected
20:00,72,48,24.5,distant surf,door reflected
20:15,72,57,10.11,breathing drain,footprints arrive
20:30,73,55,3.24,distant surf,foam under desk
20:45,84,59,34.41,static shaped like rain,floor darkening
21:00,100,66,6.22,none,foam under desk
21:15,91,71,26.61,distant surf,footprints arrive
21:30,98,80,2.41,breathing drain,light below surface
21:45,100,81,25.52,static shaped like rain,door reflected
22:00,80,88,30.06,none,floor darkening
22:15,89,97,34.57,breathing drain,floor darkening
22:30,96,104,1.09,static shaped like rain,footprints arrive
22:45,99,113,25.27,static shaped like rain,light below surface
23:00,100,114,21.16,pipe hum,clear
23:15,100,114,22.23,static shaped like rain,footprints arrive
23:30,100,114,6.6,muffled choir,footprints arrive
23:45,100,123,20.39,muffled choir,window shows sea
00:00,98,131,7.95,none,floor darkening
00:15,100,129,15.25,pipe hum,clear
00:30,100,131,21.07,muffled choir,clear
00:45,100,140,28.68,distant surf,wrong ceiling
01:00,100,142,12.44,none,footprints arrive
01:15,98,142,9.92,distant surf,floor darkening
01:30,100,150,1.87,pipe hum,footprints arrive
01:45,100,152,20.88,muffled choir,light below surface
02:00,100,153,10.94,distant surf,window shows sea
02:15,100,153,10.16,bell once,floor darkening
02:30,100,160,16.95,pipe hum,footprints arrive
02:45,100,158,23.56,gull indoors,clear
03:00,100,159,36.52,gull indoors,door reflected
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
