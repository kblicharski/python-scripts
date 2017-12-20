import string

letterGoodness = dict(zip(string.ascii_uppercase,
                            [.0817,.0149,.0278,.0425,.1270,.0223,.0202,
                                                         .0609,.0697,.0015,.0077,.0402,.0241,.0675,
                                                                                  .0751,.0193,.0009,.0599,.0633,.0906,.0276,
                                                                                                           .0098,.0236,.0015,.0197,.0007]))

                            trans_tables = [ string.maketrans(string.ascii_uppercase,
                                                 string.ascii_uppercase[i:]+string.ascii_uppercase[:i])
                                                                  for i in range(26)]

                            def goodness(msg):
                                    return sum(letterGoodness.get(char, 0) for char in msg)

                                def all_shifts(msg):
                                        msg = msg.upper()
                                            for trans_table in trans_tables:
                                                        txt = msg.translate(trans_table)
                                                                yield goodness(txt), txt

                                                                encrypted_string = codes[0]
                                                                print(max(all_shifts(encrypted_string)))
