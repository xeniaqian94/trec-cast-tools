import json


def convert_to_jsonl(doc_id, passages):
    '''
    This is the method to convert to jsonl format for passages,
    = add_passage_ids() + convert_to_trecweb(), actually writes to JSONL format.
    psg_id norm = 0-based

    '''

    passage_number = 0
    passage_splits = ''
    content = ''

    for passage in passages:
        passage_dict = {'id': str(doc_id) + '-' + str(passage['id']), 'contents': passage["body"].replace("\n", " ")}
        content += json.dumps(passage_dict) + '\n'

    return content


def convert_to_doc_jsonl(idx, url, title, body, augmented=True):
    if augmented:
        doc_dict = {'id': str(idx),
                    'contents': url.replace("\n", " ") + " " + title.replace("\n", " ") + " " + body.replace("\n", " ")}
    else:
        doc_dict = {'id': str(idx), 'contents': body.replace("\n", " ")}
    content = json.dumps(doc_dict) + "\n"
    return content


def convert_to_trecweb(passage_id, doc_title, doc_body, doc_url):
    '''
    Takes a document with passage spilts and converts it to trecweb format
    '''
    content = '<DOC>\n'
    content += '<DOCNO>'
    content += passage_id
    content += '</DOCNO>\n'
    content += '<DOCHDR>\n'
    # content += '\n'
    content += '</DOCHDR>\n'
    content += '<HTML>\n'
    content += '<TITLE>'
    content += doc_title
    content += '</TITLE>\n'
    content += '<URL>'
    content += doc_url
    content += '</URL>\n'
    content += '<BODY>\n'
    content += doc_body
    # content += '\n'
    content += '</BODY>\n'
    content += '</HTML>\n'
    content += '</DOC>\n'
    content += '\n'

    return content


def add_passage_ids(passages):
    passage_number = 0
    passage_splits = ''

    for passage in passages:
        passage_splits += '<passage id={}>\n'.format(passage["id"])
        passage_splits += passage["body"] + '\n'
        passage_splits += '</passage>\n'
        passage_number += 1

    return passage_splits
