# Sensor Log SW-MAR-2045

location: Grey Buoy Field
capture-date: 1984-11-13
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
00:00,75,0,0.97,gull indoors,footprints arrive
00:15,84,4,32.43,distant surf,light below surface
00:30,59,12,26.46,static shaped like rain,door reflected
00:45,79,18,2.52,distant surf,wrong ceiling
01:00,58,26,13.69,breathing drain,floor darkening
01:15,61,30,10.72,gull indoors,floor darkening
01:30,69,38,22.98,static shaped like rain,wrong ceiling
01:45,85,39,36.57,gull indoors,wrong ceiling
02:00,71,48,28.5,static shaped like rain,floor darkening
02:15,95,56,35.74,static shaped like rain,wrong ceiling
02:30,72,62,9.75,muffled choir,clear
02:45,72,60,34.44,pipe hum,light below surface
03:00,95,69,31.71,pipe hum,wrong ceiling
03:15,90,72,2.07,static shaped like rain,door reflected
03:30,100,77,4.38,bell once,floor darkening
03:45,100,75,5.49,pipe hum,foam under desk
04:00,89,84,10.42,bell once,foam under desk
04:15,79,93,30.5,breathing drain,clear
04:30,84,99,3.14,pipe hum,light below surface
04:45,89,108,30.5,distant surf,floor darkening
05:00,100,109,4.63,gull indoors,wrong ceiling
05:15,100,118,12.08,breathing drain,foam under desk
05:30,100,121,17.54,gull indoors,clear
05:45,100,124,36.17,distant surf,footprints arrive
06:00,97,125,26.71,pipe hum,clear
06:15,100,131,15.19,bell once,wrong ceiling
06:30,99,134,10.94,static shaped like rain,floor darkening
06:45,100,133,14.92,breathing drain,clear
07:00,100,140,17.96,static shaped like rain,light below surface
07:15,100,142,36.02,muffled choir,footprints arrive
07:30,100,143,23.44,none,clear
07:45,100,151,21.4,gull indoors,floor darkening
08:00,100,150,33.3,static shaped like rain,clear
08:15,100,156,30.47,muffled choir,wrong ceiling
08:30,100,162,9.81,static shaped like rain,light below surface
08:45,100,166,18.09,gull indoors,window shows sea
09:00,100,172,23.1,pipe hum,window shows sea
09:15,100,175,35.99,bell once,window shows sea
09:30,100,175,14.7,pipe hum,light below surface
09:45,100,183,14.83,bell once,window shows sea
10:00,100,187,28.06,pipe hum,light below surface
10:15,100,185,2.66,pipe hum,window shows sea
10:30,100,193,14.46,gull indoors,footprints arrive
10:45,100,192,3.26,gull indoors,wrong ceiling
11:00,100,194,0.9,static shaped like rain,clear
11:15,100,195,4.12,none,clear
11:30,100,202,13.14,gull indoors,wrong ceiling
11:45,100,202,1.66,none,wrong ceiling
12:00,100,206,30.93,bell once,door reflected
12:15,100,204,31.75,muffled choir,light below surface
12:30,100,205,26.07,muffled choir,light below surface
12:45,100,205,19.94,bell once,clear
13:00,100,209,17.87,pipe hum,window shows sea
13:15,100,209,10.72,distant surf,door reflected
13:30,100,213,29.49,static shaped like rain,light below surface
13:45,100,215,34.07,static shaped like rain,light below surface
14:00,100,223,23.63,bell once,door reflected
14:15,100,221,11.33,static shaped like rain,clear
14:30,100,229,33.28,static shaped like rain,door reflected
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
