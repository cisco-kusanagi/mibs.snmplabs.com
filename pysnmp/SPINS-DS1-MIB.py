#
# PySNMP MIB module SPINS-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPINS-DS1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:02:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, TimeTicks, NotificationType, enterprises, Integer32, IpAddress, ModuleIdentity, snmpModules, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectName, Counter64, Gauge32, ObjectIdentity, MibIdentifier, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "TimeTicks", "NotificationType", "enterprises", "Integer32", "IpAddress", "ModuleIdentity", "snmpModules", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectName", "Counter64", "Gauge32", "ObjectIdentity", "MibIdentifier", "Counter32", "Bits")
TruthValue, TimeStamp, DisplayString, RowStatus, TextualConvention, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "DisplayString", "RowStatus", "TextualConvention", "TestAndIncr")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
spinsDeviceServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8))
spinsDS1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 1))
if mibBuilder.loadTexts: spinsDS1.setLastUpdated('240701')
if mibBuilder.loadTexts: spinsDS1.setOrganization('Lucent Technologies')
spinsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 1, 1))
mibBuilder.exportSymbols("SPINS-DS1-MIB", spinsSystem=spinsSystem, softSwitch=softSwitch, spinsDS1=spinsDS1, lucent=lucent, spinsDeviceServer=spinsDeviceServer, products=products, PYSNMP_MODULE_ID=spinsDS1)
