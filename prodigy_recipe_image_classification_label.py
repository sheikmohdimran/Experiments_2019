"""
  Prodigy Recipe to create a Image labeller for classification task.
"""

import prodigy
from prodigy.components.loaders import Images
from prodigy.util import split_string

def add_label_to_stream(stream):
    options = [{"id": label, "text": label} for label in ("Label1", "Label2")]
    for eg in stream:
        eg["options"] = options
        yield eg

@prodigy.recipe('image-classification',
    dataset=("The dataset to use", "positional", None, str),
    source=("Path to a directory of images", "positional", None, str)
)
def image_classification(dataset, source, label=None):
    """
    Stream images from directory and apply first label among the ones in input 
    """

    stream = Images(source)
    stream = add_label_to_stream(stream)#, label)

    print(stream)

    return {
        'dataset': dataset,        # Name of dataset to save annotations
        'stream': stream,          # Incoming stream of examples
        'view_id': 'choice'
    }

# Example usage (works in prodigy 1.8.5): 
# prodigy image-classification <dataset_id> <path_where_images_are_stored> -F prodigy_recipe_image_classification_label.py
