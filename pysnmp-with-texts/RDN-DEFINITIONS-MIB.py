#
# PySNMP MIB module RDN-DEFINITIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-DEFINITIONS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:54:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
riverdelta, = mibBuilder.importSymbols("RDN-MIB", "riverdelta")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, MibIdentifier, IpAddress, NotificationType, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Integer32, Gauge32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibIdentifier", "IpAddress", "NotificationType", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Integer32", "Gauge32", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnDefinitions = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4))
rdnDefinitions.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2002-12-10 00:00', '2001-04-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rdnDefinitions.setRevisionsDescriptions(("Added Copyright Statement into MIB modules's description.", 'Updated the CONTACT-INFO.', 'remove rdnSensorsSysAvg; replace rdnSensorsFanTop and rdnSensorsFanBottom with rdnSensorsFan', 'Initial creation.',))
if mibBuilder.loadTexts: rdnDefinitions.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnDefinitions.setOrganization('Motorola')
if mibBuilder.loadTexts: rdnDefinitions.setContactInfo('Motorola Customer Service 101 Tournament Drive Horsham, PA 19044 US Tel: +1 888 944 4357 Int Tel: +1 215 323 0044 Fax: +1 215 323 1502 Email: CPSSupport@Motorola.com')
if mibBuilder.loadTexts: rdnDefinitions.setDescription('MIB module for Motorola definitions. Copyright (C) 2001, 2008 by Motorola, Inc. All rights reserved.')
mibBuilder.exportSymbols("RDN-DEFINITIONS-MIB", rdnDefinitions=rdnDefinitions, PYSNMP_MODULE_ID=rdnDefinitions)
