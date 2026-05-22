# Sensor Log SW-MAR-2014

location: Lower Bell Marina
capture-date: 2022-10-15
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
04:00,52,1,9.29,breathing drain,footprints arrive
04:15,65,5,23.11,bell once,clear
04:30,55,5,29.34,pipe hum,clear
04:45,86,10,12.5,muffled choir,footprints arrive
05:00,59,12,28.03,pipe hum,window shows sea
05:15,74,14,2.9,muffled choir,light below surface
05:30,57,12,31.03,distant surf,floor darkening
05:45,76,21,14.1,gull indoors,floor darkening
06:00,92,29,18.56,static shaped like rain,light below surface
06:15,81,29,6.3,bell once,light below surface
06:30,86,31,26.72,pipe hum,window shows sea
06:45,71,33,11.64,pipe hum,wrong ceiling
07:00,65,38,34.35,bell once,wrong ceiling
07:15,87,47,1.99,none,window shows sea
07:30,78,56,18.88,bell once,wrong ceiling
07:45,95,54,31.32,pipe hum,light below surface
08:00,88,61,2.72,gull indoors,floor darkening
08:15,82,66,28.44,none,foam under desk
08:30,100,73,24.82,breathing drain,wrong ceiling
08:45,76,77,23.1,distant surf,clear
09:00,96,86,3.65,breathing drain,wrong ceiling
09:15,100,87,25.23,none,footprints arrive
09:30,95,89,35.73,muffled choir,clear
09:45,100,96,10.45,breathing drain,window shows sea
10:00,92,100,18.63,none,window shows sea
10:15,90,101,22.6,gull indoors,floor darkening
10:30,87,104,18.65,pipe hum,floor darkening
10:45,95,108,25.52,bell once,clear
11:00,100,116,9.85,gull indoors,floor darkening
11:15,92,123,25.22,gull indoors,wrong ceiling
11:30,100,126,22.31,bell once,footprints arrive
11:45,100,124,10.57,pipe hum,window shows sea
12:00,100,123,31.93,muffled choir,wrong ceiling
12:15,94,123,26.43,gull indoors,wrong ceiling
12:30,100,127,25.11,none,light below surface
12:45,95,126,0.43,distant surf,light below surface
13:00,100,128,30.57,pipe hum,foam under desk
13:15,100,135,2.37,distant surf,clear
13:30,100,139,34.67,gull indoors,window shows sea
13:45,100,142,27.56,breathing drain,window shows sea
14:00,100,151,27.78,breathing drain,clear
14:15,100,159,6.99,distant surf,foam under desk
14:30,100,162,34.41,none,light below surface
14:45,100,166,28.02,static shaped like rain,clear
15:00,100,169,16.74,gull indoors,footprints arrive
15:15,100,169,5.62,static shaped like rain,wrong ceiling
15:30,100,175,10.57,distant surf,foam under desk
15:45,100,179,27.74,breathing drain,footprints arrive
16:00,100,184,18.82,muffled choir,foam under desk
16:15,100,183,2.53,static shaped like rain,foam under desk
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
