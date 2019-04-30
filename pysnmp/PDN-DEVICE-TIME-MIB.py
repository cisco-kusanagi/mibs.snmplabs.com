#
# PySNMP MIB module PDN-DEVICE-TIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-DEVICE-TIME-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:29:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
pdn_time, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-time")
NTPMode, = mibBuilder.importSymbols("PDN-TC", "NTPMode")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, TimeTicks, IpAddress, Gauge32, NotificationType, ObjectIdentity, Counter64, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "TimeTicks", "IpAddress", "Gauge32", "NotificationType", "ObjectIdentity", "Counter64", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Unsigned32")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
devTimeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1))
devTimeMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 2))
devTimeAndDate = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 1))
devNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2))
devDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 1, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDateAndTime.setStatus('mandatory')
devNTPServerIP = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devNTPServerIP.setStatus('mandatory')
devNTPMode = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 2), NTPMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devNTPMode.setStatus('mandatory')
devNTPSynchronised = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devNTPSynchronised.setStatus('mandatory')
mibBuilder.exportSymbols("PDN-DEVICE-TIME-MIB", devNTPSynchronised=devNTPSynchronised, devNTP=devNTP, devTimeMIBObjects=devTimeMIBObjects, devTimeMIBTraps=devTimeMIBTraps, devTimeAndDate=devTimeAndDate, devDateAndTime=devDateAndTime, devNTPServerIP=devNTPServerIP, devNTPMode=devNTPMode)
