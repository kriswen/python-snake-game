from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # set up as tuples - # Constant are name with all caps
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()  # call create_snake method
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)  # assign tuple into goto position
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())  # find end of the list, and find its x,y position

    def move(self):
        # start looping from the last segment, move to the prev segment's position
        # range takes 3 arguments ( start=2, stop=0, step=-1)
        # step is Optional. An integer number specifying the incrementation. Default is 1
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            new_position = (new_x, new_y)
            self.segments[seg_num].goto(new_position)
        # move the first segment forward by 20
        self.head.forward(MOVE_DISTANCE)
        # will continue to run and update segment positions

    def up(self):
        # snake can't go opposite direction ( to snake itself)
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # 90 = east

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  # 180 = west

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

