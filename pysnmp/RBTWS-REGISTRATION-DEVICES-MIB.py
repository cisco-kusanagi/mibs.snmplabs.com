#
# PySNMP MIB module RBTWS-REGISTRATION-DEVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:45:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
rbtwsRegistration, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsRegistration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, Unsigned32, Counter32, MibIdentifier, ObjectIdentity, Integer32, Bits, Gauge32, IpAddress, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "Unsigned32", "Counter32", "MibIdentifier", "ObjectIdentity", "Integer32", "Bits", "Gauge32", "IpAddress", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsRegistrationDevicesMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 6))
rbtwsRegistrationDevicesMib.setRevisions(('2007-08-22 00:00',))
if mibBuilder.loadTexts: rbtwsRegistrationDevicesMib.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: rbtwsRegistrationDevicesMib.setOrganization('Enterasys Networks')
rbtwsWirelessSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1))
rbtwsSwitch8100 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 1))
rbtwsSwitch8200 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 2))
rbtwsSwitch8400 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 3))
rbtwsSwitch8110 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 4))
rbtwsSwitch8500 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 5))
mibBuilder.exportSymbols("RBTWS-REGISTRATION-DEVICES-MIB", rbtwsSwitch8110=rbtwsSwitch8110, rbtwsWirelessSwitch=rbtwsWirelessSwitch, rbtwsRegistrationDevicesMib=rbtwsRegistrationDevicesMib, rbtwsSwitch8200=rbtwsSwitch8200, PYSNMP_MODULE_ID=rbtwsRegistrationDevicesMib, rbtwsSwitch8100=rbtwsSwitch8100, rbtwsSwitch8500=rbtwsSwitch8500, rbtwsSwitch8400=rbtwsSwitch8400)
