"use strict"

import React, { Component } from 'react';
import ControlMenu from './ControlMenu/ControlMenu';
import SummaryChart from './SummaryChart'; 

class Analytics extends Component {

    render() {
        return(
            <div>
                <ControlMenu />
            </div>
        );
    }
}

export default Analytics