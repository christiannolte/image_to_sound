# image_to_sound
This PythonScript converts a 512px wide bmp file to a soundfile so that the image will be represented in the generated spectrum.

As input a BMP file with 512px width is needed.
Output will be a soundfile where the image is "encoded" in the spectrum.
In fact its an easy spectrumpainter.

Limitations right now:
- Not realy usable for ham radio because the used bandwith is to big.
- I would expect sound as a noise. Currently its an "hammering" sound.

## Usage 

### Install used modules (steps done in Python3.5 other versions may require other steps)
- python -m pip install --upgrade pip
- pip install scipy
- pip install scikit-image

### Execute
- Prepare a input.bmp file in the same directory with 512px witth. When using GIMP use 24Bit RGB format to store.
- call "python image_to_sound.py"

### Enjoy
- listen to output.wav and have a look to a audio spectrum analyser with waterfall view

