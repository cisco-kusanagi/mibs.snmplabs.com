#
# PySNMP MIB module SPINS-DS2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPINS-DS2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:02:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, enterprises, ObjectName, Gauge32, TimeTicks, Unsigned32, Counter64, NotificationType, Integer32, ModuleIdentity, IpAddress, snmpModules, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "enterprises", "ObjectName", "Gauge32", "TimeTicks", "Unsigned32", "Counter64", "NotificationType", "Integer32", "ModuleIdentity", "IpAddress", "snmpModules", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Bits")
TimeStamp, RowStatus, TextualConvention, TruthValue, DisplayString, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "RowStatus", "TextualConvention", "TruthValue", "DisplayString", "TestAndIncr")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
spinsDeviceServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8))
spinsDS2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 2))
if mibBuilder.loadTexts: spinsDS2.setLastUpdated('240701')
if mibBuilder.loadTexts: spinsDS2.setOrganization('Lucent Technologies')
spinsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 2, 1))
mibBuilder.exportSymbols("SPINS-DS2-MIB", spinsSystem=spinsSystem, softSwitch=softSwitch, spinsDeviceServer=spinsDeviceServer, lucent=lucent, PYSNMP_MODULE_ID=spinsDS2, spinsDS2=spinsDS2, products=products)
