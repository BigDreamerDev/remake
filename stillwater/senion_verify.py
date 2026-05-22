#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import json
import random
import re
import zlib
from typing import Any

_KEY = [83, 87, 45, 67, 79, 68, 73, 67, 79, 76, 79, 71, 89, 45, 86, 69, 75, 45, 49, 52]
_DATA = 'D~+Jrwl)=nI*JgYPfx4V!EMHh<3)r6FKovLO-4y$eE0nA98Y~j)yXs~X3@G)Ho)`2q;s#ZZkVx#F+g-@e>Wzap+E7oblTD8HkSw}j%as&a2jNd*juQ8#<2=$#fXSY>^Y)zl!v$?*m|_wEk%*OzF_L0C8*Pq$OA0+cIZ97_Q6^*^wsA7WC#+twa<k7Fuk7CZgTNTmBB6u>@WGZys0+Gtl$uOCf>SwRFlilidfiEc&jF`(3SvjCeyygj*?ByJdozh0ot_sF}$rJO7_v>vV2M91g&gMcw00%-NG2yCfrGCm)wH?^vJhV5V+vq@f5SEi_3X>E0Dy}<BT(&u!oqcij}>yyWEpv6l4A(#GI;#oY!KFd(qPwbh3N>xsS#{I)s}Hgo!+u;zQyI@|uyK1d`6lC!)jiq^U1?lJYT>S5c$5|3^-WPJo?(h9b5ulmVoQ?e*&U62hL7h?-!SpyP@*)Dj)xaKH(u?33(8gwa^Fl;4DYArLbF<cndF@R@E~4H?G13o-6qWaBvMhqlNoA@<xmIt21PGOMBJ9_5XRug*Fuke-W7FDcqD=u-xLF!1+X{+8?;q$8YJwJO2ni}@ydt~9l-?}MGQE!M-&x^2KZBb}#d$a53mn%S$fJqK6^u7k&_l(DEeG&k2ZLbk80xSD!t&j@^zCO!B0^)NMkZ|w0|{bN{8o;m)Ad0GEJYUlXM$3uYLeN&DoCW|uVG5_ix?8cj}to9_Tk>-W3oM{I-fwCv-iukwTG$Xb2EcS?0x>v*Ps4wv#@^kx|<iv|Ibiz(Zu33XHQlrZgic`T!vhEv3KC)bbj5&*lqWbuw^9|9qKWdqRb8&2{&-gQNMzgm2b_1OGg#ED6eD=)FtIWWy*PE{09fqVngpLHzA85In=b#K(t|oXEzB3(VExtWAYBcDed}S-vHT4hMQ8~Z<LFhDaQ~sP|1^jp6I`se`3P0h!zn6OBV?cyi9<%Y`sj^=`o^IQNTLai&+5Chp0{Q|9hFtp7?%8Y8?i^Cml6RzOwR2I;iL%?@m=#D+;vNUfZnuO6dP+%f=EBn{DW3^ZM>`xcX0%t9gW-1Q71EQYCqJBO(Mc?-XZ%eVhQTu#Kn==)ul4KyJ9wWTV56i^fewF0ZYbG#D(ljW^u<K!cGue*OsVnfigTh#OPZ!3gF-nnu4AsEG~C|ks)uIe<O{?uEZm~EKO77V>Z?IAcG=b30*B<1tw|?0^%2gn6`9}-9G*0gA;OfV!(@)R)_dz@VQ^p7Ocn!B#YSrFk9hnS1I|-{{Zo$lI_`67?B9yQd9Yu94d7FS)P_P3%C*~7dS5*V57c;8d?pY;!2y4UFZe-%B&8eUSf3E8xovV<m5lkpMr7$KUdN?@LC7^QADKlzO$~yDNn;at=~&haGkbz<$+Bu~{vm+(Q)g_f`bzmO^h3zvzzJGZCQfFFa~eHf`~#ZAefa9?b)9wN^ZHd5<7${fKbiDzAQ2l;TuxmTQ6v0d_|0b~0FozA;|59z#&E^j(J>>(9}WKLTepLTkcHRM;_Nd<ik3?CUPJ&57NC!M;=KQX@I^_Eide6h%*;N=vwvBM_B+Aa6a$}JrZ9Hd^F8L4$fuN=gnQK|-f1=679N1YEJps1AzJEx7r)h$@wxM)7n}ja<pD!(`501=>oo>-_8%s826S#y5doet!o^%KRw)cqabL8B_VP>5+5Hj<%6~i)01pF$+ecxmL-jxTncO-i>G@{)(>(<UQDp!a^}e}ja^gQ~okDJm$<D^vrsJk!ZsR>Mg=YHjUpFoPOs&1-kmV3wTxBX#fw*v*ecKCo|9h-ulR*QTAYW`e<3zYcshkPDJ8<}T#qbo_akA%g15S{N;Z@E2Bv)8E1a4D8Kw9^;kS?8yr<}V@7cdJymRm)cJqR+q64rbMIT!EwR|w-pmv=S$$@KP@^2?J4X<(hlPk93WU;>P{1@`uli6AqE8QH;#!-FdgcBCbdW<s~-8evdSC7^j@7Xbqcf|nr)S8!2jGEieU6j8&cL#9&@_9mPCvwym*mXJ$3wm#n(Mu|%Z0UQEAb4ugelp*a=Uwqpw>i-|c3A(HX_M9vPhJaFlCD`$H)#rR(*r(xlH9Jb__(9Oa()XV&5vD~~c{=0~WlXrI=p6h|4u_lcQM+isAs<SSKC(mj0hjj<;Gdxqg3#m^gfgsX9xyt{nsELkA7%ZxmVW;g`q&q==ut-|`v9E7Qx#S^9AHKdGaY2G{IG!$3{7pHW$rxnSNVS37zX#{7e5Gc!3BzIL10%VWC?%IJcBA=MaJ1*VI!1bg&r=1m~G~1tC)v49yBnE8+650LydRD16ao#UMXYknVT2WoWem!M`prS>?rtah79PI2bS9=C2*5Td=|@%cqjDCnU>&kB#{mRn(kc8U5gG=82%N5U5RJ1dW?VYz~vn0dD&wWabITc$V?m0+ouKR1Ha-Z9>xw+c#N)NMPx^wRMOEU+vf^rQl??@(B%bnL3~D4$wj%_+!A)DXpy46npqW=M3O;>udB<{qI)zqKK&JogI6pxGL-Sau0Nr3GP`C^vGgwSw$ifdJC+I3vYr3!6YKUWP(nEUB+8-lq|q5eZtq@<(qFmfRFG=n?9a}Qs>{m5lko<lC%je2<}PC<3n!TUarQk+Zi;R2%_W-$g{)6{Z<K){(&OM#K*n#(Q+z<UwODR^W8sED?h%!nA~g+7r30a7SpjSr$K!w(fPv~_c?_XIo$O||_%v^`hD=iRA{`6d*&i7`J`G114c0!&085~1O=?sfjz6|&cf`|C%z+tIi>BnS&vG$no`p$}S8FcNIB=RLTpz~Q^u(@mJ9JZDp~|tbyPdl~Ad}A1;KW@GB(Bu4r8xK*GH|$8bg&32Jo@&7s5Hg8h`M*Xx_i{~C*mA%BLz66J{%Juc3n{a$EW5uk1dJ6E8Q%4F~EK7L*I^t9tV#D!)(LtI{-bH^*t{p?FAz{BFK7BArb<OcFPm9%9mebKHmS-ldSL|s&({-*FSj#PGvVQ3NnXg>tjYS$TX5s%$6^<jM41Q-)w)K88Dvf_U?Ca+IRgaC{aq2Y}^s`VeDhM=vnTj<gxPIvrmbHiUhOuu58EtnmBC<dt!B^<Lr5dRzX>_MsaLr({^(R-W7pTIHhn_n~gqSJAr(Az+S)IBcK>LjW8P1ru}oEb7s>M+Bt4}+NY6TZ+tjj$l+PL&#s_FI{1W0h}lbz{^-xYic>|oz?!z&TRke{*q(yBte$DdjJ1jdCa7a#<s?PTxI{TqQR4hg_}`1O(t=(UWygF`7xxHS$}EBx4OJUQO`Ts3EynJhT6lxO%Yb`|WflvKc0)3Aq4L<z6S71ljoNhK$Q7C~lP4R0ch2i{^RZ#AieZsajN`edr$u?nUq8k_Y^pskh_G?xK2^|&32=-=$aQiz9SEZ&)L>~YTgqNX^^$MOH!sTRU~b;_6L&YO&o9z0SDyqs()|$-5q6^$?{|n)XU#_*j7PUbJ1$-Vv7I~HD*R%Z>8THiGPlj97v6Z%93jKar=<2lC%&U3Rne6&J<F^3q9UwMji$pCI9^V9NM|h&X~zFYIY+tVLo`uHLD6jR9tlfK;?B*B)~R*3vle<J02=CWA86f6|Fi))C&YAj&WkCrs#IWc-k&qwskl>7pLL-I-!N6oj@sq4yl338O1_KCp`y_l-7J`UaM^G#HnO9msNcFMK{dMo*oGk}@j3e+;*7h1E}%04R_*RQ6W;Iws#z;W83|;6gImmr*A~8q{nf&9mE5QcVT&kBhhikXs_c0B5ldtPlA0<AJtXN3Y4lT+z)!Re&rhTYUvxOa_O1^AjJ<L($YC$PyYnm`4KJG`7e;0b-^@;<i{(BkuneFpY*-Vg<oh;G6%dW#n-FnmXOy>knp~Sy;aTUhUw#&1K~>0P_%H}dj8>N`yo_bz11n{ZV=K1y<8MqqK=?%lif+{Np$@w3Y$|1Td*-<n1ZeQarJ~)7qsUO8GSbZce01%pAiMI~c{8%ugj|f61-515kgAd?c&oTd;~Ya<8&CTu6INsdtw}O(cSDdH-JSJuXBmD0dXaaf+2dVRWO~*32~&Q`J-fCwr@XPK`dpa|RVshCmpm^*z5n;CVNO^+n)u9kT#7e)OUJoEtCKUy=HWF4Y;~CH3BM;=L%>*^eP*X=DMPcZ{|32CmNuq28)m6Qz&vg_RW#QG+66fe3S#c|Bc)%A5&*l6q&#K*fz1n*!@cW{Uhu8N(!N55D;RN*6wy6!mpb7^PD%gC?idn1B@6C5ySJIFxvaIdI%??3?m+)pl}e=rWUyk~a~u`@QsO3A;Y?0@*Ybdfo?qthE?4#kWt_;&q*d<%4HEY$A0yvc<z1jSp`hR!Tcm6u`6r8*GHNk#VcF+uDjZ1?dGM#FDv1$g0x}?U!L(dqH3C;!_XhCoK^*fPJhs!)6o24kY?pPQx8$|w8VdSp=b!t!x=!R}*^dc?#*WQZ(thm`L#QFxETt1#M&7*!Q6Zx>vPjiHj)ziahF?dH<{_UuMf6BL#zCVeXO~NJd00#ljD10;Sv<P<2mrkoJlNHx^rP@IpG*iZOWGDk{{N7F?$+ZC*Ciz3M{P&<!`$G_wo9|0mGM7yh_8*8s4&IgncviB+MEfB0dt+^KUcYRwgu$DG+8wz|Al;2nO)@KZ{B*vkO#?}gG<kyry`2)43<uHMQ2`*R;?p;1QD)LOq8oC4G9ri(AHK(85%>qtMj7DsS_qehPOb2d>gwcto2jSrB2>7s-8;cJjCWx%7H#CM_$+Gs5h*;ztPjizpul5p!qf{4SooJ5LsQ$><~RR%)vtwM|=vJn}qgNX7?U1QFPi??=Sw7$KT2)QGJqK_B1<<3`Om+QxBJ6GyD&9qgUo99rlF8U^>$cj(0G0h{s`a?}@@N8<jKy6NCt}!aR@83^(k7>|7UHL3t*GTgvgP$-+k<xBIh*uuY;?$wU'


def _load() -> dict[str, Any]:
    key = bytes(_KEY)
    blob = base64.b85decode(_DATA.encode("ascii"))
    clear = bytes(value ^ key[index % len(key)] for index, value in enumerate(blob))
    return json.loads(zlib.decompress(clear).decode("utf-8"))


def _normalise(value: str) -> str:
    value = value.lower().strip()
    value = value.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def _hash_answer(answer: str, salt: str) -> str:
    return hashlib.sha256((salt + _normalise(answer)).encode("utf-8")).hexdigest()


def _accepted(answer: str, gate: dict[str, Any], salt: str) -> bool:
    return _hash_answer(answer, salt) in set(gate["hashes"])


def _pass_gate(number: int) -> None:
    print(random.choice([
        f"Gate {number:02d} accepted. The register does not object.",
        f"Gate {number:02d} accepted. Ink comparison stable.",
        f"Gate {number:02d} accepted. Codicology witness retained.",
    ]))


def _fail_gate(number: int) -> None:
    print()
    print(f"GATE {number:02d} REFUSED.")
    print(random.choice([
        "The register closes before the translation is complete.",
        "Codicology cannot certify that reading.",
        "The answer is close enough to be dangerous, but not close enough to file.",
        "The archive records effort. The archive does not record clearance.",
    ]))
    print("Verification terminated. Restart with `verify.senion` when ready.")


def run(args: list[str], session: dict[str, Any]) -> None:
    if args and args[0].lower() not in {"rosetta", "senion", "language", "register"}:
        print("usage: verify.senion")
        print("aliases: senion.verify, rosetta.verify, verify rosetta")
        return

    data = _load()
    salt = data["salt"]

    for line in data["intro"]:
        print(line)
    print()

    for idx, gate in enumerate(data["gates"], start=1):
        print()
        print(f"GATE {idx:02d} // {gate['title']}")
        print("-" * 64)
        print(gate["prompt"])
        answer = input("translation> ")

        if not _accepted(answer, gate, salt):
            _fail_gate(idx)
            return

        _pass_gate(idx)

    session["rank"] = "Codicology-Provisional"
    session["auth_level"] = max(session.get("auth_level", 0), 1)

    contact = base64.b85decode(data["contact_b64"].encode("ascii")).decode("utf-8")
    subject = base64.b85decode(data["subject_b64"].encode("ascii")).decode("utf-8")

    print()
    print("=" * 78)
    print(data["success"][0])
    print(data["success"][1])
    print(data["success"][2])
    print()
    print(data["success"][3])
    print(data["success"][4])
    print()
    print(f"    {contact}")
    print()
    print(data["success"][5])
    print()
    print(f"    {subject}")
    print()
    print(data["success"][6])
    print(data["success"][7])
    print("=" * 78)
