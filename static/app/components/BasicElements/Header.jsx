import React, { Component } from 'react';
import { PageHeader } from 'rebass';

class Header extends Component {
	render() {
		return (
			<PageHeader
				description="Слободно превземање и визуeлизација на податоци од Фејсбук профили на политичари и партии."
				heading="Мета ФБ"
				style={{"margin" : 10}}
			>
			</PageHeader>
		);
	}
}
export default Header