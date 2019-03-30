import React from "react";
import {Modal, Button} from "react-bootstrap";

class ErrorModal extends React.Component{
  constructor(props){
    super(props);
  }

  render(){
    return(
      <Modal
        show
        size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header>
            <Modal.Title id="contained-modal-title-vcenter">
                Ууупсс... Что-то пошло не так!
            </Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <h4>Ошибка соединения!</h4>
            <p>
              Страница не смогла загрузиться.<br/>
              Перезагрузите страницу!
            </p>
          </Modal.Body>
          <Modal.Footer>
            <Button
              onClick={
                () => {
                  window.location.reload()
                }
              }
            >Закрыть</Button>
          </Modal.Footer>
    </Modal>
    )
  }

}

export default ErrorModal;
