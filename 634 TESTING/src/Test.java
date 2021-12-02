import java.sql.Driver;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Test {
public static void main(String[] args) throws InterruptedException
{
	System.setProperty("webdriver.chrome.driver", "F:\\softwares\\chromedriver.exe");
	WebDriver cd=new ChromeDriver();
	cd.get("http://localhost:8000/");//hitting url
	System.out.println(cd.getTitle());//validate if your page title is correct
	System.out.println(cd.getCurrentUrl());//validate if you are landed on current url
	Thread.sleep(3000);
	cd.manage().window().maximize();
	cd.findElement(By.linkText("About Us")).click();
	System.out.println(cd.getCurrentUrl());
	cd.findElement(By.linkText("Services")).click();
	System.out.println(cd.getCurrentUrl());
	cd.findElement(By.linkText("Contact Us")).click();
	System.out.println(cd.getCurrentUrl());
	Thread.sleep(3000);
	cd.findElement(By.linkText("Login")).click();
	Thread.sleep(3000);
	cd.findElement(By.linkText("Admin Login")).click();
	cd.findElement(By.xpath("//*[@name='username']")).sendKeys("admin");
	cd.findElement(By.xpath("//*[@id='password']")).sendKeys("admin");
	cd.findElement(By.xpath("//*[@type='submit']")).click();
	Thread.sleep(3000);
	cd.findElement(By.linkText("Add Faculty")).click();
	Thread.sleep(3000);
	cd.findElement(By.name("fullname")).sendKeys("Alexandra Harner");
	Thread.sleep(3000);
	cd.findElement(By.className("form-control")).sendKeys("zheng@gmail.com");
	cd.findElement(By.xpath("//*[@name='password']")).sendKeys("admin");
	Thread.sleep(3000);
	cd.findElement(By.name("dob")).sendKeys("29-01-2021");
	cd.findElement(By.name("phone")).sendKeys("1234567890");
	cd.findElement(By.xpath("//*[@id='id_addr']")).sendKeys("U.S.A");
	cd.findElement(By.xpath("//*[@type='submit']")).click();
	Thread.sleep(3000);
	cd.quit();
	
}
}
