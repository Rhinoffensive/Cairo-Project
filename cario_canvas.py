import cairo
import math
import numpy as np
import random

WIDTH, HEIGHT = 600, 600
bStart = (0,0.5), (1,0.5)
sinOffsetStart, sinOffsetEnd = 0.0, 0.0
A, f = 0.4, 5

matrixScalerX, matrixScalerY = 50, 50

with cairo.SVGSurface("eexampe.svg", WIDTH, HEIGHT) as surface:
    context = cairo.Context(surface)
    context.set_line_width(0.05)
    context.set_source_rgb(0, 0, 0)
    context.scale(WIDTH / matrixScalerX, HEIGHT / matrixScalerY)


    for ys in range(matrixScalerY):
        for xs in range(matrixScalerX):
            bStart, bEnd = (xs, ys + 0.5), (xs + 1, ys + 0.5)
            x0, y0, x1, y1 = *bStart, *bEnd
            context.move_to(x0, y0)
            context.line_to(bStart[0] + sinOffsetStart, y0)

            f = xs
            A = (ys + random.random() + 5) / 100


            for x in np.linspace((bStart[0] + sinOffsetStart) * WIDTH, (bEnd[0] - sinOffsetEnd) * WIDTH , 1000):
                xp = x / WIDTH
                context.line_to(xp, (np.sin(2 * math.pi * xp * f) * A * (math.cos(2 * math.pi * xp * f * 0.1)) + y0))
            context.line_to(*bEnd)
        context.stroke()
