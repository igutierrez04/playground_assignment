Playground Assignment

Level 1
    - When a user visits http://localhost:5000/play, have it render three beautiful looking blue boxes. Please use a teemplate to reender this

Level 2
    - When a user visits http://localhost:5000/play/(x), have it display the beautiful looking blue boxes x times. For example, http://localhost:5000/play/7 should display these blue boxes 7 times. Calling http://localhost:5000/play/35 would display these blue boxes 35 times.

Level 3
    - When a user visits http://localhost:5000/play/(x)/(color), have it display beautiful looking boxes x timees, but this time where the boxes appear in (color). For example, http://localhost:5000/play/5/green would display 5 beaufitul green boxes. Calling http://localhost:5000/play/35/red would display 35 beautiful red boxes


Tasks
    - Create a new Flask project
    - Have the /play route render a template with 3 blue boxes
    - Have the /play/<x> route render a template with x number of blue boxes
    - Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided values
    -NINJA BONUS: Use only one template for the whole project