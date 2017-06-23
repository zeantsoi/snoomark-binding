# SnooMark

Reddit flavored CommonMark-to-HTML conversion in Python, built upon [pulldown-cmark](https://github.com/google/pulldown-cmark).

## Setup

    cd pulldown-cmark

    cargo build

## Basic usage

    import snoomark

    snoomark.to_html("This is a string with **bold** and *italic*.")

