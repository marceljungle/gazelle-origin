red-origin
==========

`red-origin` is a script that fetches and saves torrent origin information from redacted.ch.

Example output from `red-origin`:

~~~
Artist          Pink Floyd
Name            The Dark Side of the Moon
Edition         Japan MFSL UltraDisc #1, 24 Karat Gold
Edition year    1988
Media           CD
Catalog number  UDCD 517
Record label    Mobile Fidelity Sound Lab
Original year   1973
Log             70%
File count      12
Size            219114079
Info hash       C380B62A3EC6658597C56F45D596E8081B3F7A5C
Uploaded        2016-11-24 01:34:03
Permalink       https://redacted.ch/torrents.php?torrentid=1

Pink Floyd - Dark Side of the Moon (OMR MFSL 24k Gold Ultradisc II) fixed tags/
 3732587    01 - Speak to Me.flac
14244409    02 -  Breathe.flac
16541873    03 - On the Run.flac
35907465    04 - Time.flac
20671913    05 -  The Great Gig in the Sky.flac
37956922    06 - Money.flac
39706774    07 -Us and Them.flac
18736396    08 - Any Colour You Like.flac
20457034    09 - Brain Damage.flac
11153655    10 - Eclipse.flac
    1435    Pink Floyd - Dark Side of the Moon.CUE
    3616    Pink Floyd - Dark Side of the Moon.log

[important]Staff: Technically trumped because EAC 0.95 logs are terrible. There is historic and sentimental value in keeping the first torrent ever uploaded to the site as well as a perfect modern rip. Take no action.[/important]
~~~

Motivation
----------

Having origin information locally available for each downloaded torrent has a number of benefits:
  * music can be retagged and renamed without losing immediate access to original metadata,
  * if RED is ever down or goes away, the origin information is still available, and
  * origin information can be passed to other scripts/tools (e.g., beets) to more accurately identify your music.

While some uploaders helpfully include this information in their uploads, this
is far from standard practice. Additionally, using a tool like `red-origin`
means all torrents will have consistent, parseable origin data independent of
uploader formatting.

Dependencies
------------

* Python 3.0 or later
* `pip install -r requirements.txt`

Usage
-----

~~~
usage: red-origin [-h] [--out file] cookie hash_or_id

Fetches torrent origin information from redacted.ch

positional arguments:
  cookie               session cookie for logging in to RED
  hash_or_id           either the info hash of the torrent or the RED torrent ID

optional arguments:
  -h, --help           show this help message and exit
  --out file, -o file  path to write origin data (default: print to stdout)
~~~

Examples
--------

To save an origin.txt file to the downloaded directory for a particular torrent:

    $> ./red-origin <your_cookie_here> C380B62A3EC6658597C56F45D596E8081B3F7A5C -o $HOME/downloads/"Pink Floyd - Dark Side of the Moon (OMR MFSL 24k Gold Ultradisc II) fixed tags"/origin.txt

Obtaining Your Cookie
---------------------
`red-origin` requires a browser cookie to log in and make API requests. To obtain your cookie:
* Log in to redacted.ch
* In the same tab, open the browser console:
    * Chrome: Ctrl-Shift-J (Windows) or Command-Option-J (Mac)
    * Firefox: Ctrl-Shift-K (Windows) or Command-Option-K (Mac)
* Select the Network tab and refresh the page
* Select any `.js` or `.php` resource in the list
* In the right pane, scroll down to "cookie" under "Request Headers". Copy everything after the `session=`. This your personal cookie (keep it secret!)

Other Notes
-----------

`red-origin` is best used when called automatically in your torrent client when a download finishes. For example, rtorrent users can add something like the following to their `~/.rtorrent.rc`:

~~~
method.set_key = event.download.finished,postrun,"execute2={~/postdownload.sh,$d.base_path=,$d.hash=,$d.tracker_domain=}"
~~~

Then, in `~/postdownload.sh`:
~~~
path=$1
info_hash=$2
tracker=$3
cookie=<your_cookie_here>
[ $tracker == flacsfor.me ] && /path/to/red-origin $cookie $info_hash -o "$path"/origin.txt
~~~
