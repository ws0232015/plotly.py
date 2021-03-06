import _plotly_utils.basevalidators


class ShowticksuffixValidator(
    _plotly_utils.basevalidators.EnumeratedValidator
):

    def __init__(
        self,
        plotly_name='showticksuffix',
        parent_name='scattergeo.marker.colorbar',
        **kwargs
    ):
        super(ShowticksuffixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            values=['all', 'first', 'last', 'none'],
            **kwargs
        )
