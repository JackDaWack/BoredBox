pub fn greet(name: &str) -> String {
    format!("Welcome to BoredBox, {}!", name)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_greet() {
        let result = greet("Player");
        assert_eq!(result, "Welcome to BoredBox, Player!");
    }
}