import networkx as nx
import matplotlib.pyplot as plt

COLOR_MAP = {
    #  level: color
    1: '#f09494',
    2: '#eebcbc',
    3: '#72bbd0',
    4: '#91f0a1',
    5: '#629fff',
    6: '#bcc2f2',
    7: '#eebcbc',
    8: '#f1f0c0',
    9: '#d2ffe7',
    10: '#caf3a6',
    11: '#ffdf55',
    12: '#ef77aa',
    13: '#d6dcff',
    14: '#d2f5f0'
}

GRAPH_OPTIONS = {
    'edge_color': '#FFDEA2',
    'width': 10,
    'with_labels': True,
    'font_weight': 'regular',
}


def get_data():
    """
    Get data with format: [
        [
            node id,
            node caption,
            node group,
            node weight,
        ],
        ...
    ]
    :return:
    """
    return [
        ['1', 'node 1', 0, 100],
        ['1.1', 'node 1.1', 1, 80],
        ['1.2', 'node 1.2', 2, 80],
        ['1.2.1', 'node 1.2.1', 2, 60],
        ['1.2.1.1', 'node 1.2.1.1', 2, 40],
        ['1.2.2', 'node 1.2.2', 2, 60],
        ['1.3', 'node 1.3', 3, 80],
    ]


def generate_mindmap():
    G = nx.Graph()

    for row in get_data():
        node_id = row[0]
        node_path = node_id.rsplit('.', 1)
        try:
            parent_id = node_path[-2]
        except IndexError:
            # Raise only for root node
            parent_id = None

        G.add_node(node_id, group=row[2]+1, nodesize=row[3])
        if parent_id:
            G.add_edge(node_id, parent_id)


    plt.figure(figsize=(25, 25))

    colors = [COLOR_MAP[G.node[node]['group']] for node in G]
    sizes = [G.node[node]['nodesize'] * 50 for node in G]

    """
    Using the spring layout : 
    - k controls the distance between the nodes and varies between 0 and 1
    - iterations is the number of times simulated annealing is run
    default k=0.1 and iterations=50
    """
    nx.draw(G, node_color=colors, node_size=sizes, pos=nx.spring_layout(G, k=0.25, iterations=50), **GRAPH_OPTIONS)
    ax = plt.gca()
    ax.collections[0].set_edgecolor("#555555")
    #  plt.show()
    plt.draw()
    plt.savefig('img1.png', format='png')


def main():
    generate_mindmap()


if __name__ == '__main__':
    main()
