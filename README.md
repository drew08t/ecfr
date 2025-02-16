# Getting Started

## Requirements

- [Node.js](https://nodejs.org/en)
- [Yarn](https://yarnpkg.com/)
- [Python 3](https://www.python.org/)

## Initial Setup

In the project directory, create python virtual environment.

### `cd api`

### `python3 -m venv venv`

Activate the virtual environment.

### Linux/Mac: `source venv/bin/activate`

### Windows: `venv\Scripts\activate`

Inside of the virtual environment, install python dependencies:

### `pip install flask python-dotenv iapws`

Once complete, deactive the virtual environment.

### `deactivate`

### `cd ..`

## Running

From the main directory, start the API.

### Linux/Mac: `yarn start-api-unix`

### Windows: `yarn start-api-windows`

From the main directory, install dependencies and start the frontend.

### `yarn`

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:8000/](http://localhost:8000/) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.
