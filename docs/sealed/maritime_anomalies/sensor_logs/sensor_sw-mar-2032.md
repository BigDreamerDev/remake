# Sensor Log SW-MAR-2032

location: Lighthouse 7
capture-date: 1983-07-24
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
04:00,57,7,6.12,none,wrong ceiling
04:15,80,12,35.46,static shaped like rain,light below surface
04:30,74,12,20.16,breathing drain,light below surface
04:45,66,10,15.7,none,window shows sea
05:00,65,17,6.21,bell once,wrong ceiling
05:15,72,16,28.61,none,wrong ceiling
05:30,64,23,20.49,gull indoors,floor darkening
05:45,67,29,35.53,bell once,floor darkening
06:00,75,31,11.29,gull indoors,floor darkening
06:15,85,37,25.96,pipe hum,wrong ceiling
06:30,70,40,7.7,pipe hum,floor darkening
06:45,87,47,21.24,none,door reflected
07:00,82,49,6.0,muffled choir,floor darkening
07:15,100,58,16.64,breathing drain,light below surface
07:30,82,64,9.5,gull indoors,light below surface
07:45,76,72,4.3,gull indoors,footprints arrive
08:00,100,70,18.65,breathing drain,light below surface
08:15,94,79,17.86,breathing drain,door reflected
08:30,79,78,7.87,bell once,clear
08:45,100,85,11.52,none,door reflected
09:00,95,85,8.15,breathing drain,door reflected
09:15,100,83,17.24,muffled choir,clear
09:30,85,82,11.03,distant surf,window shows sea
09:45,96,82,29.15,none,light below surface
10:00,100,89,28.64,muffled choir,clear
10:15,91,91,21.17,bell once,light below surface
10:30,85,89,2.14,static shaped like rain,door reflected
10:45,86,87,13.38,bell once,window shows sea
11:00,90,89,5.43,breathing drain,door reflected
11:15,100,90,18.16,breathing drain,foam under desk
11:30,100,93,11.32,none,wrong ceiling
11:45,100,94,17.31,pipe hum,footprints arrive
12:00,100,99,25.23,bell once,floor darkening
12:15,96,102,23.03,distant surf,wrong ceiling
12:30,88,106,19.6,static shaped like rain,wrong ceiling
12:45,100,113,30.84,breathing drain,wrong ceiling
13:00,100,120,25.58,gull indoors,wrong ceiling
13:15,100,128,11.67,distant surf,foam under desk
13:30,100,136,17.33,static shaped like rain,clear
13:45,100,136,33.9,breathing drain,light below surface
14:00,100,134,26.07,pipe hum,footprints arrive
14:15,97,138,28.22,breathing drain,light below surface
14:30,100,145,19.55,gull indoors,door reflected
14:45,100,146,14.94,pipe hum,foam under desk
15:00,100,144,6.75,muffled choir,light below surface
15:15,100,148,33.92,muffled choir,window shows sea
15:30,100,155,4.99,muffled choir,foam under desk
15:45,100,163,5.31,breathing drain,footprints arrive
16:00,100,170,6.49,gull indoors,foam under desk
16:15,100,168,22.36,bell once,foam under desk
16:30,100,167,30.48,distant surf,wrong ceiling
16:45,100,170,31.97,static shaped like rain,footprints arrive
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
