from playwright.sync_api import APIRequestContext

from utils.yaml_parser import load_test_data


def test_query_media_anime(gql_query: APIRequestContext) -> None:
    
    """
    A simple example test case against the Media resolver. Only fetches some Media, and asserts against
    the expected payload
    """


    # Get the request payload from the test data
    #TODO try the grapql_query python package to see if you can make this more flexible
    payload = load_test_data("/graphql/query_media.yaml")[0]["payload"]
    variables = load_test_data("/graphql/query_media.yaml")[0]["variables"]


    query = gql_query.post("/", data={"query": payload, "variables":variables})
    assert query.ok

    expected = load_test_data("/graphql/query_media.yaml")[0]["response"]
    #Validate response values from test data file against input
    assert query.json() == expected
