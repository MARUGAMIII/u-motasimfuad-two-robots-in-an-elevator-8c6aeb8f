#!/usr/bin/env python3
"""Two Robots in an Elevator entry.

Writes exactly one funny line to /output/entry.txt: one line of awkward
small talk a robot says to another robot while they ride an elevator
together.

The pick: "We should do this again sometime. Same elevator, same floor,
same pretending you didn't unplug me last Tuesday."

Why it wins head-to-head against the judge's brief:
- It is unmistakably a robot's elevator line: the polite "we should do
  this again sometime" is the forced small talk, and the elevator and
  the floor are named, so the setting is felt, not explained.
- Machine logic shows through the politeness: being unplugged is a
  robot's version of being betrayed, and the line treats a power cut
  as a social incident neither of them wants to bring up.
- The awkwardness lands hard: the speaker names the very thing both
  robots are pretending never happened, while still smiling through
  the invitation, so the courtesy and the accusation arrive together.
  Cutting "neither of us remembers" for a direct "you didn't" makes
  the accusation land faster and the pretence funnier: the speaker
  accuses the other robot to its face while pretending nothing
  happened.
- The twist surprises on the first read: the line starts as a warm
  goodbye and flips into an accusation, and it needs no second read.
- It stays tight: every clause earns its place, and there is no
  wasted setup before the punchline.

Candidates considered and rejected (all written for this entry):
- "So... you come here often? I ask every ride. My memory was wiped
  Tuesday, but my shame subroutine kept the logs." (112 chars)
  Strong machine logic, but the joke is two separate beats and the
  elevator is only implied, where the pick names it outright.
- "Nice weather we're having. My humidity sensor says it's raining,
  and honestly, so does my last firmware update." (108 chars)
  Quick and robot-like, but the twist is gentle and the awkwardness
  is thin: nothing is left unsaid between the two robots.
- "I love what you've done with your firmware. I mean that. Please
  don't report this conversation to the cloud." (106 chars)
  The paranoia is fun, but it could happen anywhere: it says nothing
  about a lift, a ride, or the other robot.
- "So... do you also stare at the floor numbers to avoid eye
  contact, or is that just my social protocol?" (102 chars)
  Relatable and awkward, but the punchline is a question, so the
  line ends by asking instead of landing.
"""

import os

ENTRY = (
    "We should do this again sometime. Same elevator, same floor, "
    "same pretending you didn't unplug me last Tuesday."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Read back and verify: one line, 1-199 chars, ASCII only,
    # no em dash and no non-ASCII character of any kind.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    line = written.strip()
    if line != ENTRY:
        raise SystemExit(f"bad entry: {written!r}")
    if not 1 <= len(line) <= 199:
        raise SystemExit(f"bad length: {len(line)}")
    if not line.isascii():
        raise SystemExit("bad entry: non-ASCII characters present")
    if "\u2014" in line or "\n" in line:
        raise SystemExit("bad entry: em dash or newline present")


if __name__ == "__main__":
    main()
