import React, { Component } from 'react';
import { Divider, Heading } from 'rebass';

class FbPost extends Component {

	constructor() {
		super();
	}

	render() {
		return(
			<div>
				<Divider />
				<Heading
					level={3}
					>
					Најпопуларен пост
				</Heading>
				<Divider />
				<div className="fb-post" data-href={this.props.link}></div>
			</div>
		);
	}
}

export default FbPost