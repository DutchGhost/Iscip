use std::{
    error::Error,
    io::{self, BufRead, Write},
};

const QUESTIONS: &[&str] = &[
    "Voer het aantal 1 centen in:\n",
    "Voer het aantal 2 centen in: \n",
    "Voer het aantal 5 centen in: \n",
    "Voer het aantal 10 centen in: \n",
    "Voer het aantal 20 centen in: \n",
    "Voer het aantal 50 centen in: \n",
    "Voer het aantal 1 euro's in: \n",
    "Voer het aantal 2 euro's in: \n",
];

const VALUES: &[f32] = &[0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00];

fn main() -> Result<(), Box<dyn Error + 'static>> {
    let mut ncoins = 0;
    let mut total_value: f32 = 0.0;

    {
        let stdin = io::stdin();
        let stdout = io::stdout();

        let mut stdoutlock = stdout.lock();
        let mut stdinlock = stdin.lock();

        let mut buffer = String::with_capacity(10);

        for (question, value) in QUESTIONS.iter().zip(VALUES.iter()) {
            write!(stdoutlock, "{}", question);

            let _ = stdinlock.read_line(&mut buffer)?;

            let n: usize = buffer.trim().parse()?;
            ncoins += n;
            total_value += n as f32 * value;

            buffer.clear();
        }
    } // All stdin, stdout, and locks are dropped here

    println!("You entered a total of {} coins", ncoins);
    println!("You entered a total value of {:2}", total_value);

    Ok(())
}
