# Brutal Error Copy

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Djebrix/brutal-error-copy/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Djebrix/brutal-error-copy/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy that tells the user the brutal truth about
what went wrong — and makes them laugh on the way. Entry for
[Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
on make.fun.

## The line

> We saved your file, then lost the disk we saved it on. The backup was on the same disk. Please type it all again.

## Run

```sh
ENTRY_OUTPUT_DIR=/output python3 main.py
```

Writes the line to `$ENTRY_OUTPUT_DIR/entry.txt`. Stdlib only, no network,
deterministic: two runs produce byte-identical output.
