import pgzrun

WIDTH = 1000
HEIGHT = 600

player_left = Rect(20, 20, 20, 50)
player_right = Rect(WIDTH-20, 20, 20, 50)
ball = Rect(WIDTH/2-5,HEIGHT/2-5, 10, 10)


y_speed = 5
x_speed = 3
score_left = 0
score_right = 0

def update():
    global y_speed, x_speed, score_right, score_left

    if ball.right > WIDTH:
        score_left+=1
        ball.x = WIDTH/2-10
        ball.y = HEIGHT/2-10
        x_speed =-x_speed

    if ball.left < 0:
        score_right+=1
        ball.x = WIDTH/2-10
        ball.y = HEIGHT/2-10
        x_speed =-x_speed

    ball.y += y_speed
    if ball.bottom > HEIGHT or ball.top < 0:
        y_speed = -y_speed
    
    ball.x += x_speed
    if ball.colliderect(player_left) or ball.colliderect(player_right):
        x_speed = -x_speed

    if keyboard.w:
        player_left.y -= 5
    if keyboard.s:
        player_left.y += 5

    if keyboard.up:
        player_right.y -= 5
    if keyboard.down:
        player_right.y += 5

    if player_left.bottom > HEIGHT:
         player_left.bottom = HEIGHT
    if player_left.top < 0:
         player_left.top = 0
    if player_right.bottom > HEIGHT:
         player_right.bottom = HEIGHT
    if player_right.top < 0:
         player_right.top = 0

    



def draw():
    screen.clear()
    screen.draw.filled_rect(player_left, 'white')
    screen.draw.filled_rect(player_right, 'white')
    screen.draw.filled_rect(ball, 'white')
    screen.draw.text(
        str(score_left), 
        (WIDTH/2 -11,20),fontsize=30)
    screen.draw.text("-", [WIDTH/2,20], fontsize=30)
    screen.draw.text(str(score_right), [WIDTH/2 +10,20], fontsize=30)
    

pgzrun.go()