import turtle

# Part 1: Getting Started

wn = turtle.Screen()
wn.title('Pong by @DEM_1323')
wn.bgcolor('black')
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Scores

player_a_score = 0
player_b_score = 0

        
# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0) 
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-360, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0) 
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = .3
ball.dy = .3

# Player 1 Movement

def player_move_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

    if paddle_a.ycor() > 240:
        paddle_a.goto(paddle_a.xcor(), 240)

def player_move_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

    if paddle_a.ycor() < -230:
        paddle_a.goto(paddle_a.xcor(), -230)

# Player 2 Movement

def player2_move_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

    if paddle_b.ycor() > 240:
        paddle_b.goto(paddle_b.xcor(), 240)
    

def player2_move_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

    if paddle_b.ycor() < -230:
        paddle_b.goto(paddle_b.xcor(), -230)

# Ball Movement

def ball_move():
    global player_a_score 
    global player_b_score 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.dy *= -1
    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_a_score += 1
        print_score()
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_b_score += 1
        print_score()
    if (ball.xcor() > paddle_b.xcor() - 20 and ball.xcor() < paddle_b.xcor() + 20) and ((ball.ycor() < paddle_b.ycor() + 25) and (ball.ycor() > paddle_b.ycor() - 25)):
        ball.dx *= -1 
    elif (ball.xcor() > paddle_a.xcor() - 20 and ball.xcor() < paddle_a.xcor() + 20) and ((ball.ycor() < paddle_a.ycor() + 25) and (ball.ycor() > paddle_a.ycor() - 25)):
        ball.dx *= -1 

# Keybinds

wn.listen()
wn.onkeypress(player_move_up, 'w')
wn.onkeypress(player_move_down, 's')
wn.onkeypress(player2_move_up, 'Up')
wn.onkeypress(player2_move_down, 'Down')


# Score Board

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Player  A:  {player_a_score}     |      Player  B:  {player_b_score}', align = 'center', font = ('Ariel', 24, 'bold'))

def print_score():
    pen.clear()
    pen.write(f'Player  A:  {player_a_score}     |      Player  B:  {player_b_score}', align = 'center', font = ('Ariel', 24, 'bold'))

# Game End

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color('black')
pen2.penup()
pen2.hideturtle()
pen2.goto(0,0)

def game_end(player):
    wn.clear()
    pen2.write(f'Player {player} Won', align = 'center', font =('Ariel', 24, 'bold'))
    
# Main Game Loop

def main():
    play = True

    while play:
        wn.update()
        ball_move()

        if player_a_score == 3 and player_b_score < 3:
            game_end('A')
            play = False
        elif player_b_score == 3 and player_a_score < 3:
            game_end('B')
            play = False
    
    

if __name__ == '__main__':
    main()