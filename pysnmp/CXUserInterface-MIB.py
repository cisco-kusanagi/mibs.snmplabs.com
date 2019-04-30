#
# PySNMP MIB module CXUserInterface-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXUserInterface-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
cxUserInterface, = mibBuilder.importSymbols("CXProduct-SMI", "cxUserInterface")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Gauge32, ModuleIdentity, Counter64, Unsigned32, MibIdentifier, Counter32, NotificationType, iso, TimeTicks, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Gauge32", "ModuleIdentity", "Counter64", "Unsigned32", "MibIdentifier", "Counter32", "NotificationType", "iso", "TimeTicks", "ObjectIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
uiPassword = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 8, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 16)).clone('Supervisor')).setMaxAccess("writeonly")
if mibBuilder.loadTexts: uiPassword.setStatus('mandatory')
uiTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 8, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 65535)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uiTimeOut.setStatus('mandatory')
mibBuilder.exportSymbols("CXUserInterface-MIB", uiTimeOut=uiTimeOut, uiPassword=uiPassword)
