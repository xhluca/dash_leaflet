import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Map as LeafletMap} from 'react-leaflet';

import 'leaflet/dist/leaflet.css';

/**
 * Description to be added
 */
export default class Map extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    const {
      id,
      setProps,
      children,
      center,
      className,
      style,
      zoom
    } = this.props;

    return (
      <LeafletMap
        center={center}
        zoom={zoom}
        style={style}
        ref="leaflet">
        {children}
      </LeafletMap>
    );
  }
};

Map.defaultProps = {
  style: {width: '500px', height: '300px'}
}

Map.propTypes = {

  /**
   * The ID used to identify this component in Dash callbacks
   */
  id: PropTypes.string,

  /**
   * ...
   */
  children: PropTypes.node,

  /**
   * If true, panning will always be animated if possible.
   * Defaults to false.
   */
  animate: PropTypes.bool,

  /**
   * A rectangle for the map to contain. It will be centered, and the map will
   * zoom in as close as it can while still showing the full bounds
   */
  bounds: PropTypes.object,

  /**
  * Center of the map. Changes are compared by value, so [51.0, 0.0] is
  * considered the same as {lat: 51, lng: 0}.
  */
  center: PropTypes.object,

  /**
   * Center of the map. Changes are compared by value, so [51.0, 0.0] is
   * considered the same as {lat: 51, lng: 0}.
   */
  className: PropTypes.string,

  /**
   *
   * TBA
   */
  doubleClickZoom: PropTypes.string,

  /**
   *
   * TBA
   */
  dragging: PropTypes.bool,

  /**
   *
   * TBA
   */
  keyboard: PropTypes.bool,

  /**
   *
   * TBA
   */
  maxBounds: PropTypes.object,

  /**
   *
   * TBA
   */
  viewportData: PropTypes.object,

  /**
   *
   * TBA
   */
  style: PropTypes.object,

  /**
   *
   * TBA
   */
  scrollWheelZoom: PropTypes.oneOfType([
   PropTypes.string,
   PropTypes.bool
  ]),

  /**
   *
   * TBA
   */
  useFlyTo: PropTypes.bool,

  /**
   *
   * TBA
   */
  tap: PropTypes.bool,

  /**
   *
   * TBA
   */
  touchZoom: PropTypes.bool,

  /**
  * sets the viewport based on the provided value or the center and zoom properties.
  */
  viewport: PropTypes.object,

  /**
   *
   * TBA
   */
  zoom: PropTypes.number,

  /**
   * Dash-assigned callback that should be called whenever any of the
   * properties change
   */
  setProps: PropTypes.func
};
