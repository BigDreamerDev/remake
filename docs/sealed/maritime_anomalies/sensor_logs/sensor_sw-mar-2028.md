# Sensor Log SW-MAR-2028

location: Observation Deck 4
capture-date: 1983-02-26
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
20:00,66,4,2.54,none,door reflected
20:15,50,6,9.39,pipe hum,light below surface
20:30,70,4,3.93,static shaped like rain,foam under desk
20:45,53,7,15.84,static shaped like rain,light below surface
21:00,77,13,4.48,muffled choir,window shows sea
21:15,75,14,12.82,gull indoors,window shows sea
21:30,60,21,24.9,breathing drain,foam under desk
21:45,63,23,13.46,none,clear
22:00,67,32,6.65,pipe hum,light below surface
22:15,84,37,29.87,none,clear
22:30,63,45,2.22,static shaped like rain,wrong ceiling
22:45,91,46,36.4,muffled choir,floor darkening
23:00,80,55,18.8,bell once,floor darkening
23:15,78,56,16.46,distant surf,clear
23:30,98,59,8.77,none,window shows sea
23:45,100,61,4.76,pipe hum,light below surface
00:00,100,69,27.22,static shaped like rain,footprints arrive
00:15,100,77,22.75,muffled choir,foam under desk
00:30,75,81,28.38,bell once,floor darkening
00:45,100,79,13.39,pipe hum,clear
01:00,100,84,36.61,breathing drain,foam under desk
01:15,81,83,22.89,pipe hum,floor darkening
01:30,89,88,5.33,static shaped like rain,clear
01:45,84,92,6.63,gull indoors,clear
02:00,96,100,6.33,none,foam under desk
02:15,91,107,33.97,distant surf,window shows sea
02:30,85,109,29.67,gull indoors,footprints arrive
02:45,94,112,12.32,distant surf,door reflected
03:00,100,119,3.55,muffled choir,window shows sea
03:15,96,117,21.77,none,clear
03:30,100,115,33.54,none,door reflected
03:45,100,123,14.35,pipe hum,light below surface
04:00,95,128,17.16,breathing drain,door reflected
04:15,96,129,4.55,bell once,foam under desk
04:30,100,133,17.34,breathing drain,footprints arrive
04:45,95,141,33.06,gull indoors,wrong ceiling
05:00,100,139,16.06,none,window shows sea
05:15,100,145,31.43,none,door reflected
05:30,100,144,36.0,breathing drain,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
