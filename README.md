# image_to_sound
This PythonScript converts a 512px wide bmp file to a soundfile so that the image will be represented in the generated spectrum.

As input a BMP file with 512px width is needed.
Output will be a soundfile where the image is "encoded" in the spectrum.
In fact its an easy spectrumpainter.

Limitations right now:
- Not realy usable for ham radio because the used bandwith is to big.
- I would expect sound as a noise. Currently its an "hammering" sound.

## Usage 
- Install used modules
- Prepare a input.bmp file in the same directory with 512px with
- call "python image_to_sound.py"
- listen to output.wav and have a look to a audio spectrum analyser with waterfall view

