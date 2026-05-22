# Sensor Log SW-MAR-2046

location: Rain Room 11
capture-date: 1984-12-05
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
02:00,61,9,30.41,pipe hum,clear
02:15,67,17,31.48,pipe hum,door reflected
02:30,67,21,34.1,distant surf,wrong ceiling
02:45,86,28,0.91,bell once,door reflected
03:00,61,32,36.4,gull indoors,footprints arrive
03:15,79,41,26.65,breathing drain,window shows sea
03:30,93,39,6.91,none,light below surface
03:45,89,38,2.18,breathing drain,light below surface
04:00,92,36,32.8,muffled choir,footprints arrive
04:15,63,43,1.99,muffled choir,light below surface
04:30,76,48,6.32,muffled choir,window shows sea
04:45,94,50,9.64,static shaped like rain,floor darkening
05:00,76,57,16.33,gull indoors,window shows sea
05:15,73,61,2.74,gull indoors,floor darkening
05:30,100,63,20.62,muffled choir,foam under desk
05:45,96,63,25.75,breathing drain,light below surface
06:00,81,61,17.21,breathing drain,light below surface
06:15,93,64,7.8,gull indoors,footprints arrive
06:30,100,71,24.44,static shaped like rain,footprints arrive
06:45,76,69,7.22,none,foam under desk
07:00,70,67,5.59,static shaped like rain,floor darkening
07:15,87,75,19.33,distant surf,window shows sea
07:30,99,76,23.91,pipe hum,floor darkening
07:45,100,82,4.66,distant surf,door reflected
08:00,79,89,15.67,breathing drain,door reflected
08:15,83,93,7.52,bell once,floor darkening
08:30,95,93,10.22,muffled choir,light below surface
08:45,88,100,36.05,breathing drain,window shows sea
09:00,81,99,20.58,none,footprints arrive
09:15,100,107,31.87,static shaped like rain,window shows sea
09:30,100,110,16.95,none,light below surface
09:45,98,111,15.07,breathing drain,wrong ceiling
10:00,100,117,31.1,distant surf,door reflected
10:15,100,118,12.55,bell once,footprints arrive
10:30,98,124,22.58,none,footprints arrive
10:45,100,122,32.84,none,wrong ceiling
11:00,100,130,12.56,static shaped like rain,door reflected
11:15,100,130,12.59,distant surf,wrong ceiling
11:30,100,132,3.52,muffled choir,footprints arrive
11:45,100,138,21.37,none,window shows sea
12:00,100,146,18.59,muffled choir,door reflected
12:15,100,155,2.18,breathing drain,door reflected
12:30,100,155,9.36,muffled choir,wrong ceiling
12:45,100,153,10.69,muffled choir,door reflected
13:00,100,159,23.06,distant surf,clear
13:15,100,163,13.75,pipe hum,clear
13:30,100,166,34.27,distant surf,clear
13:45,100,172,6.24,distant surf,floor darkening
14:00,100,173,12.31,static shaped like rain,footprints arrive
14:15,100,174,11.33,gull indoors,door reflected
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
