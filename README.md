# witcher3-heightmaps
Elevation data from all The Witcher 3 levels

# Download
Since GitHub's file size limit is too small for detailed terrain data, the images are hosted on MEGA (.png).

| Terrain              | Size (m) | Elevation Range (m) | Res (px) | Download                                                                           |
| -------------------- | -------- | ------------------- | -------- | ---------                                                                          |
| White Orchard        | 2000^2   | -37, 45             | 4096^2   | [19MB](https://mega.nz/file/hLcCGb4Q#QQHWK-PqXRMby8ANcxqCtgjItdp0ihCu36Vf4K2e3ZY)  |
| Novigrad + Velen     | 8625^2   | -65, 295            | 23552^2  | [389MB](https://mega.nz/file/0XkxAIDT#abT45Ba_dh1M-2oYBLQzLLX5bbJ3R0GYPp4iDyivol4) |
| Skellige             | 7472^2   | -77, 308            | 16384^2  | [170MB](https://mega.nz/file/Nftw0ZpQ#HjrNisbB8mEvSC9GaWcEa63pI4ZINUB0ZahcW1u6T00) |
| Kaer Morhen          | 8000^2   | -118, 1682          | 16384^2  | [152MB](https://mega.nz/file/8XtTFJyA#BmHB12ImXlndmIv2INQlQ04ZYTmVWZH1jRNr9m1_Q4k) |
| Toussaint            | 8000^2   | -15, 1785           | 16384^2  | [132MB](https://mega.nz/file/9KNGxDKB#cGB69qYCFTjF-HZUFfabYJO1qSJeBpq9CiaqqIWqiUE) |
| Vizima Palace        | 3600^2   | -50, 50             | 4608^2   | [1MB](https://mega.nz/file/UPFAAKCK#-70QYcXmYPmUMX0CVV8hszoPODWfYrJLr8D9RvcwmkM)   |
| Isle Of Mist         | 1868^2   | -80, 308            | 4096^2   | [12MB](https://mega.nz/file/lWFwwa6D#h9aqa-Nu_jNWgmu8GwuTcnKd5oplicrJjzkRinKcU0U)  |
| The Spiral           | 8000^2   | -100, 600           | 24576^2  | [386MB](https://mega.nz/file/FC9ATCDY#wU2N6Q-aOS5pKmiWV3G0d9v2CMt2nEwEsTX2KOvCbr0) |
| White Orchard Winter | 2000^2   | -37, 45             | 4096^2   | [19MB](https://mega.nz/file/JaVxUCKQ#akKvF4zjOR0r_alm8ripIEY2VqS8S5V26D-m0oZzNS0)  |

White Orchard Winter is a slightly altered version used in the Empress Ending, The Spiral is where "Through Time and Space" takes place.
In the game, all the terrains are centered, so the corners sit at {-0.5 * size}.

_Feel free to share your creations in the [Showcase Discussion](https://github.com/Til-Weimann/witcher3-heightmaps/discussions/3), I'm always curious to see what you came up with._

# How to obtain the files manually
Here is a quick guide on how to obtain the files on your own (Windows):

1. Install the nightly build of **WolvenKit 7** ([https://github.com/WolvenKit/WolvenKit-7](https://github.com/WolvenKit/WolvenKit-7/tags)).

2. Create a new mod in WolvenKit and open the asset browser

3. Disable the "limit results" checkbox and search for "w2ter.1.buffer", mark all and add them to the mod

4. After WolvenKit has finished exporting the files, close it, open your mod folder and browse to *files/Mod/Bundle/levels/[level]/terrain_tiles*

5. Since the way the files are named does not fully represent their order, we need to rename the files first. Since there is quite a lot of them, install **EF Multi File Renamer** (efsoftware.com/mr/e.htm, trial version).

6. Download efmr_ruleset.mrt from the repository, hit "Import Rule" in EF Multi File Renamer and select it.

7. IN EFMR, navigate to the folder with the terrain files, make sure the rules are activated and hit Rename.

5. Install **ImageMagick** (imagemagick.org)

6. Open the Console and also change the directionary to that folder.

7. Find out the terrains Tile Resolution using WolvenKit. The number is found in the terrains W2W file under "CClipMap #1", and will either be 256, 512 or 1024.

9. We will now convert the raw image data to a readable format like PNG. To do this, enter this command in the console, set the resolution value and hit enter:
  **FOR /R %a IN (*.buffer) DO magick convert -size [tileRes]x[tileRes] -depth 16 -define quantum:format=unsigned gray:"%~a" "%~dpna.png"**
  
10. After all the images have been converted, open the folder and scoll all the way down, and check for the highest value in the folder (3, 15, 31 etc.).

11. Open the console again and enter this command: **magick montage -mode concatenate -tile [VALUE+1]x tile_*.png joined.png**

12. After the individual images have been merged (this can take a bit of time depending on your computer and what image it is), you should see joined.png in your folder. Open it up and check if everything looks right, if yes, you can delete all the other files in the folder.

13. Now, the last thing you need to do is to flip the image. You can do so with **magick convert -flip joined.png flipped.png**, or just with any image editor like GIMP (Image => Transform => Flip Vertically)
  
If you have any questions or problems, head to the Discussions page and ask away. :D

# Other
- Meta information (e. g. size, tile resolution or elevation range) can be found in each worlds W2W file.

- If you wonder what data is stored in the other w2ter.N.buffer files, check out this GDC Presentation: https://archive.org/details/GDC2014Gollent
  
  To sum it up:
  
  - The individual tiles are dynamicly streamed depending on player location.
  
  - w2ter.2.buffer (control map) contains internal information on how the terrain is textured (texture indices, UV scale, slope threshold)
  
  - Buffers 3-6 are mipmaps of height and control map, followed by the color (tint) map
  
- If you're looking to obtain data beyond just height, some of the python scripts in this repo might prove useful

# Legal
I uploaded these height maps for other The Witcher fans to use them in their own fan projects since obtaining them manually can take quite a bit of time.

While I heavily doubt that CDPR will have something against this, a legal permission to do so does not exist.
You should limit the use of data extracted from the game in general to personal fan projects and refrain from using it in any commercial way without having explicit permission by CDPR.

In the case that CDPR should have something against the height data being up for download here, please contact me and I will take the files down.
