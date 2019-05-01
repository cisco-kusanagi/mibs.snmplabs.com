#
# PySNMP MIB module RBTWS-REGISTRATION-DEVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
rbtwsRegistration, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsRegistration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, Unsigned32, ModuleIdentity, IpAddress, Counter32, Bits, iso, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "IpAddress", "Counter32", "Bits", "iso", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbtwsRegistrationDevicesMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 6))
rbtwsRegistrationDevicesMib.setRevisions(('2007-08-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbtwsRegistrationDevicesMib.setRevisionsDescriptions(('v1.0: initial version, published in 6.2 release',))
if mibBuilder.loadTexts: rbtwsRegistrationDevicesMib.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: rbtwsRegistrationDevicesMib.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: rbtwsRegistrationDevicesMib.setContactInfo('www.enterasys.com')
if mibBuilder.loadTexts: rbtwsRegistrationDevicesMib.setDescription("The MIB module for Enterasys Networks wireless device OID registrations. Copyright 2007 Enterasys Networks, Inc. All rights reserved. This SNMP Management Information Base Specification (Specification) embodies confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Enterasys Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
rbtwsWirelessSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1))
rbtwsSwitch8100 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 1))
rbtwsSwitch8200 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 2))
rbtwsSwitch8400 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 3))
rbtwsSwitch8110 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 4))
rbtwsSwitch8500 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 5))
mibBuilder.exportSymbols("RBTWS-REGISTRATION-DEVICES-MIB", rbtwsSwitch8400=rbtwsSwitch8400, PYSNMP_MODULE_ID=rbtwsRegistrationDevicesMib, rbtwsSwitch8110=rbtwsSwitch8110, rbtwsWirelessSwitch=rbtwsWirelessSwitch, rbtwsRegistrationDevicesMib=rbtwsRegistrationDevicesMib, rbtwsSwitch8200=rbtwsSwitch8200, rbtwsSwitch8500=rbtwsSwitch8500, rbtwsSwitch8100=rbtwsSwitch8100)
