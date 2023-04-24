
def cal_follow(s, productions, first):
    follow = set()
    if len(s) != 1:
        return {}
    if (s == list(productions.keys())[0]):
        follow.add('$')

    for i in productions:
        for j in range(len(productions[i])):
            if (s in productions[i][j]):
                idx = productions[i][j].index(s)

                if (idx == len(productions[i][j])-1):
                    if (productions[i][j][idx] == i):
                        break
                    else:
                        f = cal_follow(i, productions, first)
                        for x in f:
                            follow.add(x)
                else:
                    while (idx != len(productions[i][j]) - 1):
                        idx += 1
                        if (not productions[i][j][idx].isupper()):
                            follow.add(productions[i][j][idx])
                            break
                        else:
                            f = cal_first(productions[i][j][idx], productions)

                            if ('*' not in f):
                                for x in f:
                                    follow.add(x)
                                break

                            elif ('*' in f and idx != len(productions[i][j])-1):
                                f.remove('*')
                                for k in f:
                                    follow.add(k)

                            elif ('*' in f and idx == len(productions[i][j])-1):
                                f.remove('*')
                                for k in f:
                                    follow.add(k)

                                f = cal_follow(i, productions, first)
                                for x in f:
                                    follow.add(x)
    return follow


def cal_first(s, productions):
    first = set()

    for i in range(len(productions[s])):
        for j in range(len(productions[s][i])):
            c = productions[s][i][j]
            if (c.isupper()):
                f = cal_first(c, productions)
                if ('*' not in f):
                    for k in f:
                        first.add(k)
                    break
                else:
                    if (j == len(productions[s][i])-1):
                        for k in f:
                            first.add(k)
                    else:
                        f.remove('*')
                        for k in f:
                            first.add(k)
            else:
                first.add(c)
                break

    return first


def main():
    productions = {}
    grammar = open("fnf.txt", "r")
    
    first = {}
    follow = {}

    for prod in grammar:
        elem = []
        for i in prod:
            if (i == "-" or i == ">" or i =="\n"):
                pass
            else:
                elem.append(i)

        print(elem)

        left_prod = elem.pop(0)
        right_prod = []
        temp_rt_prod = []

        for j in elem:
            if (j != '|'):
                temp_rt_prod.append(j)
            else:
                right_prod.append(temp_rt_prod)
                temp_rt_prod = []

        right_prod.append(temp_rt_prod)
        productions[left_prod] = right_prod

    for s in productions.keys():
        first[s] = cal_first(s, productions)
    
    print("")
    print(productions)
    print("")

    print("\n*****FIRST*****")
    for lhs, rhs in first.items():
        print(lhs, ":", rhs)

    print("")
    print(first)
    print("")

    for lhs in productions:
        follow[lhs] = set()

    for s in productions.keys():
        follow[s] = cal_follow(s, productions, first)

    print("*****FOLLOW*****")
    for lhs, rhs in follow.items():
        print(lhs, ":", rhs)

    grammar.close()


if __name__ == "__main__":
    main()