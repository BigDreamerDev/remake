# Sensor Log SW-MAR-2033

location: Blue Door Quay
capture-date: 1983-08-26
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
06:00,82,5,17.48,muffled choir,footprints arrive
06:15,69,9,1.29,gull indoors,clear
06:30,75,16,24.42,distant surf,door reflected
06:45,89,24,29.7,none,light below surface
07:00,83,31,3.8,distant surf,footprints arrive
07:15,87,38,5.17,breathing drain,clear
07:30,89,41,15.4,muffled choir,window shows sea
07:45,72,39,3.49,pipe hum,floor darkening
08:00,94,45,18.56,pipe hum,window shows sea
08:15,67,50,10.65,static shaped like rain,clear
08:30,91,57,36.61,bell once,window shows sea
08:45,71,57,26.0,muffled choir,footprints arrive
09:00,84,64,8.2,none,window shows sea
09:15,86,73,25.49,pipe hum,window shows sea
09:30,77,73,26.35,breathing drain,window shows sea
09:45,95,82,33.3,muffled choir,floor darkening
10:00,88,80,32.25,breathing drain,foam under desk
10:15,89,79,13.38,pipe hum,window shows sea
10:30,100,87,31.2,gull indoors,light below surface
10:45,84,91,10.94,bell once,footprints arrive
11:00,100,99,17.96,distant surf,foam under desk
11:15,94,106,4.6,static shaped like rain,clear
11:30,88,113,15.88,muffled choir,window shows sea
11:45,100,121,3.21,muffled choir,foam under desk
12:00,91,125,18.18,pipe hum,door reflected
12:15,100,132,22.65,bell once,light below surface
12:30,98,130,19.26,breathing drain,window shows sea
12:45,100,135,33.99,distant surf,foam under desk
13:00,100,136,2.5,bell once,clear
13:15,100,137,18.3,gull indoors,footprints arrive
13:30,100,136,17.08,bell once,light below surface
13:45,100,137,29.01,distant surf,floor darkening
14:00,99,142,1.77,pipe hum,wrong ceiling
14:15,100,146,36.74,static shaped like rain,door reflected
14:30,100,155,35.75,none,wrong ceiling
14:45,100,155,16.36,breathing drain,door reflected
15:00,100,155,8.43,pipe hum,window shows sea
15:15,100,164,25.66,static shaped like rain,door reflected
15:30,100,162,23.85,breathing drain,light below surface
15:45,100,162,19.94,gull indoors,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
