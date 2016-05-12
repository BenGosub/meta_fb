import React, { Component } from 'react';
import { Table, Heading } from 'rebass';

class TopLinks extends Component {
	render() {
		return(
			<div>
				<Heading> Најчесто споделувани линкови во периодот.</Heading>	
				<Table
					headings={['Линк']}
					data={[['link1', 'link2', 'link3']]}
				/>
			</div>
		)
	}
}

export default TopLinks