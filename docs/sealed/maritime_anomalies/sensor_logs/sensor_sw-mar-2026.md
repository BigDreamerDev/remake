# Sensor Log SW-MAR-2026

location: Old Bathing Pavilion
capture-date: 2024-01-07
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
12:00,78,3,34.06,distant surf,light below surface
12:15,66,9,18.14,bell once,clear
12:30,58,9,16.31,static shaped like rain,light below surface
12:45,62,8,10.48,muffled choir,door reflected
13:00,84,16,20.18,pipe hum,light below surface
13:15,87,16,21.98,gull indoors,light below surface
13:30,77,25,29.03,muffled choir,clear
13:45,70,33,16.1,gull indoors,window shows sea
14:00,87,39,34.85,none,floor darkening
14:15,89,43,20.9,pipe hum,door reflected
14:30,97,51,0.33,none,clear
14:45,86,50,24.6,bell once,light below surface
15:00,91,53,31.54,pipe hum,door reflected
15:15,88,61,30.59,distant surf,footprints arrive
15:30,77,64,2.9,static shaped like rain,foam under desk
15:45,100,71,0.97,bell once,clear
16:00,100,71,35.64,distant surf,door reflected
16:15,100,75,31.63,breathing drain,light below surface
16:30,89,79,6.61,breathing drain,footprints arrive
16:45,100,84,24.38,static shaped like rain,foam under desk
17:00,100,84,5.56,static shaped like rain,foam under desk
17:15,100,90,31.42,pipe hum,window shows sea
17:30,100,94,21.64,pipe hum,wrong ceiling
17:45,100,94,23.53,gull indoors,foam under desk
18:00,84,94,3.24,distant surf,floor darkening
18:15,91,92,30.73,distant surf,light below surface
18:30,87,92,9.71,breathing drain,clear
18:45,100,101,33.16,none,foam under desk
19:00,100,110,2.67,pipe hum,floor darkening
19:15,100,109,30.38,static shaped like rain,foam under desk
19:30,100,116,32.49,distant surf,wrong ceiling
19:45,100,116,32.49,muffled choir,window shows sea
20:00,100,115,19.82,pipe hum,light below surface
20:15,91,114,22.92,breathing drain,light below surface
20:30,88,112,30.78,gull indoors,foam under desk
20:45,100,119,1.44,breathing drain,window shows sea
21:00,100,122,35.71,gull indoors,footprints arrive
21:15,100,125,27.03,breathing drain,footprints arrive
21:30,100,123,21.68,breathing drain,foam under desk
21:45,100,121,21.29,static shaped like rain,wrong ceiling
22:00,95,127,19.68,static shaped like rain,light below surface
22:15,94,125,0.65,bell once,clear
22:30,100,131,19.78,bell once,floor darkening
22:45,100,134,14.34,bell once,door reflected
23:00,100,136,32.56,gull indoors,wrong ceiling
23:15,100,140,9.43,breathing drain,clear
23:30,96,138,21.9,none,clear
23:45,100,146,33.84,muffled choir,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
