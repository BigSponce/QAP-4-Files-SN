// Description: Program for St. John's Marina to keep track of yearly members.
// Author: Spencer
// Dates: Mar. 19 2025 - 


// Define constants.
const CLEANING_CHARGE = 50.00;
const VIDEO_CHARGE = 35.00;
const ALT_MEM_COST = 5.00;

const EVEN_SITE_COST = 80.00;
const ODD_SITE_COST = 120.00;

const HST_RATE = .15;
const MONTH_DUE_STD = 75.00;
const MONTH_DUE_EXEC = 150.00;

const PROCESS_FEE = 59.99;
const CANCEL_FEE = .6;


// Define format options.
const cur2Format = new Intl.NumberFormat("en-CA", {
    style: "currency",
    currency: "CAD",
    minimumFractionDigits: "2",
    maximumFractionDigits: "2",
});

// Gather user inputs.
let CurDate = prompt("Enter the date (YYYY-MM-DD): ");
let SiteNum = prompt("Enter the site number (1-100): ");
SiteNum = parseInt(SiteNum);

let MemName = prompt("Enter the member name: ");
let StreetAdd =  prompt("Enter the street address: ");
let City = prompt("Enter the city: ");
let Prov = prompt("Enter the province (XX): ");
let Postal = prompt("Enter the postal code (X0X0X0): ");

let PhoneNum = prompt("Enter the home phone (0000000000): ");
let CellNum = prompt ("Enter the cellphone number (0000000000): ");

let MemType = prompt("Enter the membership type (S / E): ");
let AltMem = prompt("Enter the number of additional members (#): ");
AltMem = parseInt(AltMem);

let Cleaning = prompt("Enter the cleaning option (Y / N): ");
let Video = prompt("Enter the video surveilance option (Y / N): ");


// Perform program calculations.
let SiteCharge = 0
if (SiteNum % 2 == 0) {
    SiteCharge = EVEN_SITE_COST
} else {
    SiteCharge = ODD_SITE_COST
}
let AltMemCost = AltMem *  ALT_MEM_COST;
let TotalSiteCharge = SiteCharge + AltMemCost;

let CleaningCharge = 0;
let CleaningFull = 0;

if (Cleaning == "Y") {
    CleaningCharge = CLEANING_CHARGE
    CleaningFull = "Yes"
} else {
    CleaningFull = "No"
}


let VideoCharge = 0;
VideoFull = 0;

if (Video == "Y") {
    VideoCharge = VIDEO_CHARGE
    VideoFull = "Yes"
} else {
    VideoFull = "No"
}

let ExtraCharges = CleaningCharge + VideoCharge;

let Subtotal = TotalSiteCharge + ExtraCharges;
let HST = Subtotal * HST_RATE;
let TotalMonthCharge = Subtotal + HST;

let MemberFull = 0;
let MonthDues = 0;

if (MemType == "S") {
    MonthDues = MONTH_DUE_STD
    MemberFull = "Standard"
} else {
    MonthDues = MONTH_DUE_EXEC
    MemberFull = "Executive"
}

let TotalMonthFees = TotalMonthCharge + MonthDues;

let YearlyFees = TotalMonthFees * 12;

let MonthlyPayment = (YearlyFees + PROCESS_FEE) / 12;
let CancelFee = YearlyFees * CANCEL_FEE;


// Display results.
document.writeln("<br />");
document.writeln("<table class='invoicetable'>");
 
document.writeln("<tr>");
document.writeln("<td colspan='2' class='centertext'>St. John's Marina & Yacht Club</br>Yearly Member Reciept</td>");
document.writeln("</tr>");
 
document.writeln("<tr>");
document.writeln("<td colspan='2'><br />Client Name and Address:<br /><br /></td>");
document.writeln("</tr>");
 
document.writeln("<tr>");
document.writeln("<td colspan='2'>" + MemName + "<br />" + StreetAdd + "<br />" + City + ", " + Prov + " " + Postal + "</br></br>" + "Phone: " + PhoneNum + "</br>" + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + CellNum + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='right'>" + "Site #: " + SiteNum + "</td>" +
    "<td class='left'>" + "Member type: " + MemberFull +"</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='right'>" + "Alternate members: " + "<br />" + "Weekly site cleaning: " + "<br />" + "Video surveillance: " + "</td>" + 
    "<td class='left'>" + AltMem + "<br />" + CleaningFull + "<br />" + VideoFull + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='right'>" + "Site charges: " + "<br />" + "Extra Charges:" +"</td>" + 
    "<td class='left'>" + cur2Format.format(TotalSiteCharge) + "<br />" + cur2Format.format(ExtraCharges) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='right'>" + "Subtotal:" + "<br />" + "Sales tax (HST):" + "</td>" + 
    "<td class='left'>" + cur2Format.format(Subtotal) + "<br />" + cur2Format.format(HST) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='right'>" + "Total monthly charges:" + "<br />" + "Monthly dues:" + "</td>" + 
    "<td class='left'>" + cur2Format.format(TotalMonthCharge) + "<br />" + cur2Format.format(MonthDues) +"</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='right'>" + "Total monthly fees:" + "<br />" + "Total yearly fees:" + "</td>" + 
    "<td class='left'>" + cur2Format.format(TotalMonthFees) + "<br />" + cur2Format.format(YearlyFees) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='right'>" + "Monthly payment:" + "</td>" + 
    "<td class='left'>" + cur2Format.format(MonthlyPayment) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='right'>" + "Issued:" + "<br />" + "HST Reg No" + "<br />" + "Cancellation fee:" + "</td>" + 
    "<td class='left'>" + CurDate + "<br />" + "549-33-5849-47" + "<br />" + cur2Format.format(CancelFee) + "</td>");
document.writeln("</tr>");