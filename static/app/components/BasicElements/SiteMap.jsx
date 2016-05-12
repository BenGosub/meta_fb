import React, { Component } from 'react';
import { Button, Space } from 'rebass';

class SiteMap extends Component {
	render() {
			return(
				<div>
					<Button
						backgroundColor="primary"
    					color="white"
					    inverted={true}
					    rounded={true}
					    href={"/"}
					>
						Дома
					</Button>
					<Space x={1} />
					<Button
						backgroundColor="primary"
    					color="white"
					    inverted={true}
					    rounded={true}
					    href={"/zanas"}
					>
						За Нас
					</Button>
				</div>
			);
	}
}

export default SiteMap