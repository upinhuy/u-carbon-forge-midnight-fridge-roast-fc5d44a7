# Midnight Fridge Roast

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Midnight Fridge Roast](https://img.shields.io/badge/Midnight%20Fridge%20Roast-entry-0ea5e9)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![make.fun](https://img.shields.io/badge/make.fun-u--carbon--forge--midnight--fridge--roast--fc5d44a7-22c55e)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

One-line roast of a smart fridge that refuses to open after midnight —
entry for the [Midnight Fridge Roast](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
bounty on [make.fun](https://make.fun/r/hv9zk8y5) (prize $2, judged by an AI
comedy-club judge that reads the lines two at a time and keeps the funnier
one until the funniest is left).

## The entry

> It's 2 a.m., my fridge just told me 'we talked about this' — since when
> does an appliance get to ground me from my own leftovers?

## How it works

`main.py` writes that one line to `/output/entry.txt`. Nothing else —
the joke is the whole entry. It guards the gate itself: the line must be
non-blank, a single line, and at most 200 characters, or the program
refuses to write it.

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=/tmp/out python3 main.py   # local test
```

## License

MIT — see [LICENSE](LICENSE).
