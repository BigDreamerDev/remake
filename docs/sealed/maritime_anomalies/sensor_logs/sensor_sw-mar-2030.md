# Sensor Log SW-MAR-2030

location: The Dry Dock With Water In It
capture-date: 1983-05-01
device: manual tide staff

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
00:00,75,0,0.43,gull indoors,wrong ceiling
00:15,75,6,25.76,pipe hum,floor darkening
00:30,87,12,21.92,muffled choir,foam under desk
00:45,66,12,20.93,none,window shows sea
01:00,60,15,30.42,none,foam under desk
01:15,85,17,5.68,distant surf,light below surface
01:30,59,16,6.93,none,floor darkening
01:45,72,19,12.7,distant surf,wrong ceiling
02:00,86,25,33.63,pipe hum,light below surface
02:15,74,31,11.48,muffled choir,footprints arrive
02:30,92,31,0.69,none,door reflected
02:45,86,33,15.28,muffled choir,clear
03:00,76,41,24.5,distant surf,door reflected
03:15,65,44,36.47,bell once,window shows sea
03:30,94,49,15.36,muffled choir,light below surface
03:45,74,53,7.25,pipe hum,wrong ceiling
04:00,75,58,10.6,muffled choir,clear
04:15,76,66,18.87,pipe hum,door reflected
04:30,76,64,30.99,static shaped like rain,clear
04:45,100,64,10.71,none,floor darkening
05:00,72,73,4.54,distant surf,door reflected
05:15,95,81,8.71,pipe hum,foam under desk
05:30,95,80,0.47,breathing drain,light below surface
05:45,91,81,4.79,distant surf,floor darkening
06:00,86,87,14.4,static shaped like rain,floor darkening
06:15,100,90,25.7,bell once,floor darkening
06:30,100,90,8.88,bell once,door reflected
06:45,92,88,9.14,muffled choir,wrong ceiling
07:00,100,94,17.86,gull indoors,door reflected
07:15,81,101,10.32,breathing drain,door reflected
07:30,100,101,2.66,muffled choir,window shows sea
07:45,100,105,31.28,gull indoors,wrong ceiling
08:00,90,104,0.68,pipe hum,floor darkening
08:15,100,109,27.86,none,clear
08:30,97,118,21.09,muffled choir,light below surface
08:45,87,116,10.31,static shaped like rain,wrong ceiling
09:00,92,114,29.91,gull indoors,foam under desk
09:15,100,114,7.96,bell once,footprints arrive
09:30,100,121,26.23,pipe hum,light below surface
09:45,100,128,27.76,bell once,floor darkening
10:00,100,127,10.95,breathing drain,door reflected
10:15,100,126,15.05,muffled choir,footprints arrive
10:30,100,126,24.96,bell once,footprints arrive
10:45,90,126,21.39,bell once,light below surface
11:00,99,124,8.23,static shaped like rain,door reflected
11:15,100,129,27.28,pipe hum,clear
11:30,97,134,17.89,static shaped like rain,footprints arrive
11:45,100,143,28.91,bell once,clear
12:00,100,146,28.26,distant surf,footprints arrive
12:15,100,149,34.85,static shaped like rain,floor darkening
12:30,100,156,25.4,pipe hum,clear
12:45,100,159,18.82,breathing drain,foam under desk
13:00,100,161,15.67,distant surf,door reflected
13:15,100,160,12.2,muffled choir,foam under desk
13:30,100,168,24.53,bell once,wrong ceiling
13:45,100,171,3.33,distant surf,light below surface
14:00,100,176,7.41,pipe hum,light below surface
14:15,100,183,32.23,gull indoors,light below surface
14:30,100,188,25.58,pipe hum,window shows sea
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
