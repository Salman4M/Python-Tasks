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


################################################################Sum and Prod
# print(' ')

import numpy

# my_array = numpy.array([ [1, 2], [3, 4] ])

# print (numpy.sum(my_array, axis = 0)  )       #Output : [4 6]
# print (numpy.sum(my_array, axis = 1) )        #Output : [3 7]
# print (numpy.sum(my_array, axis = None)  )    #Output : 10
# print (numpy.sum(my_array))                   #Output : 10



# print (numpy.prod(my_array, axis = 0)  )       #Output : [3 8]
# print (numpy.prod(my_array, axis = 1) )        #Output : [ 2 12]
# print (numpy.prod(my_array, axis = None)  )    #Output : 24
# print (numpy.prod(my_array))                   #Output : 24

##### here
# d=[]
# rows,columns=list(map(int,input().split()))
# for i in range(rows):
#     d.append(list(map(int,input().split())))

# a=numpy.sum(d,axis=0)
# print(a)
# print(numpy.prod(a))




#####################################################################Min and Max
# my_array = numpy.array([[2, 5], 
#                         [3, 7],
#                         [1, 3],
#                         [4, 0]])

# print (numpy.min(my_array, axis = 0))         #Output : [1 0]
# print (numpy.min(my_array, axis = 1))         #Output : [2 3 1 0]
# print (numpy.min(my_array, axis = None))      #Output : 0
# print (numpy.min(my_array))                   #Output : 0

#### solved
# d=[]
# rows,columns=list(map(int,input().split()))
# for i in range(rows):
#     d.append(list(map(int,input().split())))

# a=numpy.min(d,axis=1)
# # print(a)
# print(numpy.max(a))


#######################################################################Mean, Var, and Std


# my_array = numpy.array([ [1, 2], [3, 4] ])

# print (numpy.mean(my_array, axis = 0))        #Output : [ 2.  3.]
# print (numpy.mean(my_array, axis = 1))        #Output : [ 1.5  3.5]
# print (numpy.mean(my_array, axis = None))     #Output : 2.5
# print (numpy.mean(my_array))                  #Output : 2.5

# print (numpy.var(my_array, axis = 0))         #Output : [ 1.  1.]
# print (numpy.var(my_array, axis = 1))         #Output : [ 0.25  0.25]
# print (numpy.var(my_array, axis = None))      #Output : 1.25
# print (numpy.var(my_array))                   #Output : 1.25

# print (numpy.std(my_array, axis = 0))         #Output : [ 1.  1.]
# print (numpy.std(my_array, axis = 1))         #Output : [ 0.5  0.5]
# print (numpy.std(my_array, axis = None))      #Output : 1.11803398875
# print (numpy.std(my_array))                   #Output : 1.11803398875


# d=[]
# rows,columns=list(map(int,input().split()))
# for i in range(rows):
#     d.append(list(map(int,input().split())))

# print(numpy.mean(d,axis=1))
# print(numpy.var(d,axis=0))
# print(round(numpy.std(d),11))




###################################################################################Dot and Cross


import numpy

# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])

# print (numpy.dot(A, B))       #Output : 11

# print (numpy.cross(A, B))     #Output : -2


# n=int(input())
# a=[]
# b=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))

# for i in range(n):
#     b.append(list(map(int,input().split())))

# print(numpy.dot(a,b))



##################################################################################Inner and Outer


# A = numpy.array([0, 1])
# B = numpy.array([3, 4])

# print (numpy.inner(A, B))     #Output : 4
# print (numpy.outer(A, B))     #Output : [[0 0]
                            #          [3 4]]


# inner=[]
# outer=[]

# for i in range(1):
#     inner.append(list(map(int,input().split())))

# for i in range(1):
#     outer.append(list(map(int,input().split())))


# # print(inner)
# # print(outer)
# a=numpy.inner(inner,outer)
# print(a[0][0])
# print(numpy.outer(inner,outer))
# # 




#PYTHON GOLD BADGE HAS EARNED




################################################################################PROBLEM SOLVING##################################################################################

####################################################Diagonal Difference

# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(list(map(int,input().split())))

# print(arr)

# def diagonalDifference(arr):
#     a=0
#     b=0
#     for i in range(len(arr)):
#         a+=arr[i][i]
#         b+=arr[i][abs(len(arr)-1-i)] 
#     return abs(a-b) 

# a=' '
# b='#'
# n=6
# for i in range(1,n+1):

#     print(a*(n-i)+b*i)
# b=[]

# arr=[1,2,3,4,5]
# c=[]
# total=[]
# for j in range(len(arr)):
#     for i in range(len(arr)):
#             c.append(arr[i])
#             if len(c)==4:            
#                 total.append(sum(c))
#                 c=[]

# print(min(total),max(total))


# arr=[3,2,1,3]
# a=max(arr)


# print(arr.count(a))

#######################################################################Time Conversion

# hour=range(1,25)

# s = '12:05:45AM'

# b=['PM','AM']
# for i in b:
#     if i in s:
#         s= s.replace(i,'')
#         s=s.split(':')
#         if i=='AM'and int(s[0])!=12:
#              j=True
#         elif i=='AM'and int(s[0])==12:
#                 s[0]='00'

#         elif i=='PM'and int(s[0])!=12:

#             if int(s[0]) in hour and int(s[0])!=12: 
#                     s[0]= int(s[0])+12
#                     # print(s[0])
#             elif int(s[0]) ==12:
#                 s[0]='00'


# for i in range(len(s)):
#     if type(s[i])==int:
#         s[i]=str(s[i])
# for i in range(2):
#     s[i]=s[i]+':'

# b=''
# for i in s:
#     b+=i
# print(b)


#######################################################################Insertion Sort Advanced Analysis (Advanced)



# arr=[1,1,1,2,2]
# # arr=[2,1,3,1,2]
# arr=[4,3,2,1]

# b=0
# t = int(input("queries: ").strip())

# points=[]
# for t_itr in range(t):
#         n = int(input("len arr: ").strip())
#         arr = list(map(int, input().rstrip().split()))

#         for i in range(1,n):
#             arr[i]
#             for j in arr[:i]:
#                 if arr[i]<j:
#                     b+=1

#         points.append(b)

# print(points)


#####time limit exceeded error




# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]





# def merge(arr, l, m, r):
# 	n1 = m - l + 1
# 	n2 = r - m

# 	# create temp arrays
# 	L = [0] * (n1)
# 	R = [0] * (n2)

# 	# Copy data to temp arrays L[] and R[]
# 	for i in range(0, n1):
# 		L[i] = arr[l + i]

# 	for j in range(0, n2):
# 		R[j] = arr[m + 1 + j]

# 	# Merge the temp arrays back into arr[l..r]
# 	i = 0	 # Initial index of first subarray
# 	j = 0	 # Initial index of second subarray
# 	k = l	 # Initial index of merged subarray

# 	while i < n1 and j < n2:
# 		if L[i] <= R[j]:
# 			arr[k] = L[i]
# 			i += 1
# 		else:
# 			arr[k] = R[j]
# 			j += 1
# 		k += 1

# 	# Copy the remaining elements of L[], if there
# 	# are any
# 	while i < n1:
# 		arr[k] = L[i]
# 		i += 1
# 		k += 1

# 	# Copy the remaining elements of R[], if there
# 	# are any
# 	while j < n2:
# 		arr[k] = R[j]
# 		j += 1
# 		k += 1

# # l is for left index and r is right index of the
# # sub-array of arr to be sorted



# def mergeSort(arr, l, r):
# 	if l < r:

# 		# Same as (l+r)//2, but avoids overflow for
# 		# large l and h
# 		m = l+(r-l)//2

# 		# Sort first and second halves
# 		mergeSort(arr, l, m)
# 		mergeSort(arr, m+1, r)
# 		merge(arr, l, m, r)



# # Driver code to test above
# arr = [12, 11, 13, 5, 6, 7]
# n = len(arr)
# print("Given array is")
# for i in range(n):
# 	print(arr[i],end=" ")



# mergeSort(arr, 0, n-1)
# print("\n\nSorted array is")
# for i in range(n):
# 	print( arr[i],end=" ")


# This code is contributed by Mohit Kumra






################################3Grading Students


# n=int(input())

# a=1
# b=2

# grades=[26,38,44,78]

# for j in range(n):
    
#     if grades[j]>37:
#         if grades[j]%5==0:
#             print(grades[j])
#         else:
#             if (grades[j]+a)%5==0:
#                 print(grades[j]+a)
#             elif (grades[j]+b)%5==0:
#                 print(grades[j]+b)
#             else:
#                 print(grades[j])
#     else:
#         print(grades[j])
        





#################################################Apple and Orange

# first_multiple_input = input().rstrip().split()

# s = int(first_multiple_input[0])

# t = int(first_multiple_input[1])

# second_multiple_input = input().rstrip().split()

# a = int(second_multiple_input[0])

# b = int(second_multiple_input[1])

# third_multiple_input = input().rstrip().split()

# m = int(third_multiple_input[0])

# n = int(third_multiple_input[1])

# apples = list(map(int, input().rstrip().split()))

# oranges = list(map(int, input().rstrip().split()))



# app=0
# for i in apples:
#     if s<=a+i<=t:
#         app+=1
# print(app)
# org=0

# for i in oranges:
#     if s<=b+i<=t:
#         org+=1
# print(org)




###############################################Number Line Jumps


# values=list(map(int,input().split()))
# x1=values[0]
# v1=values[1]
# x2=values[2]
# v2=values[3]

# if (x1>x2 and v1<v2) or (x2>x1 and v1>v2):
#     b=x1-x2
#     a=v1-v2
#     if b%a==0:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')



##############################################Between Two Sets

# a=[2,6]
# b=[24,36]

# count=0
# for x in range(max(a),min(b)+1):
#     if all(x % num == 0 for num in a) and all(num % x == 0 for num in b):
#         count+=1

# print(count)



############################################Breaking the Record

# scores=[10 ,5 ,20 ,20, 4, 5 ,2 ,25,1]
# scores=[3 ,4 ,21, 36 ,10, 28, 35, 5 ,24, 42]

# cmin=0
# cmax=0
# min=scores[0]
# max=scores[0]
# for i in scores[1:]:
#     if i>max:
#         max=i
#         cmax+=1
#     elif i<min:
#         min=i
#         cmin+=1

# print(cmax,cmin)


# #################################################Subarray Division    
# s=[2 ,5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3 ,4 ,2 ,1]

# d=18
# m=7

# sum = 0
# count = 0


# for i in range(len(s)-m+1):
#     for j in range(i,i+m):
#         sum += s[j]
        
#     if sum == d:
#         count += 1
        
#     sum = 0
    

# print(count)


######################################Divisible Sum Pairs

# ar=[1,2,3,4,5,6]
# k=5
# sum=0
# count=0
# for ind1,val1 in enumerate(ar):
#     for ind2,val2 in enumerate(ar):
#         if ind1!=ind2:
#             sum=val1+val2
#             if sum%k==0:
#                 count+=1
#                 print(val1,val2,sum)


#             sum=0


        

# print(int(count/2))


################################################Migratory Birds   O(n2)

# arr=[1 ,2 ,3 ,4 ,5 ,4 ,3 ,2 ,1 ,3 ,4]

# numandrep=dict.fromkeys(arr,0)

# for i in arr:
#     numandrep[i]+=1

# print(numandrep) 
# a=max(numandrep.values())
# lst=sorted(list(numandrep.keys()))

# for i in lst:
#     if numandrep.get(i)==a:
#         print(i)



##### O(n) time complexity by chatgpt
# def migratoryBirds(arr):

#     bird_count = {}

#     # Iterate through the array to count occurrences of each bird type
#     for bird in arr:
#         bird_count[bird] = bird_count.get(bird, 0) + 1

#     # Initialize variables to keep track of the most common bird type and its frequency
#     max_bird = None
#     max_count = 0

#     # Iterate through the dictionary to find the most common bird type
#     for bird, count in bird_count.items():
#         if count > max_count or (count == max_count and bird < max_bird):
#             max_bird = bird
#             max_count = count

#     return max_bird



##################################################3Day of the Programmer

# jan,march,april,may,june,july,august,sep,oct,nov,dec=31,31,30,31,30,31,31,30,31,30,31

# months=[jan,march,april,may,june,july,august,sep,oct,nov,dec]
# feb=28
# year=1918
# counter=1
# day=0
# if year>=1919:
#     if (year%400==0) or (year%4==0 and year%100!=0):
#         feb+=1

# elif 1700<=year<=1917:
#     if year%4==0:
#         feb+=1

# elif year==1918:
#     feb-=13


# for i in range(len(months)):
#     feb+=months[i]

#     counter+=1
#     print(256-feb)
#     if 256-feb<30:
#         day=256-feb
#         counter+=1
#         # print(counter)
#         break

# dates=[day,counter,year]


# for i in range(len(dates)):
#     if len(str(dates[i]))==1:
#         dates[i]='0'+str(dates[i])
#     dates[i]=str(dates[i])


# full='.'.join(dates)

# print(full)



#############################################################Bill Division
# k=1
# bill=[3,10,2,9]
# b=7

# def bonAppetit(bill, k, b):

#     total=0
#     for i in range(n):
#         if i!=k:
#             total+=bill[i]

#     if total/2==b:
#         return 'Bon Appetit'
#     else:
#         total=b-total/2
#         return int(total)

# first_multiple_input = input().rstrip().split()


# n = int(first_multiple_input[0])

# k = int(first_multiple_input[1])

# bill = list(map(int, input().rstrip().split()))

# b = int(input().strip())

# myobj=bonAppetit(bill,k,b)
# print(myobj)


###############################################Sales by Match

# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# count=0

# dic= dict.fromkeys(ar,0)


# for i in ar:
#     dic[i]+=1

# for key,val in dic.items():
#     if val>=2:
#         a=val//2
#         count+=a

# print(count)


############################################Drawing Book

# n=7
# p=4
# page=1
# count=0

# if n-p>p-page:
#     page=1
#     for i in range(n):
#         if (page+1)%2!=0 or page==p:
#                 count=0
#                 break
#         else:
#             page+=2
#             count+=1
#             if page-1==p or page==p:
#                 break

# else:
#     page=n
#     for i in range(n,0,-1):
#         if n%2==0:
#             ##########if length is even and equal to target
#             if page==p:
#                 print(True)
#                 count=0
#                 break

#             else:
#                 page-=2
#                 count+=1
#                 if page==p or page+1==p:
#                     break

#             ##########if length is odd and equal to target or length minus one

#         elif n%2!=0:
#             if n-p<=1:
#                 if (page-1)%2==0 or page==p:
#                     count=0
#                     # print(True)
#                     break
#             else:
#                 page-=2
#                 count+=1
#                 if page==p or page-1==p:
#                     break


# print(count)
        

##############################################Counting Valleys

# steps = 8
# path='UDDDUDUU'
# counter=0
# valley=0
# updown=[]
# final=0
# for i in range(steps):
#     if path[i]=='U':
#         counter+=1
#         updown.append(counter)

#     elif path[i]=='D':
#         counter-=1
#         updown.append(counter)

# print(updown)

# if all( i>=0 for i in updown):
#     print(0)
# else:
#     for i in range(len(updown)):
#         if updown[i]==0 and updown[i-1]<0:
#             final+=1

# print(final)

    

###############################################Electronics Shop

# b = 10
# keyboards=[3,1]
# drives=[5,2,8]

# max=0
# for i in keyboards:
#     for j in drives:
#         a=i+j
#         if b-a>=0:
#             if a>max:
#                 max=a
# if max==0:
#     print(-1)

# print(max)


######################################################Cats and a Mouse

# def catAndMouse(x,y,z):
#     x=abs(x-z)
#     y=abs(y-z)

#     if x>y:
#         return 'Cat B'
#     elif x<y:
#         return 'Cat A'
#     else:
#         return 'Mouse C'

# x=5
# y=3
# z=1

# print(catAndMouse(x,y,z))


#####################################################Picking Numbers
# a=[1,2,2,3,1,2]
# a=[4 ,6 ,5 ,3 ,3 ,1]
# a=[1,1,2,2,2,4,4,5,5,5]


# b=sorted(a)
# print(b)
# min=0
# res=[]

# for i in range(0,len(b)):
#     for j in range(i+1,len(b)):
#         if b[i]+1==b[j] or b[i]==b[j]:
#             min+=1
#     res.append(min)
#     min=0

# results=max(res)+1

# print(results)


#####################################################Climbing the Leaderboard (medium)


# ranked=[100,90,90,80]
# # ranked=[100,100,50,40,40,20,10]

# player=[70,80,105]
# # player=[5,25,50,120]

# rankings = []
# sortRank=list(reversed(sorted(list(set(ranked)))))

# print(player,sortRank)
# length = len(sortRank)

# for i in player:
#     while (length>0 and sortRank[length-1]<=i):
#         print(sortRank[length-1],i)
#         length -= 1
#         print(length)
#     rankings.append(length+1)
# print(rankings)


############ O(n)
# sortRank=list(reversed(list(set(ranked))))
# d=len(player)
# for i in range(len(player)):
#     while d>0:
#         scores=[]
#         if not player[len(player)-d] in sortRank:
#             sortRank.append(player[len(player)-d])
#             sortRank=sorted(sortRank)
#             sortRank=list(reversed(sortRank))
#         scores.append(sortRank.index(player[len(player)-d])+1)
#         d-=1

    
# print(scores)


#############################################The Hurdle Race

# k=5
# height=[4,5,6,3,2,1]

# if all(k>=i for i in height):
#     print(0)
# else:
#     print(max(height)-k)


#############################################Designer PDF Viewer

# h=[1,3,1, 3 ,1, 4, 1 ,3 ,2 ,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# h=[1 ,3 ,1 ,3 ,1, 4 ,1 ,3 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5, 5 ,5 ,5, 5, 7]
# word='abc'
# word='zaba'

# import string

# pointsAndString={}
# a=string.ascii_lowercase

# for i in range(26):
#     pointsAndString[a[i]]=h[i]


# needs=[]
    
# for key,val in pointsAndString.items():
#     if key in word:
#         needs.append(val)

# print(needs)
# print(max(needs)*len(word))



########################################Utopian Tree
# b=0
# n=5
# for i in range(n+1):
#     if i%2==0:
#         b+=1
#     elif i%2!=0:
#         b*=2

# print(b)


#########################################Angry Professor

# k=3
# counter=0
# a=[-2,-1,0,1,2]
# a=[-1,-3,4,2]

# def angryProfessor(k, a):
#     counter=0

#     for i in range(len(a)):
#         if a[i]<=0:
#             counter+=1
    
#     if counter<k:
#         return 'YES'
#     return 'NO'
    
##########################################Beautiful Days at the Movies

# i=20
# j=23
# k=6

# counter=0
# for day in range(i,j+1):
#     g=int(str(day)[::-1])
#     if abs((day-g)%k==0):
#         counter+=1

# print(counter)
       

################################################Viral Advertising
# n=5
# shared=5
# liked=2
# cumulative=2

# for i in range(n-1):
#     shared=liked*3
#     liked=shared//2
#     cumulative+=liked
#     print(shared,liked,cumulative)

# # print(cumulative)



##############################Circular Array Rotation O(n2)
# prisoners=5
# candies=2
# start=1
# start=start-1

# for i in range(candies):
#     candies-=1
#     if start==prisoners:
#         start=0

#     start+=1

# print(start)


############### O(n)
# prisonerNo = (s+m-1)%n
#     if prisonerNo == 0:
#         return n
#     return prisonerNo



##################################################Circular Array Rotation

# k=2
# array=[1,2,3]
# queries=[0,1,2]

# for i in range(k):
#     b=array[-1]
#     array.pop()
#     array.insert(0,b)

# results=[]
# for i in queries:
#     results.append(array[i])

# print(results)

#######################################################Sequence Equation

# p=[5,2,1,3,4]
# f=sorted(p)

# for i in f:
#     for j in range(len(p)):
#         if p[p[j]-1]==i:
#             print(j+1)


#######################################################Jumping on the Clouds: Revisited

# c = [0, 0, 1, 0, 0, 1, 1, 0]
# # c = [0, 0, 1, 0]
# c=[1 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,0]


# def jumpingOnClouds(c, k):
#     b=k
#     e=100
    
#     if k>=n:
#         k=k-n

#     while k!=0:
#         if c[k]==1:
#             e-=2   
#         e-=1
#         k+=b

#         if k>=n:
#             k=k-n

#     if c[k]==1:
#         e-=2
#     e-=1  
#     return e

# n=10
# k=3


########################################################Find Digits

# n=1012
# counter=0
# for i in str(n):
#     if int(i)!=0:
#         if n%int(i)==0:
#             counter+=1
# print(counter)

##########################################################Extra Long Factorials (medium)

############recursive
# def extraLongFactorials(n):
#     if n<=1:
#         return 1
    
#     else:
#         return n*extraLongFactorials(n-1)
# n=25

# myobj=extraLongFactorials(n)    
# print(myobj)
# ################for loop
# n=25
# b=1
# for i in range(1,n+1):
#     b*=i
# print(b)




####################################################3Append and Delete

# s='hackerhappy'
# t='hackerrank'
# k=2
# sequal=0
# tequal=0
# for i in range(1,len(s)):
#     if s[0:i+1] not in t:
#         print(s[0:i+1],i)
#         sequal+=1

# for i in range(1,len(t)):
#     if t[0:i+1] not in s:
#         print(t[0:i+1],i)
#         tequal+=1

# print(sequal+tequal)

# if sequal+tequal<=k and len(s)>=len(t) or (len(set(s))==1 and len(s)>1):
#     print("YES")
# else:
#     print("NO")



########################################Sherlock and Squares

# a=35
# b=70
# counter=0
# i=0
# while i**2<=b:
#     if i**2>=a:
#         counter+=1
#     else:
#         pass
#     i+=1

# print(counter)

########################################Library Fine

# hackos=0
# d1=2
# m1=7
# y1=1014
# d2=1
# m2=1
# y2=1015

# if d1>d2:
#     hackos+=(d1-d2)*15

# if m1>m2:
#     hackos=0
#     hackos+=(m1-m2)*500
# elif m2>m1:
#     hackos=0

# if y1>y2:
#     hackos=0
#     hackos+=(y1-y2)*10000
# elif y2>y1:
#     hackos=0
    
# print(hackos)
    
################################################Cut the sticks

# arr=[5,4,4,2,2,8]

# arr=sorted(arr)
# cut=min(arr)
# iteration=len(arr)
# stick=len(arr)

# results=[]

# for i in range(iteration):
#     results.append(len(arr)-arr.count(0))
#     for j in range(len(arr)):
#         if arr[j]>=cut:
#             arr[j]=arr[j]-cut

#     counter=arr.count(0)
#     index=len(arr)-counter
#     cut=arr[-index]
#     if arr.count(0)==len(arr):
#         break
# print(results)


###################################################Repeated String
# s='epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq'

# n=549382313570

# countSingle=s.count('a')

# reps=n//len(s)

# if n%len(s)==0:
#     print(reps*countSingle)
# else:
#     print((reps*countSingle)+s[0:n%len(s)].count('a'))




#################################################Jumping on the Clouds (different than first one)

arr=[0 ,0 ,1 ,0, 0 ,0, 0, 1 ,0 ,0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1, 0 ,0 ,0 ,1 ,0, 0,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ,1 ,0 ,1 ,0 ,0]
arr=[0,0,0,1,0,0]

steps=0
k=0

for i in range(len(arr)):
    if steps<len(arr)-2:
        if arr[steps+1]==0 and arr[steps+2]==0:
            k+=1
            steps+=2
            # print(steps,'first if')
        elif arr[steps+1]==0 and arr[steps+2]==1:
            steps+=1
            k+=1
            # print(steps,'second if')

        elif arr[steps+1]==1 and arr[steps+2]==0:
            k+=1
            steps+=2
            # print(steps,'third if')

        elif arr[steps+1]==0:
            k+=1
            # print(steps,'fourth if')
        print(steps)


print(k)



