# witcher3-heightmaps
Elevation data from all The Witcher 3 levels

# Download
Since GitHub's file size limit is too small for detailed terrain data, the images are hosted on Google Drive (.tiff).

White Orchard: 
https://bit.ly/3fcbIWn (32MB) 

Novigrad + Velen: 
https://bit.ly/3lLejYN (1.03GB) 

Skellige: 
https://bit.ly/3sjswi8 (512MB) 

Kaer Morhen: 
https://bit.ly/3vSeo1s (512MB) 

Toussaint: 
https://bit.ly/31cQP5c (512MB) 

Vizima Palace:
https://bit.ly/3d6vxf4 (41MB) 

Isle Of Mist: 
https://bit.ly/39amngF (32MB) 

The Spiral (Through Time and Space): 
https://bit.ly/2QCIOoj (1.12GB) 

White Orchard Winter (Empress Ending)*: 
https://bit.ly/3chKtYX (32MB) 

*There might be not be any difference to regular White Orchard

# How to obtain the files manually
Here is a quick guide on how to obtain the files on your own (Windows):

1. Install **WolvenKit** 0.6 (https://www.nexusmods.com/witcher3/mods/3161)

2. Create a new mod in WolvenKit and open the asset browser

3. Disable the "limit results" checkbox and search for "w2ter.1.buffer", mark all and add them to the mod

4. After WolvenKit has finished exporting the files, close it, open your mod folder and browse to *files/Mod/Bundle/levels/[level]/terrain_tiles*

5. Since the way the files are named does not fully represent their order, we need to rename the files first. Since there is quite a lot of them, install **EF Multi File Renamer** (efsoftware.com/mr/e.htm, trial version).

6. Download efmr_ruleset.mrt from the repository, hit "Import Rule" in EF Multi File Renamer and select it.

7. IN EFMR, navigate to the folder with the terrain files, make sure the rules are activated and hit Rename.

5. Install **ImageMagick** (imagemagick.org)

6. Open the Console and also change the directionary to that folder.

7. Find out what resolution the individual files are. 128KB => 256x256, 512KB => 512x512

8. We will now convert the raw image data to a readable format (using .tiff here, but it really works with anything). To do this, enter this command in the console, set the resolution value and hit enter:
  **FOR /R %a IN (*.buffer) DO magick convert -size [RESOLUTION]x[RESOLUTION] -depth 16 -define quantum:format=unsigned gray:"%~a" "%~dpna.tiff"**
  
9. After all the images have been converted, open the folder and scoll all the way down, and check for the highest value in the folder (3, 15, 31 etc.).

10. Open the console and enter in this command (you can change also the output format): **magick montage -mode concatenate -tile [VALUE+1]x tile_*.tiff joined.tiff**

11. After the individual images have been merged (this can take a bit of time depending on your computer and what image it is), you should see joined.tiff in your folder. Open it up and check if everything looks right, if yes, you can delete all the other files in the folder.

12. Now the last thing we need to do is to flip the image. You can do so with **magick convert -flip joined.tiff flipped.tiff**, or just with any image editor like GIMP (Image => Transform => Flip Vertically)
  
If you have any questions or problems, head to the Discussions page and ask away. :D

# Other

- If you wonder what data is stored in the other w2ter.N.buffer files, check out this GDC Presentation: https://archive.org/details/GDC2014Gollent
  
  To sum it up:
  
  - The individual tiles are dynamicly streamed depending on player location.
  
  - w2ter.2.buffer (control map) contains internal information on how the terrain is textured (texture indices, UV scale, slope threshold)
  
  - The following numbers are LODs of height and control map

# Legal
I uploaded these height maps for other The Witcher fans to use them in their own fan projects since obtaining them manually can take quite a bit of time.

While I heavily doubt that CDPR will have something against this, a legal permission to do so not exist.
This is why you should limit the use of data extracted from the game in general to private fan projects and refrain from using them in any commercial way without having explicit permission by CDPR.

In the case that CDPR should indeed have something against the height data being up for download here, please contact me and I will take the files down.
