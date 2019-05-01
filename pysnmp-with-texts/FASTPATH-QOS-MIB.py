#
# PySNMP MIB module FASTPATH-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:12:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
fastPath, = mibBuilder.importSymbols("BROADCOM-REF-MIB", "fastPath")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, Gauge32, IpAddress, NotificationType, MibIdentifier, Counter32, ModuleIdentity, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Gauge32", "IpAddress", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
fastPathQOS = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3))
fastPathQOS.setRevisions(('2007-05-23 00:00', '2003-11-21 00:00', '2002-01-30 15:44',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathQOS.setRevisionsDescriptions(('Broadcom branding related changes.', 'Revisions made for new release.', 'Initial revision.',))
if mibBuilder.loadTexts: fastPathQOS.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: fastPathQOS.setOrganization('Broadcom Corporation')
if mibBuilder.loadTexts: fastPathQOS.setContactInfo(' Customer Support Postal: Broadcom Corporation 100, Perimeter Park Drive Morrisville, NC 27560 Tel: +1 919 865 2700')
if mibBuilder.loadTexts: fastPathQOS.setDescription('The MIB definitaions for Quality of Service Flex package.')
mibBuilder.exportSymbols("FASTPATH-QOS-MIB", PYSNMP_MODULE_ID=fastPathQOS, fastPathQOS=fastPathQOS)
