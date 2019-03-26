import React from "react";
import {Card} from "react-bootstrap";
import SearchItem from "./SearchItem";



class Results extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      answer: this.props.data,
    };
  }

  render(){
    let renderProblems = this.state.answer.map(v =>
      <SearchItem problem={v.problem} answer={v.answer} />
    );

    return(
      <div>
        <Card.Header> Ответы: </Card.Header>
        {renderProblems}
      </div>
    )
  }

}

export default Results;
