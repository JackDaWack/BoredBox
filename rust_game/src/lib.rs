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

#[wasm_bindgen]
pub struct Game {
    player_health: i32,
    monster_health: i32,
}

#[wasm_bindgen]
impl Game {
    pub fn new() -> Game {
        Game {
            player_health: 100,
            monster_health: 50,
        }
    }

    pub fn attack(&mut self) -> String {
        self.monster_health -= 10;
        if self.monster_health <= 0 {
            "Monster defeated!".to_string()
        } else {
            self.monster_attack();
            format!("Monster HP: {}", self.monster_health)
        }
    }

    fn monster_attack(&mut self) {
        self.player_health -= 5;
    }

    pub fn get_player_health(&self) -> i32 {
        self.player_health
    }
}
