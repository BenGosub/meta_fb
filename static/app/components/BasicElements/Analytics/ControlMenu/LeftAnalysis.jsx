import React, { Component } from 'react';
import LikesSummary from './LikesSummary';
import FbPost from './FbPost'
import AutocompleteDropdown from './AutocompleteDropdown';
import EngagementSummary from './EngagementSummary';
import TopLinks from './TopLinks';

class LeftAnalysis extends Component {

	render() {
		var width;
		if (this.props.otherState == 4) {
			width = "100%"
		} else {
			width = "49.5%"
		}

		var leftAnalysis;
		if (this.props.selectState != 4) {
			leftAnalysis = 
				<div className="leftContainer" style={{"width" : width, "float" : "left"}}>
					<LikesSummary className="leftStats"  likesBefore={this.props.data.likesSummary.likesBefore}
						likesNow={this.props.data.likesSummary.likesNow}
						likesChange={this.props.data.likesSummary.likesChange}
						likesPercentageChange={this.props.data.likesSummary.likesPercentageChange}
					/>
					<EngagementSummary comments={this.props.data.engagementSummary.comments}
						engagement={this.props.data.engagementSummary.engagement}
						likes={this.props.data.engagementSummary.likes}
						shares={this.props.data.engagementSummary.shares}

					/>
					
					<FbPost link={this.props.data.mostPopularLink.link}

						name={this.props.data.mostPopularLink.className}
					 />
					<TopLinks />
				</div>
		} else {
			leftAnalysis = null
		}


		return(
			<div>
				{leftAnalysis}
			</div>
		);
	}
}

export default LeftAnalysis