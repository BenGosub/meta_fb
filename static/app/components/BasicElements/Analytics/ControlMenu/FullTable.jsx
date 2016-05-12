import React, { Component } from 'react';
import Reactable from 'reactable';
import { Panel, PanelHeader, PanelFooter, Divider } from 'rebass';

class FullTable extends Component {
	render() {
		var Table = Reactable.Table

		var dataTable = this.props
		var tableOne = [{'key' : 'page_name', 'label' : 'Име'},
						{'key' : 'profile_likes', 'label' : 'Вкупно допаѓања'},
						{'key' : 'profile_likes_change', 'label' : 'Промена на допаѓања во периодот'},
						{'key' : 'post_engagement', 'label' : 'Вкупно Ангажираност'},
						{'key' : 'post_likes', 'label' : 'Допаѓања на написи'},
						{'key' : 'post_comments', 'label' : 'Коментари на написи'}
					]
		var tableTwo = [
						{'key' : 'page_name', 'label' : 'Име'},
						{'key' : 'post_shares', 'label' : 'Вкупно споделени написи'},
						{'key' : 'comment_authors', 'label' : 'Вкупно автори на коментари'},
						{'key' : 'total_links_shared', 'label' : 'Вкупно споделени линкови'},
						{'key' : 'fb_links', 'label' : 'Вкупно споделени линкови од Фејсбук'},
						{'key' : 'non_fb_links', 'label' : 'Вкупно споделени линкови надвор од Фејсбук'},
					]

		return(
			<Panel theme="info">
			  <PanelHeader
			    inverted={false}
			    theme="default"
			  >
			    Табела со статистики за сите Партии/Политичари во одбраниот период.
			  </PanelHeader>
			 	<Table className='table' sortable={true} data={this.props.table} columns={tableOne} >
				</Table>
				<Divider />
				<Table className='table' sortable={true} data={this.props.table} columns={tableTwo} >
				</Table>
			  <PanelFooter theme="default">
			    Кликни на името на колоната за сортирање.
			  </PanelFooter>
			</Panel>

				
		);
	}
}

export default FullTable
