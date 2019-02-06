from wagtail.images.formats import Format, register_image_format, unregister_image_format

unregister_image_format('fullwidth')
register_image_format(Format('fullwidth', 'Full width', 'richtext-image full-width img-fluid d-block mx-auto mb-3', 'width-800'))

unregister_image_format('left')
register_image_format(Format('left', 'Left-aligned', 'richtext-image left img-fluid d-block mx-auto float-md-left mr-md-3 mb-3', 'width-400'))

unregister_image_format('right')
register_image_format(Format('right', 'Right-aligned', 'richtext-image right img-fluid d-block mx-auto float-md-right ml-md-3 mb-3', 'width-400'))


register_image_format(Format('super_wide', 'Super wide', 'richtext-image super img-fluid mb-3', 'max-1200x1200'))