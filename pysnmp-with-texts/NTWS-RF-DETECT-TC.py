#
# PySNMP MIB module NTWS-RF-DETECT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-RF-DETECT-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:25:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, IpAddress, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, Integer32, Counter64, iso, Bits, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "IpAddress", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "Integer32", "Counter64", "iso", "Bits", "MibIdentifier", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntwsRFDetectTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 11))
ntwsRFDetectTc.setRevisions(('2008-05-15 00:03', '2007-04-18 00:02', '2007-03-28 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsRFDetectTc.setRevisionsDescriptions(('v1.1.1, MRT v1.1: Made changes in order to comply with corporate MIB conventions.', 'v1.1.0: added two new TCs, for use in ntwsInfoRFDetectMib', 'v1.0.0: initial version',))
if mibBuilder.loadTexts: ntwsRFDetectTc.setLastUpdated('200805150003Z')
if mibBuilder.loadTexts: ntwsRFDetectTc.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsRFDetectTc.setContactInfo('www.nortelnetworks.com')
if mibBuilder.loadTexts: ntwsRFDetectTc.setDescription("Textual Conventions used by Nortel Networks wireless switches. Copyright 2008 Nortel Networks. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class NtwsRFDetectClassificationReason(TextualConvention, Integer32):
    description = 'Enumeration of the reasons why a RF device is classified the way it is.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("default-classification", 2), ("rogue-list", 3), ("ap-in-modo", 4), ("neighbor-list", 5), ("ssid-masquerade", 6), ("seen-in-network", 7), ("ad-hoc", 8), ("ssid-list", 9), ("pass-fingerprint", 10), ("fail-fingerprint", 11))

class NtwsRFDetectClassification(TextualConvention, Integer32):
    description = 'The classification of an RF device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("not-classified", 2), ("member", 3), ("neighbor", 4), ("suspect", 5), ("rogue", 6))

class NtwsRFDetectNetworkingMode(TextualConvention, Integer32):
    description = 'The way an RF device is doing wireless networking.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ad-hoc", 1), ("infrastructure", 2))

mibBuilder.exportSymbols("NTWS-RF-DETECT-TC", ntwsRFDetectTc=ntwsRFDetectTc, NtwsRFDetectClassificationReason=NtwsRFDetectClassificationReason, NtwsRFDetectClassification=NtwsRFDetectClassification, NtwsRFDetectNetworkingMode=NtwsRFDetectNetworkingMode, PYSNMP_MODULE_ID=ntwsRFDetectTc)
