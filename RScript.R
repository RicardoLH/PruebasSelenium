
library(RSelenium)
library(devtools)
prof <- list(
  browser.download.dir = "/Users/ricardolarahernandez/RStudio/",
  browser.download.folderList = 2L,
  browser.download.manager.showWhenStarting = FALSE,
  browser.helperApps.alwaysAsk.force = FALSE,
  browser.helperApps.neverAsk.saveToDisk = "application/pdf",
  plugin.scan.plid.all = FALSE,
  plugin.scan.Acrobat = "99.0",
  pdfjs.disabled=TRUE
  )
  
  
  
eCaps <- list("moz:firefoxOptions" = list(prefs=prof,args = list('--headless')))
rd <- rsDriver(browser="firefox",extraCapabilities = eCaps)
rem_dr <- rd[["client"]]
rem_dr$navigate("http://www.math.tamu.edu/~dallen/m640_03c/lectures/chapter2.pdf")
rem_dr$findElement(using = "css selector", value = "#download")$clickElement()