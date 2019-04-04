import React from "react";
import {Card, Button, OverlayTrigger, Popover, ButtonToolbar} from "react-bootstrap";

class SearchItem extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      name: this.props.problem,
      answer: this.props.answer,
      id: this.props.id,
      mem: this.props.mem,
      show: false,
      find: this.props.find,
    }
  }

  componentWillReceiveProps(nextProps){
    this.setState({
      name: nextProps.problem,
      answer: nextProps.answer,
      id: nextProps.id,
      mem: nextProps.mem,

    })
  }


  render(){

    const popover = (
      <Popover id="popover-basic" title="Переписка">
        {this.state.mem}
      </Popover>
    );

    const Example = () => (
      <OverlayTrigger trigger="click" placement="bottom" overlay={popover}>
        <Button variant="success">Посмотреть переписку</Button>
      </OverlayTrigger>
    );

    return(
      <div>
      <Card>
        <Card.Body>
          <Card.Title
              style={{
                fontSize:"15pt",
                fontFamily: "Arial",
              }}
            >{this.state.id}</Card.Title>
          <Card.Text
              style={{
                fontSize: "12pt",
                fontFamily: 'Arial',
              }}
            >
            {find(this.state.name)}
            <hr/>
            {find(this.state.answer)}
            <br/>
            {(this.state.show) ? <span><hr/>{find(this.state.mem)}</span> : null}
          </Card.Text>
        </Card.Body>
        <Card.Footer>
          <Button style={{
              width: "100%",
              height: "100%"
            }}
              onClick={() => {this.setState({show: !this.state.show})}}>
              {(this.state.show) ? "Скрыть переписку" : "Просмотреть переписку"}
          </Button>
        </Card.Footer>
      </Card>
      <br />
      </div>
    );
  }
}

export default SearchItem;
