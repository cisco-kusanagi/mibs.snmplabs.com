#
# PySNMP MIB module TRAPEZE-NETWORKS-RF-DETECT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-RF-DETECT-TC
# Produced by pysmi-0.3.4 at Wed May  1 15:27:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, Unsigned32, TimeTicks, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, NotificationType, ObjectIdentity, Integer32, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Unsigned32", "TimeTicks", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "NotificationType", "ObjectIdentity", "Integer32", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzRFDetectTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 11))
trpzRFDetectTc.setRevisions(('2011-07-27 00:11', '2009-08-13 00:10', '2007-04-18 00:02', '2007-03-28 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzRFDetectTc.setRevisionsDescriptions(('v1.2.1: Revised for 7.7 release.', "v1.2.0: Added RF classification value 'tag(7)'. Introduced TrpzRFDetectDot11ModulationStandard (for 7.7 release)", 'v1.1.0: added two new TCs, for use in trpzInfoRFDetectMib', 'v1.0.0: initial version, for 6.2 release',))
if mibBuilder.loadTexts: trpzRFDetectTc.setLastUpdated('201107270011Z')
if mibBuilder.loadTexts: trpzRFDetectTc.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzRFDetectTc.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzRFDetectTc.setDescription("Textual Conventions used by Trapeze Networks wireless switches. Copyright 2007-2011 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzRFDetectClassificationReason(TextualConvention, Integer32):
    description = 'Enumeration of the reasons why a RF device is classified the way it is.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("default-classification", 2), ("rogue-list", 3), ("ap-in-modo", 4), ("neighbor-list", 5), ("ssid-masquerade", 6), ("seen-in-network", 7), ("ad-hoc", 8), ("ssid-list", 9), ("pass-fingerprint", 10), ("fail-fingerprint", 11))

class TrpzRFDetectClassification(TextualConvention, Integer32):
    description = 'The classification of an RF device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("not-classified", 2), ("member", 3), ("neighbor", 4), ("suspect", 5), ("rogue", 6), ("tag", 7))

class TrpzRFDetectNetworkingMode(TextualConvention, Integer32):
    description = 'The way an RF device is doing wireless networking.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ad-hoc", 1), ("infrastructure", 2))

class TrpzRFDetectDot11ModulationStandard(TextualConvention, Integer32):
    description = 'Enumeration to indicate the 802.11 Modulation Standard.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("dot11Unknown", 1), ("dot11Other", 2), ("dot11A", 3), ("dot11B", 4), ("dot11G", 5), ("dot11NA", 6), ("dot11NG", 7))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-RF-DETECT-TC", TrpzRFDetectClassification=TrpzRFDetectClassification, TrpzRFDetectNetworkingMode=TrpzRFDetectNetworkingMode, TrpzRFDetectDot11ModulationStandard=TrpzRFDetectDot11ModulationStandard, TrpzRFDetectClassificationReason=TrpzRFDetectClassificationReason, PYSNMP_MODULE_ID=trpzRFDetectTc, trpzRFDetectTc=trpzRFDetectTc)
