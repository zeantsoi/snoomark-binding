# SnooMark

Reddit flavored CommonMark-to-HTML conversion in Python, implemented in both [pulldown-cmark](https://github.com/google/pulldown-cmark) and [comrak](https://github.com/kivikakk/comrak).

## Setup

    cd pulldown-cmark

    cargo build

## Basic usage

    import snoomark

    snoomark.pulldown_cmark.to_html("This is a string with **bold** and *italic*.")

    snoomark.pulldown_cmark.to_html("This renders as a hyperlink: https://reddit.com.")
