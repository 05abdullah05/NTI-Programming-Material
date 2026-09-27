// Express/MySQL registration and login demo. 
// Requires a configured MySQL database.
// To run it, install Node.js/npm, then from the renamed project folder 
// run npm install and npm start. It also needs a running MySQL server 
// and a database with the expected login table. The project already has 
// node_modules and .env, but Node/npm are not available on this laptop, 
// so I couldn’t launch it. I verified the package files, start command, 
// config path, and required files; the server has no diagnostics.

// One security caveat: bcrypt is listed as a dependency, 
// but password hashing is commented out; passwords are currently 
// stored and checked as plain text. Treat this as a learning project, 
// not a production login system.

const express = require("express");
const mysql = require("mysql2");
const dotenv = require("dotenv");
const path = require("path");
// const bcrypt = require("bcrypt");

const app = express();
app.set('view engine', 'hbs')
dotenv.config({path: path.join(__dirname, ".env")});

const publicDir = path.join(__dirname, './webbsidan')

const db = mysql.createConnection({
    // värden hämtas från .env
    host: process.env.DATABASE_HOST,
    user: process.env.DATABASE_USER,
    password: process.env.DATABASE_PASSWORD,
    database: process.env.DATABASE
});

app.use(express.urlencoded({extended: 'false'}))
app.use(express.json())

db.connect((error) => {
    if(error){
        console.log(error);
    } else{
        console.log("Ansluten till MySQL");
    }
});

// Använder mallen index.hbs
app.get("/", (req, res) => {
    res.render("index");
});

// Använder mallen register.hbs
app.get("/register", (req, res) => {
    res.render("register");
});

// Använder mallen login.hbs
app.get("/login", (req, res) => {
    res.render("login");
});


// This function is to check for the email validation
// I use regex expressions here! 
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; 
    return emailRegex.test(email);
}

// This function is to check for the password security
// I use regex expressions here again! 
function CheckPassword(password) { 
    var passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$/;
    console.log(passwordRegex.test(password));
    return passwordRegex.test(password);
    
}

// Handles registration form submissions
app.post("/auth/register",(req, res) => {    
    const { name, email, password, password_confirm } = req.body;

    // 1st Check if any of the fields are empty
    if (!name || !email || !password || !password_confirm) {
        console.log("Please fill in all fields")
        return res.render('register', {
            message: 'Vänligen fyll i alla fält'
        })
    }

    // 2nd Check if passwords match 
    if (password !== password_confirm) {
        console.log("Passwords don't match")
        return res.render('register', {
            message: 'Lösenorden matchar inte'
        })
    }

    // 3rd Check if password meets complexity requirements
    if (!CheckPassword(password)) { 
        console.log("Enter a valid password")
        return res.render('register', {
            message: 'Lösenord måste vara minst 8 tecken eller ha specialtecken'
        })
    }

    // 4th Check if email is correctly formatted
    if (!validateEmail(email)) {
        console.log("Invalid email format")
        return res.render('register', {
            message: 'Ogiltig e-postadress'
        })
    }

    // 5th Check if name or email already exists in the database
    db.query('SELECT * FROM login WHERE name = ? OR email = ?', [name, email], (err, result) => {
        if (err) {
            console.log(err)
            return res.render('register', {
                message: 'Något gick fel vid registrering'
            })
        }
        
        if (result.length > 0) {
            console.log("Name or Email already exists!")
            return res.render('register', {
                message: 'Namn eller Epost redan existerar'
            })
        }

        // If name or email doesn't exist then register the new user
        db.query('INSERT INTO login SET ?', {name: name, email: email, password: password}, (err, result) => {
            if(err) {
                console.log(err)
                return res.render('register', {
                    message: 'Något gick fel vid registrering'
                })
            } else {
                console.log("Användare registrerad");
                return res.render('register', {
                    message: 'Användare registrerad'
                })
            }       
        })
    })
})



// Tar emot poster från loginsidan
app.post("/auth/login", (req, res) => {   
    const { name, password } = req.body

    db.query('SELECT name, password FROM login WHERE name = ?', [name], async (error, result) => {
        if(error){
            console.log(error)
        }
        // Om == 0 så finns inte användaren
        if( result.length == 0 ) {
            return res.render('login', {
                message: "Användaren finns ej"
            })

        } else {

            // Vi kollar om lösenordet som är angivet matchar det i databasen
            if (password === result[0].password) {
                // I added this console log to print a message aswell!
                console.log("You have logged in!") 
                return res.render('login', {
                    message: "Du är nu inloggad"
                })
           } 
           else {
                return res.render('login', {
                    message: "Fel lösenord"
                })
           }
        }
    })
})

// Körde på 4k här bara för att skilja mig åt
// från server.js vi tidigare kört som använder 3k
app.listen(4000, ()=> {
    console.log("Servern körs, besök http://localhost:4000")
})

