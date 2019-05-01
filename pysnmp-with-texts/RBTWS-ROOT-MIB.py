#
# PySNMP MIB module RBTWS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-ROOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Gauge32, Unsigned32, MibIdentifier, enterprises, Bits, TimeTicks, Integer32, Counter64, iso, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Gauge32", "Unsigned32", "MibIdentifier", "enterprises", "Bits", "TimeTicks", "Integer32", "Counter64", "iso", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4))
ctronTrapeze = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15))
rbtwsRootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1))
rbtwsRootMib.setRevisions(('2005-05-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbtwsRootMib.setRevisionsDescriptions(('v1: Initial version.',))
if mibBuilder.loadTexts: rbtwsRootMib.setLastUpdated('200505070000Z')
if mibBuilder.loadTexts: rbtwsRootMib.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: rbtwsRootMib.setContactInfo('Enterasys Networks')
if mibBuilder.loadTexts: rbtwsRootMib.setDescription("Enterasys Wireless Switch Root MIB Copyright 1996 - 2005 Enterasys Networks, Inc. All rights reserved. This Enterasys Networks SNMP Management Information Base Specification (Specification) embodies Enterasys Networks' confidential and proprietary intellectual property. Enterasys Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Enterasys Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
rbtwsProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 1))
rbtwsTemporary = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2))
rbtwsRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3))
rbtwsMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4))
rbtwsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5))
mibBuilder.exportSymbols("RBTWS-ROOT-MIB", PYSNMP_MODULE_ID=rbtwsRootMib, rbtwsTemporary=rbtwsTemporary, rbtwsRegistration=rbtwsRegistration, rbtwsTraps=rbtwsTraps, rbtwsRootMib=rbtwsRootMib, rbtwsProducts=rbtwsProducts, mibs=mibs, ctronTrapeze=ctronTrapeze, rbtwsMibs=rbtwsMibs, cabletron=cabletron)
