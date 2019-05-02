#
# PySNMP MIB module RBTWS-RF-DETECT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-RF-DETECT-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:53:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter64, MibIdentifier, Unsigned32, Bits, ModuleIdentity, iso, IpAddress, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "MibIdentifier", "Unsigned32", "Bits", "ModuleIdentity", "iso", "IpAddress", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsRFDetectTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 11))
rbtwsRFDetectTc.setRevisions(('2007-04-18 00:02', '2007-03-28 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbtwsRFDetectTc.setRevisionsDescriptions(('v1.1.0: added two new TCs, for use in rbtwsInfoRFDetectMib', 'v1.0.0: initial version, for 6.2 release',))
if mibBuilder.loadTexts: rbtwsRFDetectTc.setLastUpdated('200704191855Z')
if mibBuilder.loadTexts: rbtwsRFDetectTc.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: rbtwsRFDetectTc.setContactInfo('www.enterasys.com')
if mibBuilder.loadTexts: rbtwsRFDetectTc.setDescription("Textual Conventions used by Enterasys Networks wireless switches. Copyright 2007 Enterasys Networks, Inc. All rights reserved. This SNMP Management Information Base Specification (Specification) embodies confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Enterasys Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class RbtwsRFDetectClassificationReason(TextualConvention, Integer32):
    description = 'Enumeration of the reasons why a RF device is classified the way it is.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("default-classification", 2), ("rogue-list", 3), ("ap-in-modo", 4), ("neighbor-list", 5), ("ssid-masquerade", 6), ("seen-in-network", 7), ("ad-hoc", 8), ("ssid-list", 9), ("pass-fingerprint", 10), ("fail-fingerprint", 11))

class RbtwsRFDetectClassification(TextualConvention, Integer32):
    description = 'The classification of an RF device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("not-classified", 2), ("member", 3), ("neighbor", 4), ("suspect", 5), ("rogue", 6))

class RbtwsRFDetectNetworkingMode(TextualConvention, Integer32):
    description = 'The way an RF device is doing wireless networking.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ad-hoc", 1), ("infrastructure", 2))

mibBuilder.exportSymbols("RBTWS-RF-DETECT-TC", RbtwsRFDetectNetworkingMode=RbtwsRFDetectNetworkingMode, RbtwsRFDetectClassification=RbtwsRFDetectClassification, rbtwsRFDetectTc=rbtwsRFDetectTc, PYSNMP_MODULE_ID=rbtwsRFDetectTc, RbtwsRFDetectClassificationReason=RbtwsRFDetectClassificationReason)
