# Sensor Log SW-MAR-2039

location: Lower Bell Marina
capture-date: 1984-03-21
device: manual tide staff

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
09:00,73,4,3.15,muffled choir,clear
09:15,68,2,1.73,muffled choir,footprints arrive
09:30,61,6,18.81,gull indoors,footprints arrive
09:45,61,15,3.36,none,wrong ceiling
10:00,74,20,2.7,static shaped like rain,window shows sea
10:15,61,26,21.28,bell once,floor darkening
10:30,66,27,9.35,pipe hum,clear
10:45,89,35,13.63,muffled choir,window shows sea
11:00,89,40,3.85,distant surf,window shows sea
11:15,87,42,35.68,none,foam under desk
11:30,67,42,7.73,none,footprints arrive
11:45,98,51,20.39,distant surf,wrong ceiling
12:00,93,51,8.21,gull indoors,clear
12:15,96,57,4.73,breathing drain,clear
12:30,80,65,19.96,bell once,window shows sea
12:45,73,65,19.09,gull indoors,footprints arrive
13:00,69,63,4.54,distant surf,wrong ceiling
13:15,98,66,26.01,static shaped like rain,door reflected
13:30,74,75,7.9,gull indoors,door reflected
13:45,100,82,22.77,bell once,door reflected
14:00,81,85,6.85,none,floor darkening
14:15,100,93,11.02,pipe hum,wrong ceiling
14:30,96,98,17.95,gull indoors,clear
14:45,100,97,29.47,bell once,foam under desk
15:00,97,95,34.03,static shaped like rain,floor darkening
15:15,100,93,31.16,distant surf,floor darkening
15:30,100,102,2.79,gull indoors,wrong ceiling
15:45,100,103,35.61,breathing drain,wrong ceiling
16:00,100,112,15.84,distant surf,door reflected
16:15,100,115,12.93,pipe hum,wrong ceiling
16:30,98,118,30.18,bell once,clear
16:45,92,126,30.92,muffled choir,floor darkening
17:00,100,127,34.63,gull indoors,wrong ceiling
17:15,100,133,24.34,distant surf,light below surface
17:30,100,139,21.05,gull indoors,footprints arrive
17:45,100,142,13.77,static shaped like rain,clear
18:00,99,151,27.27,muffled choir,door reflected
18:15,100,151,24.56,breathing drain,footprints arrive
18:30,100,160,31.23,muffled choir,door reflected
18:45,100,168,5.31,static shaped like rain,floor darkening
19:00,100,170,8.89,bell once,floor darkening
19:15,100,173,17.41,distant surf,light below surface
19:30,100,172,9.18,breathing drain,wrong ceiling
19:45,100,172,34.65,gull indoors,clear
20:00,100,170,8.09,static shaped like rain,foam under desk
20:15,100,168,33.06,none,floor darkening
20:30,100,172,16.71,none,window shows sea
20:45,100,180,13.55,bell once,door reflected
21:00,100,189,29.03,static shaped like rain,footprints arrive
21:15,100,194,18.86,breathing drain,floor darkening
21:30,100,192,34.26,breathing drain,clear
21:45,100,198,12.42,bell once,clear
22:00,100,199,31.29,none,door reflected
22:15,100,203,36.51,distant surf,wrong ceiling
22:30,100,206,17.92,pipe hum,wrong ceiling
22:45,100,214,30.66,muffled choir,window shows sea
23:00,100,217,0.79,muffled choir,window shows sea
23:15,100,222,8.39,muffled choir,window shows sea
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
