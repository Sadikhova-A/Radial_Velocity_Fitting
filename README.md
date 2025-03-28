# Detecting Exoplanets via Radial Velocity Fitting
## Notes
This was by far the most fun project I've ever worked on. 
I used simulated and real stellar data to find exoplanets by determining their orbital parameters. 
There are two models, single and double planitary. 
The code uses the noisy data to find the orbital parameters of the exoplanets; period P, and semi-amplitude K, which can be used to find the masses of the planets.
The existance of an exoplanet is shown through consistent periodic variations in the stars radial velocity. If the graph is flat it is assumed no planet is found.
You can test this in the code by putting a single planet system into the double planetary model, it will give the sine curve for the planet and a strainght line showing no other plant was found.

Here are some pretty plots produced (Last one is my fav)

![One_noisy](https://github.com/user-attachments/assets/9d1701c2-f511-45b5-be32-6200bb25ad74) ![One_fit](https://github.com/user-attachments/assets/10744a4b-3913-44f3-bdc4-7c7ac3a26451)

![Two_planet_data](https://github.com/user-attachments/assets/cebf6f62-a5fd-42bb-a691-a3909cbfa7ab) ![Two_planet_fit](https://github.com/user-attachments/assets/093347a9-91f7-4cba-8747-232daa144708)
