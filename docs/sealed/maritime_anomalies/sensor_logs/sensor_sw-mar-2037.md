# Sensor Log SW-MAR-2037

location: Rain Room 11
capture-date: 1984-01-14
device: floorline acoustic monitor

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
19:00,60,0,0.93,gull indoors,foam under desk
19:15,54,3,26.54,breathing drain,light below surface
19:30,73,2,9.27,distant surf,footprints arrive
19:45,59,4,16.32,muffled choir,clear
20:00,52,3,20.48,breathing drain,window shows sea
20:15,67,8,5.44,muffled choir,window shows sea
20:30,65,12,11.84,static shaped like rain,foam under desk
20:45,73,19,21.57,muffled choir,clear
21:00,60,20,22.98,gull indoors,footprints arrive
21:15,80,27,34.44,distant surf,door reflected
21:30,72,25,22.96,muffled choir,foam under desk
21:45,89,27,29.44,muffled choir,clear
22:00,89,30,32.38,gull indoors,door reflected
22:15,72,37,3.7,none,floor darkening
22:30,64,36,35.85,static shaped like rain,wrong ceiling
22:45,77,45,20.42,pipe hum,clear
23:00,65,53,9.96,muffled choir,clear
23:15,68,52,6.89,distant surf,window shows sea
23:30,92,55,24.98,muffled choir,floor darkening
23:45,69,62,22.93,gull indoors,window shows sea
00:00,88,68,6.8,none,door reflected
00:15,86,74,29.38,pipe hum,clear
00:30,96,76,17.43,pipe hum,floor darkening
00:45,100,74,8.05,gull indoors,clear
01:00,96,76,2.11,distant surf,window shows sea
01:15,100,85,0.47,bell once,footprints arrive
01:30,95,87,7.54,pipe hum,floor darkening
01:45,97,87,22.51,breathing drain,footprints arrive
02:00,100,96,19.78,gull indoors,light below surface
02:15,85,98,9.5,pipe hum,wrong ceiling
02:30,84,105,21.02,breathing drain,clear
02:45,95,112,1.53,none,clear
03:00,100,119,17.81,distant surf,footprints arrive
03:15,100,125,31.58,static shaped like rain,window shows sea
03:30,100,133,25.65,none,light below surface
03:45,100,136,21.66,none,foam under desk
04:00,100,139,1.29,pipe hum,door reflected
04:15,100,137,27.83,breathing drain,floor darkening
04:30,100,146,13.69,breathing drain,floor darkening
04:45,100,147,23.02,gull indoors,footprints arrive
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
