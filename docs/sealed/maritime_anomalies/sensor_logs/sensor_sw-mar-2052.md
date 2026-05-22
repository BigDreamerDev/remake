# Sensor Log SW-MAR-2052

location: West Sluice Door
capture-date: 1985-07-21
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
05:00,58,2,26.24,bell once,footprints arrive
05:15,57,8,11.68,breathing drain,wrong ceiling
05:30,66,7,32.15,bell once,wrong ceiling
05:45,79,9,11.71,gull indoors,door reflected
06:00,62,14,18.8,muffled choir,light below surface
06:15,82,15,23.55,gull indoors,window shows sea
06:30,75,21,15.58,muffled choir,door reflected
06:45,89,26,33.86,none,wrong ceiling
07:00,87,27,6.25,muffled choir,wrong ceiling
07:15,64,26,9.88,distant surf,light below surface
07:30,91,33,25.73,muffled choir,foam under desk
07:45,70,36,28.78,none,floor darkening
08:00,94,43,27.57,bell once,foam under desk
08:15,97,48,16.55,static shaped like rain,clear
08:30,76,50,20.91,bell once,floor darkening
08:45,92,56,29.64,static shaped like rain,window shows sea
09:00,92,62,16.87,distant surf,door reflected
09:15,100,66,6.67,gull indoors,clear
09:30,86,73,4.91,distant surf,floor darkening
09:45,95,76,3.14,none,foam under desk
10:00,85,85,33.34,none,light below surface
10:15,86,90,26.92,bell once,footprints arrive
10:30,90,90,34.7,breathing drain,window shows sea
10:45,100,94,28.27,static shaped like rain,foam under desk
11:00,98,98,7.14,muffled choir,footprints arrive
11:15,82,103,35.68,breathing drain,clear
11:30,100,107,18.49,muffled choir,light below surface
11:45,84,106,25.55,muffled choir,door reflected
12:00,83,105,19.71,pipe hum,foam under desk
12:15,88,114,23.75,muffled choir,light below surface
12:30,96,114,23.56,muffled choir,door reflected
12:45,89,120,27.41,breathing drain,wrong ceiling
13:00,94,124,20.47,pipe hum,floor darkening
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
