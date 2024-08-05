# Add anchors to a markdown file

Reads a markdown file
Where Headings do not have an anchor one is added
Writes result to an output file

The anchor text is in slug format but omits the first work in the line which is assumed to be a section number in 1.1.1 format.

## Example usage:
add_anchors_to_markdown('input.md', 'output.md')