#
# PySNMP MIB module NTWS-REGISTRATION-DEVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ntwsRegistration, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsRegistration")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Gauge32, IpAddress, TimeTicks, ObjectIdentity, Unsigned32, iso, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Gauge32", "IpAddress", "TimeTicks", "ObjectIdentity", "Unsigned32", "iso", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsRegistrationDevicesMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 6))
ntwsRegistrationDevicesMib.setRevisions(('2008-08-08 00:01', '2007-08-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsRegistrationDevicesMib.setRevisionsDescriptions(('v1.1: added switch model 2800', 'v1.0: initial version',))
if mibBuilder.loadTexts: ntwsRegistrationDevicesMib.setLastUpdated('200808080001Z')
if mibBuilder.loadTexts: ntwsRegistrationDevicesMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsRegistrationDevicesMib.setContactInfo('www.nortelnetworks.com')
if mibBuilder.loadTexts: ntwsRegistrationDevicesMib.setDescription("The MIB module for Nortel Networks wireless device OID registrations. Copyright 2007 Nortel Networks. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
ntwsWirelessSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1))
ntwsSwitch2360 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 2))
ntwsSwitch2380 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 3))
ntwsSwitch2350 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 4))
ntwsSwitch2372 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 5))
ntwsSwitch2382 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 6))
ntwsSwitch2800 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 7))
mibBuilder.exportSymbols("NTWS-REGISTRATION-DEVICES-MIB", ntwsSwitch2380=ntwsSwitch2380, PYSNMP_MODULE_ID=ntwsRegistrationDevicesMib, ntwsSwitch2382=ntwsSwitch2382, ntwsSwitch2372=ntwsSwitch2372, ntwsSwitch2350=ntwsSwitch2350, ntwsSwitch2800=ntwsSwitch2800, ntwsRegistrationDevicesMib=ntwsRegistrationDevicesMib, ntwsWirelessSwitch=ntwsWirelessSwitch, ntwsSwitch2360=ntwsSwitch2360)
