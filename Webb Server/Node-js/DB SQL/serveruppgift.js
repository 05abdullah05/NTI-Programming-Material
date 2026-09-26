let mysql = require("mysql2")

let connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "@Abdullah123",
    database: "testar",
});

// Ansluter till databasen
connection.connect(function (err){
    if (err) throw err;
    let sql = "INSERT INTO bilar (Model, RegNr) VALUES ('KIA', 321)";
    connection.query(sql, function (err, result){
        if (err) throw err;
        console.log("Bil tillagd i databasen")
    });
});
