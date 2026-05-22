# Sensor Log SW-MAR-2053

location: Ashen Ferry Terminal
capture-date: 1985-09-06
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
00:00,66,3,10.02,none,clear
00:15,53,7,19.28,breathing drain,window shows sea
00:30,68,8,29.64,distant surf,light below surface
00:45,80,6,28.82,pipe hum,window shows sea
01:00,67,10,10.48,bell once,window shows sea
01:15,61,16,30.72,pipe hum,wrong ceiling
01:30,62,16,21.03,bell once,clear
01:45,66,18,29.48,distant surf,door reflected
02:00,72,16,31.62,bell once,clear
02:15,61,14,30.43,bell once,door reflected
02:30,55,19,18.15,breathing drain,door reflected
02:45,57,27,27.23,breathing drain,light below surface
03:00,63,33,35.04,pipe hum,light below surface
03:15,60,32,15.79,pipe hum,floor darkening
03:30,70,39,31.6,muffled choir,floor darkening
03:45,74,48,24.89,static shaped like rain,wrong ceiling
04:00,63,46,7.96,static shaped like rain,window shows sea
04:15,82,46,16.13,gull indoors,wrong ceiling
04:30,75,45,25.68,bell once,wrong ceiling
04:45,85,46,30.38,gull indoors,light below surface
05:00,71,54,27.01,bell once,foam under desk
05:15,79,63,13.72,breathing drain,window shows sea
05:30,100,65,19.35,none,footprints arrive
05:45,100,71,0.21,none,window shows sea
06:00,100,72,12.94,static shaped like rain,light below surface
06:15,95,79,2.05,pipe hum,door reflected
06:30,89,81,35.49,pipe hum,window shows sea
06:45,100,84,9.78,gull indoors,clear
07:00,85,84,7.09,breathing drain,footprints arrive
07:15,100,85,20.26,none,footprints arrive
07:30,86,91,12.16,distant surf,window shows sea
07:45,100,95,31.3,gull indoors,wrong ceiling
08:00,81,94,8.75,gull indoors,door reflected
08:15,81,92,34.99,static shaped like rain,wrong ceiling
08:30,97,98,9.41,muffled choir,clear
08:45,100,101,7.73,none,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
