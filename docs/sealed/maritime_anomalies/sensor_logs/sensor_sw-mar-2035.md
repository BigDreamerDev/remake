# Sensor Log SW-MAR-2035

location: Room 0 Flood Annex
capture-date: 1983-10-29
device: manual tide staff

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
13:00,80,9,1.74,distant surf,clear
13:15,70,15,7.13,gull indoors,footprints arrive
13:30,86,15,21.16,bell once,footprints arrive
13:45,61,23,9.12,distant surf,clear
14:00,75,30,16.45,static shaped like rain,window shows sea
14:15,71,30,24.76,distant surf,door reflected
14:30,80,30,27.23,bell once,light below surface
14:45,71,35,10.98,static shaped like rain,window shows sea
15:00,91,38,33.88,none,window shows sea
15:15,87,47,26.51,distant surf,foam under desk
15:30,85,46,31.85,distant surf,door reflected
15:45,77,46,13.26,none,window shows sea
16:00,90,50,20.23,breathing drain,window shows sea
16:15,98,52,3.05,pipe hum,door reflected
16:30,69,52,20.31,pipe hum,light below surface
16:45,96,51,10.4,pipe hum,footprints arrive
17:00,90,52,25.45,none,wrong ceiling
17:15,75,54,15.68,static shaped like rain,light below surface
17:30,95,59,6.32,none,light below surface
17:45,80,60,9.25,none,light below surface
18:00,76,68,18.44,distant surf,wrong ceiling
18:15,92,74,4.0,none,clear
18:30,85,77,12.89,muffled choir,door reflected
18:45,81,78,34.78,gull indoors,window shows sea
19:00,100,85,30.46,none,foam under desk
19:15,82,85,23.78,muffled choir,clear
19:30,94,93,2.32,breathing drain,light below surface
19:45,82,96,30.81,bell once,floor darkening
20:00,100,104,17.8,bell once,footprints arrive
20:15,100,107,35.07,pipe hum,footprints arrive
20:30,100,114,18.28,distant surf,footprints arrive
20:45,100,118,12.03,static shaped like rain,clear
21:00,100,127,29.16,muffled choir,wrong ceiling
21:15,92,132,24.61,bell once,floor darkening
21:30,100,132,24.86,pipe hum,clear
21:45,100,130,13.43,none,floor darkening
22:00,100,131,14.01,pipe hum,foam under desk
22:15,94,138,27.13,distant surf,wrong ceiling
22:30,100,139,2.31,muffled choir,window shows sea
22:45,98,137,1.75,static shaped like rain,floor darkening
23:00,100,137,8.69,muffled choir,door reflected
23:15,100,136,33.09,bell once,foam under desk
23:30,100,140,10.08,static shaped like rain,door reflected
23:45,96,139,27.29,gull indoors,wrong ceiling
00:00,100,137,19.58,static shaped like rain,footprints arrive
00:15,100,139,33.9,static shaped like rain,footprints arrive
00:30,100,143,2.11,gull indoors,door reflected
00:45,100,142,2.3,distant surf,door reflected
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
