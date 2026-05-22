# Sensor Log SW-MAR-2049

location: Lower Bell Marina
capture-date: 1985-04-08
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
18:00,55,5,4.98,muffled choir,clear
18:15,58,4,14.36,static shaped like rain,door reflected
18:30,60,3,28.56,muffled choir,floor darkening
18:45,69,5,31.62,bell once,door reflected
19:00,81,3,0.85,bell once,foam under desk
19:15,83,11,31.66,breathing drain,foam under desk
19:30,86,13,1.56,none,light below surface
19:45,80,17,22.9,pipe hum,wrong ceiling
20:00,63,18,31.61,pipe hum,wrong ceiling
20:15,77,17,1.42,bell once,clear
20:30,88,20,9.7,none,door reflected
20:45,56,24,6.73,muffled choir,clear
21:00,64,27,32.03,breathing drain,wrong ceiling
21:15,60,26,6.21,muffled choir,window shows sea
21:30,65,27,19.45,muffled choir,window shows sea
21:45,65,27,34.35,none,foam under desk
22:00,75,35,26.71,pipe hum,floor darkening
22:15,64,44,27.3,none,foam under desk
22:30,70,47,17.13,gull indoors,wrong ceiling
22:45,68,56,6.42,bell once,footprints arrive
23:00,92,60,15.32,pipe hum,footprints arrive
23:15,69,60,33.61,distant surf,footprints arrive
23:30,84,68,25.53,none,footprints arrive
23:45,100,73,3.56,gull indoors,clear
00:00,100,76,12.32,muffled choir,floor darkening
00:15,78,85,19.68,gull indoors,door reflected
00:30,78,90,16.21,breathing drain,clear
00:45,100,92,21.32,breathing drain,window shows sea
01:00,81,94,36.29,gull indoors,foam under desk
01:15,96,92,35.47,muffled choir,floor darkening
01:30,100,94,11.76,none,footprints arrive
01:45,100,100,4.62,static shaped like rain,light below surface
02:00,93,102,9.19,breathing drain,floor darkening
02:15,90,107,15.88,muffled choir,light below surface
02:30,100,115,7.67,gull indoors,light below surface
02:45,100,120,36.56,bell once,foam under desk
03:00,100,123,7.93,none,light below surface
03:15,88,121,25.52,muffled choir,wrong ceiling
03:30,100,119,18.87,static shaped like rain,door reflected
03:45,100,123,22.37,distant surf,window shows sea
04:00,100,131,9.23,none,foam under desk
04:15,100,134,20.21,pipe hum,footprints arrive
04:30,100,133,20.82,gull indoors,floor darkening
04:45,100,139,12.0,static shaped like rain,window shows sea
05:00,100,137,7.52,gull indoors,clear
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
