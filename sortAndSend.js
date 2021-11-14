compare = function (x, y) {
    var num1 = parseFloat( x[2].substring(1) );
    var num2 = parseFloat( y[2].substring(1) );
    if ( num1 < num2 ) {
      return 1;
    }
    if ( num1 > num2) {
      return -1;
    }
    return 0;
  }
  
  function myFunction() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheets()[0];
    var lastRow = sheet.getLastRow();
    var products = sheet.getRange("A2:G" + lastRow ).getValues();
    sheet.getRange("A2:G" + lastRow ).clear();
    products.sort( compare );
    for( i = 0; i < products.length; i++ )
    {
      sheet.appendRow( products[i] );
    }

    var message = {
      to: "“okan@analyticahouse.com”",
      subject: "Analytica House Case Study",
      body: "Case Study Complated",
      name: "Yusuf Abdullah ARSLANALP",
      attachments: [ SpreadsheetApp.getActiveSpreadsheet().getAs(MimeType.PDF).setName("Monthly sales report.pdf") ]
    }
    MailApp.sendEmail(message);
  
  }
  