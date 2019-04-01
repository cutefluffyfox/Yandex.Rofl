import React from "react";
import {Card, Button} from "react-bootstrap";

class SearchItem extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      name: this.props.problem,
      answer: this.props.answer,
      id: this.props.id,
    }
  }

  componentWillReceiveProps(nextProps){
    this.setState({
      name: nextProps.problem,
      answer: nextProps.answer,
      id: nextProps.id,
    })
  }


  render(){
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
            {this.state.name}
            <hr/>
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
