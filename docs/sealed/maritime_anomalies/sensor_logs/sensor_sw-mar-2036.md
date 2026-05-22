# Sensor Log SW-MAR-2036

location: Canteen Tidewell
capture-date: 1983-12-16
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
16:00,63,7,32.38,none,footprints arrive
16:15,76,15,25.04,bell once,light below surface
16:30,66,15,23.26,breathing drain,window shows sea
16:45,64,18,31.14,pipe hum,clear
17:00,72,26,12.12,breathing drain,floor darkening
17:15,73,32,16.12,none,foam under desk
17:30,87,30,35.0,gull indoors,floor darkening
17:45,62,31,4.59,none,footprints arrive
18:00,88,34,5.15,none,footprints arrive
18:15,83,32,25.16,breathing drain,light below surface
18:30,72,35,11.83,bell once,door reflected
18:45,70,35,18.89,bell once,foam under desk
19:00,88,39,23.38,breathing drain,floor darkening
19:15,91,48,29.89,breathing drain,footprints arrive
19:30,71,53,26.52,gull indoors,clear
19:45,93,57,17.36,distant surf,wrong ceiling
20:00,74,60,24.71,none,foam under desk
20:15,85,69,30.03,pipe hum,window shows sea
20:30,74,69,14.96,static shaped like rain,footprints arrive
20:45,96,71,36.26,bell once,floor darkening
21:00,93,79,30.34,distant surf,footprints arrive
21:15,93,85,0.37,bell once,clear
21:30,87,92,35.58,gull indoors,wrong ceiling
21:45,87,92,15.51,gull indoors,door reflected
22:00,95,97,6.36,muffled choir,foam under desk
22:15,93,103,33.73,pipe hum,wrong ceiling
22:30,100,103,12.16,pipe hum,door reflected
22:45,100,110,11.46,bell once,footprints arrive
23:00,100,117,35.23,none,door reflected
23:15,94,121,35.65,breathing drain,door reflected
23:30,93,122,19.57,breathing drain,door reflected
23:45,100,121,22.3,muffled choir,clear
00:00,90,122,18.76,pipe hum,clear
00:15,100,125,7.35,none,light below surface
00:30,100,125,22.84,pipe hum,wrong ceiling
00:45,100,123,18.31,none,footprints arrive
01:00,100,130,16.93,muffled choir,clear
01:15,100,130,26.99,bell once,light below surface
01:30,100,138,14.18,pipe hum,wrong ceiling
01:45,100,139,30.84,distant surf,wrong ceiling
02:00,100,143,35.09,distant surf,window shows sea
02:15,100,151,5.08,distant surf,foam under desk
02:30,100,151,11.7,breathing drain,floor darkening
02:45,100,149,6.24,static shaped like rain,window shows sea
03:00,100,147,2.92,none,clear
03:15,100,150,14.98,static shaped like rain,light below surface
03:30,100,155,16.64,pipe hum,wrong ceiling
03:45,100,158,6.03,gull indoors,foam under desk
04:00,100,159,8.92,distant surf,clear
04:15,100,157,26.78,static shaped like rain,wrong ceiling
04:30,100,162,2.11,pipe hum,footprints arrive
04:45,100,169,16.42,pipe hum,window shows sea
05:00,100,171,25.79,pipe hum,wrong ceiling
05:15,100,180,31.95,muffled choir,floor darkening
05:30,100,188,7.42,none,clear
05:45,100,190,28.07,gull indoors,clear
06:00,100,192,6.9,bell once,footprints arrive
06:15,100,199,22.81,gull indoors,light below surface
06:30,100,197,16.84,gull indoors,door reflected
06:45,100,197,10.72,none,door reflected
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
