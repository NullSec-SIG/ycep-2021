package dev.benergy10.hackerpanel.data;

import dev.benergy10.hackerpanel.data.model.LoggedInUser;

import java.io.IOException;

/**
 * Class that handles authentication w/ login credentials and retrieves user information.
 */
public class LoginDataSource {

    public Result<LoggedInUser> login(String username, String password) {

        try {
            if (username.equals("hacker") && password.equals("bypassthis!")) {
                LoggedInUser fakeUser = new LoggedInUser(java.util.UUID.randomUUID().toString(), "hacker");
                return new Result.Success<>(fakeUser);
            }
            else {
                return new Result.Error(new Exception());
            }
        } catch (Exception e) {
            return new Result.Error(new IOException());
        }
    }

    public void logout() {
        // TODO: revoke authentication
    }
}