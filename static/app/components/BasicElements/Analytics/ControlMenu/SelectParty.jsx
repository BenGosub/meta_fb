import React, { Component } from 'react';
import { Select } from 'rebass';
import LeftAnalysis from './LeftAnalysis';
import RightAnalysis from './RightAnalysis';


class SelectParty extends Component {
	constructor() {
		super();
		this.state = {
			leftValue: 4,
			rightValue: 4
		}
		this.handleChange = this.handleChange.bind(this)
	}

	handleChange(event) {
		if (event.target.name == 'leftSelectPeriod') {
			this.setState({leftValue: event.target.value});
			if (this.props.sendSelection) {
				this.props.sendSelection(this.state.leftValue);
				
			}
		}

		if (event.target.name == 'rightSelectPeriod') {
			this.setState({rightValue: event.target.value});
			if (this.props.sendSelection) {
				this.props.sendSelection(this.state.rightValue);
				
			}
		}
	}
	
	render() {
			
		var leftSelectionState = this.state.leftValue;
		var rightSelectionState = this.state.rightValue;

		var i;
		let analysisData = this.props.data.analysis;

		for (i = 0; i < analysisData.length; i++) {
			if (leftSelectionState == analysisData[i].value) {
				var leftAnalysisState = analysisData[i]
			}

			if (rightSelectionState == analysisData[i].value) {
				var rightAnalysisState = analysisData[i]
			}
		}
		
		return(
			<div>
				<div className="selectors">
						<Select
						  label="Одбери Партија/Политичар"
						  name="leftSelectPeriod"
						  options={ this.props.data.select_menu.menu } 
						  rounded={ true }
						  defaultValue={ this.state.leftValue }
						  onChange={ this.handleChange }
						>
						</Select>

						<Select
						  label="Одбери Партија/Политичар"
						  name="rightSelectPeriod"
						  options={ this.props.data.select_menu.menu } 
						  rounded={ true }
						  defaultValue={ this.state.rightValue }
						  onChange={ this.handleChange }
						>
						</Select>	
				</div>

				<LeftAnalysis data={ leftAnalysisState } selectState={ this.state.leftValue } otherState={ this.state.rightValue } />
				<RightAnalysis data={ rightAnalysisState } selectState={ this.state.rightValue } otherState={ this.state.leftValue } />
			</div>
		);
	}
}

export default SelectParty