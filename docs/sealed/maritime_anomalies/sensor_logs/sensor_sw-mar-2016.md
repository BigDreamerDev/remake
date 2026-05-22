# Sensor Log SW-MAR-2016

location: Lower Bell Marina
capture-date: 2022-12-14
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
01:00,58,0,0.49,none,light below surface
01:15,77,4,25.85,breathing drain,light below surface
01:30,80,12,35.34,none,light below surface
01:45,73,14,25.78,distant surf,floor darkening
02:00,73,19,31.55,bell once,door reflected
02:15,83,18,30.13,muffled choir,footprints arrive
02:30,66,21,28.32,bell once,light below surface
02:45,63,27,20.64,static shaped like rain,window shows sea
03:00,58,29,14.94,distant surf,foam under desk
03:15,70,38,36.36,gull indoors,light below surface
03:30,66,41,1.28,muffled choir,footprints arrive
03:45,70,43,5.45,bell once,window shows sea
04:00,79,48,36.03,gull indoors,window shows sea
04:15,80,57,9.64,none,clear
04:30,100,60,23.66,none,wrong ceiling
04:45,77,64,0.3,distant surf,wrong ceiling
05:00,100,71,10.87,muffled choir,footprints arrive
05:15,72,73,34.64,none,window shows sea
05:30,93,79,13.28,distant surf,window shows sea
05:45,100,80,20.43,muffled choir,footprints arrive
06:00,100,85,28.52,static shaped like rain,floor darkening
06:15,93,88,33.71,distant surf,door reflected
06:30,93,97,12.25,distant surf,foam under desk
06:45,81,96,22.1,pipe hum,footprints arrive
07:00,100,103,5.98,breathing drain,footprints arrive
07:15,100,104,1.56,static shaped like rain,floor darkening
07:30,100,102,6.67,pipe hum,wrong ceiling
07:45,94,102,26.0,gull indoors,floor darkening
08:00,100,107,2.27,breathing drain,wrong ceiling
08:15,95,114,3.1,gull indoors,foam under desk
08:30,100,117,14.45,pipe hum,floor darkening
08:45,100,118,14.97,gull indoors,clear
09:00,100,117,5.72,pipe hum,footprints arrive
09:15,100,115,6.74,gull indoors,light below surface
09:30,90,121,22.41,bell once,footprints arrive
09:45,100,123,35.15,bell once,light below surface
10:00,100,123,5.3,muffled choir,door reflected
10:15,100,131,27.89,distant surf,wrong ceiling
10:30,100,133,8.45,bell once,wrong ceiling
10:45,100,136,4.08,muffled choir,floor darkening
11:00,100,142,10.09,muffled choir,footprints arrive
11:15,100,140,24.48,muffled choir,foam under desk
11:30,100,148,8.97,distant surf,floor darkening
11:45,100,154,35.61,gull indoors,light below surface
12:00,100,159,28.65,bell once,door reflected
12:15,100,165,29.3,bell once,door reflected
12:30,100,171,4.12,muffled choir,window shows sea
12:45,100,176,33.2,none,door reflected
13:00,100,179,25.1,bell once,floor darkening
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
