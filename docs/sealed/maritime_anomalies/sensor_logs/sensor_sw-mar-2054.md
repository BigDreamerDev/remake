# Sensor Log SW-MAR-2054

location: Blue Door Quay
capture-date: 1985-10-12
device: manual tide staff

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
18:00,58,0,0.85,pipe hum,foam under desk
18:15,68,1,27.84,pipe hum,foam under desk
18:30,80,0,0.88,muffled choir,clear
18:45,72,0,0.46,muffled choir,clear
19:00,73,8,0.81,gull indoors,wrong ceiling
19:15,61,8,4.45,muffled choir,footprints arrive
19:30,58,15,25.25,pipe hum,footprints arrive
19:45,82,17,10.03,bell once,footprints arrive
20:00,87,19,15.55,breathing drain,foam under desk
20:15,57,20,1.37,gull indoors,floor darkening
20:30,64,26,25.96,gull indoors,foam under desk
20:45,83,31,31.54,static shaped like rain,door reflected
21:00,64,29,34.6,gull indoors,foam under desk
21:15,82,35,15.42,gull indoors,foam under desk
21:30,70,35,12.71,bell once,light below surface
21:45,63,42,20.35,muffled choir,window shows sea
22:00,93,51,27.59,distant surf,footprints arrive
22:15,89,52,23.43,bell once,wrong ceiling
22:30,77,58,19.71,muffled choir,light below surface
22:45,88,57,27.61,bell once,clear
23:00,87,65,7.54,gull indoors,footprints arrive
23:15,93,73,2.85,static shaped like rain,light below surface
23:30,83,71,25.69,bell once,floor darkening
23:45,82,73,4.46,distant surf,wrong ceiling
00:00,85,75,2.25,breathing drain,wrong ceiling
00:15,100,82,12.81,static shaped like rain,window shows sea
00:30,100,89,25.82,none,wrong ceiling
00:45,87,94,28.65,static shaped like rain,foam under desk
01:00,89,102,25.53,static shaped like rain,foam under desk
01:15,83,101,2.21,bell once,light below surface
01:30,100,110,25.93,distant surf,clear
01:45,100,114,27.67,static shaped like rain,door reflected
02:00,100,118,11.37,distant surf,light below surface
02:15,90,117,3.12,bell once,clear
02:30,98,115,32.89,static shaped like rain,window shows sea
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
