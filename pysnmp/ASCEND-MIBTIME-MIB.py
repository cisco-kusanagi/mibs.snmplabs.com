#
# PySNMP MIB module ASCEND-MIBTIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBTIME-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Gauge32, Bits, NotificationType, Unsigned32, ObjectIdentity, MibIdentifier, IpAddress, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Gauge32", "Bits", "NotificationType", "Unsigned32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibtimeDateProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 130))
mibtimeDateProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 130, 1), )
if mibBuilder.loadTexts: mibtimeDateProfileTable.setStatus('mandatory')
mibtimeDateProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1), ).setIndexNames((0, "ASCEND-MIBTIME-MIB", "timeDateProfile-Index-o"))
if mibBuilder.loadTexts: mibtimeDateProfileEntry.setStatus('mandatory')
timeDateProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 1), Integer32()).setLabel("timeDateProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: timeDateProfile_Index_o.setStatus('mandatory')
timeDateProfile_Time_Hour = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 2), Integer32()).setLabel("timeDateProfile-Time-Hour").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Time_Hour.setStatus('mandatory')
timeDateProfile_Time_Minute = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 3), Integer32()).setLabel("timeDateProfile-Time-Minute").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Time_Minute.setStatus('mandatory')
timeDateProfile_Time_Second = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 4), Integer32()).setLabel("timeDateProfile-Time-Second").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Time_Second.setStatus('mandatory')
timeDateProfile_Date_Weekday = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("sunday", 2), ("monday", 3), ("tuesday", 4), ("wednesday", 5), ("thursday", 6), ("friday", 7), ("saturday", 8)))).setLabel("timeDateProfile-Date-Weekday").setMaxAccess("readonly")
if mibBuilder.loadTexts: timeDateProfile_Date_Weekday.setStatus('mandatory')
timeDateProfile_Date_Month = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("january", 2), ("february", 3), ("march", 4), ("april", 5), ("may", 6), ("june", 7), ("july", 8), ("august", 9), ("september", 10), ("october", 11), ("november", 12), ("december", 13)))).setLabel("timeDateProfile-Date-Month").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Date_Month.setStatus('mandatory')
timeDateProfile_Date_Year = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 7), Integer32()).setLabel("timeDateProfile-Date-Year").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Date_Year.setStatus('mandatory')
timeDateProfile_Date_Day = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 8), Integer32()).setLabel("timeDateProfile-Date-Day").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Date_Day.setStatus('mandatory')
timeDateProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("timeDateProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBTIME-MIB", timeDateProfile_Action_o=timeDateProfile_Action_o, timeDateProfile_Index_o=timeDateProfile_Index_o, timeDateProfile_Time_Second=timeDateProfile_Time_Second, timeDateProfile_Date_Weekday=timeDateProfile_Date_Weekday, timeDateProfile_Time_Hour=timeDateProfile_Time_Hour, mibtimeDateProfileTable=mibtimeDateProfileTable, timeDateProfile_Date_Month=timeDateProfile_Date_Month, DisplayString=DisplayString, timeDateProfile_Time_Minute=timeDateProfile_Time_Minute, mibtimeDateProfile=mibtimeDateProfile, timeDateProfile_Date_Day=timeDateProfile_Date_Day, mibtimeDateProfileEntry=mibtimeDateProfileEntry, timeDateProfile_Date_Year=timeDateProfile_Date_Year)
