import React, { Component } from 'react';
import Menu from './BasicElements/Menu';
import Analytics from './BasicElements/Analytics/Analytics';


class Main extends Component {

    render() {
        return(
            <div>
                <Menu/>
                <Analytics />
            </div>
        );
    }
}

export default Main