import re

class Node:
    def __init__(self, name, is_dir, indent_level):
        self.name = name
        self.is_dir = is_dir
        self.indent_level = indent_level
        self.children = []

    def __repr__(self):
        return f"Node(name={self.name!r}, is_dir={self.is_dir}, children={self.children})"

def parse_treefile(content):
    """
    Parse the .treefile file content (as a string) and return a list of top-level Node objects.
    Lines may be indented using spaces or use tree branch characters such as "├──", "└──", or "│   ".
    This function replaces these branch markers with four spaces so that the indent level is computed correctly.
    """
    lines = content.splitlines()
    nodes = []
    stack = []  # Each element is (indent_level, node)

    for raw_line in lines:
        # Skip empty lines.
        if not raw_line.strip():
            continue

        # First, replace branch markers at the beginning of the line with four spaces.
        # The patterns "├── " and "└── " will be replaced by 4 spaces.
        line_processed = re.sub(r'^(├── |└── )', '    ', raw_line)
        # Also, if the line starts with "│   ", replace that with 4 spaces.
        line_processed = re.sub(r'^(│   )', '    ', line_processed)
        
        # Determine indent level based on leading spaces (assuming 4 spaces per level).
        leading = len(line_processed) - len(line_processed.lstrip(" "))
        indent_level = leading // 4

        # Remove leading spaces to get the file or folder name.
        name = line_processed.lstrip(" ")

        # Determine if this is a directory (ends with a slash) or a file.
        is_dir = name.endswith("/")
        node = Node(name, is_dir, indent_level)

        # Place node into the tree using the computed indent level.
        if not stack:
            # Top-level node.
            nodes.append(node)
            stack.append((indent_level, node))
        else:
            # Pop the stack until we find a node with a lower indent level.
            while stack and indent_level <= stack[-1][0]:
                stack.pop()
            if stack:
                parent = stack[-1][1]
                parent.children.append(node)
            else:
                nodes.append(node)
            stack.append((indent_level, node))
    return nodes
