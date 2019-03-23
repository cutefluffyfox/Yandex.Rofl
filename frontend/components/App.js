import React from "react";

class App extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      title: "Hello, World!",
    }
  }

  render(){
    return(
      <div>
        <h3>{ this.state.title }</h3>
      </div>
    );
  }
};

export default App;
