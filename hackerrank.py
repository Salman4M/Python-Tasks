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

# for i in range(len(arr)):
#     for i in arr:
#         numandrep[i]+=1
 
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