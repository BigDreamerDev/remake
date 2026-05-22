# Sensor Log SW-MAR-2042

location: Rain Room 11
capture-date: 1984-07-10
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
21:00,68,4,31.21,static shaped like rain,window shows sea
21:15,71,6,0.83,static shaped like rain,clear
21:30,65,11,16.31,bell once,light below surface
21:45,67,9,8.52,none,footprints arrive
22:00,71,15,18.06,distant surf,footprints arrive
22:15,60,24,24.4,static shaped like rain,wrong ceiling
22:30,62,24,0.85,static shaped like rain,light below surface
22:45,84,28,4.04,muffled choir,foam under desk
23:00,74,32,32.81,gull indoors,floor darkening
23:15,66,38,26.65,gull indoors,footprints arrive
23:30,64,36,5.95,bell once,window shows sea
23:45,69,40,3.18,bell once,window shows sea
00:00,81,48,28.77,pipe hum,clear
00:15,74,53,34.76,breathing drain,clear
00:30,68,58,23.41,static shaped like rain,light below surface
00:45,100,61,7.71,pipe hum,light below surface
01:00,100,70,22.91,distant surf,wrong ceiling
01:15,75,68,2.45,gull indoors,door reflected
01:30,96,76,22.16,gull indoors,window shows sea
01:45,95,77,23.42,bell once,footprints arrive
02:00,96,79,14.79,none,wrong ceiling
02:15,96,86,16.79,muffled choir,window shows sea
02:30,100,89,9.48,muffled choir,foam under desk
02:45,100,93,0.24,bell once,light below surface
03:00,81,98,29.87,none,floor darkening
03:15,100,99,10.03,none,footprints arrive
03:30,100,98,15.53,pipe hum,floor darkening
03:45,99,99,10.55,gull indoors,wrong ceiling
04:00,98,105,28.9,bell once,window shows sea
04:15,94,111,20.55,breathing drain,wrong ceiling
04:30,91,114,8.41,bell once,wrong ceiling
04:45,100,120,1.94,distant surf,light below surface
05:00,93,118,8.39,breathing drain,light below surface
05:15,100,116,33.62,breathing drain,floor darkening
05:30,87,117,10.32,breathing drain,door reflected
05:45,93,126,24.27,muffled choir,window shows sea
06:00,100,125,28.37,distant surf,window shows sea
06:15,100,124,29.39,muffled choir,foam under desk
06:30,100,133,35.39,distant surf,door reflected
06:45,100,138,15.74,gull indoors,window shows sea
07:00,100,144,24.12,pipe hum,foam under desk
07:15,100,144,20.72,distant surf,window shows sea
07:30,100,153,26.41,gull indoors,floor darkening
07:45,100,162,25.97,muffled choir,door reflected
08:00,100,165,21.54,pipe hum,footprints arrive
08:15,100,171,34.09,none,light below surface
08:30,100,169,23.44,pipe hum,door reflected
08:45,100,170,33.34,static shaped like rain,floor darkening
09:00,100,169,35.05,breathing drain,floor darkening
09:15,100,173,6.9,distant surf,door reflected
09:30,100,179,21.13,gull indoors,light below surface
09:45,100,178,29.54,none,clear
10:00,100,180,25.06,distant surf,footprints arrive
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
