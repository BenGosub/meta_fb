import React, { Component } from 'react';
import { Select } from 'rebass';

class SelectPeriod extends Component {
	render() {
		return(
			<Select
			  label="Период за анализа"
			  name="select_period"
			  options={[{children: 'Една Седмица', value: 7}, {children: 'Две Седмици', value: 14}, {children: 'Еден Месец', value: 31}]}
			  rounded={true}
			  width={50}
			>
			</Select>
		);
	}
}

export default SelectPeriod