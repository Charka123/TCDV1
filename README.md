## Tropical Cyclone Data Viewer (Work In Progress!)
Tropical Cyclone Data Viewer is the name for this project, though it is more of an expectation for how this project will shape in the future because the current feature set is so limited that it doesn't deserve this name. Please stay tuned for updates!
### Current Features 
* Reads from the latest [ATCF](https://en.wikipedia.org/wiki/Automated_Tropical_Cyclone_Forecasting_System) (Automated Tropical Cyclone Forecasting System) and processes the text into more understandable information.
* Information includes the name of tropical cyclones that are active in the world, the current classification of the storm, the numbering of the storm, current maximum winds, current minimum pressure, and current location.
* It supports the detection of subbasins (for example, the Arabian Sea and Bay of Bangel in the North Indian Ocean) and can assign the proper basin letter.
* It supports the detection of Potential Tropical Cyclones used by the NHC for the northeastern Pacific Ocean and North Atlantic Ocean.
### Known Issues 
* When the best track file for a storm has not been created by NRL (Navel Research Laboratory) yet but shows up on the ATCF track file, the storm classification will not display properly.
### Future Plan 
Over this summer, I am planning to add another feature that allows users to upload the best track file and the program can output information such as the active duration of the storm, maximum winds, minimum central pressure, and accumulated cyclone energy ([ACE](https://en.wikipedia.org/wiki/Accumulated_cyclone_energy)) of that storm. The program will also be able to generate an image of the storm's track. 
<br> <br>
Finally, all of these features will be presented in a GUI application format. I will be using Java to write the GUI as it is more suitable for it and it is also cross-platform. If you have any suggestions, please let me know by creating a new issue under this repository!
