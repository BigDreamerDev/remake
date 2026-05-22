# Sensor Log SW-MAR-2012

location: Old Bathing Pavilion
capture-date: 2022-08-02
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
16:00,84,5,12.41,bell once,footprints arrive
16:15,73,7,14.82,muffled choir,window shows sea
16:30,74,5,4.56,gull indoors,floor darkening
16:45,84,6,17.49,muffled choir,window shows sea
17:00,59,5,2.07,none,footprints arrive
17:15,56,12,34.88,gull indoors,clear
17:30,75,17,12.5,static shaped like rain,wrong ceiling
17:45,75,23,15.22,gull indoors,clear
18:00,76,25,35.91,bell once,footprints arrive
18:15,65,29,10.29,muffled choir,window shows sea
18:30,87,32,16.58,gull indoors,floor darkening
18:45,92,39,15.85,bell once,wrong ceiling
19:00,80,46,27.64,muffled choir,window shows sea
19:15,72,45,2.16,bell once,wrong ceiling
19:30,76,49,33.58,static shaped like rain,floor darkening
19:45,76,58,10.04,pipe hum,door reflected
20:00,83,62,13.29,muffled choir,footprints arrive
20:15,92,62,22.39,bell once,floor darkening
20:30,96,66,23.53,static shaped like rain,door reflected
20:45,99,75,14.85,breathing drain,footprints arrive
21:00,76,82,25.92,pipe hum,wrong ceiling
21:15,100,82,18.11,static shaped like rain,window shows sea
21:30,88,90,35.3,static shaped like rain,foam under desk
21:45,79,92,1.07,muffled choir,wrong ceiling
22:00,100,92,16.32,gull indoors,foam under desk
22:15,81,99,7.66,none,light below surface
22:30,100,102,33.56,distant surf,door reflected
22:45,100,106,14.42,pipe hum,wrong ceiling
23:00,87,112,32.48,muffled choir,wrong ceiling
23:15,100,117,28.21,distant surf,clear
23:30,100,115,34.13,pipe hum,wrong ceiling
23:45,94,114,0.26,bell once,door reflected
00:00,100,114,33.09,gull indoors,light below surface
00:15,100,117,13.3,distant surf,footprints arrive
00:30,97,123,32.92,muffled choir,footprints arrive
00:45,92,122,6.42,muffled choir,foam under desk
01:00,100,124,8.29,breathing drain,door reflected
01:15,96,127,10.71,breathing drain,clear
01:30,100,125,36.48,bell once,door reflected
01:45,89,124,9.82,bell once,wrong ceiling
02:00,100,125,26.21,breathing drain,window shows sea
02:15,100,127,1.36,bell once,door reflected
02:30,100,125,0.23,muffled choir,clear
02:45,100,132,28.69,distant surf,footprints arrive
03:00,99,135,34.13,pipe hum,floor darkening
03:15,100,142,35.19,breathing drain,footprints arrive
03:30,99,142,12.86,muffled choir,floor darkening
03:45,100,149,3.77,bell once,door reflected
04:00,100,154,15.16,static shaped like rain,window shows sea
04:15,100,161,33.09,none,foam under desk
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
