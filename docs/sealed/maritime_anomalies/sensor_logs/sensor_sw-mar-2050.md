# Sensor Log SW-MAR-2050

location: Lighthouse 7
capture-date: 1985-05-09
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
12:00,61,1,10.47,muffled choir,floor darkening
12:15,81,10,21.3,static shaped like rain,clear
12:30,59,13,28.82,gull indoors,clear
12:45,75,16,23.81,none,wrong ceiling
13:00,77,16,9.44,distant surf,door reflected
13:15,64,21,9.94,static shaped like rain,foam under desk
13:30,91,27,3.76,static shaped like rain,window shows sea
13:45,86,35,19.26,bell once,clear
14:00,73,37,6.88,static shaped like rain,window shows sea
14:15,94,37,35.33,none,clear
14:30,76,37,27.78,bell once,floor darkening
14:45,64,42,20.88,none,door reflected
15:00,80,51,26.69,distant surf,clear
15:15,78,50,30.23,breathing drain,foam under desk
15:30,93,56,32.58,pipe hum,floor darkening
15:45,77,60,23.61,static shaped like rain,floor darkening
16:00,97,59,9.84,breathing drain,light below surface
16:15,86,67,33.91,gull indoors,wrong ceiling
16:30,89,69,7.51,none,clear
16:45,73,77,35.37,none,wrong ceiling
17:00,89,78,19.13,bell once,foam under desk
17:15,99,76,36.05,muffled choir,footprints arrive
17:30,87,79,14.23,static shaped like rain,clear
17:45,79,88,20.43,static shaped like rain,foam under desk
18:00,100,89,7.82,gull indoors,footprints arrive
18:15,100,90,16.52,distant surf,window shows sea
18:30,100,95,1.32,breathing drain,light below surface
18:45,94,95,27.45,muffled choir,door reflected
19:00,92,94,36.65,none,clear
19:15,100,97,27.61,static shaped like rain,window shows sea
19:30,100,106,7.43,static shaped like rain,window shows sea
19:45,98,110,24.43,bell once,door reflected
20:00,92,119,3.89,none,wrong ceiling
20:15,100,124,2.76,muffled choir,footprints arrive
20:30,90,123,1.74,muffled choir,window shows sea
20:45,100,129,32.7,pipe hum,window shows sea
21:00,100,129,20.42,pipe hum,footprints arrive
21:15,100,129,15.25,none,wrong ceiling
21:30,100,134,12.47,distant surf,clear
21:45,100,133,16.19,static shaped like rain,foam under desk
22:00,100,136,11.82,muffled choir,floor darkening
22:15,100,139,29.09,gull indoors,floor darkening
22:30,100,142,27.99,muffled choir,floor darkening
22:45,100,142,34.77,static shaped like rain,wrong ceiling
23:00,100,147,7.51,bell once,floor darkening
23:15,100,154,12.26,bell once,footprints arrive
23:30,100,157,29.55,none,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
