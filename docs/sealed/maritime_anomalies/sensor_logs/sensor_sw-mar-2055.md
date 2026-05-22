# Sensor Log SW-MAR-2055

location: Rain Room 11
capture-date: 1985-11-17
device: salt-lens array

```csv
time,humidity,depth_mm,salinity_ppt,audio_note,visual_note
02:00,62,5,2.74,gull indoors,light below surface
02:15,83,9,33.02,gull indoors,wrong ceiling
02:30,70,18,4.11,distant surf,floor darkening
02:45,70,24,12.87,distant surf,foam under desk
03:00,78,27,16.09,bell once,clear
03:15,65,27,22.85,muffled choir,floor darkening
03:30,86,28,28.93,static shaped like rain,clear
03:45,82,33,15.71,muffled choir,clear
04:00,92,33,29.72,static shaped like rain,window shows sea
04:15,90,31,34.19,none,door reflected
04:30,80,33,11.81,breathing drain,wrong ceiling
04:45,91,39,8.05,distant surf,wrong ceiling
05:00,70,41,33.72,gull indoors,footprints arrive
05:15,80,40,6.53,bell once,clear
05:30,69,46,22.68,pipe hum,light below surface
05:45,100,55,12.48,static shaped like rain,floor darkening
06:00,93,64,4.03,none,window shows sea
06:15,83,64,23.48,none,door reflected
06:30,96,70,28.72,pipe hum,light below surface
06:45,100,74,10.26,gull indoors,foam under desk
07:00,100,73,34.87,muffled choir,foam under desk
07:15,78,76,12.09,distant surf,clear
07:30,98,81,5.61,pipe hum,clear
07:45,100,87,6.64,distant surf,foam under desk
08:00,84,90,22.46,breathing drain,light below surface
08:15,99,90,33.25,static shaped like rain,footprints arrive
08:30,96,93,30.35,static shaped like rain,window shows sea
08:45,100,101,21.84,muffled choir,light below surface
09:00,86,104,33.25,breathing drain,foam under desk
09:15,100,111,17.58,none,footprints arrive
09:30,88,120,2.79,distant surf,light below surface
09:45,100,128,36.52,bell once,light below surface
10:00,100,126,5.48,breathing drain,window shows sea
10:15,100,131,0.57,muffled choir,window shows sea
10:30,100,140,24.36,distant surf,clear
10:45,100,145,31.38,pipe hum,window shows sea
11:00,96,144,22.55,pipe hum,floor darkening
11:15,100,148,23.37,distant surf,light below surface
11:30,100,153,24.81,gull indoors,clear
11:45,100,159,11.62,none,floor darkening
12:00,100,167,24.43,pipe hum,light below surface
12:15,100,171,8.34,none,footprints arrive
12:30,100,180,21.86,breathing drain,clear
12:45,100,189,28.83,muffled choir,window shows sea
13:00,100,187,6.37,bell once,wrong ceiling
13:15,100,193,26.99,none,clear
13:30,100,197,10.76,none,light below surface
13:45,100,196,22.65,bell once,window shows sea
14:00,100,204,30.38,bell once,floor darkening
14:15,100,209,16.75,breathing drain,clear
14:30,100,207,7.46,bell once,window shows sea
14:45,100,212,34.42,muffled choir,wrong ceiling
15:00,100,217,28.71,distant surf,clear
15:15,100,225,12.47,pipe hum,light below surface
15:30,100,230,28.14,bell once,light below surface
15:45,100,230,7.69,bell once,wrong ceiling
```

Automated flags are intentionally conservative. A human reviewer should treat any reading
that combines indoor surf audio with a nonzero salinity value as a corridor event until
disproved by three dry witnesses.
