# VSDC-KAR-IAOMR-CONFERENCE

Welcome to the VSDC Karnataka IAOMR Conference project repository!

This full-stack project is designed for managing the VSDC Karnataka IAOMR conference. It utilizes HTML, CSS, JavaScript, Node.js, Express, and MongoDB technologies to provide a comprehensive platform for event management.

## Features

- **Event Details**: The front page includes all the relevant details of the VSDC Karnataka IAOMR conference.
  
- **Registration**: Users can register for the conference using unique QR codes for students, staff, and pre-conference events.
  
- **Payment Handling**: Upon payment, a unique 4-digit ID is generated and stored in the MongoDB database. Currently, UPI transaction IDs are manually verified, but integration with a payment gateway is feasible.
  
- **Confirmation Email**: Upon successful registration, users receive a confirmation email containing their unique ID.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Node.js, Express
- **Database**: MongoDB

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/DEEPTHIIIIII/VSDC-KAR-IAOMR-CONFERENCE.git
   ```

2. Navigate to the project directory:

   ```
   cd VSDC-KAR-IAOMR-CONFERENCE
   ```

3. Install dependencies:

   ```
   npm install
   ```

4. Set up MongoDB:
   
   - Install MongoDB on your system if not already installed.
   - Configure the MongoDB connection in `server.js` .

5. Start the server:

   ```
   node server.js
   ```

6. Access the application:

   Open a web browser and go to `http://localhost:3000` to access the application.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

