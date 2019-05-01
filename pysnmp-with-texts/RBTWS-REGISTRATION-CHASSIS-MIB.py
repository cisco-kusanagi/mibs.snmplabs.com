#
# PySNMP MIB module RBTWS-REGISTRATION-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
rbtwsRegistration, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsRegistration")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, TimeTicks, Unsigned32, Gauge32, MibIdentifier, iso, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "TimeTicks", "Unsigned32", "Gauge32", "MibIdentifier", "iso", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsRegistrationChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 5))
rbtwsRegistrationChassisMib.setRevisions(('2007-08-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbtwsRegistrationChassisMib.setRevisionsDescriptions(('v1.0: initial version, published in 6.2 release',))
if mibBuilder.loadTexts: rbtwsRegistrationChassisMib.setLastUpdated('200708231753Z')
if mibBuilder.loadTexts: rbtwsRegistrationChassisMib.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: rbtwsRegistrationChassisMib.setContactInfo('www.enterasys.com')
if mibBuilder.loadTexts: rbtwsRegistrationChassisMib.setDescription("The MIB module for Enterasys Networks wireless switch chassis component OID registrations. These are generic OIDs: they apply to any switch model, if the respective chassis component is present in the switch. Copyright 2007 Enterasys Networks, Inc. All rights reserved. This SNMP Management Information Base Specification (Specification) embodies confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Enterasys Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
rbtwsChassisComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4))
rbtwsChasCompPowerSupplies = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1))
rbtwsChasCompFans = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2))
rbtwsChasCompPowerSupply1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1, 1))
rbtwsChasCompPowerSupply2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1, 2))
rbtwsChasCompFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 1))
rbtwsChasCompFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 2))
rbtwsChasCompFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 3))
mibBuilder.exportSymbols("RBTWS-REGISTRATION-CHASSIS-MIB", rbtwsChasCompPowerSupplies=rbtwsChasCompPowerSupplies, rbtwsChasCompPowerSupply1=rbtwsChasCompPowerSupply1, rbtwsChasCompFan3=rbtwsChasCompFan3, rbtwsRegistrationChassisMib=rbtwsRegistrationChassisMib, rbtwsChassisComponents=rbtwsChassisComponents, rbtwsChasCompPowerSupply2=rbtwsChasCompPowerSupply2, rbtwsChasCompFan2=rbtwsChasCompFan2, rbtwsChasCompFans=rbtwsChasCompFans, rbtwsChasCompFan1=rbtwsChasCompFan1, PYSNMP_MODULE_ID=rbtwsRegistrationChassisMib)
