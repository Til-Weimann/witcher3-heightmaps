set len=32
magick montage -mode concatenate -tile %len%x tile_*bg.png bg.png
magick convert -flip bg.png bg.png
magick montage -mode concatenate -tile %len%x tile_*ol.png ol.png
magick convert -flip ol.png ol.png
magick montage -mode concatenate -tile %len%x tile_*uv.png uv.png
magick convert -flip uv.png uv.png
magick montage -mode concatenate -tile %len%x tile_*sl.png sl.png
magick convert -flip sl.png sl.png