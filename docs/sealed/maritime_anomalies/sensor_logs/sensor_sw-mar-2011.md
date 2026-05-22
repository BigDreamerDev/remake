# Sensor Log SW-MAR-2011

location: Mirrorpool Basin
capture-date: 2022-06-18
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
11:00,67,4,29.25,distant surf,clear
11:15,51,6,25.18,static shaped like rain,wrong ceiling
11:30,64,9,24.11,static shaped like rain,wrong ceiling
11:45,78,14,25.92,bell once,foam under desk
12:00,72,20,25.55,breathing drain,window shows sea
12:15,81,28,1.39,static shaped like rain,door reflected
12:30,80,33,21.81,distant surf,footprints arrive
12:45,94,42,24.07,static shaped like rain,foam under desk
13:00,95,48,2.01,distant surf,wrong ceiling
13:15,94,46,7.48,gull indoors,footprints arrive
13:30,83,51,6.39,muffled choir,light below surface
13:45,82,60,28.86,distant surf,footprints arrive
14:00,69,60,14.44,none,light below surface
14:15,88,69,31.64,distant surf,floor darkening
14:30,100,70,25.75,bell once,foam under desk
14:45,93,73,22.39,pipe hum,floor darkening
15:00,100,79,36.39,gull indoors,window shows sea
15:15,84,85,14.49,breathing drain,door reflected
15:30,82,83,35.88,bell once,door reflected
15:45,100,84,16.58,bell once,wrong ceiling
16:00,77,88,22.76,bell once,foam under desk
16:15,98,96,11.81,none,clear
16:30,87,96,25.63,none,light below surface
16:45,96,102,33.18,muffled choir,window shows sea
17:00,91,103,9.24,pipe hum,wrong ceiling
17:15,81,101,14.56,gull indoors,window shows sea
17:30,100,104,10.86,pipe hum,clear
17:45,88,113,31.41,distant surf,wrong ceiling
18:00,100,115,1.76,breathing drain,door reflected
18:15,100,120,19.78,pipe hum,door reflected
18:30,100,129,11.27,muffled choir,footprints arrive
18:45,100,128,7.8,muffled choir,door reflected
19:00,100,133,12.55,breathing drain,wrong ceiling
19:15,100,140,2.98,bell once,footprints arrive
19:30,100,146,29.85,bell once,footprints arrive
19:45,100,152,24.84,distant surf,door reflected
20:00,100,155,14.89,bell once,floor darkening
20:15,100,154,32.11,pipe hum,light below surface
20:30,100,163,21.88,distant surf,clear
20:45,100,170,0.49,bell once,clear
21:00,100,174,14.1,bell once,window shows sea
21:15,100,177,31.19,static shaped like rain,footprints arrive
21:30,100,181,2.23,breathing drain,foam under desk
21:45,100,184,7.84,bell once,clear
22:00,100,183,29.22,static shaped like rain,floor darkening
22:15,100,187,34.1,bell once,wrong ceiling
22:30,100,196,10.81,bell once,foam under desk
22:45,100,204,23.28,breathing drain,door reflected
23:00,100,202,6.73,distant surf,clear
23:15,100,208,7.38,bell once,foam under desk
23:30,100,216,2.95,pipe hum,floor darkening
23:45,100,215,24.07,distant surf,light below surface
00:00,100,222,17.64,gull indoors,clear
00:15,100,223,20.61,static shaped like rain,clear
00:30,100,221,31.9,none,foam under desk
00:45,100,226,9.45,distant surf,wrong ceiling
01:00,100,224,3.73,gull indoors,clear
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
