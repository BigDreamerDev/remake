# Sensor Log SW-MAR-2020

location: Sublevel K Drainage
capture-date: 2023-05-16
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
11:00,60,4,9.25,muffled choir,door reflected
11:15,59,10,3.59,bell once,window shows sea
11:30,70,13,13.73,static shaped like rain,floor darkening
11:45,75,16,4.84,muffled choir,footprints arrive
12:00,58,18,33.56,distant surf,window shows sea
12:15,67,17,7.34,bell once,door reflected
12:30,70,18,25.24,muffled choir,light below surface
12:45,71,18,29.0,static shaped like rain,floor darkening
13:00,58,21,26.04,static shaped like rain,footprints arrive
13:15,63,30,6.67,gull indoors,light below surface
13:30,66,35,3.92,distant surf,floor darkening
13:45,87,35,1.33,muffled choir,clear
14:00,94,42,11.58,bell once,light below surface
14:15,74,47,32.32,gull indoors,light below surface
14:30,92,50,7.97,gull indoors,window shows sea
14:45,93,48,11.55,muffled choir,clear
15:00,77,52,14.43,static shaped like rain,window shows sea
15:15,99,54,22.49,distant surf,foam under desk
15:30,97,59,13.49,static shaped like rain,foam under desk
15:45,80,63,21.1,gull indoors,window shows sea
16:00,89,68,6.37,gull indoors,wrong ceiling
16:15,85,75,29.1,none,clear
16:30,100,83,4.61,pipe hum,door reflected
16:45,77,87,26.57,gull indoors,footprints arrive
17:00,100,90,15.53,breathing drain,foam under desk
17:15,85,89,18.22,pipe hum,foam under desk
17:30,82,89,1.06,breathing drain,footprints arrive
17:45,100,92,17.11,none,door reflected
18:00,100,93,1.56,static shaped like rain,clear
18:15,100,91,29.05,pipe hum,footprints arrive
18:30,100,100,9.53,muffled choir,foam under desk
18:45,82,102,29.6,muffled choir,door reflected
19:00,86,111,24.81,muffled choir,door reflected
19:15,100,119,6.66,bell once,foam under desk
19:30,100,128,31.68,none,floor darkening
19:45,100,133,12.05,none,floor darkening
20:00,100,137,2.09,pipe hum,floor darkening
20:15,100,143,28.27,distant surf,light below surface
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
