#
# PySNMP MIB module TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter64, TimeTicks, Counter32, ModuleIdentity, MibIdentifier, iso, Gauge32, Bits, Integer32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter64", "TimeTicks", "Counter32", "ModuleIdentity", "MibIdentifier", "iso", "Gauge32", "Bits", "Integer32", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzRegistration, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzRegistration")
trpzRegistrationChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 3, 5))
trpzRegistrationChassisMib.setRevisions(('2007-08-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzRegistrationChassisMib.setRevisionsDescriptions(('v1.0: initial version, published in 6.2 release',))
if mibBuilder.loadTexts: trpzRegistrationChassisMib.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: trpzRegistrationChassisMib.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzRegistrationChassisMib.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzRegistrationChassisMib.setDescription("The MIB module for Trapeze Networks wireless switch chassis component OID registrations. These are generic OIDs: they apply to any switch model, if the respective chassis component is present in the switch. Copyright 2007 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
trpzChassisComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4))
trpzChasCompPowerSupplies = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 1))
trpzChasCompFans = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2))
trpzChasCompPowerSupply1 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 1, 1))
trpzChasCompPowerSupply2 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 1, 2))
trpzChasCompFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 1))
trpzChasCompFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 2))
trpzChasCompFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 3))
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB", trpzChasCompPowerSupplies=trpzChasCompPowerSupplies, trpzChasCompPowerSupply1=trpzChasCompPowerSupply1, trpzChasCompPowerSupply2=trpzChasCompPowerSupply2, trpzChasCompFans=trpzChasCompFans, trpzChasCompFan1=trpzChasCompFan1, trpzChasCompFan3=trpzChasCompFan3, PYSNMP_MODULE_ID=trpzRegistrationChassisMib, trpzChassisComponents=trpzChassisComponents, trpzChasCompFan2=trpzChasCompFan2, trpzRegistrationChassisMib=trpzRegistrationChassisMib)
