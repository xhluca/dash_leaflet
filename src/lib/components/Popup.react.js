import React, {Component, Fragment} from 'react';
import PropTypes from 'prop-types';
import { Popup as LeafletPopup} from 'react-leaflet';

/**
 * Description to be added
 */
class Popup extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    const {
      children,
      position
    } = this.props;

    return (
      <LeafletPopup position={position}>
        <div>{children}</div>
      </LeafletPopup>
    );
  }
}

Popup.propTypes = {

  /**
   * The ID used to identify this component in Dash callbacks
   */
  id: PropTypes.string,

  /**
   * ...
   */
  children: PropTypes.string,

  /**
   * To be added
   */
  position: PropTypes.object,

  /**
   * Dash-assigned callback that should be called whenever any of the
   * properties change
   */
  setProps: PropTypes.func
}

export default Popup;
