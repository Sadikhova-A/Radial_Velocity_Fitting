# Detecting Exoplanets via Radial Velocity Fitting
## Notes
This was by far the most fun project I've ever worked on. 
I used simulated and real stellar data to find exoplanets by finding their orbital parameters. 
There are two models, single and double planitary. 
The code uses the noisy data to find the orbital parameters of the exoplanets; period P, and semi-amplitude K, which can be used to find the masses of the planets.
The existance of an exoplanet is shown through consistent periodic variations in the stars radial velocity. If the graph is flat it is assumed no planet is found.
You can test this in the code by putting a single planet system into the double planetary model, it will give the sine curve for the planet and a strainght line showing no other plant was found.
