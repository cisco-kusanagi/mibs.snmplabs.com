#
# PySNMP MIB module NTWS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-ROOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, ObjectIdentity, Gauge32, Unsigned32, NotificationType, Counter32, Integer32, MibIdentifier, TimeTicks, Bits, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "ObjectIdentity", "Gauge32", "Unsigned32", "NotificationType", "Counter32", "Integer32", "MibIdentifier", "TimeTicks", "Bits", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntwsRootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1))
ntwsRootMib.setRevisions(('2007-08-15 00:04', '2006-03-31 00:03', '2005-04-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsRootMib.setRevisionsDescriptions(('v2.0.1, MRT v3: Removed unnecessary comment. Changed IMPORT of enterprises from RFC1155-SMI to SNMPv2-SMI. Made changes in order to make MIB compile cleanly and comply with corporate MIB conventions.', 'v2.0: Revised for release.', 'v1: Initial version.',))
if mibBuilder.loadTexts: ntwsRootMib.setLastUpdated('200708150004Z')
if mibBuilder.loadTexts: ntwsRootMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsRootMib.setContactInfo('Nortel Networks')
if mibBuilder.loadTexts: ntwsRootMib.setDescription("Nortel Wireless Switch Root MIB Copyright 2005-2007 Nortel Networks, Inc. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. Nortel Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
ntwsProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 1))
ntwsTemporary = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 2))
ntwsRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3))
ntwsMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4))
ntwsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 5))
mibBuilder.exportSymbols("NTWS-ROOT-MIB", PYSNMP_MODULE_ID=ntwsRootMib, ntwsMibs=ntwsMibs, ntwsRootMib=ntwsRootMib, ntwsTraps=ntwsTraps, ntwsTemporary=ntwsTemporary, ntwsRegistration=ntwsRegistration, ntwsProducts=ntwsProducts)
