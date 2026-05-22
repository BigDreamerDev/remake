# Sensor Log SW-MAR-2007

location: Grey Buoy Field
capture-date: 2022-01-20
device: floorline acoustic monitor

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
22:00,56,1,27.32,muffled choir,light below surface
22:15,81,9,26.76,distant surf,window shows sea
22:30,63,12,25.87,bell once,floor darkening
22:45,75,16,29.4,bell once,door reflected
23:00,85,14,32.74,muffled choir,floor darkening
23:15,79,14,28.15,muffled choir,light below surface
23:30,64,18,30.48,breathing drain,clear
23:45,59,22,7.33,static shaped like rain,light below surface
00:00,57,27,11.3,pipe hum,light below surface
00:15,77,35,2.17,static shaped like rain,floor darkening
00:30,81,35,6.51,none,foam under desk
00:45,92,35,21.69,distant surf,floor darkening
01:00,83,43,12.57,static shaped like rain,footprints arrive
01:15,61,41,24.79,distant surf,window shows sea
01:30,78,44,21.11,distant surf,door reflected
01:45,98,53,27.76,none,foam under desk
02:00,89,56,25.91,muffled choir,foam under desk
02:15,73,57,10.03,none,footprints arrive
02:30,100,56,15.79,bell once,footprints arrive
02:45,98,61,15.51,muffled choir,clear
03:00,88,70,5.92,distant surf,clear
03:15,83,77,16.43,gull indoors,door reflected
03:30,100,82,17.57,muffled choir,foam under desk
03:45,95,84,2.23,pipe hum,floor darkening
04:00,79,91,11.98,muffled choir,clear
04:15,97,94,20.73,bell once,wrong ceiling
04:30,91,102,16.18,gull indoors,footprints arrive
04:45,100,101,32.93,muffled choir,light below surface
05:00,100,104,21.14,distant surf,light below surface
05:15,91,111,3.35,breathing drain,window shows sea
05:30,100,119,34.62,breathing drain,light below surface
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
