import React, { Component } from 'react';
import { Menu, NavItem } from 'rebass';

class PeriodMenu extends Component {
	render() {
		return(
			<Menu rounded={true}>
			  <NavItem is="a">
			    Menu
			  </NavItem>
			  <NavItem is="a">
			    NavItem
			  </NavItem>
			  <NavItem is="a">
			    NavItem
			  </NavItem>
			</Menu>
		)
	}
}

export default PeriodMenu