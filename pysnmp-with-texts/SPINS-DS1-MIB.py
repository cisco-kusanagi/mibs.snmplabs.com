#
# PySNMP MIB module SPINS-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPINS-DS1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ModuleIdentity, TimeTicks, Unsigned32, MibIdentifier, ObjectName, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, snmpModules, Integer32, Counter64, ObjectIdentity, Gauge32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ModuleIdentity", "TimeTicks", "Unsigned32", "MibIdentifier", "ObjectName", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "snmpModules", "Integer32", "Counter64", "ObjectIdentity", "Gauge32", "Bits", "NotificationType")
TestAndIncr, TextualConvention, TruthValue, TimeStamp, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "TextualConvention", "TruthValue", "TimeStamp", "RowStatus", "DisplayString")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
spinsDeviceServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8))
spinsDS1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 1))
if mibBuilder.loadTexts: spinsDS1.setLastUpdated('240701')
if mibBuilder.loadTexts: spinsDS1.setOrganization('Lucent Technologies')
if mibBuilder.loadTexts: spinsDS1.setContactInfo('')
if mibBuilder.loadTexts: spinsDS1.setDescription('The MIB module for entities implementing the xxxx protocol.')
spinsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 1, 1))
mibBuilder.exportSymbols("SPINS-DS1-MIB", spinsDeviceServer=spinsDeviceServer, lucent=lucent, spinsDS1=spinsDS1, softSwitch=softSwitch, spinsSystem=spinsSystem, PYSNMP_MODULE_ID=spinsDS1, products=products)
