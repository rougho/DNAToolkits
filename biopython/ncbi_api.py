import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote_plus
import xmltodict
import json


# Global session object
session = requests.Session()

# Cache for storing responses
response_cache = {}


def get_data(url):
    # Check if the response is cached
    if url in response_cache:
        return response_cache[url]

    response = session.get(url)
    if response.status_code == 200:
        # Cache the response
        response_cache[url] = response.text
        return response.text
    else:
        return None


def convert_xml_to_dict(xml_data):
    try:
        # Parse XML and convert to dictionary
        dict_data = xmltodict.parse(xml_data)
        return dict_data
    except Exception as e:
        print(f"Error: {e}")
        return None


def extract_ids(search_term, database='nuccore'):
    encoded_search_term = quote_plus(search_term)
    base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    search_url = f'{base_url}esearch.fcgi?db=nuccore&term={encoded_search_term}&retmode=xml'
    response = requests.get(search_url)
    root = ET.fromstring(response.content)
    ids = []
    for id_elem in root.findall('.//IdList/Id'):
        ids.append(id_elem.text)
    return ids


def extract_ids_summery(IDs, database='nuccore'):
    baseUrls = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    urls = []
    for id in IDs:
        summary = f'{baseUrls}esummary.fcgi?db={database}&id={id}'
        urls.append(summary)
    return urls


def get_AccessionVersion(dictResponse):
    accessionVersions = []
    for response_key, response_value in dictResponse.items():
        items = response_value['eSummaryResult']['DocSum']['Item']

        for item in items:
            if item['@Name'] == 'AccessionVersion' and '#text' in item:
                accessionVersions.append(item['#text'])
    return accessionVersions


def api_call(term, database):
    # Check if the response for this term is cached
    cache_key = f"{term}_{database}"
    if cache_key in response_cache:
        return response_cache[cache_key]

    IDs = extract_ids(term, database)
    urls = extract_ids_summery(IDs, database)
    dictResponse = {}
    for i, url in enumerate(urls):
        xml_data = get_data(url)
        if xml_data:
            dict_data = convert_xml_to_dict(xml_data)
            if dict_data:
                # Using the URL or another unique identifier as the key
                dictResponse[f'response_{i+1}'] = dict_data

    accessionVersions = get_AccessionVersion(dictResponse)
    # Cache the final result
    response_cache[cache_key] = accessionVersions
    return accessionVersions


def extract_fasta(term, database):
    baseUrl = 'https://www.ncbi.nlm.nih.gov/'
    accessionVersions = api_call(term, database)
    fasta = []
    for accVer in accessionVersions:
        temp = f'{baseUrl}{term}/{accVer}?report=fasta&log$=seqview&format=text'
        fasta.append(get_data(temp))
        print(get_data(temp))
    return fasta
