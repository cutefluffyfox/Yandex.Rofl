import React from "react";
import {Card, Button, Popover} from "react-bootstrap";
import SearchItem from "./SearchItem";



class Results extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      answer: this.props.data,
      found: this.props.found,
    };
    this.find = this.find.bind(this);
  }

  find(text){
    this.state.found.split(' ').forEach(v => {
      text = text.replace(v, '<span style="background: #E2FF16">' + v + '</span>')
    });
    return text
  }

  componentWillReceiveProps(nextProps){
    this.setState({
      answer: nextProps.data,
      found: nextProps.found,
    })
  }

  render(){
    let renderProblems = this.state.answer.map((v, i) =>
      <SearchItem key={i} problem={this.find(v.description)} answer={this.find(v.reply)} id={v.problem_id} mem={this.find(v.CALLBACKMEMO)} />
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
