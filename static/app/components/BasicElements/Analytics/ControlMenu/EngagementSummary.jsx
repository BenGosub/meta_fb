import React, { Component } from 'react';
import { Heading, Stat, Divider } from 'rebass';
import { Flex } from 'reflexbox';

class EngagementSummary extends Component {
	render() {
		return(
			<div>
				<Heading>Сумарни статистики за ангажираноста на постовите во избраниот период.</Heading>
				<Flex align="center" justify='space-between' wrap={true}>
					<Stat
						label="Ангажираност"
						value={this.props.engagement}
					/>
					<Stat 
						label="Коментари"
						value={this.props.comments}
					/>
					<Stat 
						label="Допаѓања"
						value={this.props.likes}
					/>
					<Stat 
						label="Споделувања"
						value={this.props.shares}
					/>
				</Flex>
				<Divider />
			</div>
		)
	}
}

export default EngagementSummary