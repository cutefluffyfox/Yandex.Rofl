import React from "react";
import {Card, Button} from "react-bootstrap";

class SearchItem extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      name: this.props.description,
      answer: this.props.reply,
    }
  }
  render(){
    return(
      <div>
      <Card>
        <Card.Body>
          <Card.Title>{this.state.name}</Card.Title>
          <Card.Text>
            {this.state.answer}
          </Card.Text>
        </Card.Body>
      </Card>
      <br />
      </div>
    );
  }
}

export default SearchItem;
