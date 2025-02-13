import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import colored
from colored import cprint

senders = {
'ugtnddpzej@rambler.ru':'9506681adi6MU',
'cisvzeeuyg@rambler.ru':'6301453fJo4s9',
'ggflngvlih@rambler.ru':'22408953S2gby',
'nvynpxnkkd@rambler.ru':'2510571xHHdgR',
'fjzoyuouuz@rambler.ru':'59097784rDPPd',
'bzgqlptwhl@rambler.ru':'0816705Tr1FYG',
'vigzkazhat@rambler.ru':'31932120MtFlm',
'afgunihnfe@rambler.ru':'9061194g5B45C',
'ngvxtwpesz@rambler.ru':'2011142rqGxFR',
'egvwsdlkyr@rambler.ru':'9037151L6w49u',
'tfdmxqejns@rambler.ru':'7787340bbA3sL',
'thrcxqfhxt@rambler.ru':'4033354R50aaM',
'gzbsslvpgb@rambler.ru':'8608390st77PG',
'vgwkozobgf@rambler.ru':'0713430AUe0Jj',
'xthokzcxta@rambler.ru':'0362278TxeHl1',
'ulgtgyesux@rambler.ru':'4621758slMQ2q',
'mekpwikznr@rambler.ru':'3416279IFmuKQ',
'clgplzxnqw@rambler.ru':'6412121gc7Dcu',
'azfingoovg@rambler.ru':'6148697BuRbwO',
'xfjhvzmnac@rambler.ru':'9670930pBIR7W',
'thgwrxhltj@rambler.ru':'2369423cUvLuf',
'agpjaemyqm@rambler.ru':'6572399A8cFh6',
'wvicwdopps@rambler.ru':'7661495MeRn88',
'kpuaeogels@rambler.ru':'02848019U4yxH',
'dzdhnhsfia@rambler.ru':'6976310gzYoE2',
'vlldcxigrj@rambler.ru':'9022806maOtUs',
'hlfczgnfrr@rambler.ru':'9916462168Ypp',
'jtmtruwscg@rambler.ru':'9923365hkHeN6',
'aozzmmsvvi@rambler.ru':'0399945jLmU7B',
'nglqkjipix@rambler.ru':'0058167GPjOZR',
'dxldwtdips@rambler.ru':'4221180vuJqsB',
'fnymojqdux@rambler.ru':'4820302GP03Ru',
'elvyorfunb@rambler.ru':'9023694jkXJV4',
'yiredoekax@rambler.ru':'3543487Cm2P2a',
'hpobxpntkg@rambler.ru':'9360288IzyHkP',
'owbsixedjj@rambler.ru':'6443042VnSBeS',
'hgwptrmpwz@rambler.ru':'9923510OpfY1W',
'cyblanwvop@rambler.ru':'5825453FKm1ZE',
'uwtjezecrs@rambler.ru':'6411755QBcF7p',
'ybjbggdruu@rambler.ru':'4065298o86MLm',
'uckmapemvh@rambler.ru':'9531228JLg96F',
'jkjportalx@rambler.ru':'2401077inLnJj',
'kolnanjvkw@rambler.ru':'86294929rsQvg',
'rhzlhaagsc@rambler.ru':'03837749f9qvW',
'fdroghhuoy@rambler.ru':'13627259IrATl',
'jhripippie@rambler.ru':'8596550xkdTvR',
'ghjullwyxo@rambler.ru':'7784503Dl60Kl',
'srdicexvfo@rambler.ru':'8943491TEOSke',
'jgxvvtcsvi@rambler.ru':'2851226DI6zY5',
'krihsllwpz@rambler.ru':'4272238ts9X3z',
'jolonbfrbl@rambler.ru':'2637507DppJyT',
'uqblakalnx@rambler.ru':'3735373NSS8lz',
'owiwwvgrrx@rambler.ru':'0592924zRhm4W',
'qtjwomftjv@rambler.ru':'6049164OqDaxz',
'aiosomfxks@rambler.ru':'6919172lA1N45',
'xmqrrmybdl@rambler.ru':'5597456YOjL0c',
'lkawwbtmaj@rambler.ru':'0796449gknSFs',
'lomxgjndyr@rambler.ru':'2467557Ib1ZVu',
'jqwcsddyrg@rambler.ru':'1102645xGeLhj',
'kacftekdeq@rambler.ru':'0261527ivGs1S',
'alazchgdiv@rambler.ru':'9751444kT01fm',
'vgymcieuft@rambler.ru':'3312197YSGrOc',
'cogyjubzkl@rambler.ru':'0174602bkNHod',
'weinejwyir@rambler.ru':'0637170gHYLdN',
'uxsoazzpwb@rambler.ru':'4936893zRSsTC',
'sbbzmlvdgo@rambler.ru':'2224249cGnGIv',
'ymycqoegto@rambler.ru':'4818009OHorIl',
'vqueaeveat@rambler.ru':'50476661392iV',
'vunvhfkbks@rambler.ru':'6880622LYLbfc',
'xjetfnzjhi@rambler.ru':'0518737rzBvTd',
'liekddtuws@rambler.ru':'5819586i6eSoS',
'ycencrfdxd@rambler.ru':'1051144aZoHRP',
'bpkishuvbc@rambler.ru':'5154664Vwi6Ua',
'wsnypwafbt@rambler.ru':'9707576JDK9Fw',
'oytrjytdpr@rambler.ru':'0906843MAu7RU',
'smeaipdrpu@rambler.ru':'5648933ztPS6u',
'fmyzcbctri@rambler.ru':'3308444zi68By',
'iurqgpxynb@rambler.ru':'8366202xmgCYS',
'wqhcmaknrv@rambler.ru':'0502120gdP9zL',
'fbnkspvdjz@rambler.ru':'7945888mcrStg',
'hpbpeeptcc@rambler.ru':'3788419Pc252T',
'xksxdxwdze@rambler.ru':'7078149cqEy4T',
'wdpuletfdl@rambler.ru':'5322696L0N9l9',
'bziqrktkhy@rambler.ru':'3246091kgTTaZ',
'saelakwdmc@rambler.ru':'0563798ptrtSN',
'anitjpnnos@rambler.ru':'7990575MCToVl',
'ixvpbrsnyd@rambler.ru':'95615495uwOsN',
'ifrxkefqxo@rambler.ru':'1264966unxLRo',
'mhqgjgjxvv@rambler.ru':'2226251mpDJ9n',
'uowohxbqei@rambler.ru':'3504468bIHRWV',
'cvdkpcwdmq@rambler.ru':'6488683AEsgdG',
'qxnrsosnwp@rambler.ru':'0370763iQaWfn',
'opnvudfwap@rambler.ru':'1873848oOgVLA',
'pswrzpjlnj@rambler.ru':'4119723UWtRMq',
'lvhqxrbyjx@rambler.ru':'9096999IwuiNK',
'iiuphvfjck@rambler.ru':'6800251g3qPxP',
'szlbpfqfnu@rambler.ru':'57915343pGk9Z',
'kmnsazmofd@rambler.ru':'9881154UFzUnz',
'xlngvgdfyy@rambler.ru':'8503734lIaDOq',
'toksegumgm@rambler.ru':'1206136M2pgxK',
'lzxweynvmk@rambler.ru':'0656844M8Ua7r',
'piltwbqahv@rambler.ru':'1571843HwjOy5',
'rwbqxcjhij@rambler.ru':'2627820ygMv0p',
'ybxdyezeaw@rambler.ru':'8683132Fm75um',
'rhlumlbqxc@rambler.ru':'0502630CYEngx',
'qstvhreejj@rambler.ru':'2436299apZbqS',
'cpldnzlqgs@rambler.ru':'7520506dxK7nW',
'eumghdgkgm@rambler.ru':'5129031GzG03Z',
'qwfahkwfjh@rambler.ru':'7088021Myistn',
'twhvlnbtvt@rambler.ru':'9399429GaJJa4',
'jhddwfikgw@rambler.ru':'1393287IB0PZo',
'pzvrccwdbm@rambler.ru':'7758769ekQe1f',
'shwrdzijmf@rambler.ru':'3873842XH3bgL',
'vbuigzynnm@rambler.ru':'3856920aHzE4A',
'ztwiwilejq@rambler.ru':'8616981WYFTCk',
'vuszmpdppy@rambler.ru':'7726003c24PVz',
'dacoapnvnt@rambler.ru':'81066143Zm1fp',
'apkjscfntk@rambler.ru':'3546871Y7Bk0w',
'oainbrnnrp@rambler.ru':'84346062U6MFe',
'pidhhlesak@rambler.ru':'5135415L1Dnqt',
'ehwulsfufl@rambler.ru':'5801265ubPOzK',
'irzgfdicah@rambler.ru':'3719696WyxpXh',
'yzjduaakxc@rambler.ru':'2438994ACJaub',
'hodqdiuklo@rambler.ru':'767841344A1tF',
'nzlqpjwpot@rambler.ru':'6915997SUqN84',
'xhvhvjqvrt@rambler.ru':'17843148GoORZ',
'opbghlryyi@rambler.ru':'6187779N2tt8r',
'vbzayzmnnz@rambler.ru':'2765133rIsG4W',
'wnmuqoxgvg@rambler.ru':'4030133AjIHEa',
'fwczlkjeqx@rambler.ru':'6138606ClwDQY',
'mdmspcvyaw@rambler.ru':'0098146Yud02L',
'hrdswjzgqw@rambler.ru':'0856046puV88r',
'xyqgrjswfr@rambler.ru':'81996872YvIq7',
'entkfoopcd@rambler.ru':'5336523l9K1n2',
'djtueljvss@rambler.ru':'9936980wtNXfX',
'dzmctubwws@rambler.ru':'4622840Q7HZyO',
'wzuwzzgnvl@rambler.ru':'6153631PNMlBx',
'rmtcqdgvnd@rambler.ru':'9338592pDQDSq',
'cmueytlsbc@rambler.ru':'5897484z7lKrY',
'prpsvvroci@rambler.ru':'2722168RHYhcx',
'juyhlrlzvt@rambler.ru':'1838830ziEfOH',
'ofuggpdykx@rambler.ru':'8520503CZNHjV',
'qfjwtjbhpo@rambler.ru':'4156828Jf4enw',
'rwrwswudhv@rambler.ru':'8266122J4AqLc',
'xxyxszaaqr@rambler.ru':'11798633kGF38',
'zlhlyybkbp@rambler.ru':'5168039gkHAkf',
'zrajbxewkt@rambler.ru':'01285925IinUA',
'lybjgnaaqg@rambler.ru':'6251735AhBL0N',
'twivzuqoth@rambler.ru':'8953852Squ69v',
'ifachrohjq@rambler.ru':'6493652wiEikB',
'myjhbsfeen@rambler.ru':'627375988utRh',
'mgitqvmqpn@rambler.ru':'0551846dwPIRy',
'wihhibhnzt@rambler.ru':'6339855JrieYb',
'wqyqfejfde@rambler.ru':'8320490aKnTOl',
'ppnzdnsaex@rambler.ru':'5946797PCCQbt',
'xgfwhtiodv@rambler.ru':'1076982D2fVan',
'jtbkavwonp@rambler.ru':'2167743FHBnvK',
'jhgnpipwzi@rambler.ru':'0213954Bb6HLN',
'jfnbeyfmap@rambler.ru':'1833567Xfs3Zz',
'jzpvhqpeou@rambler.ru':'2582828Fqk74i',
'zkoyaouflp@rambler.ru':'0837359dfuJlw',
'xjlijveaic@rambler.ru':'0433010ACosxN',
'fgqkunnxuf@rambler.ru':'7050015TdukKM',
'wjujeqszmu@rambler.ru':'6801665tMQsNw',
'myfdfokpcq@rambler.ru':'9580174PIIaDB',
'dbwzzwreaw@rambler.ru':'4503607jKRRxg',
'kzjffhsqzm@rambler.ru':'7541663G4h8ff',
'ogwwxhodgp@rambler.ru':'9026462cBffsb',
'orbqllwfic@rambler.ru':'7731849gMxIRX',
'lkjryvlrkk@rambler.ru':'4584518olcMQd',
'kcwzjfymsg@rambler.ru':'2697206gH7N2j',
'mpidmygqpw@rambler.ru':'8743805dkRTHf',
'upuvifnpgv@rambler.ru':'8995521oep4fI',
'daktrhbkhx@rambler.ru':'7299608dROBrL',
'hsgcdmawhg@rambler.ru':'9049438FM4AwM',
'izyqvsqgyb@rambler.ru':'5061241OrRQvL',
'jmakpgklid@rambler.ru':'6306172L1vo7F',
'vojzlsygaw@rambler.ru':'68760161Y5Qc1',
'xissuvpdsw@rambler.ru':'8463274QCOysy',
'bfrqorylrl@rambler.ru':'7007968e6zR4D',
'ussakdyclz@rambler.ru':'9126092iyxMtf',
'dlvnuoywwi@rambler.ru':'6650255RQm6PZ',
'kwhypobcqy@rambler.ru':'6753512Zu3QqH',
'ijzhqfpxfd@rambler.ru':'9982131JljUpU',
'onjukiabwr@rambler.ru':'9999847KmBCcq',
'axwoyxhehh@rambler.ru':'5593617efqURG',
'ktcbvgmedu@rambler.ru':'6584452BrQ969',
'oeljddjwqv@rambler.ru':'7386064fCZMlz',
'mddougbwlb@rambler.ru':'6873332TIeG8F',
'tpocbfvyre@rambler.ru':'9675226LFKwRO',
'pqmsonwrrx@rambler.ru':'2415353VkimGL',
'lzpvenpnur@rambler.ru':'4494046oos6kD',
'evsrczefvq@rambler.ru':'1981259DsjrsG',
'dkebyytjrl@rambler.ru':'5720478lk3u9X',
'bdmxcbyjgt@rambler.ru':'7240932V5fVZR',
'tpzaoqtayx@rambler.ru':'9676101I3Af84',
'kcujemkfnl@rambler.ru':'6632444LCeeuA',
'cpkaqjxlaq@rambler.ru':'8158799QlPzh8',
'omlllacuhf@rambler.ru':'1984022BFd4qb',
'kashdhmtvv@rambler.ru':'390755782Rn04',
'imqqmtuggk@rambler.ru':'9357633G6MyYn',
'uaiodcrerw@rambler.ru':'2461236zuhlDx',
'oqputgndap@rambler.ru':'20692247SGS8a',
'gbqlutzdca@rambler.ru':'9768268oRiSSw',
'ktesatgssv@rambler.ru':'0684725Mf7VKP',
'jiynakjgyd@rambler.ru':'3637610o5Kl4P',
'pmqkykszvg@rambler.ru':'5466953jvGECw',
'sxpqnbxfgt@rambler.ru':'4265394mLYBoX',
'owlatdcvap@rambler.ru':'68425495iJVl4',
'zivdifdmja@rambler.ru':'5017633pews8P',
'iigbhtwffd@rambler.ru':'0158311HUDci2',
'iqolabntmj@rambler.ru':'3696752WtpCBQ',
'udxkikhenc@rambler.ru':'5230944pVpJa1',
'tdainafogs@rambler.ru':'1479817xdFEa3',
'ddhavbgovc@rambler.ru':'35963964uL6Zx',
'dyxxnlddri@rambler.ru':'9835924OFo82U',
'szqhbtahdj@rambler.ru':'9732972Pf7YVX',
'pheilxtzdp@rambler.ru':'3798892ibIhLo',
'guruesnrny@rambler.ru':'1127416a5kN1S',
'canlrwmbtz@rambler.ru':'4495454pfHMxR',
'bviylhwmpg@rambler.ru':'06152842r2KmG',
'tjqmzvvflj@rambler.ru':'63963647Gl8FG',
'ktqwcmuazg@rambler.ru':'69655371OYt77',
'mbyinljbwq@rambler.ru':'5072263iMw2V4',
'lmyjnbydqx@rambler.ru':'34786225dlQ55',
'lxsfwyruiy@rambler.ru':'9489974ssFXqn',
'wzwgcufsoo@rambler.ru':'5826393KfInE7',
'vvbuqwqied@rambler.ru':'4249236pewtC9',
'gqwirofmjf@rambler.ru':'9283282nbQ5GK',
'vqevacjnsv@rambler.ru':'4899725kM8rKT',
'effhddiqal@rambler.ru':'1512943nrY5TN',
'qrznkghzmx@rambler.ru':'1741706Kwrx4H',
'ogusnctnhf@rambler.ru':'2394265lm1Hc9',
'kqvlzvqazc@rambler.ru':'1717008paBOnL',
'daowvtpzek@rambler.ru':'2346534Jp8NHl',
'wbbipzhzyw@rambler.ru':'0543120bJl0Ly',
'rgpbonfqhj@rambler.ru':'3976206M39T8v',
'bmoouqbpxl@rambler.ru':'0961594LTt87j',
'iruxmqpkpo@rambler.ru':'6742659p9KCnW',
'xjzaxqyscz@rambler.ru':'1813628QLnV8k',
'cxzguplstz@rambler.ru':'0472468DITsU2',
'zmutrpskzc@rambler.ru':'9061032Q8XkOc',
'lihtyubtis@rambler.ru':'9067530mwE2Z4',
'uquacqlvrh@rambler.ru':'4995515zgvYk2',
'dxdcwfjkwr@rambler.ru':'0997427IdH9If',
'mylkzncdqz@rambler.ru':'0554174SF6hxH',
'xozdfwxdge@rambler.ru':'1594107UC4cgp',
'qxlskakyrw@rambler.ru':'8329586GRn1yg',
'sqjmzkqplu@rambler.ru':'7977820Rg4Cug',
'kiowipszrh@rambler.ru':'7440327xnshaY',
'yvcrwkrqkt@rambler.ru':'2188228LqV5iL',
'konxlfvxck@rambler.ru':'8001466E1E0pt',
'eeucoepqwx@rambler.ru':'4221996BHGqkQ',
'rbwnajwssb@rambler.ru':'4418291q0pO9Q',
'itdgtxpyeb@rambler.ru':'0510139bJgNxi',
'bavuuusibh@rambler.ru':'2133928qDHF3K',
'cssgkgwhqa@rambler.ru':'959014174qXG3',
'grczehsbgy@rambler.ru':'1833927GccUgh',
'tyqpgkrbna@rambler.ru':'3223661odePym',
'qezgkdoceq@rambler.ru':'1749341rGotmB',
'erdbokiyrq@rambler.ru':'1240186YA1lCN',
'mfyosvypfx@rambler.ru':'1529362HjySLq',
'vkeobbnpfh@rambler.ru':'57391160fYOkj',
'jqfzgmsoke@rambler.ru':'1665323tNhxlq',
'jrfckizumd@rambler.ru':'30295639Cn7jn',
'tdtofzbxyc@rambler.ru':'9432737zEA3Rb',
'tlolhafizf@rambler.ru':'8187560T7iX8Z',
'fbgtygfvbo@rambler.ru':'4817024n9Yryi',
'kbfcsxpand@rambler.ru':'4797454CkXl1P',
'fcyihdhjzp@rambler.ru':'7845590y1Zuno',
'uvjdqhnpyy@rambler.ru':'2131196Dt7lht',
'jwfckuaxnu@rambler.ru':'8383081Q2nlnM',
'oofbwmgsvu@rambler.ru':'4079597yfVFqq',
'wiwortjxrd@rambler.ru':'8492478BXG5Of',
'acydvhsizp@rambler.ru':'6810797R0lapH',
'exhizlkrsq@rambler.ru':'0349949mrAsUY',
'cqawqlpwuf@rambler.ru':'8359817P9sAAi',
'ypdcseqdes@rambler.ru':'2980191OengK3',
'hhatkdcenx@rambler.ru':'1871876PG0TbF',
'flnszhoont@rambler.ru':'4640903S67ouF',
'tnacdyfsau@rambler.ru':'5064257z8LEO8',
'kvitchuijs@rambler.ru':'2285873wrTvpX',
'rzxnzrtylp@rambler.ru':'5233630N0nFHz',
'czxunsubhz@rambler.ru':'7932502muEukG',
'ihczltsfju@rambler.ru':'593973230tErH',
'wfxvwrtejt@rambler.ru':'6934348uLPgJ1',
'xbritillug@rambler.ru':'7009776fD828o',
'oyjtzfmmqz@rambler.ru':'8690848XsuO2j',
'oralbqbocz@rambler.ru':'3982484XIPVIp',
'nuumlqqiyg@rambler.ru':'6007529rJ6RXX',
'tzwjqorfiz@rambler.ru':'1543768F9euIT',
'yeprgtztqx@rambler.ru':'1737744Rz0pw3',
'xedhaqmvyi@rambler.ru':'5554244rGYYJW',
'xzvooqfbnz@rambler.ru':'2956950VviMdt',
'deeaqacscw@rambler.ru':'2542396q2F1vg',
'qyyaoxpilq@rambler.ru':'0910846wXTNt8',
'jffwkmwvrf@rambler.ru':'12691397ebbrD',
'xxasmxczsq@rambler.ru':'2617790dyZFC3',
'rdpnpxanbh@rambler.ru':'6363250lOijjL',
'jgyloelzpy@rambler.ru':'9269063hjsjID',
'szyumzwsne@rambler.ru':'0663226qHamTE',
'lqrvzdoczi@rambler.ru':'00480808p6BGZ',
'ozaorfdyvy@rambler.ru':'8080035QpzthE',
'cckkcithvw@rambler.ru':'8084572djPEZt',
'ijnlscnubk@rambler.ru':'7096542Eu1BrB',
'ontxnfpjxg@rambler.ru':'9866476ZvOowy',
'ysnhvdfcvb@rambler.ru':'9032549xeTYnL',
'rsjhdghdar@rambler.ru':'89983129e1G3H',
'ckadwlpvoz@rambler.ru':'6917106LYUZRi',
'damfwdmcxm@rambler.ru':'2256483yrWm2s',
'rocjdlzvfo@rambler.ru':'9002232hJYz4O',
'bytvkosxrg@rambler.ru':'4931484mM4S0x',
'zxxvlwixuc@rambler.ru':'5760846TFhsE9',
'aukobhqatt@rambler.ru':'9479685vzdz6Q',
'imkkquvcfc@rambler.ru':'0037310i4mAW0',
'fqijztsauv@rambler.ru':'3054418WoCFIU',
'lvjjrickmi@rambler.ru':'6379625aMCvp5',
'wwtxouknmm@rambler.ru':'8052749CQvnQj',
'vsgwnluvxr@rambler.ru':'7627990UamGZK',
'ntwxumqbsq@rambler.ru':'5364758Xtovje',
'dxnmommdnv@rambler.ru':'13248931vzKcM',
'cejrbnmxwn@rambler.ru':'2394289XNrfhO',
'rxwurlxlhh@rambler.ru':'7621026pa5PAj',
'yagaxmnqmp@rambler.ru':'9852439OHirOz',
'pozdxpmvks@rambler.ru':'8849569otz4zA',
'fkaftmhfzl@rambler.ru':'9182968tV7DsJ',
'edacbkidcf@rambler.ru':'0846668ovtFp4',
'mgznxqcupe@rambler.ru':'2819234fnwm4D',
'koawlypkhu@rambler.ru':'3140303oixYrO',
'umoowzfnxj@rambler.ru':'4955797XqdCwO',
'julxqsixdf@rambler.ru':'5524135Uw0f4G',
'pdozgcnwxk@rambler.ru':'9015009amfO9x',
'tsuhjzposh@rambler.ru':'5346622JR1mFI',
'ltgepfikkf@rambler.ru':'9196678SqSrNo',
'rseboxipnu@rambler.ru':'5273881rI53Q4',
'csrrduvhva@rambler.ru':'0197098oKVcgl',
'rnronnawvy@rambler.ru':'5904151bLInb3',
'rizztpwxyd@rambler.ru':'2987451FcdS9W',
'lpkooejmvn@rambler.ru':'60126542fjqTr',
'cvqhekksqc@rambler.ru':'9797778IDBtEB',
'pjqcttofdo@rambler.ru':'2388998PnjxXu',
'wgcopmhxgh@rambler.ru':'9358453IMyU8y',
'opaquxfpts@rambler.ru':'7561482OZeKI4',
'eaadnycsts@rambler.ru':'6416827JHSDrt',
'laonvtjfel@rambler.ru':'7560427uY24i2',
'xnhmnupwzr@rambler.ru':'0051569GHG6u5',
'shwnuhgqqg@rambler.ru':'4351266KnZn4V',
'dyiujjtnew@rambler.ru':'3980109iwPLPY',
'iwqjkfelvu@rambler.ru':'4863666lH6V3F',
'zthjgxtrpg@rambler.ru':'8369557WxoHo7',
'ojqtyvwncq@rambler.ru':'7256338Mv7n3t',
'hjnsizlgrm@rambler.ru':'8110884EZeyQN',
'kahzgsmkmt@rambler.ru':'0671533VIPWwu',
'kkrcdhrrlo@rambler.ru':'3389329h61aBP',
'sfeqfkurdt@rambler.ru':'2925887SxhsLr',
'ofaqyrsvuh@rambler.ru':'8560532Y4y9ST',
'dauzyaogpz@rambler.ru':'7525890u5k6fY',
'lpxahsdzse@rambler.ru':'8786157vOA06e',
'wwfhbxmsok@rambler.ru':'7143633fR8nVD',
'mwcgsgjfuk@rambler.ru':'6217831LCupHU',
'tjvramifwa@rambler.ru':'2757277idtpdI',
'mnglvhevjd@rambler.ru':'16070642NbiNv',
'fmyuigwxzb@rambler.ru':'02393808PjTDl',
'eyoadncsuz@rambler.ru':'9508621ADxNXJ',
'rjwzqnmtym@rambler.ru':'10304919ONiwi',
'kjjxdenroa@rambler.ru':'1945719Pd1KpX',
'qizipqicyk@rambler.ru':'75748031V2Yvq',
'psdapkcwlo@rambler.ru':'0738153oxxK6l',
'yivgugcrmv@rambler.ru':'0717090HGXo4m',
'rfmntxpdli@rambler.ru':'7475026YLuOVd',
'jzyhkqzrwg@rambler.ru':'32829246ADDDy',
'hsgcxbjpmw@rambler.ru':'5925366KieMqr',
'onvubjifqd@rambler.ru':'8025909RO2wjU',
'yojdtnotoh@rambler.ru':'3778117YQ5icX',
'dppeqqtnid@rambler.ru':'5383257QEzNWG',
'mmzlvrmnja@rambler.ru':'7097422ifCSZU',
'ynzxuwcogt@rambler.ru':'3439942j0bDR6',
'jzyteqvijn@rambler.ru':'4350877lnGya2',
'vhzjmmtlaa@rambler.ru':'0364214JbqVTT',
'fgfjxwridh@rambler.ru':'25963867kQxJ5',
'szyumzwsne@rambler.ru':'0663226qHamTE',
'lqrvzdoczi@rambler.ru':'00480808p6BGZ',
'ozaorfdyvy@rambler.ru':'8080035QpzthE',
'cckkcithvw@rambler.ru':'8084572djPEZt',
'ijnlscnubk@rambler.ru':'7096542Eu1BrB',
'ontxnfpjxg@rambler.ru':'9866476ZvOowy',
'ysnhvdfcvb@rambler.ru':'9032549xeTYnL',
'rsjhdghdar@rambler.ru':'89983129e1G3H',
'ckadwlpvoz@rambler.ru':'6917106LYUZRi',
'damfwdmcxm@rambler.ru':'2256483yrWm2s',
'rocjdlzvfo@rambler.ru':'9002232hJYz4O',
'bytvkosxrg@rambler.ru':'4931484mM4S0x',
'zxxvlwixuc@rambler.ru':'5760846TFhsE9',
'aukobhqatt@rambler.ru':'9479685vzdz6Q',
'imkkquvcfc@rambler.ru':'0037310i4mAW0',
'fqijztsauv@rambler.ru':'3054418WoCFIU',
'lvjjrickmi@rambler.ru':'6379625aMCvp5',
'wwtxouknmm@rambler.ru':'8052749CQvnQj',
'vsgwnluvxr@rambler.ru':'7627990UamGZK',
'ntwxumqbsq@rambler.ru':'5364758Xtovje',
'dxnmommdnv@rambler.ru':'13248931vzKcM',
'cejrbnmxwn@rambler.ru':'2394289XNrfhO',
'rxwurlxlhh@rambler.ru':'7621026pa5PAj',
'yagaxmnqmp@rambler.ru':'9852439OHirOz',
'pozdxpmvks@rambler.ru':'8849569otz4zA',
'fkaftmhfzl@rambler.ru':'9182968tV7DsJ',
'edacbkidcf@rambler.ru':'0846668ovtFp4',
'mgznxqcupe@rambler.ru':'2819234fnwm4D',
'koawlypkhu@rambler.ru':'3140303oixYrO',
'umoowzfnxj@rambler.ru':'4955797XqdCwO',
'julxqsixdf@rambler.ru':'5524135Uw0f4G',
'pdozgcnwxk@rambler.ru':'9015009amfO9x',
'tsuhjzposh@rambler.ru':'5346622JR1mFI',
'ltgepfikkf@rambler.ru':'9196678SqSrNo',
'rseboxipnu@rambler.ru':'5273881rI53Q4',
'csrrduvhva@rambler.ru':'0197098oKVcgl',
'rnronnawvy@rambler.ru':'5904151bLInb3',
'rizztpwxyd@rambler.ru':'2987451FcdS9W',
'lpkooejmvn@rambler.ru':'60126542fjqTr',
'cvqhekksqc@rambler.ru':'9797778IDBtEB',
'pjqcttofdo@rambler.ru':'2388998PnjxXu',
'wgcopmhxgh@rambler.ru':'9358453IMyU8y',
'opaquxfpts@rambler.ru':'7561482OZeKI4',
'eaadnycsts@rambler.ru':'6416827JHSDrt',
'laonvtjfel@rambler.ru':'7560427uY24i2',
'xnhmnupwzr@rambler.ru':'0051569GHG6u5',
'shwnuhgqqg@rambler.ru':'4351266KnZn4V',
'dyiujjtnew@rambler.ru':'3980109iwPLPY',
'iwqjkfelvu@rambler.ru':'4863666lH6V3F',
'zthjgxtrpg@rambler.ru':'8369557WxoHo7',
'ojqtyvwncq@rambler.ru':'7256338Mv7n3t',
'hjnsizlgrm@rambler.ru':'8110884EZeyQN',
'kahzgsmkmt@rambler.ru':'0671533VIPWwu',
'kkrcdhrrlo@rambler.ru':'3389329h61aBP',
'sfeqfkurdt@rambler.ru':'2925887SxhsLr',
'ofaqyrsvuh@rambler.ru':'8560532Y4y9ST',
'dauzyaogpz@rambler.ru':'7525890u5k6fY',
'lpxahsdzse@rambler.ru':'8786157vOA06e',
'wwfhbxmsok@rambler.ru':'7143633fR8nVD',
'mwcgsgjfuk@rambler.ru':'6217831LCupHU',
'tjvramifwa@rambler.ru':'2757277idtpdI',
'mnglvhevjd@rambler.ru':'16070642NbiNv',
'fmyuigwxzb@rambler.ru':'02393808PjTDl',
'eyoadncsuz@rambler.ru':'9508621ADxNXJ',
'rjwzqnmtym@rambler.ru':'10304919ONiwi',
'kjjxdenroa@rambler.ru':'1945719Pd1KpX',
'qizipqicyk@rambler.ru':'75748031V2Yvq',
'psdapkcwlo@rambler.ru':'0738153oxxK6l',
'yivgugcrmv@rambler.ru':'0717090HGXo4m',
'rfmntxpdli@rambler.ru':'7475026YLuOVd',
'jzyhkqzrwg@rambler.ru':'32829246ADDDy',
'hsgcxbjpmw@rambler.ru':'5925366KieMqr',
'onvubjifqd@rambler.ru':'8025909RO2wjU',
'yojdtnotoh@rambler.ru':'3778117YQ5icX',
'dppeqqtnid@rambler.ru':'5383257QEzNWG',
'mmzlvrmnja@rambler.ru':'7097422ifCSZU',
'ynzxuwcogt@rambler.ru':'3439942j0bDR6',
'jzyteqvijn@rambler.ru':'4350877lnGya2',
'vhzjmmtlaa@rambler.ru':'0364214JbqVTT',
'fgfjxwridh@rambler.ru':'25963867kQxJ5',
}
receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def logo():
    
    cprint("Snoser ot Vasi | by @glavniyskamer and @DedSecAccount " , "red")


def menu():
    print("1. СНОСUНГ АКК0В")
    print("2. СНОСUНГ КАНАЛ0В")
    print("3. СНОСUНГ Б0Т0В")
    print("4. СНОСUНГ ЧАТОВ")
    cprint("----------------------------------" , "black")
    choice = input("ВbIБUРАЙ: ")
    cprint("----------------------------------" , "black")
    return choice
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.rambler.ru', 25)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    logo()
    choice = menu()

    if choice == '1':
        print("1. ЗА СПАМ, РЕКЛАМУ")
        print("2. ЗА ДОКСUНГ")
        print("3. ЗА ТРОЛЛUНГ(ОСК)")
        print("4. ПР0ДАЖА/РЕКЛАМА НАРК0ТЫ")
        print("5. КУРАТ0РСТВО В НАРК0ШОПЕ")
        print("6. ПРОДАЖА ЦП")
        print("7. ВbIМ0ГАНUЕ UНТUМНЫХ ФОТО У НЕСОВЕРШЕННОЛЕТНUХ")
        print("8. УГНЕТАНUЕ НАЦИИ")
        print("9. УГНЕТАНUЕ РЕЛUГUU")
        print("10. РАСПР0СТР0НЯЕТ РАСЧЛЕНЕНКУ")
        print("11. РАСПР0СТР0НЯЕТ ЖUВОДЕРКУ")
        print("12. РАСПР0СТР0НЯЕТ ПОРНУХУ")
        print("13. СУТЕНЕР(ШЛЮХ ПРОДАЕТ)")
        print("14. ПРUЗЫВ К САМ0ВbIПUЛУ")
        print("15. ПРUЗbIВ К ТЕРР0РУ")
        print("16. УГРОЗbI СВАТА U ТП")
        print("17. УГРОЗbI РАСПРАВbI")
        print("18. СНОС СЕССИЙ")
        print("19. С ВUРТ Н0МЕРОМ")
        print("20. С ПРEМКОЙ")
        print("21. ПР0СТ0 СН0С (НЕ ЭФФЕКТUВЕН)")
        cprint("----------------------------------" , "black")
        comp_choice = input("ВbIБUРАЙ: ")
        cprint("----------------------------------" , "black")

        if comp_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17" ]:
            print("СЛЕДУЙ УКАЗАНUЯМ")
            username = input("USERNAME: ")
            id = input("TG ID: ")
            chat_link = input("CCbIЛКА НА ЧАТ: ")
            violation_link = input("ССbIЛКА НА НАРУШЕНUЕ В ЧАТЕ: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "4": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который продает и рекламирует наркотические вещества. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользоателю путем блокировки его аккаунта.",
                "5": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который привлекает людей в сферу нарко-бизнеса. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировни его аккаунта.",
                "6": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который продает порнографические материалы с участием несовешеннолетних. Его юзернейм - {username}, его айди {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "7": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который вымогает фото интимного характера у несовершенно летних, его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры к данному пользователю путем блокировки его аккаунта.",
                "8": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который угнетает нацию и разжигает конфликты. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователб=ю путем блокировки его аккаунта.",
                "9": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который угнетает религию и разжигает конфликты. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользоателю путем блокировки его аккаунта.",
                "10": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который распростроняет видео и фото шокирущего контента с убийством людей. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "11": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который распростроняет видео и фото шокирующего контента с убийством животных. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "12": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который распростроняет фото и видео порнографического типа. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "13": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который продает услуги проституции. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "14": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который отправляет сообщения которые приводят людей к суициду. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примине меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "15": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который отправляет сообщения с призывом к террризму. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "16": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который угрожает людям распростронением личной информации. Его юзернейи - {username}, его айди {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "17": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который угрожает людям расправой. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["18", "21"]:
            print("СЛЕДУЙ УКАЗАНUЯМ")
            username = input("USERNAME: ")
            id = input("TG ID: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "18": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии",
                "21": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя с подозрительной активностью на аккаунте. Его юзернейм - {username}, его айди - {id}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки аккаунта."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["19", "20"]:
            print("СЛЕДУЙ УКАЗАНUЯМ")
            username = input("USERNAME: ")
            id = input("TG ID: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "19": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "20": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 14888
                    time.sleep(5)


    elif choice == "2":
        
        print("1. С ЛUЧНЫМU ДАННЫМU")
        print("2. С ЖUВОДЕРСТВ0М ")
        print("3. С ДЕТСКUМ П0РНО")
        print("4. ДЛЯ КАНАЛ0В ТИПА ПРАЙСОВ")
        print("5. С РАСЧЛЕНЕНК0Й")
        print("6. РУЛЕТКU (КАЗUК)")
        print("7. НАРК0-Ш0П")
        print("8. ПРUЗbIВ К ТЕРРОРУ")
        print("9. ПРUЗbIВ К САМ0ВbIПUЛУ")
        print("10. РАЗЖUГАНUE НЕНАВUCTU")
        print("11. ПРОПОГАНДА НАСUЛUЯ")
        print("12. ПРОДАЖА ДЕТСКUХ UНТUМ0К")
        print("13. УГНЕТЕНUЕ НАЦUU")
        print("14. УГНЕТЕНUЕ РЕЛUГUU")
        print("15. С П0РНУХОЙ")
        cprint("----------------------------------" , "black")
        ch_choice = input("ВbIБUРАЙ: ")
        cprint("----------------------------------" , "black")

        if ch_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]:
            channel_link = input("ССbIЛКА НА КАНАЛ: ")
            channel_violation = input("ССbIЛКА НА НАРУШЕНUЕ В КАНАЛЕ: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАCb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте, уважаемый модератор телеграмма. хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "5": f"Здравствуйте, уважаемая поддержка Телеграмма. На вашей платформе я нашел канал который распространяет шокирующие кадры убийства людей. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "6": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который распростроняет рулетки или же казино, которые запрещены на территории РФ статьей 171 УКРФ. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "5": f"Здравствуйте, уважаемая поддержка Телеграмма. На вашей платформе я нашел канал который распространяет шокирующие кадры убийства людей. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "7": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который пропогондирует продажу наркотических веществ, которые запрещены на территории РФ статьей 228.1 УКРФ. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "8": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который призывает людей к террору что запрещено на территории РФ статьей 205.2 УКРФ. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "9": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который призывает людей к суициду что запрещено на территории РФ статьей 110.1 УКРФ. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "10": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который разжигает ненависть в сторону определенных людей или же групп лиц. Ссылка на канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "11": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который пропогандирует насилие что запрещено на территории РФ статьей 282 УКРФ. Ссылка на канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "12": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который занимается продажей детских интимных фото что запрещено на территории РФ статьей 242.1 УКРФ. Ссылка на канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "13": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который пропогондирует угнетение нации что запрещено на территории РФ статьей 282 УКРФ. Ссылка на канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "14": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который пропогондирует угнетение религии что запрещено на территории РФ статьей 148 УКРФ. Ссылка на канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "15": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который пропогонирует порнографические материалы. Ссыока на канал - {channel_link}, Ссылка на нарушение - {channel_violation}. Просьба заблокировать данный канал."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 100000
                    time.sleep(5)


    elif choice == "3":
        print("1. ГЛА3 Б0ГА ")
        print("2. ТUПА СUНЕГ0 КUТА")
        print("3. ПР0ДАЖА ЦП")
        print("4. М0ШЕННИЧЕСКUЕ СХЕМЫ")
        print("5. СПАМ, РЕКЛАМА")
        print("6. ШАНТАЖ")
        print("7. UЗВРАЩЕНUЯ(СНАФФ,ЦП U ТП)")
        cprint("----------------------------------" , "black")
        bot_ch = input("ВbIБUРАЙ: ")
        cprint("----------------------------------" , "black")

        if bot_ch in ["1", "2", "3", "4", "5", "6", "7"]:
            bot_user = input("USERNAME BOTA: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "2": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который путем заданий приводит людей к суициду что запрещено на территории РФ статьей 110.1 УКРФ. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "3": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который продает порнографические материалы с участием лиц не достигших совершеннолетия, что запрещено на территории РФ статьей 242.1 УКРФ. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "4": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который занимается мошенническими схемами и обманывает людей на деньги что запрещено на территории РФ статьей 159 УКРФ. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "5": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который рассылает навязчивую рекламу и спамит ей в чатах. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "6": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который путем шантажа вымогает из людей деньги, личные данные и другие вещи. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "7": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который распростроняет видео шокируещего контента по типу детского порно и расчленения людей. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
             }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 10000
                    time.sleep(5)
        
    elif choice == "4":
        print("1. ПРОСТО СНОС(НЕ ЭФФЕКТUВЕН)")
        print("2. СПАМ/РЕКЛАМА")
        print("3. ЗА АВУ UЛU НАЗВАНUЕ")
        print("4. ПР0П0ГАНДА НАСИЛИЯ U ТП")
        print("5. НАКРУТКА")
        print("6. ОСКU В ЧАТЕ")
        cprint("----------------------------------" , "black")
        bottik = input("ВbIБUРАЙ: ")
        cprint("----------------------------------" , "black")

        if bottik in ["1", "2", "3", "4", "5"]:
            user_chat = input("ССbIЛКА НА ЧАТ: ")
            id_chat = input("TG ID ЧАТА: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу с подозрительной активностью. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону данной группы и заблокируйте ее.",
                "2": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой проходят спам-рассылки. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее.",
                "3": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой стоит вызывающая аватарка и имя, разжигающее конфликты. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее.",
                "4": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой пропогондируется насилие и другие подобные жестокости. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее",
                "5": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой происходит накрутка подписчиков. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее"
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bottik]
                    comp_body = comp_text.format(user_chat=user_chat.strip(), id_chat=id_chat.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на группу телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 10000
                    time.sleep(5)     

        elif bottik == "6":
            username_chat = input("ССbIЛКА НА ЧАТ: ")    
            idtg_chata = input("TG ID CHATA: ")   
            ssilka = input("ССbIЛКА НА НАРУШЕНUЕ: ")
            cprint("----------------------------------" , "black")  
            cprint("ATAKA НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "6": f"Здравствуйте, уважаемая поддержка телеграмма. Я нашел группу с которой оскорбляют людей и используют ненормативную лексику в их сторону. Ссылка на группу - {username_chat}, Айди группы - {idtg_chata}, Ссылка на нарушение - {ssilka}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее"
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bottik]
                    comp_body = comp_text.format(username_chat=username_chat.strip(), idtg_chata=idtg_chata.strip(), ssilka=ssilka.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на группу телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 10000
                    time.sleep(5)     

  
if __name__ == "__main__":
    main()
    