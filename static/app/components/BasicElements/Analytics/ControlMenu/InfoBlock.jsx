import React, { Component } from 'react';
import { Block, Media, Heading, Text } from 'rebass';

class InfoBlock extends Component {
	constructor() {
		super();
	}

	render() {
		return(
			<Block
			  borderLeft={true}
			  color="blue"
			  px={2}
			>
				<Media img={this.props.image}>
					<Heading
						level={2}
						size={0}>
						{this.props.name}
					</Heading>
					<Text>
						<a href={this.props.link} target="_blank">Линк до профилот</a>
					</Text>
				</Media>
			</Block>
		);
	}
}

export default InfoBlock

				// <Media img="http://placehold.it/128/08e/fff">
				// 	<Heading
				// 		level={2}
				// 		size={0}>
				// 	</Heading>
				// 	<Text>
				// 		Линк до профилот 
				// 		<a href={this.props.link}>
				// 		</a>
				// 	</Text>
				// </Media >