# Sensor Log SW-MAR-2004

location: Oyster Stair
capture-date: 2021-10-12
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
03:00,76,1,32.94,bell once,footprints arrive
03:15,69,10,22.75,pipe hum,footprints arrive
03:30,55,11,28.09,static shaped like rain,light below surface
03:45,67,15,22.04,gull indoors,footprints arrive
04:00,61,19,0.96,gull indoors,light below surface
04:15,66,21,12.56,none,footprints arrive
04:30,67,21,23.74,pipe hum,light below surface
04:45,82,21,24.63,gull indoors,door reflected
05:00,77,27,36.07,pipe hum,foam under desk
05:15,70,36,7.29,none,wrong ceiling
05:30,86,42,11.02,distant surf,footprints arrive
05:45,67,50,21.37,static shaped like rain,floor darkening
06:00,75,49,5.58,muffled choir,footprints arrive
06:15,94,57,31.24,bell once,clear
06:30,71,63,10.39,none,door reflected
06:45,100,61,23.94,muffled choir,wrong ceiling
07:00,96,70,8.34,bell once,door reflected
07:15,75,71,17.48,muffled choir,light below surface
07:30,87,71,17.42,none,window shows sea
07:45,88,74,10.88,bell once,clear
08:00,85,73,12.41,muffled choir,foam under desk
08:15,100,75,19.72,distant surf,door reflected
08:30,100,77,36.65,bell once,footprints arrive
08:45,75,78,18.82,bell once,clear
09:00,95,80,12.81,gull indoors,foam under desk
09:15,84,89,0.46,none,window shows sea
09:30,85,93,28.8,bell once,footprints arrive
09:45,100,94,34.73,muffled choir,light below surface
10:00,88,96,22.72,none,foam under desk
10:15,87,98,32.83,distant surf,door reflected
10:30,100,101,11.78,pipe hum,light below surface
10:45,96,108,29.3,static shaped like rain,light below surface
11:00,100,109,14.87,bell once,floor darkening
11:15,85,111,31.21,breathing drain,clear
11:30,98,109,13.46,distant surf,window shows sea
11:45,100,118,14.53,muffled choir,clear
12:00,97,116,3.35,static shaped like rain,wrong ceiling
12:15,100,116,25.77,none,window shows sea
12:30,100,116,15.07,muffled choir,light below surface
12:45,100,123,34.26,muffled choir,clear
13:00,100,122,12.03,static shaped like rain,footprints arrive
13:15,100,122,25.19,breathing drain,window shows sea
13:30,100,128,16.56,muffled choir,wrong ceiling
13:45,100,134,14.91,gull indoors,foam under desk
14:00,100,134,34.18,muffled choir,window shows sea
14:15,100,138,28.46,breathing drain,clear
14:30,100,143,2.41,breathing drain,footprints arrive
14:45,100,148,25.33,none,door reflected
15:00,100,148,11.43,breathing drain,foam under desk
15:15,100,154,20.67,none,light below surface
15:30,100,158,23.6,none,door reflected
15:45,100,162,21.13,gull indoors,window shows sea
16:00,100,164,27.11,none,clear
16:15,100,164,1.03,breathing drain,footprints arrive
16:30,100,165,17.77,bell once,wrong ceiling
16:45,100,167,27.84,pipe hum,light below surface
17:00,100,170,23.82,breathing drain,clear
17:15,100,171,11.8,gull indoors,wrong ceiling
17:30,100,178,9.06,pipe hum,light below surface
17:45,100,178,22.02,static shaped like rain,floor darkening
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
