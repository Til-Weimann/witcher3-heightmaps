# witcher3-heightmaps
Elevation data from all The Witcher 3 levels

# Download
Since GitHub's file size limit is too small for detailed terrain data, the images are hosted on MEGA (.png).

White Orchard: 
https://mega.nz/file/hLcCGb4Q#QQHWK-PqXRMby8ANcxqCtgjItdp0ihCu36Vf4K2e3ZY (19MB) 

Novigrad + Velen: 
https://mega.nz/file/0XkxAIDT#abT45Ba_dh1M-2oYBLQzLLX5bbJ3R0GYPp4iDyivol4 (389MB) 

Skellige: 
https://mega.nz/file/Nftw0ZpQ#HjrNisbB8mEvSC9GaWcEa63pI4ZINUB0ZahcW1u6T00 (170MB) 

Kaer Morhen: 
https://mega.nz/file/8XtTFJyA#BmHB12ImXlndmIv2INQlQ04ZYTmVWZH1jRNr9m1_Q4k (152MB)

Toussaint: 
https://mega.nz/file/9KNGxDKB#cGB69qYCFTjF-HZUFfabYJO1qSJeBpq9CiaqqIWqiUE (132MB) 

Vizima Palace:
https://mega.nz/file/UPFAAKCK#-70QYcXmYPmUMX0CVV8hszoPODWfYrJLr8D9RvcwmkM (1MB) 

Isle Of Mist: 
https://mega.nz/file/lWFwwa6D#h9aqa-Nu_jNWgmu8GwuTcnKd5oplicrJjzkRinKcU0U (12MB) 

The Spiral (Through Time and Space): 
https://mega.nz/file/FC9ATCDY#wU2N6Q-aOS5pKmiWV3G0d9v2CMt2nEwEsTX2KOvCbr0 (386MB) 

White Orchard Winter (Empress Ending): 
https://mega.nz/file/JaVxUCKQ#akKvF4zjOR0r_alm8ripIEY2VqS8S5V26D-m0oZzNS0 (19MB) 

_Feel free to share your creations in the [Showcase Discussion](https://github.com/Til-Weimann/witcher3-heightmaps/discussions/3), I'm always curious to see what you came up with._

# How to obtain the files manually
Here is a quick guide on how to obtain the files on your own (Windows):

1. Install the nightly build of **WolvenKit 7** (https://github.com/WolvenKit/WolvenKit-7).

2. Create a new mod in WolvenKit and open the asset browser

3. Disable the "limit results" checkbox and search for "w2ter.1.buffer", mark all and add them to the mod

4. After WolvenKit has finished exporting the files, close it, open your mod folder and browse to *files/Mod/Bundle/levels/[level]/terrain_tiles*

5. Since the way the files are named does not fully represent their order, we need to rename the files first. Since there is quite a lot of them, install **EF Multi File Renamer** (efsoftware.com/mr/e.htm, trial version).

6. Download efmr_ruleset.mrt from the repository, hit "Import Rule" in EF Multi File Renamer and select it.

7. IN EFMR, navigate to the folder with the terrain files, make sure the rules are activated and hit Rename.

5. Install **ImageMagick** (imagemagick.org)

6. Open the Console and also change the directionary to that folder.

7. Find out what resolution the individual files are. 128KB => 256x256, 512KB => 512x512, 2048KB => 1024x1024

8. We will now convert the raw image data to a readable format (using .tiff here, but it really works with anything). To do this, enter this command in the console, set the resolution value and hit enter:
  **FOR /R %a IN (*.buffer) DO magick convert -size [RESOLUTION]x[RESOLUTION] -depth 16 -define quantum:format=unsigned gray:"%~a" "%~dpna.tiff"**
  
9. After all the images have been converted, open the folder and scoll all the way down, and check for the highest value in the folder (3, 15, 31 etc.).

10. Open the console and enter in this command (you can change also the output format): **magick montage -mode concatenate -tile [VALUE+1]x tile_*.tiff joined.tiff**

11. After the individual images have been merged (this can take a bit of time depending on your computer and what image it is), you should see joined.tiff in your folder. Open it up and check if everything looks right, if yes, you can delete all the other files in the folder.

12. Now the last thing we need to do is to flip the image. You can do so with **magick convert -flip joined.tiff flipped.tiff**, or just with any image editor like GIMP (Image => Transform => Flip Vertically)
  
If you have any questions or problems, head to the Discussions page and ask away. :D

# Other
- The terrains do not use the same scale, the ratio between image size and actual terrain size is not always the same. One way you can find out the right dimensions is to use the xy() console command ingame to teleport yourself to the edges. For example, Velen is 8250²m² and Skellige 7475²m².

- If you wonder what data is stored in the other w2ter.N.buffer files, check out this GDC Presentation: https://archive.org/details/GDC2014Gollent
  
  To sum it up:
  
  - The individual tiles are dynamicly streamed depending on player location.
  
  - w2ter.2.buffer (control map) contains internal information on how the terrain is textured (texture indices, UV scale, slope threshold)
  
  - Buffers 3-6 are mipmaps of height and control map, followed by the color (tint) map
  
- If you're looking to obtain data beyond just height, some of the python scripts in this repo might prove useful

# Legal
I uploaded these height maps for other The Witcher fans to use them in their own fan projects since obtaining them manually can take quite a bit of time.

While I heavily doubt that CDPR will have something against this, a legal permission to do so does not exist.
This is why you should limit the use of data extracted from the game in general to personal fan projects and refrain from using them in any commercial way without having explicit permission by CDPR.

In the case that CDPR should indeed have something against the height data being up for download here, please contact me and I will take the files down.
