# -*- coding:utf-8 -*-

import requests
import json


if __name__ == '__main__':

    def _replace(s):
        return s.replace('$$', '$').replace('<span x-underline="">', '<span style="text-decoration: underline;">')

    def replace(body, explanation, answer, options):
        body = _replace(body)
        explanation = _replace(explanation)
        new_answer = []
        for s in answer:
            new_answer.append(_replace(s))
        new_options = []
        for o in options:
            new_options.append(_replace(o))
        return body, explanation, new_answer, new_options

    def check(origin):
        for r in origin:
            if r['question_type'] == 'correction':
                continue
            r['body'], r['explanation'], r['answer'], r['options'] = replace(
                r['body'], r['explanation'], r['answer'], r['options']
            )
            if r['subs']:
                for s in r['subs']:
                    s['body'], s['explanation'], s['answer'], s['options'] = replace(
                        s['body'], s['explanation'], s['answer'], s['options']
                    )
        return origin

    import requests
    import json
    res = requests.get('http://ai.alexwang.cc/api/exam/z/edit?exam_uid=9b64f5e50').json()
    q = res['data']['origin']
    print(q)
    print(check(q))
