from causalgraphicalmodels import CausalGraphicalModel
# from collections.abc import Iterable
#sed -i 's/collections/collections.abc/g' /usr/local/lib/python3.10/dist-packages/causalgraphicalmodels/cgm.py
#esercizio 1
"C:\Users\Marco\.vscode\extensions\ms-python.vscode-pylance-2024.11.3\dist\.cache\local_indices\f52d93893aff4693b68bd6b4c99839bdc3b7479b66f28cc61e82b293899bb6d4\causalgraphicalmodels.json"
"""
m1 = CausalGraphicalModel(
    nodes = ["X", "Z", "W", "Y"],
    edges= [
        ("X", "Z"),
        ("Z", "W"),
        ("W", "Y"),
        ("X", "Y")
    ]
)
m1.draw()"""