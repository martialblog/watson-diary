#!/usr/bin/env python3


import dashboard

def main():

    app = dashboard.create_app()

    app.run(host='0.0.0.0',
            debug=True,
            port=5000)

if __name__ == "__main__":
    main()
