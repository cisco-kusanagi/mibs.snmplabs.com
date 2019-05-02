#
# PySNMP MIB module CXUserInterface-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXUserInterface-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:33:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
cxUserInterface, = mibBuilder.importSymbols("CXProduct-SMI", "cxUserInterface")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Unsigned32, TimeTicks, IpAddress, ObjectIdentity, ModuleIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, MibIdentifier, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "TimeTicks", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "MibIdentifier", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
uiPassword = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 8, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 16)).clone('Supervisor')).setMaxAccess("writeonly")
if mibBuilder.loadTexts: uiPassword.setStatus('mandatory')
if mibBuilder.loadTexts: uiPassword.setDescription('Determines the password the system requires to allow users to gain access to the console port. You must enter this password when you are using a TTY terminal or a PC running a TTY terminal emulation program to configure the console port. Range of Values: from 6 to 16 alphanumeric characters. You can use any combination of letters and numbers, however you cannot use blank spaces. Use a dash or underscore as a delimiter. Default Value: Supervisor Configuration Changed: operative')
uiTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 8, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 65535)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uiTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: uiTimeOut.setDescription('Determines the length of time, in seconds, the console port can remain inactive before the system logs out the user. Once the timer expires, the user needs to log in again to regain access to the console port. Range of Values: a maximum of five digits between 10 and 65535. Default Value: 600 Configuration Changed: operative')
mibBuilder.exportSymbols("CXUserInterface-MIB", uiTimeOut=uiTimeOut, uiPassword=uiPassword)
