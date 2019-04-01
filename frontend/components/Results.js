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

  componentWillReceiveProps(nextProps){
    this.setState({
      answer: nextProps.data,
    })
  }

  render(){
    let renderProblems = this.state.answer.map((v, i) =>
      <SearchItem key={i} problem={v.description} answer={v.reply} id={v.problem_id}/>
    );
    let header = (this.state.answer.length) ? <Card.Header> Ответы: </Card.Header>: null;

    return(
      <div>
        {header}
        {renderProblems}
      </div>
    )
  }

}

export default Results;
