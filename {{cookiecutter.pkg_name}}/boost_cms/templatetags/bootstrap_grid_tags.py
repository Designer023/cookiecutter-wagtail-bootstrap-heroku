from django import template

register = template.Library()

@register.simple_tag
def column_classes(col_block):
    """
    Creates a list of classes for column classes
    :param col_block: a Column block from a StructBlock
    :return:
    """
    class_str = ''

    for val, size in col_block.value['columns'].items():
        if size:
            class_str += 'col-{}-{} '.format(val, size)

    for val, size in col_block.value['offset'].items():
        if size:
            class_str += 'offset-{}-{} '.format(val, size)

    for val, size in col_block.value['order'].items():
        if size:
            class_str += 'order-{}-{} '.format(val, size)

    return class_str
