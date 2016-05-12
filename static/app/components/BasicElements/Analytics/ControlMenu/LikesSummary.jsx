import React, { Component } from 'react';
import { Heading, Stat, Divider } from 'rebass';
import { Flex } from 'reflexbox';

class LikesSummary extends Component {
	render() {
		return(
			<div>
				<Heading>Статистика за избраниот период.</Heading>
				<Flex align="center" justify='space-between' wrap={true}>
					<Stat
						label="Промена на допаѓања"
						unit="↑"
						value={this.props.likesChange}
					/>
					<Stat 
						label="Вкупно допаѓања"
						value={this.props.likesNow}
					/>
					<Stat 
						label="Вкупно допаѓања на почетокот на селектираниот период"
						value={this.props.likesBefore}
					/>
					<Stat 
						label="Процентуална промена на допаѓања"
						value={this.props.likesPercentageChange}
					/>
				</Flex>
				<Divider />
			</div>
		);
	}
}

export default LikesSummary