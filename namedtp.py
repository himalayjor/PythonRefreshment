from collections import namedtuple
import json

ForceAlignManifestRecord = namedtuple('ForceAlignManifest', ['corpus_file', 'audio_file', 'language',
                                                             'feature_cache_location', 'frequency', 'domain'])

xx = ForceAlignManifestRecord(corpus_file="cor",
                              audio_file="aud",
                              language="lang",
                              feature_cache_location="feat_cac_loc",
                              frequency="freq",
                              domain="dom")

print(json.dumps(xx._asdict()))