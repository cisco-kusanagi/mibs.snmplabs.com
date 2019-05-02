#
# PySNMP MIB module RDN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:54:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, Integer32, Counter32, Unsigned32, Bits, IpAddress, TimeTicks, iso, Counter64, enterprises, NotificationType, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Integer32", "Counter32", "Unsigned32", "Bits", "IpAddress", "TimeTicks", "iso", "Counter64", "enterprises", "NotificationType", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
riverdelta = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981))
riverdelta.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2000-05-23 00:00', '2000-04-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: riverdelta.setRevisionsDescriptions(("Added Copyright Statement into MIB modules's description.", '+ Updated the CONTACT-INFO. + Reorder REVISION/DESCRIPTION in required reverse chronological order.', 'Clean up CONTACT-INFO.', "Moved 'riverdelta' definition into a separate file; this allows an external module to not include the entire riverdelta chassis mib when needing only the 'riverdelta' definition.", 'Initial creation.',))
if mibBuilder.loadTexts: riverdelta.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: riverdelta.setOrganization('Motorola')
if mibBuilder.loadTexts: riverdelta.setContactInfo('Motorola Customer Service 101 Tournament Drive Horsham, PA 19044 US Tel: +1 888 944 4357 Int Tel: +1 215 323 0044 Fax: +1 215 323 1502 Email: CPSSupport@Motorola.com')
if mibBuilder.loadTexts: riverdelta.setDescription('MIB module definition for Motorola. Copyright (C) 2000, 2008 by Motorola, Inc. All rights reserved.')
mibBuilder.exportSymbols("RDN-MIB", PYSNMP_MODULE_ID=riverdelta, riverdelta=riverdelta)
