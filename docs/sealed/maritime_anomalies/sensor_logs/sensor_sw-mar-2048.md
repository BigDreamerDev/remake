# Sensor Log SW-MAR-2048

location: South Intake Tunnel
capture-date: 1985-02-16
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
07:00,69,2,15.35,none,clear
07:15,74,6,8.2,bell once,door reflected
07:30,78,7,5.2,pipe hum,clear
07:45,49,5,30.7,distant surf,floor darkening
08:00,58,4,24.72,pipe hum,light below surface
08:15,60,7,15.42,pipe hum,window shows sea
08:30,73,5,12.8,none,wrong ceiling
08:45,76,8,35.75,gull indoors,foam under desk
09:00,81,13,5.87,static shaped like rain,footprints arrive
09:15,60,13,16.63,gull indoors,light below surface
09:30,86,20,3.53,bell once,clear
09:45,86,25,21.34,breathing drain,light below surface
10:00,60,25,6.13,none,foam under desk
10:15,68,30,1.03,none,wrong ceiling
10:30,78,31,28.95,pipe hum,clear
10:45,61,30,14.06,bell once,foam under desk
11:00,75,36,23.64,pipe hum,floor darkening
11:15,76,41,5.12,none,window shows sea
11:30,74,42,12.28,static shaped like rain,wrong ceiling
11:45,93,51,10.67,muffled choir,door reflected
12:00,90,58,2.85,pipe hum,foam under desk
12:15,94,65,0.72,pipe hum,clear
12:30,86,64,2.19,static shaped like rain,floor darkening
12:45,78,70,15.85,muffled choir,floor darkening
13:00,100,79,3.7,bell once,floor darkening
13:15,86,83,8.63,static shaped like rain,light below surface
13:30,80,90,33.06,pipe hum,wrong ceiling
13:45,100,94,29.46,bell once,footprints arrive
14:00,90,102,0.78,none,clear
14:15,96,107,0.93,breathing drain,light below surface
14:30,100,115,35.38,none,footprints arrive
14:45,100,114,4.32,breathing drain,floor darkening
15:00,100,123,15.12,bell once,floor darkening
15:15,100,126,22.52,pipe hum,floor darkening
15:30,100,128,1.06,none,clear
15:45,100,133,14.29,none,floor darkening
16:00,100,132,2.88,muffled choir,foam under desk
16:15,100,132,21.49,none,window shows sea
16:30,100,135,4.1,none,light below surface
16:45,100,143,15.63,distant surf,window shows sea
17:00,100,144,33.49,muffled choir,window shows sea
17:15,100,145,34.51,gull indoors,footprints arrive
17:30,100,152,6.88,none,floor darkening
17:45,100,159,8.81,muffled choir,floor darkening
18:00,100,168,4.5,breathing drain,window shows sea
18:15,100,166,33.33,bell once,light below surface
18:30,100,169,20.91,muffled choir,foam under desk
18:45,100,173,31.46,static shaped like rain,clear
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
