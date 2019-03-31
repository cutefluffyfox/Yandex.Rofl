import React from "react";
import {Image, Button, Modal} from "react-bootstrap";

class Autorization extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      showModal: this.props.showModal,
    }
  }

  componentWillReceiveProps(nextProps){
    this.setState({
        showModal: nextProps.showModal,
    })
  }
x
  render(){
    return(
      <Modal
        show={this.state.showModal}
        size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header closeButton>
          <Modal.Title id="contained-modal-title-vcenter">
            Modal heading
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <h4>Centered Modal</h4>
          <p>
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
            dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta
            ac consectetur ac, vestibulum at eros.
          </p>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={this.props.onHide}>Close</Button>
        </Modal.Footer>
      </Modal>
    )
  }
}

export default Autorization;
