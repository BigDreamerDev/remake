# Sensor Log SW-MAR-2005

location: The Third Jetty
capture-date: 2021-11-06
device: floorline acoustic monitor

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
20:00,66,5,0.2,pipe hum,foam under desk
20:15,66,9,32.36,pipe hum,clear
20:30,58,16,27.23,distant surf,door reflected
20:45,63,23,3.81,distant surf,light below surface
21:00,67,30,9.13,none,floor darkening
21:15,70,35,15.12,bell once,floor darkening
21:30,88,33,34.32,muffled choir,wrong ceiling
21:45,88,41,9.09,bell once,floor darkening
22:00,96,43,36.58,distant surf,footprints arrive
22:15,95,51,31.04,breathing drain,foam under desk
22:30,99,55,15.85,gull indoors,window shows sea
22:45,93,58,27.14,bell once,wrong ceiling
23:00,96,58,3.11,distant surf,floor darkening
23:15,100,65,2.58,pipe hum,window shows sea
23:30,90,67,32.35,gull indoors,footprints arrive
23:45,93,74,26.04,bell once,door reflected
00:00,83,80,9.77,muffled choir,floor darkening
00:15,100,81,7.9,breathing drain,window shows sea
00:30,93,82,34.27,none,window shows sea
00:45,86,91,32.07,muffled choir,foam under desk
01:00,82,98,29.83,pipe hum,window shows sea
01:15,100,104,32.11,gull indoors,foam under desk
01:30,87,105,30.28,static shaped like rain,footprints arrive
01:45,90,106,33.99,breathing drain,clear
02:00,100,113,34.47,distant surf,door reflected
02:15,100,117,28.62,distant surf,foam under desk
02:30,95,123,23.69,static shaped like rain,floor darkening
02:45,100,124,12.39,distant surf,clear
03:00,100,127,12.48,muffled choir,footprints arrive
03:15,95,125,34.75,breathing drain,floor darkening
03:30,91,126,35.98,gull indoors,window shows sea
03:45,97,131,16.45,static shaped like rain,clear
04:00,98,131,3.99,bell once,floor darkening
04:15,99,139,11.75,none,light below surface
04:30,100,148,36.34,pipe hum,door reflected
04:45,100,148,5.8,breathing drain,floor darkening
05:00,100,149,14.3,gull indoors,light below surface
05:15,100,147,13.51,breathing drain,footprints arrive
05:30,100,152,11.08,static shaped like rain,window shows sea
05:45,100,155,0.67,gull indoors,foam under desk
06:00,100,159,15.91,bell once,clear
06:15,100,163,14.14,bell once,window shows sea
06:30,100,171,5.07,muffled choir,window shows sea
06:45,100,178,19.46,none,floor darkening
07:00,100,177,16.42,breathing drain,light below surface
07:15,100,178,34.18,breathing drain,window shows sea
07:30,100,186,7.23,none,footprints arrive
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
