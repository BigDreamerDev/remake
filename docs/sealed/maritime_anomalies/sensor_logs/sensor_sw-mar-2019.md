# Sensor Log SW-MAR-2019

location: Canteen Tidewell
capture-date: 2023-04-05
device: pressure bell

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
09:00,71,0,0.47,distant surf,footprints arrive
09:15,57,7,19.83,distant surf,wrong ceiling
09:30,59,8,18.39,bell once,light below surface
09:45,82,9,33.58,none,foam under desk
10:00,80,17,35.63,none,wrong ceiling
10:15,76,23,22.1,gull indoors,footprints arrive
10:30,89,22,16.01,static shaped like rain,wrong ceiling
10:45,72,28,1.47,gull indoors,foam under desk
11:00,72,37,3.29,bell once,window shows sea
11:15,76,43,35.36,breathing drain,door reflected
11:30,92,48,3.28,gull indoors,clear
11:45,93,53,34.7,breathing drain,floor darkening
12:00,75,59,3.74,breathing drain,window shows sea
12:15,100,67,11.55,distant surf,wrong ceiling
12:30,100,75,34.03,none,wrong ceiling
12:45,100,79,16.04,bell once,footprints arrive
13:00,78,85,0.25,static shaped like rain,wrong ceiling
13:15,81,92,0.28,breathing drain,footprints arrive
13:30,85,94,29.89,muffled choir,floor darkening
13:45,85,101,22.34,bell once,clear
14:00,88,105,14.43,gull indoors,footprints arrive
14:15,92,108,27.04,pipe hum,foam under desk
14:30,100,115,20.5,static shaped like rain,door reflected
14:45,100,123,26.45,bell once,door reflected
15:00,100,124,32.5,pipe hum,footprints arrive
15:15,100,129,32.65,gull indoors,wrong ceiling
15:30,100,127,21.02,distant surf,clear
15:45,100,133,17.44,breathing drain,clear
16:00,100,142,21.29,breathing drain,footprints arrive
16:15,100,145,8.75,pipe hum,door reflected
16:30,100,148,9.36,distant surf,window shows sea
16:45,100,153,28.16,distant surf,wrong ceiling
17:00,100,151,15.39,muffled choir,footprints arrive
17:15,100,153,19.26,none,foam under desk
17:30,100,158,34.67,pipe hum,foam under desk
17:45,100,166,36.51,muffled choir,clear
18:00,100,172,4.21,breathing drain,window shows sea
18:15,100,174,13.59,distant surf,foam under desk
18:30,100,181,31.96,breathing drain,light below surface
18:45,100,180,2.35,muffled choir,light below surface
19:00,100,189,19.92,gull indoors,foam under desk
19:15,100,192,4.35,static shaped like rain,clear
19:30,100,196,16.22,distant surf,clear
19:45,100,197,1.57,breathing drain,clear
20:00,100,203,35.54,breathing drain,footprints arrive
20:15,100,210,26.32,muffled choir,wrong ceiling
20:30,100,211,0.76,muffled choir,light below surface
20:45,100,215,21.12,muffled choir,foam under desk
21:00,100,224,33.75,static shaped like rain,foam under desk
21:15,100,230,17.29,static shaped like rain,window shows sea
21:30,100,235,34.5,static shaped like rain,light below surface
21:45,100,240,34.08,pipe hum,foam under desk
22:00,100,243,20.72,none,door reflected
22:15,100,251,11.66,none,foam under desk
22:30,100,258,29.09,bell once,footprints arrive
22:45,100,266,28.06,bell once,clear
23:00,100,272,28.41,muffled choir,window shows sea
23:15,100,277,16.52,muffled choir,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
