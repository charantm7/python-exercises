const credentials = {
  charan: "charan",
  dheeraj: "Dheeraj",
};

const main = (user, password) => {
  if (!user || !password) {
    return "Invalid credentials";
  }

  if (credentials[user]) {
    if (credentials[user] === password) {
      return "Login Successfull";
    } else {
      return "Incorrect Password";
    }
  } else {
    return "User not found";
  }
};

const PasswordStrenghtChecker = (password) => {
  const Uppercase = /[A-Z]/.test(password);
  const Lowercase = /[a-z]/.test(password);
  const Digits = /[0-9]/.test(password);
  const symbols = /[!@#$%^&*()_+<>,.|]/.test(password);

  return { Uppercase, Lowercase, Digits, symbols };
};

const signup = (user, password, cpassword) => {
  if (!user || !password || !cpassword) {
    return "Invalid credentials";
  }

  if (user == password) {
    return "Password must not be username";
  }

  if (password !== cpassword) {
    return "Password does not match";
  }

  const check = PasswordStrenghtChecker(password);

  switch (true) {
    case password.length < 8:
      return "Password must be 8 characters.";

    case !check.Digits:
      return "Password must contain Digits";

    case !check.Lowercase:
      return "Password must contain lowercase letters";

    case !check.Uppercase:
      return "Password must contain uppercase letters";

    case !check.symbols:
      return "Password must contain the special characters";
  }
  if (credentials[user]) {
    return "Username already exists";
  } else {
    credentials[user] = password;
    return "User created successfully, Login to Access web page";
  }
};

// console.log(main("charan", "charan"));
// console.log(main("charan", "charan1"));
// console.log(main("hello", "charan"));

console.log(signup("hbk", "Charantm@2005", "Charantm@2005"));
