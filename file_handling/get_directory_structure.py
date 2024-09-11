import os


def get_directory_tree(path, exclude_files=None):
    exclude_files = exclude_files or []
    def add_node(parent, node_name, is_directory=True, full_path=""):
        # Create a new node
        node = {"label": node_name, "value": full_path, "children": [] if is_directory else None}
        parent["children"].append(node)
        return node

    def process_directory(path, parent_node):
        
        try:
            with os.scandir(path) as entries:
                for entry in entries:
                    if entry.name in exclude_files:
                        continue
                    if entry.is_dir():
                        # Process directories
                        node = add_node(parent_node, entry.name, is_directory=True, full_path=entry.path)
                        process_directory(entry.path, node)
                    elif entry.is_file():
                        # Add files
                        add_node(parent_node, entry.name, is_directory=False, full_path=entry.path)
        except PermissionError:
            pass  # Skip directories that we don't have permission to access

    root_nodes = []
    for entry in os.scandir(path):
        if entry.is_dir() and entry.name not in exclude_files:
            root_node = {"label": entry.name, "value": entry.path, "children": []}
            root_nodes.append(root_node)
            process_directory(entry.path, root_node)
        elif entry.is_file():
            # Include files at the root level
            root_nodes.append({"label": entry.name, "value": entry.path, "children": None})

    root_node = [{"label": os.path.basename(path), "value": path, "children": root_nodes}]
    return root_node

