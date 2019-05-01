#
# PySNMP MIB module CODAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CODAN-SMI
# Produced by pysmi-0.3.4 at Wed May  1 12:25:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, iso, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, enterprises, NotificationType, Gauge32, IpAddress, Counter64, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "iso", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "enterprises", "NotificationType", "Gauge32", "IpAddress", "Counter64", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
codanGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 23304))
codanGroup.setRevisions(('2009-02-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: codanGroup.setRevisionsDescriptions(('1.0 Initial version of this MIB module.',))
if mibBuilder.loadTexts: codanGroup.setLastUpdated('200902110000Z')
if mibBuilder.loadTexts: codanGroup.setOrganization('Codan Limited.')
if mibBuilder.loadTexts: codanGroup.setContactInfo(' Magda Raltcheva Postal: Codan Limited 81 Graves St. Newton 5074 Australia Tel: +61-8-83050311 Fax: +61-8-83050411 Web: www.codan.com.au')
if mibBuilder.loadTexts: codanGroup.setDescription('The Structure of Management Information for the Codan enterprise. Copyright(c) 2009 All rights reserved')
codanMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 1))
satcomMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2))
mibBuilder.exportSymbols("CODAN-SMI", satcomMibs=satcomMibs, codanMibs=codanMibs, PYSNMP_MODULE_ID=codanGroup, codanGroup=codanGroup)
