########################################################List Comprehensions
# x = 1
# y = 1
# z = 1
# n = 2


# per= [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

# newlist=[]
# for i in range(len(per)):
#     if sum(per[i])!=n:
#         if per[i][0]<=x and per[i][1]<=y and per[i][2]<=z:
#             newlist.append(per[i])

# print(newlist)



# listx = range(x+1)
# listy = range(y+1)
# listz = range(z+1)
# result = [[i,j,k] for i in listx for j in listy for k in listz if sum([i,j,k])!=n]
# print(result)


#########################################################Find the Runner-Up Score!

# n = int(input())
# arr = map(int, input().split())

# scores=[i for i in arr]
# setscores= set(scores)
# listscores= list(setscores)
# listscores.sort()


# q=1
# for i in range(listscores[-1]-listscores[-2]):
#     if len(listscores)>2:
#         if (listscores[-1]-q) in listscores:
#             print(listscores[-1]-q)
#             break
#         else:
#             q+=1
#     else:
#         print(min(listscores))
#         break



#########################################################Nested Lists

# records = []

# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     records.append([name,score])


# points=[]

# for ind,val in enumerate(records):
#     points.append(val[1])
#     # if val[1]>max:
#     #     max=val[1]
#     #     records.remove(val)

# names=[]
# points=list(set(points))
# points.sort()
# for ind,val in enumerate(records):
#     if points[1]==val[1]:
#         names.append(val[0])
# names.sort()

# for i in names:
#     print(i)



#########################################################Finding the percentage

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()

# for key,val in student_marks.items():
#     if query_name==key:
#         a=sum(val)/3
#         print(f'{a:.2f}')


##########################################################String Formatting


# decli=[]
# hexli=[]
# octli=[]
# binli=[]

# number=17

# lastbinli=[]
# lastoctli=[]
# lasthexli=[]
# lastdecli=[]


# for i in range(1,number+1):
#     decli.append(str(i))
#     hexli.append(str(hex(i)[2:].upper()))
#     octli.append(str(oct(i)[2:].upper()))
#     binli.append(str(bin(i)[2:].upper()))


# for i in range(len(binli)):
#     b=len(binli[-1])-len(binli[i])
#     if b>0:
#         a=b*' '
#         lastbinli.append(a+binli[i].strip())
#     else:
#         a=(b-1)*' '
#         lastbinli.append(a+binli[i].strip())


# for i in range(len(octli)):
#     b=len(binli[-1])-len(octli[i])
#     if b>0:
#         a=b*' '
#         lastoctli.append(a+octli[i].strip())
#     else:
#         a=(b-1)*' '
#         lastoctli.append(a+octli[i].strip())



# for i in range(len(hexli)):
#     b=len(binli[-1])-len(hexli[i])
#     if b>0:
#         a=b*' '
#         lasthexli.append(a+hexli[i].upper().strip())
#     else:
#         a=(b-1)*' '
#         lasthexli.append(a+hexli[i].upper().strip())



# for i in range(len(decli)):
#     b=len(binli[-1])-len(decli[i])
#     if b>0:
#         a=b*' '
#         lastdecli.append(a+decli[i].strip())
#     else:
#         a=(b-1)*' '
#         lastdecli.append(a+decli[i].strip())


# v = [lastdecli,lastoctli,lasthexli,lastbinli]


# for i in range(len(v)):
#     for j in range(len(v[i])):
#         if i==0:
#             print(v[i][j] , v[i+1][j], v[i+2][j], v[i+3][j])







#####################################################################Alphabet Rangoli


# print(len("------------------j------------------"))
# print(len("--------e--------"))
# print(len('----c----'))
# a="j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j"
# print(a.count('-'))
# q=3
# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']






# a= "abcdefghijklmnopqrstuvwxyz"
# def print_rangoli(size):
#     rowcount = 2*size - 1
#     for i in range(rowcount):
#         letters = a[abs(size-i-1):size]
#         dashed = "-".join(letters[::-1]+letters[1:])
#         print(dashed.center((4*size-3),"-"))


# print(print_rangoli(5))

# a="edc"
# print(a[:-1])

# size=5
# n_rows = 2 * size - 1
# print(n_rows)




###########################################################Capitalize!
# s=input("Should be Sentence Capitalize: ")
# # b=[]
# # for i in s:
# #     if i==' ':
# #         b.append(i)
# # print(b)

# a=s.split(' ')
# d=[]
# b=''
# print(a)


# for i in range(len(a)):
#     if a[i].isalpha():
#         a[i]=a[i].lower().capitalize()
#         # print(a[i])
#     d.append(a[i])

# print(d)
# for i in d:
#     if ' 'in d:
#         if i==' ':
#             b+=' '
#     else:
#         i+=' '
    
#     b+=i

# print(b)


#################################################################The Minion Game


# k, s = 0, 0
# string = "BANANA"

# for i in range(len(string)):
#     if string[i] in 'AEUIO':
#         k += len(string) - i
#     else:
#         s += len(string) - i

# if k > s:
#     print('Kevin', k)
# elif s > k:
#     print('Stuart', s)
# else:
#     print('Draw')


###################################################################Merge the Tools!
# k=3452

# string="KYQYTWXTDQXWDLKIXNWIITFBLIHRNGDZGVYCRXVWNUVSFFACUXMCSTFFBNWQVBQCWOEPNBOAVJUCOUGITSMNLSUOFRFAUXETNIKAJYCEJWIXSOHMGUBTOWKVPPXJOCEBKPDWNFCXDLWVZEJIALBOJLLYCIJQKOTXDWTSDVRIGOEIUPQUCRKLFVLHFXASNVPSUKKXHCGOSMYMDOIGHUTMPHWWEYORTFJNPVNXZVNTJNFMBPSIJOXAVTXZRNSKTDAKANJAKYTTLBFMSAXCOUCJNBKGPESKHSWJHGJREFKSISGASDCIZHTOKFUBJNLSFIBPQNGWSROCLVCDAHNAQGOALJCUYPOFZPUPEDMYWAAHXDKAMXACFQCQBGMZWAHVRBNYEZWABXJBCVBOSDQZTSPVZDWXFDSZHFXNGTQISZLUVMKPPAPIVGFWKCTRHNQQVPEBJULDVYAQKKGBLXMIDREPVZHFMZVJPZNAVADRZDHJOPNBMZLSQRHOQQTEQQOFSDFNDKGCOQOEFBHUASMSJTIBMDFCUVHOYOBCYKGOAWSHXBDZTPUELEFXINZEIISJYVNWFTNHQHPPJSREKNJXRQUZDVDOFVZDRMBYHOGZYXRHRILBVWYMPUOURRIWPJBIVFGFVOGTLXADHOGCMHRBDFWVYGTPQVXNCGUXUBRGYTLGJRKWADZEIVZJEUAURAJTGERCFIKFDVLNPWJPZITKGUVKPVGGXPADVTGCBQIGOTTDREUTPQFVKCFBZNKXEMAAFICIBMOPGKUZOQUDGZYTDFUDUGAZUCBZNFJQSAFAKBBYRWEYXETBMPEGWGHQKISZOBPIDWINXJORHSRFWKGIZMRXSYOEHIEXLTHPQPCPASGIMXPJJVTJHMGBLWHUELTQHAHZRJOTEXDQWSBGNXPWJXXWUHQASJSBLZCCJRWPQZFMUHSHEJEPHDMDKCDFOWIZVLEGECVUDDIXKDFQMLFVQRYDWEKMCSNZFRGJTDFZGOWSTBIFOOBHHBKDHUPJMDJSWRDSUJRDZNVSRGZHUCODGYHNUYXJDIDCZGUVRNYSAWMTCMDYORBWSKKMJJVORYQSHMNAZOTCKFVORAMISNEKAQYLZUZSUSKDEYEEMXGYEDMYEYGYNMKNDIYEEAXBSHEYHICVHKTMQHKUFSUVGEKJMLQTNNUFWYDEJIBQSVCIEOEMGAHNETYTEOMRDGYAEEGNMJGGEIRLZVXFYEUCXTVEJJXNPWPWAXLMGRUNCLYBHVIFBDJAYHGHQEWGANECMPQTJKILWIOFFWMIBVIZCPJVVHDVVHXJYPEHZMUVUKABJMJKISMMJVHGCKBZTAJSPPBOCYMYIMARZLEJFQXQNHWPRZRNBCFQRIHVGVURHWKIJOTPGRFTYCLRBEGDGLVZWEVEZRVJPIRYWLNFETAEVLXYPEBXRZXNDSSDLPMAXFYWSMBYHBCCPACGGEEXDDLIXFNIUBISHGOBURABSCFJEIQKOWITZVBWCPEWQOQZUEBRXBSQFYBKGRWUNENMBQKDFQCYESXZZYQWBKOHIQRQHNMXUBLXSWDZMFXRXVSYVKVZULGFBZXLOKKKNVIFTLFISEBPBTQZFNYBYEIADGNTSXEFSMLOZSWRYXIASYZXLXAMDJMIRBBJYHQSTDGUXENWBWYTWXSKWVWBGKJXLMILUADPEMKBQZZSVXNUWIESDCVJMEIZTSKNSPEYBOAUQBOLZBFVLLQONLZBQJALDMYWCCWFTYZJAPWZTEUERKVFWWIOGJZJVZHZDEHWCGHCYGDRKYVBKSIIPRYVCZGZYOZCUGAYOKDMQGFCGDFTVQBKHAHLBOKAELEARGYISDWIKCMSFULCKPNRRUCSKOUOAYQTHRBZUAKGCWZJQMLCBATSVXNHOHYOGOHPFLOALYGPXHAPUNSVONQLNDSBKQPSHYHMLYOYWXNTEPLYDDWRQMCDRWGDNXWWWFIJDXICWXXANIZQNXJEJNJCJQFYNDULLFXOEFSACQAPYBHMYQSJDDLPVTNLWKWHPTYTAQVDGVUHZCVZUNJYQWPOPEZMOXVFTTATKVWSTTBUVWTPJCPCZGQQLPEZOAHHVJBHFZAASBUPYNHJSWNTFFJQWORLQYSLITTPVTRNWLFWAMISKVLPBXFXNXKDXDOHYHYTCPJBAOXBAFVKDJCEIHDVGOYGTONRYMLCDUDEKDHKICWLNYRVIXQONQWGHMZFAMHDGNHSQQCYVBMIZFGJEYARPWZYIZDILMMUZVMPORQJSCTTJZDOYDHPZHPKGSURGINGGAXURNFLRYEDAJRAMYROFGYNAUHGDUOJUMFNBKYTIFWIOPKDPBRVHRIJLPQQMGBISGWWQWPZDNJSEWXTXOQHHZQUQILEPONJVJFLHWMLLYFPUEJTSZCBATXTDIXSZMEUVJFFGUSTSZJODUHXVKYYFVRIGQDFDHBASIHACZUWYDMDZUAUGYUNWLXEEALJJMLEUVEZUYVVDIYEEBZMBTZXHWDNZOYKALOXGTWDTTYZDYDHZETBAUAHTEWUSWEVHVSOQQRLJRKNPOWRSSSSMSBHYZBRVIODDGTVYMGHDRWUHTLZLFUZYXHYXKPUSFXXNSSLEZVJSREZMRAZXWZXUIVTSNNLSNIGFDRMEOVWGZXUTZUQYVNUDINXVCIOPTWXYNJCCGAKIZGBAARYVGUAOJYMMICDDYCBNNFRUFDCGKFHKYHIECKSNIGBTIFYIJAWXHPTPTXVFCERAMBEQMYDWFFPPMQYXQWUZLNOGMKLOOFQCGUSSVYPAFGPTWPQOLNOZACFPOTDDYWFEQAZNYQPFWFYVWOLIDBHGGOVUHYZHUHONHNCHDSOBZMYVCKFGNMMTBHOKHPSEWITFVXMAPABOOCMTORBBGNVHWLTFANLXVGCQERSTTWKIYWDMPENVTKCRVYWWLKVHQXZUQSQKQAUOYXCNDRJWCNNZNLXZVSIOSJIIDASTCOJANLQQFBMJQBIENGDIANWSWHBAJVVMMFOZSEQXHEIYGRCTZHDZUCSSLVUUSQGEVXEPBWNJAVJGOLZPSFPOJJIUGDOYTXFQUJFXFUIFSROIENYYUPMDYXXEAOEVNJLJUSGZPRHHIVPPKPNFECKCZKIZYPWNYJWTBEUQXDZIYRXLGKSLMCPLMAMMPIBPRXKVEFNDINLJGIUMTMZHQRVDTHRISTZJSKEWRUABHNKNWEBRSDAJWVOPDFZVYYGTKNRBHRDOHPDDUGWOJWZHSNWXTVSTWAMGNGKUXNKECPJYWHPHEOPYCLVXJPSFRHNFNZBMOMTTBERZMIJSXYQBLNYWESDVZRAOSCBHQUATYTTMCCEZCWCPJAMPUPLUINIBRLKJHKDIDYUFCZGEXIVJKHYFZLBJZJMSXWCEGFMMDHRHIALFIIOVSPARABCBMRULPWQYDCKILDPVDCDOKTLCILVJOAMCRGOGEGEHKQRYUGTZIWNVSYZALVLBXYGOGWWLCDUOTMMPUGPFEEAWFZZSWKUTKCJRYGECLYQGMFWHLNORRQQWRPROBLJMPTFPBJROHJUWOSFBFTTXJLVAAMQDZCPOVWFYFWOPIILWBQAILVFWGDWIPPLRRDFOZLOHJCWTMJSPBSYMNDIVGGDYXQPOTWEVJSCVWYOJHGYKYWWNCGIKONIMEXCZWJUFBWAAWPJFXJPWGLLKTUUIJFWPCAPAJJGNIINEXWMVFBTNPEXIAUSMZQBDRQEACMNKUAQSYCPGGKTVOTFRPYDOQERHXXKZJXLEABYAGNGMXCJNVOEKOJAFQTMNRWMCWXGYAEYITFWSHFIEWOQKYQPOJEBCAPFYOLYOSXZNEVINDQTZGJJGZBUKFXNHOSGCFGTZDSPJPZYURRTXAFEBGAOLABSOVATCHMEMGTYVSWSJOLIQQMSWPGJPJCDGEWILKMAQHYOBUGMITVBMJTIYBUNKYTQCRAQCPQUWOKYIQKTMHUYRPIPSCFEAYUDRWTTLJQIZAIJTUEFEAFVPNMHQTNSRJVLGQERBWBAXLKQIQXMRCJGPVQHPDAINXTVOAMPWQSVDENLUKXLOGUGEMNVRPFENBBDBQUZGMVJQIXNVUYJDURHGHEYWJELKGOLWJNEXIPQSMDPJDBMYSVGZZGYILJVTYGRJVXGFOWYBBNMFOAFHVLIWSGGFSBASKRBFOJLCGLFJYTOPTTYQHGMBPTGHWIZGZCMPLZTTKBDKUTZQPXGWGVZXQHEMPFTOHHFUGYOSBTCYMCOBBUZHRYEHFKUURPKYWRVESJWTEYRQCFSECTNVSUDXEZUWQGWOYRSQCQLGQFZTKTZOMMKEIPEPQANGGLUGDOYHEMQURPPDIOSUDEBNVFCLFPTNBNWGBUPHGFBXWTDGHVBMBEAYJEJQUCFXRBFSYUZGCCGYVJFFGIRJMTHXYSPUUWTNAYFAUGGWKOVGZCNFMGOAAXXAPOULKPYKNDKHLTGWJDEJFRQTXFTZESZUGVFSKEFZJRJXMPTWSZFZSVSPCNRHFQDNOIFAOMCYELVQCQOWRTVJRPAVCRCJKHWAQDAEQEEWPBMRTDNKYKVPBYLDPPMBXKDPOGVEKAAADOTXRJJQTHHXFSAWIPYHZBWNJRTUTTUZKPWDYHTUODRVVTSFKSOKVKZFEVZXQVWAKUELEZHUCYQATKHECWQXGRCMMDMDYKDJFJWLLDHNDXPWJXCLTSLBKNOYRABRKHARSWCDBMRELIBVFDGYYRAKHOIAQMRATUSNSWRUIKYUSBPYFXWFRYPYOXAEJTFENZSGVJCGVCCNETLLSKQJKFJZEJDQDKUSJOAHXCPUHRILMVWEHOOSVZRZLWRQHMIQALZAPOWWHEHTAFYJVOBQNUSARJQYXBQAMQCBGYYODHHFPHQKXSBLMVNFGEFEFYETQIUWGUMLEUSTDJFBDIORDBXKHEQMCWHSEEPKYBYEXSZDBFEENUWTVVDFZTTEPBWVFNHFRFKQYJTBQZIETGXRBCWCXPGOSFJXUQDLWPEWAXXRZFVUNUNOWLTTBBHTIQTDIYOGNUCNUCETJBNXVDNTOIORKXLSPGVYEMETGJGANNVYQLXOOLJCTYUFVHALPVJTJPMSYUULJQMCDJQRUZVQZRXVAXIPVRIEGWYHTTUELGGQQYJMAEEZWCUWZCOUVWBEVZNQUHUHOBXGBGSBNZBLBXJACXXZUYDRZQHUABDQEBWGHQHUPKFSIPVMOSLKSRBRJINJMRZSSXYBQIYHUFACWVQLPCVHVZYEHMOVDPOXPOAFYYOTGOXCLOPASLHNKIRTUHRZZHYQXYVWZLPFAMHNCZOUKXJWFDRZKKALRYBPXYLYKCDMQMZTLPPXNZVUENWQXWCRXFGWETUQVXCLLDGXVYWKZSEDHATGZXXWDFSHYOXVNBJYGPXBPULOOQTVSNDRKBNPIHWHXVCKYLJFDIGUCULQKENCTRWGULVCVULSRQFQDQVGYDDDXOTJUJOOCMWYXRASNONFESVHISQIXTLXJHIDQWTUKPSIHUCWIPBMJYWTSMCQHNPQUXTMWNGGCAQLVTIFKLUUKQNCERULFLBBJWOHLWPQXGDUBNZLZVHLLXPROMCTXFXIELPPJHHINLEQAGBZBLMPICGWOJSLQPUUCLKLSTWHGAXHGZIIKVZUXFQNOKAHZUBDINRAHNINNFWWGFGSAFMZKFMBPMIRJLURZLTGYDVOLSMRXUMZZAYLFMOXAYOLKKEJWYRWDOMOIAIHUUGVWGHCUXBXWPIIZNTXNMWQAIFLJNSDJBZFJIJEFKBDBJNDYGALSWEVHJGSYAXJBYQNGAROMUTQFHTEPVRISVFBGNTEPQPTPGGXIXNWTHMYQFEFBWPVTWYAJRGZHWSYEYWMXLIQSXQKCVQFTFAMCAMNRVOBRIBXIZJFLTXDQQOVLGAENDQRDFFXAVYTEZQMZBUKWTPPJFKULMAZPTQVYXSATSTZRLLSOHEKBUZMBLHNYJOPCGKAGECBWXAQILIYVPJYJKKKWRZWDNLFWYICCKDBIDRSQBRNQCLBMWMKPNISDUYZUGDWSIZANQVFSMTKQEMEAAPQNZKQTIRPQWOJENJREGXYSQIIWUNXUEPIDBAZKUOCQCLXSXOWDNUYDEICZVBVBQFHTGIDCYGSDTRVQGRUTNSZRCBSYCQBUVKNDSTFRBAUURPNZIJVVDUOFXJFZZHVWRKAMFHDGJZDBOQCWZXTCRJHQUNRTWMSPZSBEZELLFQOTGQRHOMJHYSYSFPOBEGRDYUJZBUKGMYCSRVZFIKOIDOAKEOOKUFPUBYWCVIJHJLCAGBHQOVYRKBDQPRCMYRIAPGCKPLUYYWAFZHXNEYGQZKGQBIEABNARTEDKQXKQTKXTRVIYTPOUZXKCHPCJEEAZJFKBFURYHPTAMCYHTNBSKNUREZAKFCKOKWRPSLPBAJCONAVGNYAZLWTSVVCDAORKMLZHWQIYBKMOLHWAHYCUVVMSQRVQFPCUADBYUJWVUIMFRKHYJJUGEHAXAWPFNSZPVANRKJNGTBNMNUMWEGEKPFHPDXVQRWFMZUELFTRYWEKJAWGGCMRURAJUZGKQDRFELLPQEIQCOALQYTXDGQXXQGSSNEKSYRYLCPCIXUKNXWDVPCAXSXVLGPDVVPPTHNFJCJUBDEOACTYSWYPQYMBEDGZZWQSDDZOHKIIONYQRROLPNDGNPHRTQSUMIMRNOFUYQCOFCFWVVILKLTXACOVSIPEQEXFSDZSVDHAFOWBJEOURHRULGPEQHKHLIOFNOZITGIZUECGLSACBRWMZOQQVBZGJNNWDMGXVOYRUCXFUXKXRGJQUAIRDJZOZMMEBSDWGBNAFLIBKSYBYIUVKCMNOODNAPRDHVBPYPPECXHMPIOQQKNCMBRAPUPSLHVSEXHCOYISYSGPAWFQGUUTWLVNHLFSUDM"

# # k=3

# # string = 'AABCAAADA'
# # string = 'AAABCADDE'

# d=[]
# z=0
# l=int(len(string)/k)

# for i in range(l):
#     d.append(list(reversed(string[z:z+k])))
#     z+=k

# empty_list=[]

# for i in range(len(d)):
#     em=[]
#     test=[]
#     for j in range(len(d[i])):
#         em.append(d[i][j])
#         if em.count(d[i][j])>1:
#             em.remove(d[i][j])
#     test=em

#     empty_list.append(test)


# for i in range(len(empty_list)):
#     empty_list[i]=list(reversed(empty_list[i]))



# a=''
# results=[]
# for i in range(len(empty_list)):
#     for j in range(len(empty_list[i])):
#         if len(empty_list[i])>1:
#             a+=empty_list[i][j]
#         else:
#             a+=empty_list[i][j]
#     results.append(a)
#     a=''


# for i in range(len(results)):
#     if '[' in results[i] or ']' in results[i] or "'" in results[i]:
#         results[i]=results[i].replace('[','')
#         results[i]=results[i].replace(']','')
#         results[i]=results[i].replace("'",'')

#     print(results[i])




##############################################################################Validating Email Addresses With a Filter

# a=["@something.com","lar!a@hackerrank.com","brian-23@hackerank.com", "britts_54@hackerrank.com"]


# import string
# numbs = list(range(10))
# alp = list(string.ascii_letters)
# total = numbs+alp+["_",'-']

# correct=[]

# for i in range(len(a)):
#     if '@' in a[i] and '.' in a[i]:
#         at= a[i].index('@')
#         b = a[i].index('.')
#         if at!=0:
#             if len(a[i][b+1:len(a[i])])<=3 and a[i][b+1:len(a[i])].isalpha():
#                         if a[i][at+1:b].isalnum():
#                             correct.append(a[i])


# notd=[]

# for z in range(len(correct)):
#     at= correct[z].index('@')

#     for j in range(len(correct[z][:at])):
#           if not correct[z][j] in str(total): 
#                 notd.append(correct[z])


# for i in correct:
#     if i in notd:
#         correct.remove(i)

# print(correct)



####### same code but optimized by chatgpt 

# def fun(s):
#         if '@' not in s or '.' not in s:
#             return False
        
#         try:
#             at_index = s.index('@')
#             dot_index = s.index('.')
        
#             if at_index == 0:
#                 return False
            
#             # Check username
#             if not all(c in string.ascii_letters + string.digits + '-' + '_' for c in s[:at_index]):
#                 return False
            
#             # Check website name
#             if not all(c in string.ascii_letters + string.digits for c in s[at_index + 1:dot_index]):
#                 return False
            
#             # Check extension
#             if not s[dot_index + 1:].isalpha() or len(s[dot_index + 1:]) > 3:
#                 return False
            
#             return True
#         except ValueError:
#             return False



####################################################Reduce Function

# from fractions import Fraction
# from functools import reduce

# from math import gcd,lcm
# # print(gcd(2,4,8))
# # print(lcm(2,4,6))
# # print(reduce(lambda x, y : x + y,[1,2,3]))

# print(reduce(gcd, [2,4,8],3))  #gcd(3, 2) returns 1 since the greatest common divisor of 3 and 2 is 1.
                               #Next, gcd(1, 4) returns 1 since the greatest common divisor of 1 and 4 is also 1.
                               #Finally, gcd(1, 8) returns 1 since the greatest common divisor of 1 and 8 is 1.

# print(reduce(lambda x, y : x + y, [4,8,12], -3))



# print(Fraction(1,2))

##solved here
# def product(fracs):
#     t = reduce(lambda x, y : x * y, fracs)
#     return t.numerator, t.denominator


# fracs = []
# for _ in range(int(input())):
#     fracs.append(Fraction(*map(int, input().split())))
# result = product(fracs)
# print(*result)



#######################################################Floor, Ceil and Rint


# import numpy

# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# # print(numpy.floor(my_array))           #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]                    # smaller integer
# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# # print(numpy.ceil(my_array) )         #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]             # bigger integer

# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])              
# # print(numpy.rint(my_array))          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]         nearest integer to float (in .5 it belong to bigger integer) 

# numpy.set_printoptions(legacy='1.13')

# # print(numpy.rint(my_array))          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]         nearest integer to float (in .5 it belong to bigger integer) 

# newarr= list(map(float,input().split()))

# newarr= numpy.asarray(newarr)
# print(numpy.floor(newarr))
# print(numpy.ceil(newarr))
# print(numpy.rint(newarr))

# print(numpy.floor(newarray))


