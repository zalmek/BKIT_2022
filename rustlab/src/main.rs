use std::io;

fn main() {
    println!("Hello, world!");
    for x in get_roots_vec(getkoefs()) {
        if x > 0 as f64 {
            println!("{} {}",x.sqrt(),-x.sqrt())
        }
        else if x== 0 as f64 {
            println!("{}",x)
        }
    }
}

fn get_roots(a: i64, b: i64, c: i64) -> [f64; 2] {
    let mut result: [f64; 2] = [-99999999.9, -999999999.9];
    let d: f64 = (b * b - 4 * a * c) as f64;
    let mut root: f64 = 0.0;
    if d == 0.0 {
        root = -(b as f64) / (2.0 * (a as f64));
        result[0] = root;
    } else if d > 0.0 {
        let sq_d: f64 = d.sqrt();
        let root1 = (-(b as f64) + sq_d) / (2.0 * (a as f64));
        let root2 = (-(b as f64) - sq_d) / (2.0 * (a as f64));
        result[0] = root1;
        result[1] = root2;
    } else {}
    return result;
}

fn get_roots_vec(intvec: [i64;3]) -> [f64; 2] {
    let a: i64 = intvec[0];
    let b: i64 = intvec[1];
    let c: i64 = intvec[2];
    let mut result: [f64; 2] = [-99999999.9, -999999999.9];
    let d: f64 = (b * b - 4 * a * c) as f64;
    let mut root: f64 = 0.0;
    if d == 0.0 {
        root = -(b as f64) / (2.0 * (a as f64));
        result[0] = root;
    } else if d > 0.0 {
        let sq_d: f64 = d.sqrt();
        let root1 = (-(b as f64) + sq_d) / (2.0 * (a as f64));
        let root2 = (-(b as f64) - sq_d) / (2.0 * (a as f64));
        result[0] = root1;
        result[1] = root2;
    } else {}
    return result;
}


//"1 2 3"
fn getkoefs() -> [i64; 3] {
    loop {
        let mut input = String::new();
        println!("Enter int64 koefs");
        io::stdin()
            .read_line(&mut input)
            .expect("Неверно введена строка");
        let vec = input.split(" ").collect::<Vec<&str>>();
        let mut intvec: [i64; 3] = [0, 0, 0];
                for i in 0..3 {
                    let res_pars = (vec[i]).parse::<i64>();
                    match res_pars{
                        Ok(res_i64) => {intvec[i] = res_i64;}
                        Err(_e) => {println!("ERROR")}
                    }

                }
        return intvec;
    };
}
