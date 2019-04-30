#
# PySNMP MIB module FC-DS2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FC-DS2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:58:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, Counter32, iso, Bits, TimeTicks, MibIdentifier, ModuleIdentity, Integer32, snmpModules, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, ObjectIdentity, IpAddress, enterprises, ObjectName = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Counter32", "iso", "Bits", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Integer32", "snmpModules", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "ObjectIdentity", "IpAddress", "enterprises", "ObjectName")
TextualConvention, DisplayString, TimeStamp, TruthValue, RowStatus, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp", "TruthValue", "RowStatus", "TestAndIncr")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
fcDeviceServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9))
fcDS2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 2))
if mibBuilder.loadTexts: fcDS2.setLastUpdated('240701')
if mibBuilder.loadTexts: fcDS2.setOrganization('Lucent Technologies')
fcSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 2, 1))
fCServer = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fCServer.setStatus('current')
fCApp = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2048))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fCApp.setStatus('current')
fCDescText = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fCDescText.setStatus('current')
mibBuilder.exportSymbols("FC-DS2-MIB", fCDescText=fCDescText, softSwitch=softSwitch, fCServer=fCServer, fcSystem=fcSystem, lucent=lucent, fcDS2=fcDS2, products=products, fCApp=fCApp, fcDeviceServer=fcDeviceServer, PYSNMP_MODULE_ID=fcDS2)
