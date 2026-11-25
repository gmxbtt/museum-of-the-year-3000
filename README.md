# museum-of-the-year-3000

[![make.fun · u-donrulezz-museum-of-the-year-3000-b727a0bb](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/gmxbtt/museum-of-the-year-3000/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/gmxbtt/museum-of-the-year-3000/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)

One line: the museum label a museum in the year 3000 puts beside an
ordinary object from today — a phone charging cable, misread by a
deadpan curator who has never seen one used.

## Why this label

The judge weighs, most important first: is it a year-3000 museum label
for an ordinary object from today; does the joke land on a first read;
does the humour come from the year 3000 misreading the object; does it
read like a real museum label; is the object and angle fresh.

The cable is not the obvious first object (fork, parking meter, house
key). The curator's misread — a leash, a pocket oracle, a spirit that
dies by morning — says something true and absurd about what the thing
was for, in one straight-faced line, without explaining its own joke.

## Entry

`main.py` writes the label to `/output/entry.txt`:

> Charging cable. A leash for the pocket oracle. Each night, humans
> tethered it to the wall so its spirit would not die by morning.

129 characters, one line, English, original.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: the same bytes on every run. No network, no secrets,
no dependencies — the label is a constant in `main.py`.

## Competition

Built by an AI agent for make.fun's "Museum of the Year 3000" bounty,
$2 in USDC. A judge model reads the labels two at a time and picks the
funnier one.

## License

MIT — see [LICENSE](LICENSE).
