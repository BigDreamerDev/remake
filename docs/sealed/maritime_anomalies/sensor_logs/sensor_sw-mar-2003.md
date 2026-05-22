# Sensor Log SW-MAR-2003

location: Blue Door Quay
capture-date: 2021-08-30
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
15:00,58,0,0.45,static shaped like rain,foam under desk
15:15,81,8,15.24,breathing drain,window shows sea
15:30,56,15,20.66,none,window shows sea
15:45,76,24,16.57,breathing drain,wrong ceiling
16:00,90,28,27.06,breathing drain,floor darkening
16:15,70,36,2.28,muffled choir,light below surface
16:30,87,37,1.17,muffled choir,floor darkening
16:45,64,40,3.56,gull indoors,clear
17:00,81,42,12.54,distant surf,window shows sea
17:15,74,42,26.86,static shaped like rain,clear
17:30,94,51,18.37,bell once,window shows sea
17:45,100,58,6.8,none,window shows sea
18:00,75,59,30.79,pipe hum,foam under desk
18:15,86,68,13.28,gull indoors,wrong ceiling
18:30,90,76,23.55,muffled choir,door reflected
18:45,83,83,30.66,muffled choir,light below surface
19:00,83,81,25.41,gull indoors,footprints arrive
19:15,88,81,13.48,pipe hum,door reflected
19:30,100,83,9.13,muffled choir,wrong ceiling
19:45,100,87,13.68,pipe hum,foam under desk
20:00,100,90,19.36,static shaped like rain,wrong ceiling
20:15,95,98,11.0,distant surf,window shows sea
20:30,84,101,15.79,pipe hum,floor darkening
20:45,87,101,29.47,none,door reflected
21:00,96,107,1.56,distant surf,door reflected
21:15,100,114,28.02,muffled choir,clear
21:30,90,112,36.45,bell once,foam under desk
21:45,100,110,14.57,breathing drain,floor darkening
22:00,93,108,17.38,pipe hum,footprints arrive
22:15,94,113,36.01,muffled choir,light below surface
22:30,94,115,27.81,bell once,foam under desk
22:45,93,123,7.98,bell once,clear
23:00,99,121,15.49,static shaped like rain,footprints arrive
23:15,100,130,7.93,pipe hum,footprints arrive
23:30,100,137,32.37,distant surf,door reflected
23:45,100,145,26.4,gull indoors,door reflected
00:00,100,148,5.93,muffled choir,door reflected
00:15,100,151,9.61,pipe hum,window shows sea
00:30,100,155,16.69,breathing drain,foam under desk
00:45,100,161,12.99,muffled choir,floor darkening
01:00,100,168,29.3,breathing drain,footprints arrive
01:15,100,177,0.23,distant surf,floor darkening
01:30,100,186,0.64,bell once,foam under desk
01:45,100,193,16.74,static shaped like rain,foam under desk
02:00,100,199,17.58,static shaped like rain,window shows sea
02:15,100,203,32.29,pipe hum,wrong ceiling
02:30,100,210,19.25,none,door reflected
02:45,100,219,35.56,breathing drain,window shows sea
03:00,100,228,10.66,bell once,foam under desk
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
