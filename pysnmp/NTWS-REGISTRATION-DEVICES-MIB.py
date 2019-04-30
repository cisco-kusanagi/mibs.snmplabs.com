#
# PySNMP MIB module NTWS-REGISTRATION-DEVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntwsRegistration, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsRegistration")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter64, Gauge32, Bits, Counter32, NotificationType, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, ModuleIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "Gauge32", "Bits", "Counter32", "NotificationType", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsRegistrationDevicesMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 6))
ntwsRegistrationDevicesMib.setRevisions(('2008-08-08 00:01', '2007-08-22 00:00',))
if mibBuilder.loadTexts: ntwsRegistrationDevicesMib.setLastUpdated('200808080001Z')
if mibBuilder.loadTexts: ntwsRegistrationDevicesMib.setOrganization('Nortel Networks')
ntwsWirelessSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1))
ntwsSwitch2360 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 2))
ntwsSwitch2380 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 3))
ntwsSwitch2350 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 4))
ntwsSwitch2372 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 5))
ntwsSwitch2382 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 6))
ntwsSwitch2800 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 7))
mibBuilder.exportSymbols("NTWS-REGISTRATION-DEVICES-MIB", ntwsRegistrationDevicesMib=ntwsRegistrationDevicesMib, ntwsSwitch2800=ntwsSwitch2800, ntwsWirelessSwitch=ntwsWirelessSwitch, PYSNMP_MODULE_ID=ntwsRegistrationDevicesMib, ntwsSwitch2382=ntwsSwitch2382, ntwsSwitch2372=ntwsSwitch2372, ntwsSwitch2360=ntwsSwitch2360, ntwsSwitch2380=ntwsSwitch2380, ntwsSwitch2350=ntwsSwitch2350)
