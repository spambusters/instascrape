# instadb

## This script is currently deprecated due to Instagram removing the public /media/ endpoint  

## Features

* Download ALL media files from an Instagram user (images, carousel media, videos)
* Write metadata to ALL media files
* Skip already downloaded files
* Download media to custom directory
* Proxy support
* Upon connection error (with or without a proxy), enter a new proxy to resume
* Skip downloading posts that don't have enough likes  
* Write user posts metadata to an Sqlite3 database
* Download just photos, or just videos, or everything

## Installation
Simply download this repository, or use `git clone https://github.com/spambusters/instadb.git`

## Requirements
1. python 3.5+
2. requests  
    * Network requests
    * ```pip3 install requests```
3.  mutagen  
    * Video metadata
    * ```pip3 install mutagen```
4. exiftool  
    * Photo metadata  
    * Ubuntu
        * `sudo apt install libimage-exiftool-perl`
    * Windows / OSX  
        * Download from the [offical site](https://sno.phy.queensu.ca/~phil/exiftool/), then add it to your system's PATH  

## Usage
```
usage: instadb.py [-h] [--proxy PROXY] [--rate-limit LIMIT] [--likes LIKES]
                  [--photos] [--videos] [--tags  [...]] [--path PATH] [--new]
                  [--db] [--only-db]
                  user

positional arguments:
  user                Instagram user

optional arguments:
  -h, --help          show this help message and exit
  --proxy PROXY       Proxy must be in the format address:port
  --rate-limit LIMIT  Seconds between Instagram requests (default: 1)
  --likes LIKES       Only download media with at least this many likes
  --photos            Only download photos
  --videos            Only download videos
  --path PATH         Custom path for saving local files. (default:
                      "$USER/Downloads/instadb/$ig_user/")
  --new               Only download new media files

Metadata:
  --tags  [ ...]      Space separated media tags (default: [user,
                      "instagram"])
  --db                Write user metadata to an Sqlite3 database
  --only-db           Skip downloading media files
```

### Examples
*Example account:* https://www.instagram.com/espn/  

Download all media with the default rate limit, metadata tags, and write metadata to an Sqlite3 database  
`instadb.py espn --db`  

Use a proxy to download only photos with at least 2000 likes and no rate limit  
`instadb.py espn --proxy 192.168.0.1:8080  --photos --likes 2000 --rate-limit 0`  

Download only videos and tag them as "espn", "video", "sports"  
`instadb.py espn --videos --tags espn video sports`

Download only new files to a custom path  
`instadb.py espn --path "/media/DataHoarder/espn/" --new`  

Skip downloading media files and only write the metadata database  
`instadb.py espn --only-db`

### Example Output
![alt text](https://thumbs.gfycat.com/VictoriousTiredEyas-max-14mb.gif)

## Metadata
### Videos
Video metadata is useful for media servers like *Plex*.
1. Video Title
    * Same as the filename (user + shortcode)
2. Cast Members / Studio
    * The Instagram user
3. Genres
    * The default tags are [user, "instagram"], but custom tags can be specified with the `--tags` CLI arg 
4. Video Summary
    * The post caption

Here's an example video in *Plex* from the https://www.instagram.com/espn/ account:

![alt text](https://i.imgur.com/TFU2ieJ.png)

Because the videos are downloaded from Instagram, they're already optimized for streaming and should require no further conversions.

### Photos
Photo metadata is useful for photo browsing programs that support it, like *Shotwell*

![alt text](https://i.imgur.com/APXyIiW.png)

But the metadata can also be useful in a plain old file browser, like Windows explorer

![alt text](https://i.imgur.com/WvD7IhF.png)  

Notice the `Date Taken` value. This is the time which the photo was originally uploaded to Instagram. This value is also written as the last "Modification date" for the file, so you can sort to your heart's content.

## Database
When you specify the `--db` or `--only-db` CLI args, post metadata will be written to an Sqlite3 database in the downloads folder.  

I suggest using [DB Browser for SQLite](http://sqlitebrowser.org/) for browsing.  
It will allow you to sort by column, so for example you can sort by likes to find the most popular post.

![alt text](https://i.imgur.com/wA8frS2.png)
