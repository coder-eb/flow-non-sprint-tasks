const express = require('express');
const app = express();
const fs = require('fs');

//Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true}))

//ROUTES
app.get('/', (req,res) => {
    res.send('Welcome to the Library');
});

const dbFile = "db.json";

app.post('/list_books', (req,res) =>{
    fs.readFile(dbFile, function(err, data){
        try {
            if(err) throw new Error('Database file error');
            let body = req.body;
            var books = JSON.parse(data);

            let fields_to_filter = ['purchase_date', 'author']
            for (let field_to_filter of fields_to_filter) {
                if (field_to_filter in body) {
                    var books = books.filter(book => {
                        return book[field_to_filter] === body[field_to_filter];
                    })
                }
            }
            if ( books.length === 0 ) {
                res.send({'message': 'No books found'})
            }
            else {
                res.send(books);
            }
        }
        catch (err) {
            res.status(500).send(err.message)
        }
    }); 
});

const validate_req = (body, fields_to_check, res) => {
    
    let missing_fields = []
    for (let field_to_check of fields_to_check) {
        if (!(field_to_check in body)) {
            missing_fields.push(field_to_check)
        }
    }
    let no_of_missing = missing_fields.length;
    if (no_of_missing !== 0) {
        let res_string = 
            (no_of_missing > 1) ? 
            `Required fields: [${missing_fields}] are not present` 
            : 
            `Required field: [${missing_fields}] is not present` 

        res.status(422).send(res_string)
        return false
    }
    return true
}

app.post('/add_book', (req,res) =>{
    
    let newBook = req.body;
    let fields_to_check = ['book_name', 'author', 'category', 'purchase_date']
    let validate_success = validate_req(newBook, fields_to_check, res);

    if (validate_success) {
        fs.readFile(dbFile, function(err, data){
            try {
                if(err) throw new Error('Database file error');
        
                let books = JSON.parse(data);        
                books.push(newBook);
                
                fs.writeFileSync(dbFile, JSON.stringify(books, null, 2));
        
                res.send({ "message": "successfully inserted" });
            }
            catch (err) {
                res.status(500).send(err.message)
            }
        }); 
    }
});

app.delete('/delete_book', (req,res) =>{
    
    let fields_to_check = ['author']
    let validate_success = validate_req(req.body, fields_to_check, res);
    
    if (validate_success) {
        let author = req.body.author;
        fs.readFile(dbFile, function(err, data){
            try {
                if(err) throw new Error('Database file error');
                
                var books = JSON.parse(data);
                var books = books.filter(note => {
                    return note['author'] != author;
                })

                fs.writeFileSync(dbFile, JSON.stringify(books, null, 2));
                res.send({"message": "successfully deleted"});
            }
            catch (err) {
                res.status(500).send(err.message)
            }
        });
    }
});


app.listen(process.env.PORT || 3000);