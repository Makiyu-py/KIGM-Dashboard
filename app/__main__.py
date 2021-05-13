from sys import argv
from app import app

if len(argv) > 1:
    
    # TODO: An actual flag system instead of using sys.argv lists

    # check port flags
    try:
        port = int(argv[argv.index("-p")+1])
    except (KeyError, ValueError, IndexError):
        port = 5000

    # checks site mode/status
    try:
        site_mode = argv[argv.index("--mode")+1]
    except (KeyError, ValueError, IndexError):
        site_mode = "development"

    if site_mode.lower() in ("prod", "production"):
        app.run(port=port)
    else:
        app.run(debug=True, port=port)
        
else:
    app.run(debug=True)