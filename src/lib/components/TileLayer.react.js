import React, {Component} from 'react';
import PropTypes from 'prop-types';
import { TileLayer as LeafletTileLayer} from 'react-leaflet';


/**
 * Description to be added
 */
export default class TileLayer extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    const {
      id,
      setProps,
      url,
      attribution,
      opacity
    } = this.props;

    return (
      <LeafletTileLayer
        attribution={attribution}
        url={url}
        opacity={opacity}
      />
    );
  }
};

TileLayer.defaultProps = {
  attribution: '&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
  url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
}

TileLayer.propTypes = {

  /**
   * The ID used to identify this component in Dash callbacks
   */
  id: PropTypes.string,

  /**
   * TBA
   */
  attribution: PropTypes.string,

  /**
   * TBA
   */
  url: PropTypes.string,

  /**
   * TBA
   */
  opacity: PropTypes.number,

  /**
   * Dash-assigned callback that should be called whenever any of the
   * properties change
   */
  setProps: PropTypes.func
}
