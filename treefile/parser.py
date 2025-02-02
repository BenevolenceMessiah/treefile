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
    Lines should be indented (preferably using 4 spaces per level) and may include tree branch characters.
    """
    lines = content.splitlines()
    nodes = []
    stack = []  # Each element is (indent_level, node)

    for raw_line in lines:
        # Skip empty lines
        if not raw_line.strip():
            continue

        # Determine indent level based on leading spaces (assuming 4 spaces per indent)
        leading = len(raw_line) - len(raw_line.lstrip(" "))
        indent_level = leading // 4

        # Remove common tree-drawing characters and extra whitespace
        line = raw_line.strip()
        # Remove branch markers if present.
        if line.startswith("├── "):
            line = line[4:]
        elif line.startswith("└── "):
            line = line[4:]
        elif line.startswith("── "):
            line = line[3:]
        # Now, line is the file/directory name.
        name = line

        # Determine if this is a directory (ends with a slash) or a file.
        is_dir = name.endswith("/")
        node = Node(name, is_dir, indent_level)

        # Place node into the tree using the current indent level.
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
