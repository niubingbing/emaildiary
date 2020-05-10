import {ApolloClient} from 'apollo-client'
import {HttpLink} from 'apollo-link-http'
import {InMemoryCache} from 'apollo-cache-inmemory'
import VueApollo from 'vue-apollo'
import {ApolloLink} from 'apollo-link'
import Vue from "vue"


Vue.use(VueApollo);

//设置 header,设置 Authorization
const middlewareLink = new ApolloLink((operation, forward) => {
    const token = localStorage.getItem('token');
    operation.setContext({
        headers: {
            Authorization: `JWT ${token}` || null
        }
    });
    return forward(operation);
})

const httpLink = new HttpLink({
    uri: 'http://emaildiary.net:8000/graphql',
});

const apolloClient = new ApolloClient({
    link: middlewareLink.concat(httpLink),
    cache: new InMemoryCache(),
    connectToDevTools: true,
});

const apolloProvider = new VueApollo({
    defaultClient: apolloClient,
    clients: {default: apolloClient},
});

export default apolloProvider;
