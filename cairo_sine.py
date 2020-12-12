import cairo


with cairo.SVGSurface("sine.svg", 200, 200) as surface:
    context = cairo.Context(surface)
    x, y, x1, y1 = 0.0, 0.5, 1, 0.5
    context.scale(200, 200)
    context.set_line_width(0.02)
    context.move_to(x, y)
    context.line_to(x1,y1)
    context.stroke()




