#
# PySNMP MIB module ASCEND-MIBTIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBTIME-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, Bits, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, ModuleIdentity, Unsigned32, IpAddress, Counter64, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Bits", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "ModuleIdentity", "Unsigned32", "IpAddress", "Counter64", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibtimeDateProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 130))
mibtimeDateProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 130, 1), )
if mibBuilder.loadTexts: mibtimeDateProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibtimeDateProfileTable.setDescription('A list of mibtimeDateProfile profile entries.')
mibtimeDateProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1), ).setIndexNames((0, "ASCEND-MIBTIME-MIB", "timeDateProfile-Index-o"))
if mibBuilder.loadTexts: mibtimeDateProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibtimeDateProfileEntry.setDescription('A mibtimeDateProfile entry containing objects that maps to the parameters of mibtimeDateProfile profile.')
timeDateProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 1), Integer32()).setLabel("timeDateProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: timeDateProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: timeDateProfile_Index_o.setDescription('')
timeDateProfile_Time_Hour = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 2), Integer32()).setLabel("timeDateProfile-Time-Hour").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Time_Hour.setStatus('mandatory')
if mibBuilder.loadTexts: timeDateProfile_Time_Hour.setDescription('Number of hours, in 24 hour format, where midnight is a zero, etc.')
timeDateProfile_Time_Minute = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 3), Integer32()).setLabel("timeDateProfile-Time-Minute").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Time_Minute.setStatus('mandatory')
if mibBuilder.loadTexts: timeDateProfile_Time_Minute.setDescription('Number of minutes since last hour.')
timeDateProfile_Time_Second = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 4), Integer32()).setLabel("timeDateProfile-Time-Second").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Time_Second.setStatus('mandatory')
if mibBuilder.loadTexts: timeDateProfile_Time_Second.setDescription('Number of seconds since last minute.')
timeDateProfile_Date_Weekday = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("sunday", 2), ("monday", 3), ("tuesday", 4), ("wednesday", 5), ("thursday", 6), ("friday", 7), ("saturday", 8)))).setLabel("timeDateProfile-Date-Weekday").setMaxAccess("readonly")
if mibBuilder.loadTexts: timeDateProfile_Date_Weekday.setStatus('mandatory')
if mibBuilder.loadTexts: timeDateProfile_Date_Weekday.setDescription('The day of the week, where Sunday is a one, and Saturday is a seven.')
timeDateProfile_Date_Month = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("january", 2), ("february", 3), ("march", 4), ("april", 5), ("may", 6), ("june", 7), ("july", 8), ("august", 9), ("september", 10), ("october", 11), ("november", 12), ("december", 13)))).setLabel("timeDateProfile-Date-Month").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Date_Month.setStatus('mandatory')
if mibBuilder.loadTexts: timeDateProfile_Date_Month.setDescription('The month of the year (i.e. 1..12).')
timeDateProfile_Date_Year = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 7), Integer32()).setLabel("timeDateProfile-Date-Year").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Date_Year.setStatus('mandatory')
if mibBuilder.loadTexts: timeDateProfile_Date_Year.setDescription("The year in 'yyyy' format should be in the range (1990 - 2089). The year in 'yy' format should be in the range (00 - 99). Year from (0 - 89) will be taken as (2000 - 2089) and (90 - 99) will be taken as (1990 - 1999).")
timeDateProfile_Date_Day = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 8), Integer32()).setLabel("timeDateProfile-Date-Day").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Date_Day.setStatus('mandatory')
if mibBuilder.loadTexts: timeDateProfile_Date_Day.setDescription('The day in the month (i.e. 1..31).')
timeDateProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("timeDateProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: timeDateProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBTIME-MIB", timeDateProfile_Time_Minute=timeDateProfile_Time_Minute, timeDateProfile_Date_Day=timeDateProfile_Date_Day, timeDateProfile_Date_Year=timeDateProfile_Date_Year, mibtimeDateProfile=mibtimeDateProfile, timeDateProfile_Action_o=timeDateProfile_Action_o, timeDateProfile_Index_o=timeDateProfile_Index_o, timeDateProfile_Time_Hour=timeDateProfile_Time_Hour, DisplayString=DisplayString, timeDateProfile_Date_Month=timeDateProfile_Date_Month, timeDateProfile_Date_Weekday=timeDateProfile_Date_Weekday, mibtimeDateProfileTable=mibtimeDateProfileTable, timeDateProfile_Time_Second=timeDateProfile_Time_Second, mibtimeDateProfileEntry=mibtimeDateProfileEntry)
