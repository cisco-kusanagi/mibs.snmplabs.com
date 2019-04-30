#
# PySNMP MIB module FC-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FC-DS1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:58:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Counter64, iso, Gauge32, snmpModules, Unsigned32, ObjectIdentity, MibIdentifier, TimeTicks, Counter32, enterprises, Bits, ObjectName, IpAddress, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Counter64", "iso", "Gauge32", "snmpModules", "Unsigned32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Counter32", "enterprises", "Bits", "ObjectName", "IpAddress", "ModuleIdentity", "NotificationType")
RowStatus, TestAndIncr, TextualConvention, TruthValue, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TestAndIncr", "TextualConvention", "TruthValue", "DisplayString", "TimeStamp")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
fcDeviceServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9))
fcDS1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 1))
if mibBuilder.loadTexts: fcDS1.setLastUpdated('240701')
if mibBuilder.loadTexts: fcDS1.setOrganization('Lucent Technologies')
fcSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 1, 1))
fCServer = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fCServer.setStatus('current')
fCApp = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2048))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fCApp.setStatus('current')
fCDescText = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fCDescText.setStatus('current')
mibBuilder.exportSymbols("FC-DS1-MIB", fcDeviceServer=fcDeviceServer, products=products, fcDS1=fcDS1, fcSystem=fcSystem, PYSNMP_MODULE_ID=fcDS1, fCDescText=fCDescText, fCApp=fCApp, fCServer=fCServer, softSwitch=softSwitch, lucent=lucent)
