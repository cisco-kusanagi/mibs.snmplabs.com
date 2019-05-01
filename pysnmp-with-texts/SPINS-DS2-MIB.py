#
# PySNMP MIB module SPINS-DS2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPINS-DS2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, enterprises, ModuleIdentity, Unsigned32, snmpModules, ObjectName, Integer32, Gauge32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, NotificationType, Counter32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "enterprises", "ModuleIdentity", "Unsigned32", "snmpModules", "ObjectName", "Integer32", "Gauge32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "NotificationType", "Counter32", "MibIdentifier", "Bits")
DisplayString, TestAndIncr, TimeStamp, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TestAndIncr", "TimeStamp", "RowStatus", "TruthValue", "TextualConvention")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
spinsDeviceServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8))
spinsDS2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 2))
if mibBuilder.loadTexts: spinsDS2.setLastUpdated('240701')
if mibBuilder.loadTexts: spinsDS2.setOrganization('Lucent Technologies')
if mibBuilder.loadTexts: spinsDS2.setContactInfo('')
if mibBuilder.loadTexts: spinsDS2.setDescription('The MIB module for entities implementing the xxxx protocol.')
spinsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 2, 1))
mibBuilder.exportSymbols("SPINS-DS2-MIB", PYSNMP_MODULE_ID=spinsDS2, spinsSystem=spinsSystem, lucent=lucent, spinsDS2=spinsDS2, spinsDeviceServer=spinsDeviceServer, products=products, softSwitch=softSwitch)
