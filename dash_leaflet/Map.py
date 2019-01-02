# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Map(Component):
    """A Map component.
Description to be added

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): ...
- id (string; optional): The ID used to identify this component in Dash callbacks
- animate (boolean; optional): If true, panning will always be animated if possible.
Defaults to false.
- bounds (dict; optional): A rectangle for the map to contain. It will be centered, and the map will
zoom in as close as it can while still showing the full bounds
- center (dict; optional): Center of the map. Changes are compared by value, so [51.0, 0.0] is
considered the same as {lat: 51, lng: 0}.
- className (string; optional): Center of the map. Changes are compared by value, so [51.0, 0.0] is
considered the same as {lat: 51, lng: 0}.
- doubleClickZoom (string; optional): TBA
- dragging (boolean; optional): TBA
- keyboard (boolean; optional): TBA
- maxBounds (dict; optional): TBA
- viewportData (dict; optional): TBA
- style (dict; optional): TBA
- scrollWheelZoom (string | boolean; optional): TBA
- useFlyTo (boolean; optional): TBA
- tap (boolean; optional): TBA
- touchZoom (boolean; optional): TBA
- viewport (dict; optional): sets the viewport based on the provided value or the center and zoom properties.
- zoom (number; optional): TBA

Available events: """
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, animate=Component.UNDEFINED, bounds=Component.UNDEFINED, center=Component.UNDEFINED, className=Component.UNDEFINED, doubleClickZoom=Component.UNDEFINED, dragging=Component.UNDEFINED, keyboard=Component.UNDEFINED, maxBounds=Component.UNDEFINED, viewportData=Component.UNDEFINED, style=Component.UNDEFINED, scrollWheelZoom=Component.UNDEFINED, useFlyTo=Component.UNDEFINED, tap=Component.UNDEFINED, touchZoom=Component.UNDEFINED, viewport=Component.UNDEFINED, zoom=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'animate', 'bounds', 'center', 'className', 'doubleClickZoom', 'dragging', 'keyboard', 'maxBounds', 'viewportData', 'style', 'scrollWheelZoom', 'useFlyTo', 'tap', 'touchZoom', 'viewport', 'zoom']
        self._type = 'Map'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'id', 'animate', 'bounds', 'center', 'className', 'doubleClickZoom', 'dragging', 'keyboard', 'maxBounds', 'viewportData', 'style', 'scrollWheelZoom', 'useFlyTo', 'tap', 'touchZoom', 'viewport', 'zoom']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Map, self).__init__(children=children, **args)

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
            return ('Map(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Map(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
