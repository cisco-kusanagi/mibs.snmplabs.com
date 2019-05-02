#
# PySNMP MIB module NTWS-REGISTRATION-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ntwsRegistration, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsRegistration")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, Gauge32, MibIdentifier, TimeTicks, NotificationType, Counter32, Bits, ObjectIdentity, Unsigned32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Gauge32", "MibIdentifier", "TimeTicks", "NotificationType", "Counter32", "Bits", "ObjectIdentity", "Unsigned32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntwsRegistrationChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 5))
ntwsRegistrationChassisMib.setRevisions(('2007-08-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsRegistrationChassisMib.setRevisionsDescriptions(('v1.0: initial version',))
if mibBuilder.loadTexts: ntwsRegistrationChassisMib.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: ntwsRegistrationChassisMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsRegistrationChassisMib.setContactInfo('www.nortelnetworks.com')
if mibBuilder.loadTexts: ntwsRegistrationChassisMib.setDescription("The MIB module for Nortel Networks wireless switch chassis component OID registrations. These are generic OIDs: they apply to any switch model, if the respective chassis component is present in the switch. Copyright 2007 Nortel Networks. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
ntwsChassisComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4))
ntwsChasCompPowerSupplies = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1))
ntwsChasCompFans = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2))
ntwsChasCompPowerSupply1 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1, 1))
ntwsChasCompPowerSupply2 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1, 2))
ntwsChasCompFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 1))
ntwsChasCompFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 2))
ntwsChasCompFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 3))
mibBuilder.exportSymbols("NTWS-REGISTRATION-CHASSIS-MIB", ntwsChasCompPowerSupplies=ntwsChasCompPowerSupplies, PYSNMP_MODULE_ID=ntwsRegistrationChassisMib, ntwsChasCompFan3=ntwsChasCompFan3, ntwsChasCompPowerSupply2=ntwsChasCompPowerSupply2, ntwsRegistrationChassisMib=ntwsRegistrationChassisMib, ntwsChasCompFans=ntwsChasCompFans, ntwsChasCompPowerSupply1=ntwsChasCompPowerSupply1, ntwsChasCompFan1=ntwsChasCompFan1, ntwsChassisComponents=ntwsChassisComponents, ntwsChasCompFan2=ntwsChasCompFan2)
