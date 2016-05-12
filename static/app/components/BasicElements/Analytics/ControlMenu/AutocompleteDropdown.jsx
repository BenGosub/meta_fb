import React, { Component } from 'react';
import Autosuggest from 'react-autosuggest';
import theme from './autosuggestTheme.css';

const searchItems = [
	{name: 'ВМРО'},
	{name: 'СДСМ'}
];

function escapeRegexCharacters(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function getSuggestions(value) {
  const escapedValue = escapeRegexCharacters(value.trim());
  
  if (escapedValue === '') {
    return [];
  }

  const regex = new RegExp('^' + escapedValue, 'i');

  return searchItems.filter(searchItem => regex.test(searchItem.name));
}

function getSuggestionValue(suggestion) {
  return suggestion.name;
}

function renderSuggestion(suggestion) {
  return (
    <span>{suggestion.name}</span>
  );
}

class AutocompleteDropdown extends Component {

	constructor() {
    	super();

    	this.state = {
    		value: '',
    		suggestions: getSuggestions('')
    	};

    	this.onChange = this.onChange.bind(this);
    	this.onSuggestionsUpdateRequested = this.onSuggestionsUpdateRequested.bind(this);
	}

	onChange(event, { newValue, method }) {
		this.setState({
		  value: newValue
		});
	}

	onSuggestionsUpdateRequested({ value }) {
		this.setState({
		  suggestions: getSuggestions(value)
		});
	}

	render() {

	    const { value, suggestions } = this.state;
	    const inputProps = {
	      placeholder: "Внеси име на Парија или Политичар",
	      value,
	      onChange: this.onChange
	    };
				
		return(
			<Autosuggest suggestions={suggestions}
					   theme={theme}
			           onSuggestionsUpdateRequested={this.onSuggestionsUpdateRequested}
			           getSuggestionValue={getSuggestionValue}
			           renderSuggestion={renderSuggestion}
			           inputProps={inputProps} />
		);
	}
}

export default AutocompleteDropdown