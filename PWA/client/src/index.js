import React from 'react';
import ReactDOM from 'react-dom';

import { ApolloProvider, ApolloClient, InMemoryCache } from '@apollo/client'
import Auth from "./Auth";
import App from "./App";

const client = new ApolloClient({
    uri: 'http://localhost:5000',
    cache: new InMemoryCache()
})

ReactDOM.render(
    <ApolloProvider client={client}>
        <Auth />
    </ApolloProvider>,
  document.getElementById('root')
);
