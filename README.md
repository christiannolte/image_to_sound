# image_to_sound
This PythonScript converts a 512px wide bmp file to a soundfile so that the image will be represented in the generated spectrum.

As input a BMP file with 512px width is needed.
Output will be a soundfile where the image is "encoded" in the spectrum.
In fact its an easy spectrumpainter.

Limitations right now:
- not usable for ham radio because the used bandwith is to big
- I would expect sound as a noise. Currently its an "hammering" sound.

## Usage 
Install used modules
call
python image_to_sound.py

