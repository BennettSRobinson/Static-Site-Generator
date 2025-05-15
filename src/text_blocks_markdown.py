def markdown_to_blocks(markdown):
    blocks = markdown.strip().split("\n\n")
    new_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block:
            lines = stripped_block.split("\n")
            cleaned_block = "\n".join(line.strip() for line in lines)
            new_blocks.append(cleaned_block)
    return new_blocks
