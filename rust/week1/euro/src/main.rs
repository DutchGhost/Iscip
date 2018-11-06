extern crate byte_num;

use byte_num::from_ascii::FromAscii;

use std::{
    error::Error,
    io::{self, Read, Write},
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
    let mut stdin = io::stdin();
    let mut stdout = io::stdout();

    let mut buffer = vec![0; 64];

    let mut ncoins = 0;
    let mut total_value: f32 = 0.0;

    for (question, value) in QUESTIONS.iter().zip(VALUES.iter()) {
        let _ = stdout.write(question.as_bytes())?;

        let amt = stdin.read(&mut buffer)?;

        #[cfg(target_os = "windows")]
        let n = usize::atoi(&buffer[..amt - 2])?;

        #[cfg(target_os = "linux")]
        let n = usize::atoi(&buffer[..amt - 1])?;

        ncoins += n;
        total_value += n as f32 * value;
    }

    drop(stdout);
    drop(stdin);

    println!("You entered a total of {} coins", ncoins);
    println!("You entered a total value of {:2}", total_value);

    Ok(())
}
