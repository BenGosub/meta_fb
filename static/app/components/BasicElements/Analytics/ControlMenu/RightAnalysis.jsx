import React, { Component } from 'react';
import SelectParty from './SelectParty';
import LikesSummary from "./LikesSummary";
import FbPost from "./FbPost";
import EngagementSummary from './EngagementSummary';
import TopLinks from './TopLinks';

class RightAnalysis extends Component {
	render() {
		
		var width;
		if (this.props.otherState == 4) {
			width = "100%"
		} else {
			width = "49.5%"
		}

		var rightAnalysis;
		if (this.props.selectState != 4) {
			rightAnalysis = 
				<div className="rightContainer" style={{"width" : width, "float" : "right"}}>
					<LikesSummary className="rightStats"  likesBefore={this.props.data.likesSummary.likesBefore}
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
			rightAnalysis = null
		}

		return(
			<div>
				{rightAnalysis}
			</div>
			
		);
	}
}

export default RightAnalysis