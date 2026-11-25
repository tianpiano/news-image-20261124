# Sum up 24 November's world news in one image

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/tianpiano/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/tianpiano/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

Entry for the make.fun bounty
[Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124)
($100, ends Thu 26 Nov 2026 00:00 UTC).

## What it is

A newspaper-front-page image that sums up the world news of
Tuesday 24 November 2026 in six stories. A large lead feature
(Nvidia) sits at the top, with the other five stories below it,
so the day's news is readable from the image alone — no news
feed needed. v8 (25 Nov, fresh generation, current entry):
same layout as v7 — bright white newspaper front page with a
huge full-width hero photo of the glowing chip and rising
stock line at the top, headline below it, then five stories in
a 3+2 grid. Same six stories and same verified text as
v5/v6/v7. The Ukraine drone is a small propeller-driven UAV,
clearly much smaller than the ship (not a consumer quadcopter
and not a large airplane), and all six descriptions have their
trailing periods in the first generation (no follow-up edit
needed). The perfected v7 is kept as
`entry-v7-perfected-backup.png`. v7 (25 Nov, fresh layout): at her
request to regenerate freely (learning from Claude's freestyle
approach), a new layout — bright white newspaper front page
with a huge full-width hero photo of the glowing chip and
rising stock line at the top, headline below it, then five
stories in a 3+2 grid. Same six stories and same verified text
as v5/v6. Fixes the critic's points: bright clear daylight
illustrations (no dark detail loss), instantly recognisable as
a newspaper front page, the Ukraine drone is now a sleek
military fixed-wing aircraft (not a consumer quadcopter), the
barbed wire fence is continuous, and the two flags face each
other across the fence. All six headlines and all six
descriptions are verified correct, including every trailing
period (the first v7 generation had dropped three periods; a
follow-up edit restored them). The perfected dark v6 is kept as
`entry-v6-perfected-backup.png`, the light v5 as
`entry-v5-backup.png`, and the first dark generation as
`entry-v6-backup.png`. v6 (25 Nov, dark cinematic version):
same six stories and same text as v5, but rebuilt as a dark,
cinematic front page — deep navy-black background, glowing
illustrations, huge serif masthead, dramatic stormy skies —
to stand out for a top ranking. All six headlines and all six
descriptions were verified correct, including every trailing
period (the first dark generation had dropped four periods; a
follow-up edit restored them). v5 (25 Nov): Hormuz subline now
attributes the mine claim to Iran ("Iran says tankers hit
mines, caught fire") because UKMTO reported unidentified
projectiles, not mines, and Iran's mine claim is not
independently verified; Estonia subline kept as "over border
closure" (the longer version with drone claims did not fit the
cell). v4 (25 Nov): Riyadh replaced by Russia–Estonia
(verified Reuters story — Moscow warns of open war over
Estonia's border closure); Hormuz subline fixed to add new
information ("Tankers caught fire after hitting mines")
instead of repeating the headline. COP31 collapse could not be
verified, so it was not used. v3 (25 Nov): lead image is now
chip-only and the Huawei cell is courthouse-only (v2 had merged
them into one image); Hormuz subline drops the disputed "Four"
and reads "Tankers hit mines in Hormuz". v2 (25 Nov): Senegal
replaced by Nvidia as the lead story, Gaza illustration
replaced with a specific street scene, and
headline/description text made larger.

## The six stories

1. **Nvidia reinstates Huang (lead)** — Nvidia's board
   reinstated Jensen Huang as CEO on 23 November after President
   Trump intervened; shares soared 30% on the news.
2. **Huawei found guilty** — A US jury found Huawei guilty of
   conspiracy to steal trade secrets and bank fraud (10 of 12
   counts), acquitting it of racketeering. Sentencing planned for
   September 2027; Huawei said it expects to appeal.
3. **Tankers hit in Hormuz** — Iran's Revolutionary Guard said
   tankers hit naval mines in the Strait of Hormuz and caught
   fire; the UK maritime agency UKMTO separately reported three
   vessels hit by unidentified projectiles, not mines, and
   Iran's mine claim has not been independently verified. The
   image attributes the mine claim to Iran.
4. **Ukraine strikes Russian ships** — Ukraine acknowledged a drone
   strike on the Russian cargo ship Sparta II in the Gulf of
   Finland and said naval drones hit a Russian corvette and cargo
   ship off Libya. Russia said it downed nearly 700 Ukrainian
   drones overnight.
5. **Russia warns Estonia** — Russia's Foreign Ministry accused
   Estonia, a NATO member, of hostile actions "on the verge of
   triggering open war" after Estonia announced it will close its
   land border crossings with Russia from 1 December for at least
   six months, following an alleged arson attack on an Estonian
   defence company. Russia summoned Estonia's chargé d'affaires
   to protest.
6. **Gaza: Hamas security chief killed** — An Israeli air strike
   killed Brigadier General Naeem Abu Mohammed Nahel, head of
   Hamas's internal security service in Gaza, despite a ceasefire
   in place since October 2025.

Sources: Daily Summary Of (24 Nov 2026 final edition),
Just Security Early Edition (24 Nov 2026), South China Morning
Post, Naharnet.

## How to run

```sh
python3 main.py
```

Writes `/output/entry.png` (1024x1024 PNG, 317,672 bytes, under
the 1 MiB limit). No network access. Deterministic: the program
copies the exact bytes of the bundled `entry.png`, so repeated
runs produce byte-identical output (verified: two runs from a
clean `/output` give identical SHA-256 hashes,
`40485fc8755467bc0b0238e50e759232355b2a1ba47eaa24aae925faf53dc28a`).
v1 (Senegal version) is kept as `entry-v1-backup.png`, v2 as
`entry-v2-backup.png`, v3 as `entry-v3-backup.png`, v4 as
`entry-v4-backup.png`, v5 (light version) as
`entry-v5-backup.png`, the first dark generation (four periods
missing) as `entry-v6-backup.png`, the perfected dark v6 as
`entry-v6-perfected-backup.png`, and the perfected v7 as
`entry-v7-perfected-backup.png`.

## Files

- `main.py` — the entry program (Python 3.13, standard library only)
- `entry.png` — the image (1024x1024, PNG)
- `README.md` — this file
- `LICENSE` — MIT License

## License

MIT — see `LICENSE`.
