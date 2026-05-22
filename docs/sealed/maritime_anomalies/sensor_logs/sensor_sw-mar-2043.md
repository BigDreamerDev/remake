# Sensor Log SW-MAR-2043

location: Lower Bell Marina
capture-date: 1984-08-24
device: manual tide staff

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
10:00,66,0,0.48,static shaped like rain,door reflected
10:15,82,6,9.89,static shaped like rain,foam under desk
10:30,64,6,6.16,gull indoors,light below surface
10:45,52,14,1.37,pipe hum,footprints arrive
11:00,88,17,21.58,none,clear
11:15,70,19,26.7,bell once,window shows sea
11:30,86,19,34.63,pipe hum,clear
11:45,73,24,27.06,bell once,door reflected
12:00,79,24,5.55,gull indoors,clear
12:15,76,30,22.37,distant surf,footprints arrive
12:30,81,30,12.53,none,foam under desk
12:45,79,29,1.23,muffled choir,clear
13:00,80,35,25.61,bell once,floor darkening
13:15,64,37,30.87,breathing drain,wrong ceiling
13:30,64,40,27.85,gull indoors,clear
13:45,92,41,14.86,none,window shows sea
14:00,68,44,34.16,static shaped like rain,light below surface
14:15,90,51,31.37,static shaped like rain,wrong ceiling
14:30,88,56,14.99,gull indoors,foam under desk
14:45,94,58,9.64,gull indoors,floor darkening
15:00,94,56,35.46,distant surf,window shows sea
15:15,73,64,7.61,pipe hum,floor darkening
15:30,95,71,1.5,none,floor darkening
15:45,94,78,14.72,pipe hum,door reflected
16:00,90,84,28.73,muffled choir,foam under desk
16:15,89,91,34.76,bell once,door reflected
16:30,100,98,20.77,none,footprints arrive
16:45,100,97,14.59,static shaped like rain,light below surface
17:00,90,99,16.59,distant surf,wrong ceiling
17:15,88,107,3.37,pipe hum,wrong ceiling
17:30,100,105,33.1,muffled choir,clear
17:45,100,106,5.09,breathing drain,clear
18:00,93,104,15.11,muffled choir,door reflected
18:15,100,111,13.09,static shaped like rain,light below surface
18:30,100,118,30.34,none,foam under desk
18:45,100,119,15.42,static shaped like rain,light below surface
19:00,100,121,29.84,pipe hum,foam under desk
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
