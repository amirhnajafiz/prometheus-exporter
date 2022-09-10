use std::{
    io::{prelude::*, BufRead},
    net::{TcpListener, TcpStream},
};

fn main() {
    // creating a TCP listener
    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        println!("Connection established!");
    }
}
