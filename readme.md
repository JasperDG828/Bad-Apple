# Bad apple

**an in-console video player**
by JasperDG828

### History

Bad apple is a remix of a song in the game Touhou, the song was released in 2007 by Alstroemeria Records with the voice of Nomico. A storybord for the video got uploaded in 2008 by Nico Nico Douga who asked the community to animate it. A lot of people replied with their versions but the one we know today was submitted by a collaborative group led by Anira on october 27th 2009.

Since then, a lot of people tried to play the video in the weirdes possible ways, for example:

- Jan 2014: a user by the name of fb39ca4 uploaded a video to YouTube showcasing a version of the video and audio running on a TI-84+ SE.
- 2019: YouTube user otter_us made a Python program which converts an image into an Braille pattern, ran every frame of the music video, converted it into a subtitle file, and uploaded a blank YouTube video with the file as the subtitles.
- mid-2020: Sarah Purohit programmed her Epyc 64 core processor to display a 16x8 graphic of the video using the CPU's thread usage in task manager.

###### (source and full list: https://en.wikipedia.org/wiki/Bad_Apple!!)

### The actual program

This program is made to play the Bad Apple video in the console.

**framesToText.py**

framesToText.py converts the given frames into ASCII-art with the characters #, =, - and space.
The program expects full paths. The maximum size is the maximum width and height you want the ASCII-art to be.

ex.

```
IN Directory > /home/jasperdg/Bad-Apple/Frames
OUT Directory > /home/jasperdg/Bad-Apple/Frames_txt
MAX Size > 100
```

**play.py**

play.py is used to play the ASCII-art generated by framesToText.py.
The "IN Directory" is the directory where you saved the ASCII-art ("OUT Directory" in framesToText.py)

### Demo


(Videos don't seem to work correctly, so <a href="https://youtu.be/UXCW4gyiFq8">here</a> is link)

