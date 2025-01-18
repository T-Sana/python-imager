try: from pyimager.main import *
except: from main import *

def draw_char(img, char, pts, colour=COL.red, fontSize=1, thickness=1, lineType=0, angle=0, help=False):
    if help:
        img.circle(pts[-1], 4, COL.green, 0)
        for p in pts[:-1:]: img.circle(p, 3, COL.red, 0)
        img.write(char, pts[0])
    col, fs, tk, lt, an = colour, fontSize, thickness, lineType, angle
    ct = ct_cr(*pts)
    p1, p2, p3, p4 = ps = [coosCircle(p, fontSize, a+an) for p,a in zip(pts, (45, 135, 315, 225))]
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4)
    cth, ctb, ctg, ctd = ct_sg(ct, ch), ct_sg(ct, cb), ct_sg(ct, cg), ct_sg(ct, cd)
    ct1, ct2, ct3, ct4 = ct_sg(ct, p1), ct_sg(ct, p2), ct_sg(ct, p3), ct_sg(ct, p4)
    phg, phd, pbg, pbd = ct_sg(p1, ch), ct_sg(p2, ch), ct_sg(p3, cb), ct_sg(p4, cb)
    pgh, pdh, pgb, pdb = ct_sg(p1, cg), ct_sg(p2, cd), ct_sg(p3, cg), ct_sg(p4, cd)
    LINES = []
    match char:
        ## "Control" chars #####################################
        case "00": ## Unknown char !
            pt, rs = pt_sg(ct, ch, 3), (dist(ct, p1)*0.2, dist(ct, p1)*0.3)
            pt1 = coosEllipse(pt, rs, 90, an)
            pt2, pt3 = coosCircle(pt1, dist(p1, p3)/10, 90+an), coosCircle(pt1, dist(p1, p3)/5, 90+an)
            LINES = [[ch, cd], [cd, cb], [cb, cg], [cg, ch], [pt1, pt2]] + [[pts[(0,1,3,2)[i]], pts[(0,1,3,2)[(i+1)%4]]] for i in range(4)]
            img.ellipse(pt, rs, col, tk, lt, 200, 450, an)
            img.circle(pt3, tk, col, 0, lt)
        case "06": ## Full char
            img.polygon([*pts[:2:], *pts[:1:-1]], col, 0, lt)
        ## Symbols #############################################
        case "A0": ## 0
            r = (dist(ct, ct_sg(cd, ctd)), dist(ct, ch))
            img.ellipse(ct, r, col, tk, lt, angle=an)
            LINES = [[coosEllipse(ct, r, 140, an), coosEllipse(ct, r, 320, an)]]
        case "A1": ## 1
            LINES = [[ct_sg(ct1, pgh), ch], [ch, cb], [p3, p4]]
        case "A2": ## 2
            r = (dist(ct, cd), dist(cth, ch))
            img.ellipse(cth, r, col, tk, lt, 210, 400, an)
            LINES = [[coosEllipse(cth, r, 400, an), p3], [p3, p4]]
        case "A3": ## 3
            img.ellipse(cth, (dist(ct, cd), dist(cth, ch)), col, tk, lt, 220, 450, an)
            img.ellipse(ctb, (dist(ct, cd), dist(ctb, cb)), col, tk, lt, 270, 510, an)
        case "A4": ## 4
            LINES = [[phd, ct_sg(cg, pgb)], [ct_sg(cg, pgb), ct_sg(cd, pdb)], [phd, pbd]]
        case "A5": ## 5 # FIXME
            LINES = [[p1, p2], [p1, cg], [cg, cd], [cd, p4], [p3, p4]]
        case "A6": ## 6 # FIXME
            img.ellipse(cth, (dist(ct, ct_sg(cd, ctd)), dist(ctb, cb)), col, tk, lt, 0, 130, an+180)
            img.ellipse(ctb, (dist(ct, ct_sg(cd, ctd)), dist(cth, ch)), col, tk, lt, angle=an)
            LINES = [[ct_sg(ct1, pgh), ct_sg(ct3, pgb)]]
        case "A7": ## 7
            LINES = [[p1, phd], [phd, cb], [ctg, cd]]
        case "A8": ## 8
            img.ellipse(cth, (dist(ct, ct_sg(cd, ctd))*0.9, dist(cth, ch)), col, tk, lt, angle=an)
            img.ellipse(ctb, (dist(ct, ct_sg(cd, ctd)), dist(ctb, cb)), col, tk, lt, angle=an)
        case "A9": ## 9 # FIXME
            img.ellipse(ctb, (dist(ct, ct_sg(cd, ctd)), dist(ctb, cb)), col, tk, lt, 0, 130, an)
            img.ellipse(cth, (dist(ct, ct_sg(cd, ctd)), dist(cth, ch)), col, tk, lt, angle=an)
            LINES = [[ct_sg(ct2, pdh), ct_sg(ct4, pdb)]]
        case "B0": ## .
            img.circle(cb, fontSize*0.2, col, -tk, lt)
        case "B1": ## ,
            LINES = [[ct_sg(ct4, cb), ct_sg(pbg, cb)]]
        case "B2": ## :
            img.circle(cb, fontSize*0.2, col, -tk, lt)
            img.circle(ct, fontSize*0.2, col, -tk, lt)
        case "B3": ## ;
            img.circle(ct, fontSize*0.2, col, -tk, lt)
            LINES = [[ct_sg(ct4, cb), ct_sg(pbg, cb)]]
        case "B4": ## -
            LINES = [[ct_sg(cg, ctg), ct_sg(cd, ctd)]]
        case "B5": ## _
            LINES = [[p3, p4]]
        case "B6": ## !
            LINES = [[ch, ctb]]
            img.circle(cb, fontSize*0.2, col, -tk, lt)
        case "B7": ## ?
            LINES = [[ct, ctb]]
            img.ellipse(cth, (dist(ch, p1), dist(cth, ch)), col, tk, lt, 210, 450, an)
            img.circle(cb, fontSize*0.2, col, -tk, lt)
        case "B8": ## ¡
            LINES = [[cth, cb]]
            img.circle(ch, fontSize*0.2, col, -tk, lt)
        case "B9": ## ¿
            LINES = [[ct, cth]]
            img.ellipse(ctb, (dist(cb, p3), dist(ctb, cb)), col, tk, lt, 30, 270, an)
            img.circle(ch, fontSize*0.2, col, -tk, lt)
        case "C0": ## '
            LINES = [[ch, cth]]
        case "C1": ## "
            a = 3
            LINES = [[pt_sg(ch, p1, a), pt_sg(cth, pgh, a)], [pt_sg(ch, p2, a), pt_sg(cth, pdh, a)]]
        case "C2": ## ·
            img.circle(ct, fontSize*0.2, col, -tk, lt)
        case "C3": ## $
            LINES = [[ch, cb]]
            draw_char(img, "A18", ps, col, fs, tk, lt, an)
        case "C4": ## %
            LINES = [[ct2, ct3]]
            for pt in [ct1, ct4]:
                p = pt_sg(pt, ct, 5, 2)
                img.circle(p, dist(pt, p), col, tk, lt)
        case "C5": ## &
            p = pt_sg(cth, ch, 5, 2)
            r, r1, r2 = (dist(cth, ct1), dist(cth, ch)), (dist(ct1, p)*0.7, dist(p, ch)), (dist(ctb, pgb), dist(ctb, cb))
            a1, a2, a3 = 140, 420, 220
            img.ellipse(cth, r, col, tk, lt, a1, 270, an)
            img.ellipse(p, r1, col, tk, lt, 270, a2, an)
            img.ellipse(ctb, r2, col, tk, lt, -20, a3, an)
            LINES = [[coosEllipse(cth, r, a1, an), p4], [coosEllipse(p, r1, a2, an), coosEllipse(ctb, r2, a3, an)]]
        case "C6": ## /
            LINES = [[phd, pbg]]
        case "C7": ## =
            LINES = [[ct_sg(cg, ct1), ct_sg(cd, ct2)], [ct_sg(cg, ct3), ct_sg(cd, ct4)]]
        case "C8": ## +
            LINES = [[cth, ctb], [ct_sg(cg, ctg), ct_sg(cd, ctd)]]
        case "C9": ## *
            cs = ct, dist(ct, ct_sg(cd, ctd))
            LINES = [[coosCircle(*cs, a), coosCircle(*cs, a+180)] for a in [30, 90, 150]]
        case "D0": ## (
            img.ellipse(ctd, (dist(ct, cg), dist(ct, ch)*1.2), col, tk, lt, 120, 240, an)
        case "D1": ## )
            img.ellipse(ctg, (dist(ct, cg), dist(ct, ch)*1.2), col, tk, lt, 120, 240, an+180)
        case "D2": ## [
            LINES = [[phg, phd], [phg, pbg], [pbg, pbd]]
        case "D3": ## ]
            LINES = [[phg, phd], [phd, pbd], [pbg, pbd]]
        case "D4": ## { # TODO
            ...
        case "D5": ## } # TODO
            ...
        case "D6": ## |
            LINES = [[ch, cb]]
        case "D7": ## @
            img.ellipse(ct, (dist(ct, cd), dist(ct, cb)), col, tk, lt, 60, 360, an)
            img.ellipse(ct, (dist(ctb, ct4), dist(ctb, cb)), col, tk, lt, angle=an)
            img.ellipse(ctd, (dist(ctd, cd), dist(ctd, ct4)), col, tk, lt, 0, 90, an)
            LINES = [[ct2, ct4]]
        case "D8": ## #
            LINES = [[ct_sg(cg, pgh), ct_sg(cd, pdh)], [ct_sg(cg, pgb), ct_sg(cd, pdb)], [ch, ct_sg(p3, pbg)], [ct_sg(p2, phd), cb]]
        case "D9": ## ¬
            LINES = [[ct_sg(cg, ctg), ct_sg(cd, ctd)], [ct_sg(cd, ctd), ct_sg(ct4, pdb)]]
        case "E0": ## º # TODO
            ...
        case "E1": ## ª # TODO
            ...
        case "E2": ## `
            LINES = [[pt_sg(*pts[:2:], 2), pt_sg(*ps[:2:], 1, 2)]]
        case "E3": ## ´
            LINES = [[pt_sg(*pts[:2:], 1, 2), pt_sg(*ps[:2:], 2)]]
        case "E4": ## ^
            LINES = [[ct_sg(*pts[:2:]), pt_sg(*ps[:2:], 4)], [ct_sg(*pts[:2:]), pt_sg(*ps[:2:], 1, 4)]]
        ## Letters #############################################
        case "A00": ## A
            LINES = [[p3, ch], [ch, p4], [ct_sg(p3, ch), ct_sg(ch, p4)]]
        case "A01": ## B
            LINES = [[p1, p3], [p3, cb], [cg, ct], [p1, ch]]
            img.ellipse(cth, (dist(ch, p2)*0.8, dist(cth, ch)), col, tk, lt, 270, 450, an)
            img.ellipse(ctb, (dist(ct, cd), dist(ctb, cb)), col, tk, lt, 270, 450, an)
        case "A02": ## C
            img.ellipse(ct, (dist(ct, cd), dist(ct, ch)), col, tk, lt, 50, 300, an)
        case "A03": ## D
            LINES = [[p1, p3], [p3, cb], [p1, ch]]
            img.ellipse(ct, (dist(ct, cd), dist(ct, ch)), col, tk, lt, 270, 450, an)
        case "A04": ## E
            LINES = [[p1, p3], [cg, ctd], [p3, p4], [p1, p2]]
        case "A05": ## F
            LINES = [[p1, p3], [cg, ctd], [p1, p2]]
        case "A06": ## G
            img.ellipse(ct, (dist(ct, cd), dist(ct, ch)), col, tk, lt, 0, 300, an)
            LINES = [[ct, cd]]
        case "A07": ## H
            LINES = [[p1, p3], [p2, p4], [cg, cd]]
        case "A08": ## I
            LINES = [[p1, p2], [p3, p4], [ch, cb]]
        case "A09": ## J
            LINES = [[phg, p2], [p2, pdb]]
            img.ellipse(ctb, (dist(pdb, ctb), dist(ctb, cb)), col, tk, lt, 0, 135, an)
        case "A10": ## K
            p = pt_sg(cg, p3, 3)
            LINES = [[p1, p3], [p, p2], [pt_sg(p, p2, 2), p4]]
        case "A11": ## L
            LINES = [[p1, p3], [p3, p4]]
        case "A12": ## M
            LINES = [[p1, p3], [p1, pt_sg(ct, cb, 3)], [pt_sg(ct, cb, 3), p2], [p2, p4]]
        case "A13": ## N
            LINES = [[p1, p3], [p1, p4], [p2, p4]]
        case "A14": ## O
            img.ellipse(ct, (dist(ct, cd), dist(ct, ch)), col, tk, lt, angle=an)
        case "A15": ## P
            LINES = [[p1, p3], [cg, ct], [p1, ch]]
            img.ellipse(cth, (dist(ch, p2)*0.8, dist(cth, ch)), col, tk, lt, 270, 450, an)
        case "A16": ## Q
            img.ellipse(ct, (dist(ct, cd), dist(ct, ch)), col, tk, lt, angle=an)
            LINES = [[pt_sg(cb, ct, 4), p4]]
        case "A17": ## R
            LINES = [[p1, p3], [cg, ct], [p1, ch], [ct, p4]]
            img.ellipse(cth, [dist(ch, p2)*0.8, dist(cth, ch)], col, tk, lt, 270, 450, an)
        case "A18": ## S ## FIXME
            img.ellipse(cth, (dist(ch, p2)*0.8, dist(cth, ch)), col, tk, lt, 90, 300, an)
            img.ellipse(ctb, (dist(cb, p4)*0.8, dist(ctb, cb)), col, tk, lt, -90, 130, an)
        case "A19": ## T
            LINES = [[p1, p2], [ch, cb]]
        case "A20": ## U
            LINES = [[p1, pgb], [p2, pdb]]
            img.ellipse(ctb, (dist(ct, cd), dist(ctb, cb)), col, tk, lt, 0, 180, an)
        case "A21": ## V
            LINES = [[p1, cb], [p2, cb]]
        case "A22": ## W
            LINES = [[p1, pbg], [ct, pbg], [ct, pbd], [p2, pbd]]
        case "A23": ## X
            LINES = [[p1, p4], [p2, p3]]
        case "A24": ## Y
            LINES = [[p1, ct], [p2, ct], [ct, cb]]
        case "A25": ## Z
            LINES = [[p1, p2], [p2, p3], [p3, p4]]
        ########################################################
        case "B00": # a
            img.ellipse(ctb, (dist(cb, pbg), dist(ctb, cb)), col, tk, lt, angle=an)
            LINES = [[ctd, pbd]]
        case "B01": # b
            img.ellipse(ctb, (dist(cb, pbg), dist(ctb, cb)), col, tk, lt, angle=an)
            LINES = [[ct1, pbg]]
        case "B02": # c
            img.ellipse(ctb, (dist(cb, pbg), dist(ctb, cb)), col, tk, lt, 60, 300, an)





        ########################################################
        case "A000": ...
    #################################################
        case _: draw_char(img, "00", pts, col, fs, tk, lt, an, False)
    for a, b in LINES: img.line(a, b, col, tk, lt) ##
    return ##########################################
def draw_diacr(img, char, *args, **kwargs):
    match char:
        case "40": char = "E2"
        case "41": char = "E3"
        case "42": char = "E4"
        case "46": char = "E5"
        case _: char = "00"
    draw_char(img, char, *args, **kwargs)