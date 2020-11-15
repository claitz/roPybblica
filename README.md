# roPybblica

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

roPybblica is a python script that leverages Markov Chains to generate fake newspaper headlines and output as png for meme purposes.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Instructions for [deployment](#deployment) are WIP.

### Prerequisites

Python3.8

Install with PIP:

    - PIL
    - markovify
    - textwrap
    - random
    - newspaper3k

### Installing

Clone this repository and type the following in the terminal to generate your first meme using the provided dataset.

```
python pyMeme.py
```

Output images will be generated in the `/output` folder.

To add more titles to the model type:

```
python loadNews.py
```

and follow instructions.

Edit `loadNews.py` to add your own sources - the file structure is straightforward.