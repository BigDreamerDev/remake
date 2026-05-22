# Sensor Log SW-MAR-2001

location: The Empty Aquarium
capture-date: 2021-06-08
device: manual tide staff

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
21:00,83,0,0.03,none,clear
21:15,56,0,0.17,gull indoors,door reflected
21:30,83,5,18.55,breathing drain,clear
21:45,76,3,19.23,bell once,foam under desk
22:00,69,10,30.07,bell once,foam under desk
22:15,62,13,4.74,gull indoors,window shows sea
22:30,86,12,19.5,gull indoors,light below surface
22:45,83,11,9.13,muffled choir,floor darkening
23:00,69,9,4.47,gull indoors,floor darkening
23:15,89,18,24.78,muffled choir,wrong ceiling
23:30,83,21,31.12,gull indoors,footprints arrive
23:45,86,27,35.36,pipe hum,light below surface
00:00,86,26,33.07,bell once,window shows sea
00:15,62,26,5.07,bell once,clear
00:30,86,33,21.85,pipe hum,floor darkening
00:45,88,41,21.74,gull indoors,wrong ceiling
01:00,70,46,26.54,bell once,wrong ceiling
01:15,83,53,12.75,bell once,wrong ceiling
01:30,97,55,23.45,distant surf,clear
01:45,75,58,27.79,none,window shows sea
02:00,72,60,10.01,distant surf,light below surface
02:15,82,60,28.27,muffled choir,wrong ceiling
02:30,95,60,29.82,static shaped like rain,door reflected
02:45,100,64,22.84,distant surf,wrong ceiling
03:00,80,70,19.99,none,floor darkening
03:15,97,70,25.35,static shaped like rain,floor darkening
03:30,100,72,29.26,muffled choir,wrong ceiling
03:45,100,77,2.57,breathing drain,clear
04:00,91,75,29.55,breathing drain,clear
04:15,91,79,0.24,bell once,floor darkening
04:30,96,77,21.97,gull indoors,window shows sea
04:45,99,75,12.0,pipe hum,clear
05:00,82,74,12.47,muffled choir,floor darkening
05:15,87,80,18.54,none,window shows sea
05:30,94,81,15.07,gull indoors,window shows sea
05:45,89,90,26.85,gull indoors,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
