## Autograder Output
============================= test session starts ==============================

    collecting ... collected 11 items
    
    source/tests.py::test_problem_1 
    FAILED
    source/tests.py::test_problem_2 FAILED
    source/tests.py::test_problem_3 FAILED
    source/tests.py::test_problem_4 FAILED
    source/tests.py::test_problem_5 FAILED
    source/tests.py::test_problem_6 FAILED
    source/tests.py::test_problem_7 FAILED
    source/tests.py::test_problem_8 FAILED
    source/tests.py::test_problem_9 FAILED
    source/tests.py::test_problem_10 FAILED
    source/tests.py::test_problem_11 FAILED
    
    =================================== FAILURES ===================================
    ________________________________ test_problem_1 ________________________________
    
    problem = Problem(artifacts=None, input={'password': 'c1c0efe26c5d0d9c47de46e06275b6b9', 'salt': '557b55664bb39303eb4c1e390618fcfd'}, output='1234567890', reference='17dbc2eebd64cea21e2d90eca2e7e959b9e7b6dc60a4c51cf36633afe9ef6238')
    
        @weight(name="problem 1", worth=1)
        def test_problem_1(problem: Problem):
    >       assert problem.output == problem.reference
    E       AssertionError: assert '1234567890' == '17dbc2eebd64cea21e2d90eca2e7e959b9e7b6dc60a4c51cf36633afe9ef6238'
    E         - 17dbc2eebd64cea21e2d90eca2e7e959b9e7b6dc60a4c51cf36633afe9ef6238
    E         + 1234567890
    
    source/tests.py:6: AssertionError
    ________________________________ test_problem_2 ________________________________
    
    problem = Problem(artifacts=None, input='824fdc7e390ed6e5d187c0c4422f68cc3954a35648264c937e64a642a67f2467', output='1234567890',...50d297ad723afbf528db'], 'mac': 'ad9aabaa1b76b3984511b57f2316a184', 'search_terms': '73e1fe81b9f6f95f9e690e5a832119e0'})
    
        @weight(name="problem 2", worth=1)
        def test_problem_2(problem: Problem):
    >       assert problem.output == problem.reference
    E       AssertionError: assert '1234567890' == {'feistel': ['66b45d3adad350269ce6836b8d2f60e1',\n             '668a3d3dec65a223ca888ebad0f43ece',\n             'c904c85881007d8a5245bba5281b274b',\n             '6e2d53aff49850d297ad723afbf528db'],\n 'mac': 'ad9aabaa1b76b3984511b57f2316a184',\n 'search_terms': '73e1fe81b9f6f95f9e690e5a832119e0',\n 'validator': 'e3cde8f1a59dd9a6befafdeb62423aa2'}
    E         +'1234567890'
    E         -{'validator': 'e3cde8f1a59dd9a6befafdeb62423aa2', 'feistel': ['66b45d3adad350269ce6836b8d2f60e1', '668a3d3dec65a223ca888ebad0f43ece', 'c904c85881007d8a5245bba5281b274b', '6e2d53aff49850d297ad723afbf528db'], 'mac': 'ad9aabaa1b76b3984511b57f2316a184', 'search_terms': '73e1fe81b9f6f95f9e690e5a832119e0'}
    
    source/tests.py:11: AssertionError
    ________________________________ test_problem_3 ________________________________
    
    problem = Problem(artifacts=None, input={'key': 'ec5866e721e271f94809c91cc0d31e22', 'data': 'e0bcbab8d264fce468b0f79fbc438a3767c...4fce468b0f79fbc438a37d2f5adff94757cb1b6d6a47dabd252493ce251ccb7151fc5fc5ce9c8aa19ef86c6aee3e047ae41f647cfce0fcb7bb59c')
    
        @weight(name="problem 3", worth=1)
        def test_problem_3(problem: Problem):
    >       assert problem.output == problem.reference
    E       AssertionError: assert None == 'e0bcbab8d264fce468b0f79fbc438a37d2f5adff94757cb1b6d6a47dabd252493ce251ccb7151fc5fc5ce9c8aa19ef86c6aee3e047ae41f647cfce0fcb7bb59c'
    E         +None
    E         -'e0bcbab8d264fce468b0f79fbc438a37d2f5adff94757cb1b6d6a47dabd252493ce251ccb7151fc5fc5ce9c8aa19ef86c6aee3e047ae41f647cfce0fcb7bb59c'
    
    source/tests.py:16: AssertionError
    ________________________________ test_problem_4 ________________________________
    
    problem = Problem(artifacts=None, input={'key': 'e00ff9c9a831a1226d4f9e5215aec7b6', 'data': '4edd7417f52579b081dfca17d88de76901d...1d5194d1bb2d8add521c401dd0d03e4258d841894f80f212ebd45ab46b64f70234935febdb9c353d9f21a7a9bbbd87257244c7982e630204338c9')
    
        @weight(name="problem 4", worth=1)
        def test_problem_4(problem: Problem):
    >       assert problem.output == problem.reference
    E       AssertionError: assert '1234567890' == '9d26dab03e11d5194d1bb2d8add521c401dd0d03e4258d841894f80f212ebd45ab46b64f70234935febdb9c353d9f21a7a9bbbd87257244c7982e630204338c9'
    E         - 9d26dab03e11d5194d1bb2d8add521c401dd0d03e4258d841894f80f212ebd45ab46b64f70234935febdb9c353d9f21a7a9bbbd87257244c7982e630204338c9
    E         + 1234567890
    
    source/tests.py:21: AssertionError
    ________________________________ test_problem_5 ________________________________
    
    problem = Problem(artifacts=None, input={'keys': ['c45a73ce279460bae465a2b1b0ffe2f4', '3984ccc6677e50f6c84ff63c2befcdb4', '736bd...c956e1c8f23801e1a7b84a520e6cb0e227dfb6a0c990491590827e90397a4faa66d7c588d24ab9de7f7e7e6ccf7a8d90b1d0c62eaa19d46596a5c')
    
        @weight(name="problem 5", worth=1)
        def test_problem_5(problem: Problem):
    >       assert problem.output == problem.reference
    E       AssertionError: assert '1234567890' == 'e67a4cb751ac956e1c8f23801e1a7b84a520e6cb0e227dfb6a0c990491590827e90397a4faa66d7c588d24ab9de7f7e7e6ccf7a8d90b1d0c62eaa19d46596a5c'
    E         - e67a4cb751ac956e1c8f23801e1a7b84a520e6cb0e227dfb6a0c990491590827e90397a4faa66d7c588d24ab9de7f7e7e6ccf7a8d90b1d0c62eaa19d46596a5c
    E         + 1234567890
    
    source/tests.py:26: AssertionError
    ________________________________ test_problem_6 ________________________________
    
    problem = Problem(artifacts=None, input={'keys': ['9c4d2d32ac65b96d57439979839260bd', '87b9289611b93f22af5523671a7ef8a6', '12d3a...a1e538a00a98e777e71e0857b0009dc5bfb5e906c3570d2bcdd1c0f77d45fc793ca07bb35c49c8f182a178ae1dfb8572c58eedc81a17c3e66e16c')
    
        @weight(name="problem 6", worth=1)
        def test_problem_6(problem: Problem):
    >       assert problem.output == problem.reference
    E       AssertionError: assert '1234567890' == '6bfaec8975ba1e538a00a98e777e71e0857b0009dc5bfb5e906c3570d2bcdd1c0f77d45fc793ca07bb35c49c8f182a178ae1dfb8572c58eedc81a17c3e66e16c'
    E         - 6bfaec8975ba1e538a00a98e777e71e0857b0009dc5bfb5e906c3570d2bcdd1c0f77d45fc793ca07bb35c49c8f182a178ae1dfb8572c58eedc81a17c3e66e16c
    E         + 1234567890
    
    source/tests.py:31: AssertionError
    ________________________________ test_problem_7 ________________________________
    
    problem = Problem(artifacts=None, input={'key': '2ca6f8c45d3557317d7b6477907f8dad', 'data': '764bc021be90879ef513e255a0c7067c861...10b45f02ee59149ee'}, output='1234567890', reference='56022a0f9c8282e9879d37e83044a8fac96a3b55fe250d5d0a101cdc7cc7abef')
    
        @weight(name="problem 7", worth=1)
        def test_problem_7(problem: Problem):
    >       assert problem.output == problem.reference
    E       AssertionError: assert '1234567890' == '56022a0f9c8282e9879d37e83044a8fac96a3b55fe250d5d0a101cdc7cc7abef'
    E         - 56022a0f9c8282e9879d37e83044a8fac96a3b55fe250d5d0a101cdc7cc7abef
    E         + 1234567890
    
    source/tests.py:36: AssertionError
    ________________________________ test_problem_8 ________________________________
    
    problem = Problem(artifacts=None, input=':sObuoXcPMO7a\n  \t)XqFi8MyGgPmDToJ89HeM\x0b\x0c+rEyaWjvV?\t \t\n}5ycTZ1L\n\n$x2OCfx0L4...reference=['0OJxRvU4V', '1krPQmv53', '5ycTZ1L', '7f55', 'VqSOx3q', 'df7s2em', 'rEyaWjvV', 'sObuoXcPMO7a', 'x2OCfx0L4'])
    
        @weight(name="problem 8", worth=1)
        def test_problem_8(problem: Problem):
    >       assert set(problem.output) == set(problem.reference)
    E       AssertionError: assert {'9', '0', '1', '4', '7', '8', '2', '6', '3', '5'} == {'0OJxRvU4V',\n '1krPQmv53',\n '5ycTZ1L',\n '7f55',\n 'VqSOx3q',\n 'df7s2em',\n 'rEyaWjvV',\n 'sObuoXcPMO7a',\n 'x2OCfx0L4'}
    E         Extra items in the left set:
    E         '9'
    E         '0'
    E         '1'
    E         '4'
    E         '7'
    E         '8'
    E         '2'
    E         '6'
    E         '3'
    E         '5'
    E         Extra items in the right set:
    E         '1krPQmv53'
    E         'x2OCfx0L4'
    E         '7f55'
    E         'rEyaWjvV'
    E         'sObuoXcPMO7a'
    E         '0OJxRvU4V'
    E         'VqSOx3q'
    E         '5ycTZ1L'
    E         'df7s2em'
    E         Full diff:
    E           {
    E         -  '0OJxRvU4V',
    E         -  '1krPQmv53',
    E         -  '5ycTZ1L',
    E         +  '0',
    E         +  '1',
    E         +  '2',
    E         +  '3',
    E         +  '4',
    E         -  '7f55',
    E         ?   ---
    E         +  '5',
    E         +  '6',
    E         +  '7',
    E         +  '8',
    E         +  '9',
    E         -  'VqSOx3q',
    E         -  'df7s2em',
    E         -  'rEyaWjvV',
    E         -  'sObuoXcPMO7a',
    E         -  'x2OCfx0L4',
    E           }
    
    source/tests.py:41: AssertionError
    ________________________________ test_problem_9 ________________________________
    
    problem = Problem(artifacts=None, input='PSC6YJz1gkY {1G𝩊k5A𑱒Hr5IKo3,\x0c\r\x0b=gJqCwsLtb<\n \r{BBPU24ldrp2juz3ZDUMQ$\x0b\t \r.t...Y', 'Z6ූN౨7Bq︴x', 'aLXE𖾔𖩦DO7p8', 'd0Cpk', 'f_DlJR', 'gJqCwsLtb', 'tgzQ', 'wUnD', 'z0zA', 'zse𐐖fQ𑑔88dx', '󠆨eᾮaSaoE້qC'])
    
        @weight(name="problem 9", worth=1)
        def test_problem_9(problem: Problem):
    >       assert set(problem.output) == set(problem.reference)
    E       AssertionError: assert {'9', '0', '1', '4', '7', '8', '2', '6', '3', '5'} == {'0Kdm﹏sHP',\n '0bpNJｐ3',\n '4P6Ls0Wcw',\n '7yv62wN',\n '975uWASaQ',\n 'E516Bmb',\n 'E5MaLoLBdRUY',\n 'ImූvᶽCxЎF𓐀Iǲ',\n 'NiK2X7Rrx',\n 'PSC6YJz1gkY',\n 'Z6ූN౨7Bq︴x',\n 'aLXE𖾔𖩦DO7p8',\n 'd0Cpk',\n 'f_DlJR',\n 'gJqCwsLtb',\n 'tgzQ',\n 'wUnD',\n 'z0zA',\n 'zse𐐖fQ𑑔88dx',\n '󠆨eᾮaSaoE້qC'}
    E         Extra items in the left set:
    E         '9'
    E         '0'
    E         '1'
    E         '4'
    E         '7'
    E         '8'
    E         '2'
    E         '6'
    E         '3'
    E         '5'
    E         Extra items in the right set:
    E         '0bpNJｐ3'
    E         'z0zA'
    E         '975uWASaQ'
    E         '󠆨eᾮaSaoE້qC'
    E         'ImූvᶽCxЎF𓐀Iǲ'
    E         'NiK2X7Rrx'
    E         '4P6Ls0Wcw'
    E         'aLXE𖾔𖩦DO7p8'
    E         'zse𐐖fQ𑑔88dx'
    E         'PSC6YJz1gkY'
    E         'gJqCwsLtb'
    E         'wUnD'
    E         'tgzQ'
    E         '0Kdm﹏sHP'
    E         '7yv62wN'
    E         'E5MaLoLBdRUY'
    E         'E516Bmb'
    E         'f_DlJR'
    E         'Z6ූN౨7Bq︴x'
    E         'd0Cpk'
    E         Full diff:
    E           {
    E         -  '0Kdm﹏sHP',
    E         -  '0bpNJｐ3',
    E         -  '4P6Ls0Wcw',
    E         -  '7yv62wN',
    E         -  '975uWASaQ',
    E         -  'E516Bmb',
    E         -  'E5MaLoLBdRUY',
    E         -  'ImූvᶽCxЎF𓐀Iǲ',
    E         -  'NiK2X7Rrx',
    E         -  'PSC6YJz1gkY',
    E         -  'Z6ූN౨7Bq︴x',
    E         -  'aLXE𖾔𖩦DO7p8',
    E         -  'd0Cpk',
    E         -  'f_DlJR',
    E         -  'gJqCwsLtb',
    E         -  'tgzQ',
    E         -  'wUnD',
    E         -  'z0zA',
    E         ?   - --
    E         +  '0',
    E         -  'zse𐐖fQ𑑔88dx',
    E         -  '󠆨eᾮaSaoE້qC',
    E         +  '1',
    E         +  '2',
    E         +  '3',
    E         +  '4',
    E         +  '5',
    E         +  '6',
    E         +  '7',
    E         +  '8',
    E         +  '9',
    E           }
    
    source/tests.py:46: AssertionError
    _______________________________ test_problem_10 ________________________________
    
    problem = Problem(artifacts=None, input='=9K3E46j6EY.\x0b\x0b \x0cER2N8ZPv2Aor(\x0c\x0b*Aa7f1jtC\n\x0b3U\x0c \x0c}uUNo%\x0c%hTRd...dfot*', 'htrdfotz*', 'htrdfotzp*', 'htrdfotzpw*', 'htrdfotzpw0*', 'htrdfotzpw0l', 'ofhi*', 'ofhip*', 'ofhipn', 'uuno'])
    
        @weight(name="problem 10", worth=1)
        def test_problem_10(problem: Problem):
    >       assert set(problem.output) == set(problem.reference)
    E       AssertionError: assert {'9', '0', '1', '4', '7', '8', '2', '6', '3', '5'} == {'9k3e*',\n '9k3e4*',\n '9k3e46*',\n '9k3e46j*',\n '9k3e46j6*',\n '9k3e46j6e*',\n '9k3e46j6ey',\n 'aa7f*',\n 'aa7f1*',\n 'aa7f1j*',\n 'aa7f1jt*',\n 'aa7f1jtc',\n 'ac5p*',\n 'ac5pi*',\n 'ac5pia*',\n 'ac5pias*',\n 'ac5piasb',\n 'er2n*',\n 'er2n8*',\n 'er2n8z*',\n 'er2n8zp*',\n 'er2n8zpv*',\n 'er2n8zpv2*',\n 'er2n8zpv2a*',\n 'er2n8zpv2ao*',\n 'er2n8zpv2aor',\n 'fjcp*',\n 'fjcpd*',\n 'fjcpdk*',\n 'fjcpdkt*',\n 'fjcpdktq*',\n 'fjcpdktqz*',\n 'fjcpdktqzq*',\n 'fjcpdktqzqj*',\n 'fjcpdktqzqji',\n 'htrd*',\n 'htrdf*',\n 'htrdfo*',\n 'htrdfot*',\n 'htrdfotz*',\n 'htrdfotzp*',\n 'htrdfotzpw*',\n 'htrdfotzpw0*',\n 'htrdfotzpw0l',\n 'ihgn*',\n 'ihgnb*',\n 'ihgnbc*',\n 'ihgnbc3*',\n 'ihgnbc3x*',\n 'ihgnbc3xd*',\n 'ihgnbc3xdr*',\n 'ihgnbc3xdrf*',\n 'ihgnbc3xdrfl',\n 'ofhi*',\n 'ofhip*',\n 'ofhipn',\n 'ojia*',\n 'ojiaw*',\n 'ojiawr*',\n 'ojiawrw*',\n 'ojiawrwu*',\n 'ojiawrwuk*',\n 'ojiawrwukr',\n 'uuno'}
    E         Extra items in the left set:
    E         '9'
    E         '0'
    E         '1'
    E         '4'
    E         '7'
    E         '8'
    E         '2'
    E         '6'
    E         '3'
    E         '5'
    E         Extra items in the right set:
    E         'ojiawr*'
    E         'ofhipn'
    E         'aa7f1*'
    E         'htrdfo*'
    E         'uuno'
    E         'ac5piasb'
    E         'aa7f1j*'
    E         'ihgnbc3xdrf*'
    E         'ofhi*'
    E         'aa7f1jt*'
    E         'ihgnbc3xdr*'
    E         'ojiaw*'
    E         'ojiawrw*'
    E         'ihgnbc3x*'
    E         'er2n8zpv2a*'
    E         'htrd*'
    E         'ojia*'
    E         '9k3e46*'
    E         'fjcpdk*'
    E         'fjcp*'
    E         '9k3e46j6e*'
    E         'ac5p*'
    E         'fjcpdktqzq*'
    E         'ojiawrwukr'
    E         'er2n8z*'
    E         'er2n8zpv2ao*'
    E         'htrdfotzpw0l'
    E         'htrdfotzpw*'
    E         'ihgnbc3xd*'
    E         'fjcpdktqz*'
    E         'er2n8zpv2*'
    E         'ojiawrwuk*'
    E         'er2n*'
    E         'ac5pia*'
    E         'er2n8zp*'
    E         'er2n8zpv*'
    E         'ihgnbc3xdrfl'
    E         'aa7f*'
    E         'fjcpdktqzqj*'
    E         'er2n8zpv2aor'
    E         'aa7f1jtc'
    E         'ojiawrwu*'
    E         'ac5pi*'
    E         'ofhip*'
    E         'fjcpdktq*'
    E         'ihgn*'
    E         'ac5pias*'
    E         '9k3e46j6*'
    E         'fjcpd*'
    E         'fjcpdkt*'
    E         'fjcpdktqzqji'
    E         '9k3e*'
    E         'htrdfotz*'
    E         'ihgnb*'
    E         '9k3e4*'
    E         'er2n8*'
    E         'ihgnbc3*'
    E         'htrdfotzp*'
    E         '9k3e46j*'
    E         'htrdf*'
    E         '9k3e46j6ey'
    E         'htrdfot*'
    E         'ihgnbc*'
    E         'htrdfotzpw0*'
    E         Full diff:
    E           {
    E         +  '0',
    E         +  '1',
    E         +  '2',
    E         +  '3',
    E         +  '4',
    E         +  '5',
    E         +  '6',
    E         +  '7',
    E         +  '8',
    E         +  '9',
    E         -  '9k3e*',
    E         -  '9k3e4*',
    E         -  '9k3e46*',
    E         -  '9k3e46j*',
    E         -  '9k3e46j6*',
    E         -  '9k3e46j6e*',
    E         -  '9k3e46j6ey',
    E         -  'aa7f*',
    E         -  'aa7f1*',
    E         -  'aa7f1j*',
    E         -  'aa7f1jt*',
    E         -  'aa7f1jtc',
    E         -  'ac5p*',
    E         -  'ac5pi*',
    E         -  'ac5pia*',
    E         -  'ac5pias*',
    E         -  'ac5piasb',
    E         -  'er2n*',
    E         -  'er2n8*',
    E         -  'er2n8z*',
    E         -  'er2n8zp*',
    E         -  'er2n8zpv*',
    E         -  'er2n8zpv2*',
    E         -  'er2n8zpv2a*',
    E         -  'er2n8zpv2ao*',
    E         -  'er2n8zpv2aor',
    E         -  'fjcp*',
    E         -  'fjcpd*',
    E         -  'fjcpdk*',
    E         -  'fjcpdkt*',
    E         -  'fjcpdktq*',
    E         -  'fjcpdktqz*',
    E         -  'fjcpdktqzq*',
    E         -  'fjcpdktqzqj*',
    E         -  'fjcpdktqzqji',
    E         -  'htrd*',
    E         -  'htrdf*',
    E         -  'htrdfo*',
    E         -  'htrdfot*',
    E         -  'htrdfotz*',
    E         -  'htrdfotzp*',
    E         -  'htrdfotzpw*',
    E         -  'htrdfotzpw0*',
    E         -  'htrdfotzpw0l',
    E         -  'ihgn*',
    E         -  'ihgnb*',
    E         -  'ihgnbc*',
    E         -  'ihgnbc3*',
    E         -  'ihgnbc3x*',
    E         -  'ihgnbc3xd*',
    E         -  'ihgnbc3xdr*',
    E         -  'ihgnbc3xdrf*',
    E         -  'ihgnbc3xdrfl',
    E         -  'ofhi*',
    E         -  'ofhip*',
    E         -  'ofhipn',
    E         -  'ojia*',
    E         -  'ojiaw*',
    E         -  'ojiawr*',
    E         -  'ojiawrw*',
    E         -  'ojiawrwu*',
    E         -  'ojiawrwuk*',
    E         -  'ojiawrwukr',
    E         -  'uuno',
    E           }
    
    source/tests.py:51: AssertionError
    _______________________________ test_problem_11 ________________________________
    
    problem = Problem(artifacts=None, input='v4Wja3Pva\x0c\'z\'\tlKMF1sMKwcogpA\t \x0b5Sq8n6dGj8p\n\t\r~B}\x0b\x0b\x0b-VFdK}\rGLhY=\...3*', 'v4wja3p*', 'v4wja3pv*', 'v4wja3pva', 'xnwz', 'xopp*', 'xopp8*', 'xopp8g*', 'xopp8g7*', 'xopp8g7t*', 'xopp8g7tl'])
    
        @weight(name="problem 11", worth=1)
        def test_problem_11(problem: Problem):
    >       assert set(problem.output) == set(problem.reference)
    E       AssertionError: assert {'9', '0', '1', '4', '7', '8', '2', '6', '3', '5'} == {'5qkg*',\n '5qkga*',\n '5qkgai*',\n '5qkgaid*',\n '5qkgaido*',\n '5qkgaidou*',\n '5qkgaidout*',\n '5qkgaidoutf',\n '5sq8*',\n '5sq8n*',\n '5sq8n6*',\n '5sq8n6d*',\n '5sq8n6dg*',\n '5sq8n6dgj*',\n '5sq8n6dgj8*',\n '5sq8n6dgj8p',\n 'bg﹍ꞈ*',\n 'bg﹍ꞈp*',\n 'bg﹍ꞈpi*',\n 'bg﹍ꞈpi𐐬*',\n 'bg﹍ꞈpi𐐬h',\n 'g6b9*',\n 'g6b9r*',\n 'g6b9rṡ*',\n 'g6b9rṡ7*',\n 'g6b9rṡ7ꓢ*',\n 'g6b9rṡ7ꓢ0*',\n 'g6b9rṡ7ꓢ0d*',\n 'g6b9rṡ7ꓢ0dw',\n 'glhy',\n 'htvαι*',\n 'htvαιk*',\n 'htvαιk9*',\n 'htvαιk9j*',\n 'htvαιk9ju*',\n 'htvαιk9juj',\n 'j0ɠn*',\n 'j0ɠnｐ*',\n 'j0ɠnｐe',\n 'j3my*',\n 'j3my੯*',\n 'j3my੯1*',\n 'j3my੯1αι*',\n 'j3my੯1αιr',\n 'khzs',\n 'lfgf*',\n 'lfgfq*',\n 'lfgfqh',\n 'piaq*',\n 'piaq󠄌',\n 'qvoe*',\n 'qvoeu*',\n 'qvoeun*',\n 'qvoeunk*',\n 'qvoeunkg*',\n 'qvoeunkgm',\n 'rdg4*',\n 'rdg4w*',\n 'rdg4wo*',\n 'rdg4woa',\n 's5u8*',\n 's5u8𐳫',\n 'shu_*',\n 'shu_y*',\n 'shu_yk',\n 'v4wj*',\n 'v4wja*',\n 'v4wja3*',\n 'v4wja3p*',\n 'v4wja3pv*',\n 'v4wja3pva',\n 'vfdk',\n 'w2oǌ*',\n 'w2oǌw*',\n 'w2oǌw𖩦*',\n 'w2oǌw𖩦7*',\n 'w2oǌw𖩦7j*',\n 'w2oǌw𖩦7jh',\n 'xnwz',\n 'xopp*',\n 'xopp8*',\n 'xopp8g*',\n 'xopp8g7*',\n 'xopp8g7t*',\n 'xopp8g7tl'}
    E         Extra items in the left set:
    E         '9'
    E         '0'
    E         '1'
    E         '4'
    E         '7'
    E         '8'
    E         '2'
    E         '6'
    E         '3'
    E         '5'
    E         Extra items in the right set:
    E         'g6b9rṡ7ꓢ0d*'
    E         'rdg4*'
    E         'g6b9rṡ7*'
    E         'g6b9r*'
    E         'w2oǌw𖩦7j*'
    E         'v4wj*'
    E         'qvoeun*'
    E         'bg﹍ꞈpi𐐬*'
    E         'htvαι*'
    E         'j0ɠn*'
    E         'bg﹍ꞈpi𐐬h'
    E         'htvαιk9*'
    E         'xopp8g*'
    E         'qvoeunkg*'
    E         'glhy'
    E         'v4wja3*'
    E         'rdg4wo*'
    E         'j3my੯1*'
    E         'xopp8*'
    E         'xnwz'
    E         'piaq󠄌'
    E         'bg﹍ꞈp*'
    E         'w2oǌw𖩦7jh'
    E         'khzs'
    E         'j0ɠnｐe'
    E         'lfgfq*'
    E         'xopp8g7*'
    E         '5qkg*'
    E         'qvoeu*'
    E         '5qkgaidou*'
    E         'w2oǌ*'
    E         '5sq8n6dgj*'
    E         'g6b9rṡ*'
    E         'w2oǌw𖩦7*'
    E         'j3my੯1αιr'
    E         'vfdk'
    E         'htvαιk*'
    E         'xopp*'
    E         '5sq8n6dgj8p'
    E         '5sq8n6*'
    E         'htvαιk9ju*'
    E         'g6b9rṡ7ꓢ0dw'
    E         'xopp8g7tl'
    E         'j3my*'
    E         'j0ɠnｐ*'
    E         'piaq*'
    E         '5sq8n6d*'
    E         '5sq8n6dg*'
    E         '5sq8n6dgj8*'
    E         'htvαιk9juj'
    E         '5qkgaido*'
    E         'w2oǌw𖩦*'
    E         'xopp8g7t*'
    E         'qvoeunk*'
    E         'shu_y*'
    E         'htvαιk9j*'
    E         '5qkgaid*'
    E         '5qkgai*'
    E         'w2oǌw*'
    E         'v4wja3pv*'
    E         'shu_*'
    E         '5qkgaidoutf'
    E         'j3my੯*'
    E         'v4wja3p*'
    E         'v4wja*'
    E         'g6b9*'
    E         'qvoeunkgm'
    E         'shu_yk'
    E         'bg﹍ꞈpi*'
    E         '5qkga*'
    E         '5sq8*'
    E         'lfgf*'
    E         'lfgfqh'
    E         'v4wja3pva'
    E         's5u8𐳫'
    E         's5u8*'
    E         'qvoe*'
    E         'j3my੯1αι*'
    E         '5sq8n*'
    E         'g6b9rṡ7ꓢ0*'
    E         '5qkgaidout*'
    E         'g6b9rṡ7ꓢ*'
    E         'rdg4woa'
    E         'rdg4w*'
    E         'bg﹍ꞈ*'
    E         Full diff:
    E           {
    E         +  '0',
    E         +  '1',
    E         +  '2',
    E         +  '3',
    E         +  '4',
    E         +  '5',
    E         +  '6',
    E         +  '7',
    E         +  '8',
    E         +  '9',
    E         -  '5qkg*',
    E         -  '5qkga*',
    E         -  '5qkgai*',
    E         -  '5qkgaid*',
    E         -  '5qkgaido*',
    E         -  '5qkgaidou*',
    E         -  '5qkgaidout*',
    E         -  '5qkgaidoutf',
    E         -  '5sq8*',
    E         -  '5sq8n*',
    E         -  '5sq8n6*',
    E         -  '5sq8n6d*',
    E         -  '5sq8n6dg*',
    E         -  '5sq8n6dgj*',
    E         -  '5sq8n6dgj8*',
    E         -  '5sq8n6dgj8p',
    E         -  'bg﹍ꞈ*',
    E         -  'bg﹍ꞈp*',
    E         -  'bg﹍ꞈpi*',
    E         -  'bg﹍ꞈpi𐐬*',
    E         -  'bg﹍ꞈpi𐐬h',
    E         -  'g6b9*',
    E         -  'g6b9r*',
    E         -  'g6b9rṡ*',
    E         -  'g6b9rṡ7*',
    E         -  'g6b9rṡ7ꓢ*',
    E         -  'g6b9rṡ7ꓢ0*',
    E         -  'g6b9rṡ7ꓢ0d*',
    E         -  'g6b9rṡ7ꓢ0dw',
    E         -  'glhy',
    E         -  'htvαι*',
    E         -  'htvαιk*',
    E         -  'htvαιk9*',
    E         -  'htvαιk9j*',
    E         -  'htvαιk9ju*',
    E         -  'htvαιk9juj',
    E         -  'j0ɠn*',
    E         -  'j0ɠnｐ*',
    E         -  'j0ɠnｐe',
    E         -  'j3my*',
    E         -  'j3my੯*',
    E         -  'j3my੯1*',
    E         -  'j3my੯1αι*',
    E         -  'j3my੯1αιr',
    E         -  'khzs',
    E         -  'lfgf*',
    E         -  'lfgfq*',
    E         -  'lfgfqh',
    E         -  'piaq*',
    E         -  'piaq󠄌',
    E         -  'qvoe*',
    E         -  'qvoeu*',
    E         -  'qvoeun*',
    E         -  'qvoeunk*',
    E         -  'qvoeunkg*',
    E         -  'qvoeunkgm',
    E         -  'rdg4*',
    E         -  'rdg4w*',
    E         -  'rdg4wo*',
    E         -  'rdg4woa',
    E         -  's5u8*',
    E         -  's5u8𐳫',
    E         -  'shu_*',
    E         -  'shu_y*',
    E         -  'shu_yk',
    E         -  'v4wj*',
    E         -  'v4wja*',
    E         -  'v4wja3*',
    E         -  'v4wja3p*',
    E         -  'v4wja3pv*',
    E         -  'v4wja3pva',
    E         -  'vfdk',
    E         -  'w2oǌ*',
    E         -  'w2oǌw*',
    E         -  'w2oǌw𖩦*',
    E         -  'w2oǌw𖩦7*',
    E         -  'w2oǌw𖩦7j*',
    E         -  'w2oǌw𖩦7jh',
    E         -  'xnwz',
    E         -  'xopp*',
    E         -  'xopp8*',
    E         -  'xopp8g*',
    E         -  'xopp8g7*',
    E         -  'xopp8g7t*',
    E         -  'xopp8g7tl',
    E           }
    
    source/tests.py:56: AssertionError
    =========================== short test summary info ============================
    FAILED source/tests.py::test_problem_1 - AssertionError: assert '1234567890' ...
    FAILED source/tests.py::test_problem_2 - AssertionError: assert '1234567890' ...
    FAILED source/tests.py::test_problem_3 - AssertionError: assert None == 'e0bc...
    FAILED source/tests.py::test_problem_4 - AssertionError: assert '1234567890' ...
    FAILED source/tests.py::test_problem_5 - AssertionError: assert '1234567890' ...
    FAILED source/tests.py::test_problem_6 - AssertionError: assert '1234567890' ...
    FAILED source/tests.py::test_problem_7 - AssertionError: assert '1234567890' ...
    FAILED source/tests.py::test_problem_8 - AssertionError: assert {'9', '0', '1...
    FAILED source/tests.py::test_problem_9 - AssertionError: assert {'9', '0', '1...
    FAILED source/tests.py::test_problem_10 - AssertionError: assert {'9', '0', '...
    FAILED source/tests.py::test_problem_11 - AssertionError: assert {'9', '0', '...
    ============================== 11 failed in 0.06s ==============================
    
    tests used input json:
    {
        "problem 1": {
            "password": "c1c0efe26c5d0d9c47de46e06275b6b9",
            "salt": "557b55664bb39303eb4c1e390618fcfd"
        },
        "problem 2": "824fdc7e390ed6e5d187c0c4422f68cc3954a35648264c937e64a642a67f2467",
        "problem 3": {
            "key": "ec5866e721e271f94809c91cc0d31e22",
            "data": "e0bcbab8d264fce468b0f79fbc438a3767cc6e24af2215d96c226da86935f254b67652264eea3d17a456437c0cc55634b3bcf0587f47cae9aff999345ce72a1f"
        },
        "problem 4": {
            "key": "e00ff9c9a831a1226d4f9e5215aec7b6",
            "data": "4edd7417f52579b081dfca17d88de76901dd0d03e4258d841894f80f212ebd45ab46b64f70234935febdb9c353d9f21a7a9bbbd87257244c7982e630204338c9"
        },
        "problem 5": {
            "keys": [
                "c45a73ce279460bae465a2b1b0ffe2f4",
                "3984ccc6677e50f6c84ff63c2befcdb4",
                "736bde0c0c1be5d24cc232e6fcc93534",
                "10503e6855071a6355f4a56da6a2fd61"
            ],
            "plaintext": "37dd2a33ce1b5a29cd7e651a8d13817b569e519cd4e64ecdfa736122fda0e3a5fcfc59cbd38a8641d504ca73777bb33634b4c3dbc701514651fb5886dbd10920"
        },
        "problem 6": {
            "keys": [
                "9c4d2d32ac65b96d57439979839260bd",
                "87b9289611b93f22af5523671a7ef8a6",
                "12d3ac20acd40d5529802b4ebf43abe8",
                "b3aa686236ea98d2696759b1553d3d5c"
            ],
            "ciphertext": "2b204d184fb15464efb73db36263018a3562bb50cd00eab1ee0c5048dfc419aedd73d0bf1ad868f0136606bf86e705fbf405f40d31e343827f303c5a512f8b2e"
        },
        "problem 7": {
            "key": "2ca6f8c45d3557317d7b6477907f8dad",
            "data": "764bc021be90879ef513e255a0c7067c86185ac9828b51eaf573de78e7082098454130dc7e861fe860ec634d2a9757d624372d7d2360cf510b45f02ee59149ee"
        },
        "problem 8": ":sObuoXcPMO7a\n  \t)XqFi8MyGgPmDToJ89HeM\u000b\f+rEyaWjvV?\t \t\n}5ycTZ1L\n\n$x2OCfx0L4\t}VqSOx3q \n\u000b_cciGmFWUnAjc?\rdf7s2em$ \n\t\n7f55^ \n\u000b\r0OJxRvU4V`\t1krPQmv53\t\n\r\t",
        "problem 9": "PSC6YJz1gkY {1G\ud836\ude4ak5A\ud807\udc52Hr5IKo3,\f\r\u000b=gJqCwsLtb<\n \r{BBPU24ldrp2juz3ZDUMQ$\u000b\t \r.tgzQ\f\t\n=y.\t\"E516Bmb}\t\r\f\n4P6Ls0Wcw\u000b\n+cl1 #wjpmlECD2fYhonlS\u000b\r\n7yv62wN\n\fK\f\t&d0Cpk\u000b\u000b\u000b\fF\u0694e;\n\n)\u01f2jq7UW2SdI\ua4e2\u0dd6oxh\ud80d\udc00\ud802\udc9a\u1825p\u207f\u000bE5MaLoLBdRUY\r\fz0zA   \t-f\n \u000b\r/wUnD\\\r .UgnIFw\ufa853\u02b2\u1f9ecuY2Y\u0e47HVrL\r \r~0Kdm\ufe4fsHP\n9D\ud804\udf72fyQmttm0ae2UZP\u1f9el\u1db8-\n\f\n\n975uWASaQ% \t`5j0WLs3xXnCrL57Ui\n\u000b\ff_DlJR\f\n\f\f@fK2KSTx3SIyWJc\r[\udb40\udda8e\u1faeaSaoE\u0ec9qC<\t\u000b\t\ti\ua788: \\d37?  \u000b;zse\ud801\udc16fQ\ud805\udc5488dx\r\f !NiK2X7Rrx\n\t\r\n\u0694K\u0dd61xlS\ud801\udc16tT2XV^\rZ6\u0dd6N\u0c687Bq\ufe34x\t\r\u000b\ry2Fu4R0PJjBUOA3zPWxa \r\n\r~aLXE\ud81b\udf94\ud81a\ude66DO7p8\u000b\n 0\u000b\t\rIm\u0dd6v\u1dbdCx\u040eF\ud80d\udc00I\u01f2~\r\u000b*4o&\n\n\n{0bpNJ\uff503[\r\r\f\f^qWpH\u0159\ud802\udc9abJ4E6fsvUy\u1faepO\t\n\r#o0DYF3VJZSYEiifJv.\u000b \f\r",
        "problem 10": "=9K3E46j6EY.\u000b\u000b \fER2N8ZPv2Aor(\f\u000b*Aa7f1jtC\n\u000b3U\f \f}uUNo%\f%hTRdfOTZpw0L \f\fIhgNbC3xdRfL\u000b\u000bofhIpN& OB\r\t\f%Ac5pIASb\n\u000b~OjiAWRWUkr+\r1Bdgj8IFwpussbKQlTt_\fFjCPDKtqzQJI\"\f\u000b\u000b\f",
        "problem 11": "v4Wja3Pva\f'z'\tlKMF1sMKwcogpA\t \u000b5Sq8n6dGj8p\n\t\r~B}\u000b\u000b\u000b-VFdK}\rGLhY=\fxopP8g7tl \ta$ Cu2qPs\u1fbc\u020ehM5J\u01cb4\u000b\u000b\t\u000bqVOeuNkGM\r\u000b\u000b$r \u000blfgfqH^ \\TZ;\t\n\u000b\t/RDG4WOA \u000b\u000b\\xNWz\u000b\t5qkgAiDoutF\r  6`\f}1Kw41WCIdEqYeG\n\u000b\r\tkHzS\u000b \f 7zj~\u000b\n\t\n[J3My\u0a6f1\u1fbcr\t|g8X\u000b\f\fDrqA1k\u1da3v\u1fbcs5\u0a69\u0260\u1da3yCvcES\u000b\nsHU_Yk#\u000b  \fBJP5tvLd0WBO7~ \n<S5u8\ud803\udceb:\u000b\f\u000b`Yf\u1faeRNN4R3TSq1c\f\f\f\n)G6B9R\u1e607\ua4e20dw^\f\t+d\n\n\r\u000b-hTv\u1fbcK9JUj\\ 3ULEHMj\u1dbdp2r1e\uff2fW6\u1fbceW\ufa85\"\r \fzPy9rk8dkY6PFF Bg\ufe4d\ua788pi\ud801\udc04H`\r\n%\u0a69\u1fad\u000b`J0\u0260n\uff50E\nW2o\u01cbW\ud81a\ude667jh\t-tvz1XPxP6if3ji\n \r{PIAq\udb40\udd0c)\t\t"
    }
    
    fencrypt generated json:
    {
        "problem 1": "1234567890",
        "problem 2": "1234567890",
        "problem 4": "1234567890",
        "problem 5": "1234567890",
        "problem 6": "1234567890",
        "problem 7": "1234567890",
        "problem 8": "1234567890",
        "problem 9": "1234567890",
        "problem 10": "1234567890",
        "problem 11": "1234567890"
    }``

---
Thanks for submitting. Remember that you can re-submit as many times as you like, as long as the assignment is open!

---
problem 1 (0.0/1.0)

---
problem 2 (0.0/1.0)

---
problem 3 (0.0/1.0)

---
problem 4 (0.0/1.0)

---
problem 5 (0.0/1.0)

---
problem 6 (0.0/1.0)

---
problem 7 (0.0/1.0)

---
problem 8 (0.0/1.0)

---
problem 9 (0.0/1.0)

---
problem 10 (0.0/1.0)

---
problem 11 (0.0/1.0)

## AUTOGRADER SCORE

0.0 / 0.0

### FAILED TESTS

1.  [problem 1 (0.0/1.0)](https://www.gradescope.com/courses/360029/assignments/1898459/submissions/114376536#problem%201)
2.  [problem 2 (0.0/1.0)](https://www.gradescope.com/courses/360029/assignments/1898459/submissions/114376536#problem%202)
3.  [problem 3 (0.0/1.0)](https://www.gradescope.com/courses/360029/assignments/1898459/submissions/114376536#problem%203)
4.  [problem 4 (0.0/1.0)](https://www.gradescope.com/courses/360029/assignments/1898459/submissions/114376536#problem%204)
5.  [problem 5 (0.0/1.0)](https://www.gradescope.com/courses/360029/assignments/1898459/submissions/114376536#problem%205)
6.  [problem 6 (0.0/1.0)](https://www.gradescope.com/courses/360029/assignments/1898459/submissions/114376536#problem%206)
7.  [problem 7 (0.0/1.0)](https://www.gradescope.com/courses/360029/assignments/1898459/submissions/114376536#problem%207)
8.  [problem 8 (0.0/1.0)](https://www.gradescope.com/courses/360029/assignments/1898459/submissions/114376536#problem%208)
9.  [problem 9 (0.0/1.0)](https://www.gradescope.com/courses/360029/assignments/1898459/submissions/114376536#problem%209)
10.  [problem 10 (0.0/1.0)](https://www.gradescope.com/courses/360029/assignments/1898459/submissions/114376536#problem%2010)
11.  [problem 11 (0.0/1.0)](https://www.gradescope.com/courses/360029/assignments/1898459/submissions/114376536#problem%2011)
