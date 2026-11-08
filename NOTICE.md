# Third-party notices

## fishdraw

- Source: https://github.com/LingDong-/fishdraw/tree/a514372de1d05b4aa32a9e35aadec9a5299689a2
- Original creator: Lingdong Huang
- Local execution and video: Xity
- Included in: `src/fish-plush/fishdraw.vendored.js` and inlined into `index.html`
- Modifications: exposes the fish's eye position (`__fd_eye`), adds `fd_make(name)` which resets the noise table so the same name always draws the same fish, and adds `fd_randomName()`.

```
MIT License

Copyright (c) 2021 Lingdong Huang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## PyElastica

- Source: https://github.com/GazzolaLab/PyElastica/tree/0688eb4f0d6091288a38367fcea4ac0c57fb0f96
- License: MIT, Copyright (c) 2019–2026 GazzolaLab — https://github.com/GazzolaLab/PyElastica/blob/0688eb4f0d6091288a38367fcea4ac0c57fb0f96/LICENSE
- Theory: https://www.cosseratrods.org/
- Use here: the yarn follows PyElastica's Cosserat-rod discretization (nodes and elements, stretch and bend) re-implemented in a simplified browser form (Verlet nodes with length and bending constraints, twist omitted). No PyElastica source code is included in this repository.

## three.js

- https://github.com/mrdoob/three.js — MIT License, Copyright © 2010-2024 three.js authors
- Loaded at runtime from jsDelivr (`three@0.160.0`); not included in this repository.

## Fonts

- Nanum Myeongjo, IBM Plex Sans KR, IBM Plex Mono — SIL Open Font License 1.1, loaded from Google Fonts.

## Knitting conventions referenced

Chart reading direction, bind-off placement and intarsia colour changes follow common hand-knitting practice as described in, for example:
- Purl Soho, "Reading a Chart" — https://www.purlsoho.com/create/reading-a-chart/
- KnittingHelp forum, "Can I BO at both ends of a row?" — https://forum.knittinghelp.com/t/can-i-bo-at-both-ends-of-a-row/26233
- Interweave, "Knitting in Color: Intarsia Basics" — https://www.interweave.com/article/knitting/knitting-in-color-intarsia-basics/
