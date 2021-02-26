# Krita Skripts by Karen.

<img src='https://i.imgur.com/lwp1k4R.png'/>

## Utils
## generate video out of files

> Change framerate to larger numbers to get smoother transitions once you have enough pics

```
cat *.png | ffmpeg -framerate 1 -f image2pipe -i - output.mp4
```

> with numbered files (for ex from img_0.png to img_99.png), the command above will not work as intented. To **preserve order** use:

```
cat *_{0..99}.png | ffmpeg -framerate 5 -f image2pipe -i - ../../../obj_det/output.mp4
```

> Python RUlez.
