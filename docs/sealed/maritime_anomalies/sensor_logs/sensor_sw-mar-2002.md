# Sensor Log SW-MAR-2002

location: West Sluice Door
capture-date: 2021-07-19
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
12:00,78,3,28.14,distant surf,floor darkening
12:15,67,4,14.96,gull indoors,wrong ceiling
12:30,78,6,8.99,gull indoors,floor darkening
12:45,80,13,23.47,distant surf,floor darkening
13:00,57,14,18.3,distant surf,floor darkening
13:15,74,18,34.91,static shaped like rain,floor darkening
13:30,79,26,26.07,static shaped like rain,clear
13:45,72,31,24.84,distant surf,footprints arrive
14:00,79,32,12.78,breathing drain,footprints arrive
14:15,65,39,31.9,muffled choir,wrong ceiling
14:30,94,41,24.08,bell once,foam under desk
14:45,69,50,16.18,breathing drain,footprints arrive
15:00,81,56,32.39,breathing drain,light below surface
15:15,95,62,25.63,gull indoors,floor darkening
15:30,90,70,10.63,static shaped like rain,door reflected
15:45,76,77,16.19,pipe hum,clear
16:00,100,84,10.58,gull indoors,window shows sea
16:15,100,87,18.2,breathing drain,door reflected
16:30,81,94,5.57,gull indoors,foam under desk
16:45,85,102,13.4,bell once,floor darkening
17:00,100,102,2.55,gull indoors,wrong ceiling
17:15,100,110,17.32,gull indoors,door reflected
17:30,90,108,7.29,bell once,foam under desk
17:45,89,116,9.05,none,window shows sea
18:00,100,122,19.52,bell once,wrong ceiling
18:15,100,128,32.97,static shaped like rain,wrong ceiling
18:30,100,135,14.12,bell once,foam under desk
18:45,100,144,16.69,pipe hum,door reflected
19:00,100,153,32.68,distant surf,window shows sea
19:15,100,156,12.81,static shaped like rain,foam under desk
19:30,100,155,4.58,pipe hum,light below surface
19:45,100,162,8.82,bell once,clear
20:00,100,167,31.38,none,wrong ceiling
20:15,100,174,34.02,pipe hum,door reflected
20:30,100,181,18.55,bell once,footprints arrive
20:45,100,184,33.48,gull indoors,foam under desk
21:00,100,184,14.33,breathing drain,foam under desk
21:15,100,183,5.38,bell once,door reflected
21:30,100,183,21.44,pipe hum,floor darkening
21:45,100,184,33.78,distant surf,light below surface
22:00,100,192,7.98,static shaped like rain,floor darkening
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
