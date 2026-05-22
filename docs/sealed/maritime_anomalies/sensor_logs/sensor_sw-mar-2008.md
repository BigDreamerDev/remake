# Sensor Log SW-MAR-2008

location: Ward C Washroom
capture-date: 2022-03-14
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
03:00,56,8,5.49,static shaped like rain,door reflected
03:15,74,13,24.77,none,wrong ceiling
03:30,72,21,13.93,gull indoors,window shows sea
03:45,65,21,13.54,gull indoors,clear
04:00,66,30,11.44,bell once,window shows sea
04:15,93,39,33.93,muffled choir,door reflected
04:30,84,39,4.16,static shaped like rain,door reflected
04:45,97,47,12.73,none,light below surface
05:00,95,53,21.06,static shaped like rain,door reflected
05:15,97,54,22.12,pipe hum,wrong ceiling
05:30,72,62,29.75,static shaped like rain,wrong ceiling
05:45,100,60,12.41,none,window shows sea
06:00,78,63,1.17,distant surf,clear
06:15,90,64,6.44,pipe hum,wrong ceiling
06:30,90,65,8.89,pipe hum,door reflected
06:45,98,63,12.95,gull indoors,footprints arrive
07:00,82,67,22.38,distant surf,foam under desk
07:15,100,75,24.48,pipe hum,floor darkening
07:30,100,75,30.49,none,foam under desk
07:45,100,78,8.44,breathing drain,clear
08:00,89,85,18.47,pipe hum,foam under desk
08:15,95,87,13.6,distant surf,footprints arrive
08:30,78,90,33.45,pipe hum,window shows sea
08:45,100,89,32.26,distant surf,light below surface
09:00,100,95,29.99,muffled choir,door reflected
09:15,95,102,17.43,muffled choir,foam under desk
09:30,100,103,5.49,none,door reflected
09:45,100,111,36.74,muffled choir,floor darkening
10:00,89,119,28.84,breathing drain,wrong ceiling
10:15,100,127,1.0,static shaped like rain,foam under desk
10:30,100,131,35.29,pipe hum,clear
10:45,96,134,33.47,breathing drain,light below surface
11:00,100,136,4.04,distant surf,footprints arrive
11:15,100,135,14.76,breathing drain,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
