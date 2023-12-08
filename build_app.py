from playwright.sync_api import Playwright, sync_playwright

app_link = input("Enter the link to your WorkDay application: ")
Email = input("Enter your email address: ")
Password = input("Enter desired password: ")
Resume = input("Enter the filepath to your resume: ")
Address = input("Enter your address: ")
City = input("Enter your city: ")
State = input("Enter your state: ")
Zip = input("Enter your zip code: ")
LinkedIn = input("Enter your LinkedIn URL: ")
GitHub = input("Enter your GitHub URL: ")


def main(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # go to page
    page.goto(app_link)
    page.get_by_role("button", name="Apply").click()
    page.get_by_role("button", name="Autofill with Resume").click()
    page.get_by_role("button", name="Create Account").click()
    # create account
    page.get_by_label("Email Address").click()
    page.get_by_label("Email Address").fill(Email)
    # password for account
    page.get_by_label("Password", exact=True).click()
    page.get_by_label("Password", exact=True).fill(Password)
    page.get_by_label("Password", exact=True).press("Tab")
    page.get_by_label("Verify New Password").fill(Password)
    page.get_by_label("Yes, I have read and consent").check()
    page.get_by_label("Create Account").click()
    # next page after account creation
    page.get_by_role("button", name="Select file").click()
    page.get_by_role("button", name="Select file").set_input_files(Resume)
    page.get_by_role("button", name="Continue").click()
    # next page after resume upload

    page.get_by_label("How Did You Hear About Us?").click()
    page.get_by_label("How Did You Hear About Us?").fill("LinkedIn")
    page.get_by_label("Address Line 1*").click()
    page.get_by_label("Address Line 1*").fill(Address)
    page.get_by_label("City*").click()
    page.get_by_label("City*").fill(State)
    page.get_by_label("Postal Code*").click()
    page.get_by_role("button", name="Save and Continue").click()
    page.get_by_role("group", name="From* current value is MM/YYYY").get_by_label(
        "Calendar"
    ).click()
    page.get_by_label("July").click()
    page.get_by_label("To*").get_by_label("Calendar").click()
    page.get_by_label("August").click()
    page.get_by_label("From", exact=True).get_by_text("YYYY").click()
    page.get_by_label("From", exact=True).get_by_label("Year").fill("2022")
    page.get_by_text("YYYY", exact=True).click()
    page.get_by_label("To (Actual or Expected)").get_by_label("Year").fill("2025")
    page.get_by_label("Add Websites").click()
    page.get_by_label("URL*").click()
    if page.get_by_label("LinkedIn").is_visible():
        page.get_by_label("URL*").fill(LinkedIn)
    elif page.get_by_label("GitHub").is_visible():
        page.get_by_label("URL*").fill("https://github.com/Sharvin-M")
    page.get_by_role("button", name="Save and Continue").click()
    page.get_by_label("Are you eligible to work in").click()
    page.get_by_text("Yes").click()
    page.get_by_label("As of today's date, are you").click()
    page.get_by_label("Do you now, or will you in").click()
    page.get_by_text("No", exact=True).click()
    page.get_by_role("button", name="Save and Continue").click()
    page.get_by_label("Asian (Not Hispanic or Latino").check()
    page.get_by_label("Please select your gender.").click()
    page.get_by_text("Male", exact=True).click()
    page.get_by_label("Please select if you identify").click()
    page.get_by_text("No", exact=True).click()
    page.get_by_label("Please select your Veteran's").click()
    page.get_by_text("I AM NOT A VETERAN").click()
    page.get_by_role("button", name="Save and Continue").click()
    page.get_by_label("Name*").click()
    page.get_by_label("Name*").fill("Sharvin Shailesh Manjrekar")
    page.get_by_label("Date*").click()
    page.get_by_label("Calendar").click()
    page.get_by_label("Selected Today").click()
    page.get_by_label("No, I do not have a").check()
    page.get_by_role("button", name="Save and Continue").click()
    page.get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        main(playwright)
