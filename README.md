# BAKA Extractor
it does ONE thing  
extracts every "baka" said in every file in the "input" directory  
REQUIRES english "ass" subtitle in the mkv file  

right now only ASS subtitle is supported, PGSUB, SRT support might come later  

## Requires:
ffmpeg  
ffmpeg-python  
, that's it  

# How to use
1. Clone the Repo
2. install the nessary stuff, ffmpeg (make sure it is properly added to PATH), and ffmpeg-python libary
3. `python3 main.py` it will automaticlly create the nessary folder
4. drop the mkv file in the `input` folder (works best with any file that has the english subtitle on the 3rd track, any other config and it will break) (external subtitle is NOT supported... yet)
5. `python3 main.py` again to start the process
6. it will ask you if you want burn sub or not, always answer NO, (currenly working on it, anyone smarter than me is welcome to come help, make a PR, it will break)

# Question I'm sure I will get
Q: why does the output file .mp4 instead of mkv?  
A: Shit breaks with mkv, timestamp all over the place and stuff (unusable footage I just gave up and make it export everything as mp4)

Q: Does it work with multiple subtitle tracks?  
A: simple NO! (unless the first subtitle track is full subs), it is hardcoded to read the first subtitle track (Track No.2 (start from 0 of couse))
also NO, multiple audio track will break it so forget what you're thinking dub people
(if anyone want to pick it up and fix this flaw you're welcome to)

Q: when will burn in subtitle work?  
A: when I figure out how to burn it without it erroing out all over my f&******* terminal

Q: why are the answer so agressive?  
A: it is written by a sleepy teenager at midnight that just about to slam their keyboard into their $2,000 laptop after spending hours figuring out WHY subtitle burn wont work properly with mp4 and why mkv output split out garbage timeline that make it unusable

also BIG thanks to OpenAI ChatGPT without it this would't been possible

wanna pay for my laptop screen replacement? my profile readme has the info you need

## legal boring stuff
I'm NOT responsible for chaos people may cause using this software, I'm just a developer, this software only extracts certain "words" from provided content  
I'm NOT responsible for any illegally obtained content people process through this software
Also this software is protected under GNU General Public License v3.0