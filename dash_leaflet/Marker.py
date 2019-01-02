# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Marker(Component):
    """A Marker component.
Description to be added

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): ...
- id (string; optional): The ID used to identify this component in Dash callbacks
- position (dict; optional): To be added
- draggable (boolean; optional): To be added
- zIndexOffset (number; optional): To be added
- opacity (number; optional): To be added
- iconAnchor (list; optional): https://leafletjs.com/reference-1.3.4.html#icon
- iconSize (list; optional): https://leafletjs.com/reference-1.3.4.html#icon
- popupAnchor (list; optional): https://leafletjs.com/reference-1.3.4.html#icon
- shadowSize (list; optional): https://leafletjs.com/reference-1.3.4.html#icon
- tooltipAnchor (list; optional): https://leafletjs.com/reference-1.3.4.html#icon

Available events: """
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, position=Component.UNDEFINED, draggable=Component.UNDEFINED, zIndexOffset=Component.UNDEFINED, opacity=Component.UNDEFINED, iconAnchor=Component.UNDEFINED, iconSize=Component.UNDEFINED, popupAnchor=Component.UNDEFINED, shadowSize=Component.UNDEFINED, tooltipAnchor=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'position', 'draggable', 'zIndexOffset', 'opacity', 'iconAnchor', 'iconSize', 'popupAnchor', 'shadowSize', 'tooltipAnchor']
        self._type = 'Marker'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'id', 'position', 'draggable', 'zIndexOffset', 'opacity', 'iconAnchor', 'iconSize', 'popupAnchor', 'shadowSize', 'tooltipAnchor']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Marker, self).__init__(children=children, **args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('Marker(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Marker(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
