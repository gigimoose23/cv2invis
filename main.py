import cv2 as p0, numpy as p1
import base64 as z5a

def vnm(k9, h3, t4):
    setattr(k9, h3, t4)

p1.alphaNode = p1.flip
vnm(p1, "mc1sx", p1.alphaNode)

a91 = p0.VideoCapture(1)
r4 = None
for _ in range(50): _, r4 = a91.read()

xf = "utf-8"
setattr(z5a, "l9", getattr(z5a, "b64decode"))

vnm(p0, "lfm1", p0.bitwise_and)
vnm(p0, "sqp7", p0.inRange)
vnm(p0, "xxe2", p0.imshow)
vnm(p0, "kkz9", p0.waitKey)
vnm(p0, "r1", p0.morphologyEx)
vnm(p0, "d2", p0.dilate)
vnm(p0, "e2", p0.MORPH_OPEN)

vnm(p1, "b1r", getattr(p1, z5a.l9(b"YXJyYXk=").decode(xf)))
vnm(p0, "j5", getattr(p0, z5a.l9(b"YWRkV2VpZ2h0ZWQ=").decode(xf)))
vnm(p0, "g6", getattr(p0, z5a.l9(b"Yml0d2lzZV9ub3Q=").decode(xf)))
vnm(p0, "n8", getattr(p0, z5a.l9(b"Y3Z0Q29sb3I=").decode(xf)))

r47 = p1.mc1sx(r4, 0)

while True:
    _, k0 = a91.read()
    k0445 = p1.flip(k0, 1)
    h = p0.n8(k0445, p0.COLOR_BGR2HSV)

    a = p1.b1r([100,40,40])
    b = p1.b1r([100,255,255])
    m1 = p0.sqp7(h, a, b)

    c = p1.b1r([155,40,40])
    d = p1.b1r([180,255,255])
    m2 = p0.sqp7(h, c, d)

    mf = m1 + m2
    mf = p0.r1(mf, p0.e2, p1.ones((3,3)), None, None, 2)
    mf = p0.d2(mf, p1.ones((3,3)), None, None, 1)

    invMask = p0.g6(mf)
    combo1 = p0.lfm1(r4, r4, None, mf)
    combo2 = p0.lfm1(k0, k0, None, invMask)
    final = p0.j5(combo1, 1, combo2, 1, 0)

    p0.xxe2("w", final)

    if p0.kkz9(1) == int(z5a.l9(b"MzI=").decode()):
        break
