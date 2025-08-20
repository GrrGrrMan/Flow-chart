from graphviz import Digraph

# Create a flowchart
dot = Digraph(comment="Operations Flowchart for Grinny")

# Nodes
dot.node("Concept", "Concept (Grinny)")
dot.node("Build", "Build/Production\n(Unreal Engine + Free Models)")
dot.node("Launch", "Launch\n(Itch.io Only)")
dot.node("Instructions", "Installation & Play\nInstructions on Itch.io")
dot.node("Virtual", "Virtual-Only Product\n(No Physical Production)\n+ Lower Environmental Impact")

# Edges
dot.edge("Concept", "Build")
dot.edge("Build", "Launch")
dot.edge("Launch", "Instructions")
dot.edge("Launch", "Virtual")

# Render flowchart
dot.format = "png"
file_path = "/mnt/data/grinny_operations_flowchart"
dot.render(file_path, view=True)

file_path + ".png"
