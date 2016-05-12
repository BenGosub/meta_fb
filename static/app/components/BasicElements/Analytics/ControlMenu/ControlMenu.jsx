import React, { Component } from 'react';
import SelectPeriod from './SelectPeriod';
import { Button, Divider } from 'rebass';
import RightAnalysis from './RightAnalysis';
import LeftAnalysis from './LeftAnalysis';
var data = require('json!./data.json');
import FullTable from './FullTable';
import SelectParty from './SelectParty';

class ControlMenu extends Component {
    render() {

        var Table = Reactable.Table
        var tableData = {}
        tableData.table = data.table

        var selectMenu = {}
        selectMenu.data = data.select_menu

        return(
            <div>
                <div > 
                    <SelectPeriod />
                    <SelectParty data={ data }/>
                    
                </div>    

                <div >
                    
                    <FullTable {...tableData}/>
                </div>
            </div>
        );
    }
}

export default ControlMenu
