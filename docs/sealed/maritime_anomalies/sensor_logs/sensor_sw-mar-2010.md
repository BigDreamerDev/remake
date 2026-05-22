# Sensor Log SW-MAR-2010

location: Blue Door Quay
capture-date: 2022-05-14
device: corridor hygrometer

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
17:00,79,0,0.71,breathing drain,clear
17:15,62,1,27.29,muffled choir,floor darkening
17:30,54,10,9.13,breathing drain,foam under desk
17:45,56,18,1.49,muffled choir,floor darkening
18:00,70,27,6.67,breathing drain,clear
18:15,69,29,5.83,distant surf,floor darkening
18:30,74,35,2.83,muffled choir,clear
18:45,59,34,23.29,none,wrong ceiling
19:00,62,32,15.18,distant surf,footprints arrive
19:15,92,41,16.77,pipe hum,door reflected
19:30,65,40,33.68,pipe hum,foam under desk
19:45,96,39,18.52,gull indoors,floor darkening
20:00,77,46,34.04,none,door reflected
20:15,78,46,13.45,bell once,light below surface
20:30,99,50,15.54,pipe hum,clear
20:45,91,53,5.9,muffled choir,footprints arrive
21:00,83,56,30.51,bell once,clear
21:15,95,61,2.75,muffled choir,light below surface
21:30,93,63,28.78,gull indoors,footprints arrive
21:45,86,62,7.43,none,wrong ceiling
22:00,77,65,27.99,pipe hum,foam under desk
22:15,100,70,21.13,muffled choir,window shows sea
22:30,75,70,29.24,distant surf,light below surface
22:45,73,75,18.23,gull indoors,wrong ceiling
23:00,82,79,23.35,gull indoors,floor darkening
23:15,93,81,9.05,none,floor darkening
23:30,100,80,32.14,gull indoors,foam under desk
23:45,78,79,1.02,distant surf,floor darkening
00:00,84,83,30.41,distant surf,window shows sea
00:15,100,92,1.38,none,foam under desk
00:30,92,98,15.5,pipe hum,clear
00:45,100,99,16.68,distant surf,window shows sea
01:00,100,103,10.33,breathing drain,wrong ceiling
01:15,100,106,14.81,gull indoors,wrong ceiling
01:30,100,114,35.72,gull indoors,floor darkening
01:45,100,116,5.25,gull indoors,door reflected
02:00,91,116,13.58,bell once,floor darkening
02:15,100,122,13.92,distant surf,window shows sea
02:30,100,121,13.32,gull indoors,clear
02:45,100,123,8.89,distant surf,window shows sea
03:00,100,130,9.55,breathing drain,clear
03:15,100,129,9.09,bell once,wrong ceiling
03:30,93,128,16.56,distant surf,floor darkening
03:45,100,136,4.36,pipe hum,window shows sea
04:00,100,140,14.16,breathing drain,wrong ceiling
04:15,100,140,36.68,muffled choir,wrong ceiling
04:30,100,138,21.37,muffled choir,footprints arrive
04:45,100,137,17.92,pipe hum,wrong ceiling
05:00,100,146,10.63,gull indoors,window shows sea
05:15,100,152,2.82,none,floor darkening
05:30,100,156,2.13,none,door reflected
05:45,100,154,14.01,distant surf,footprints arrive
06:00,100,156,7.98,muffled choir,window shows sea
06:15,100,161,35.44,muffled choir,light below surface
06:30,100,167,11.9,distant surf,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
