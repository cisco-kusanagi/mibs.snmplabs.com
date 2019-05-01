#
# PySNMP MIB module RBTWS-REGISTRATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-REGISTRATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
rbtwsRegistration, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsRegistration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, IpAddress, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Integer32, MibIdentifier, Counter32, ModuleIdentity, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "IpAddress", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Integer32", "MibIdentifier", "Counter32", "ModuleIdentity", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbtwsRegistrationMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 3))
rbtwsRegistrationMib.setRevisions(('2006-05-22 00:08', '2005-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbtwsRegistrationMib.setRevisionsDescriptions(('v2.0.7: Revised for 4.1 release', 'v1: initial version, as for 4.0 and older releases',))
if mibBuilder.loadTexts: rbtwsRegistrationMib.setLastUpdated('200605301630Z')
if mibBuilder.loadTexts: rbtwsRegistrationMib.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: rbtwsRegistrationMib.setContactInfo('www.enterasys.com')
if mibBuilder.loadTexts: rbtwsRegistrationMib.setDescription("The MIB module for Enterasys Networks wireless switch registrations. Copyright 2006 Enterasys Networks, Inc. All rights reserved. This SNMP Management Information Base Specification (Specification) embodies confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Enterasys Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
rbtwsChassisComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4))
rbtwsChasCompPowerSupplies = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1))
rbtwsChasCompFans = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2))
rbtwsChasCompPowerSupply1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1, 1))
rbtwsChasCompPowerSupply2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1, 2))
rbtwsChasCompFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 1))
rbtwsChasCompFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 2))
rbtwsChasCompFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 3))
rbtwsWirelessSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1))
rbtwsSwitch8100 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 1))
rbtwsSwitch8200 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 2))
rbtwsSwitch8400 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 3))
mibBuilder.exportSymbols("RBTWS-REGISTRATION-MIB", rbtwsSwitch8100=rbtwsSwitch8100, rbtwsWirelessSwitch=rbtwsWirelessSwitch, rbtwsChassisComponents=rbtwsChassisComponents, rbtwsChasCompFan1=rbtwsChasCompFan1, rbtwsChasCompFan2=rbtwsChasCompFan2, rbtwsChasCompFan3=rbtwsChasCompFan3, rbtwsSwitch8200=rbtwsSwitch8200, rbtwsRegistrationMib=rbtwsRegistrationMib, rbtwsChasCompPowerSupplies=rbtwsChasCompPowerSupplies, rbtwsChasCompPowerSupply2=rbtwsChasCompPowerSupply2, rbtwsChasCompPowerSupply1=rbtwsChasCompPowerSupply1, rbtwsSwitch8400=rbtwsSwitch8400, rbtwsChasCompFans=rbtwsChasCompFans, PYSNMP_MODULE_ID=rbtwsRegistrationMib)
