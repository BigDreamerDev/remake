# Sensor Log SW-MAR-2058

location: South Intake Tunnel
capture-date: 1986-03-07
device: manual tide staff

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
02:00,75,0,0.99,breathing drain,clear
02:15,71,0,0.08,gull indoors,light below surface
02:30,52,9,15.54,none,foam under desk
02:45,57,16,31.92,gull indoors,floor darkening
03:00,66,22,36.54,none,floor darkening
03:15,62,26,10.08,bell once,door reflected
03:30,91,31,4.65,pipe hum,foam under desk
03:45,74,32,27.76,breathing drain,floor darkening
04:00,70,37,35.9,static shaped like rain,foam under desk
04:15,90,45,12.4,pipe hum,floor darkening
04:30,81,51,36.6,breathing drain,clear
04:45,70,52,31.13,gull indoors,clear
05:00,76,60,27.73,gull indoors,clear
05:15,76,65,5.54,pipe hum,wrong ceiling
05:30,81,69,12.74,distant surf,window shows sea
05:45,100,69,1.23,pipe hum,foam under desk
06:00,74,70,16.53,bell once,footprints arrive
06:15,75,77,5.49,muffled choir,floor darkening
06:30,100,78,18.41,pipe hum,wrong ceiling
06:45,100,80,14.34,breathing drain,window shows sea
07:00,75,78,36.35,distant surf,clear
07:15,100,79,28.12,distant surf,door reflected
07:30,92,88,10.95,pipe hum,footprints arrive
07:45,100,93,19.03,static shaped like rain,foam under desk
08:00,100,98,35.96,bell once,door reflected
08:15,100,96,28.24,breathing drain,clear
08:30,87,101,5.06,bell once,foam under desk
08:45,97,110,28.22,pipe hum,window shows sea
09:00,94,114,3.72,pipe hum,floor darkening
09:15,97,120,7.01,distant surf,door reflected
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
