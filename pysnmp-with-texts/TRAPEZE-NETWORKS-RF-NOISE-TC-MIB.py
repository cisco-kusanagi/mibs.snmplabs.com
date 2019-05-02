#
# PySNMP MIB module TRAPEZE-NETWORKS-RF-NOISE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-RF-NOISE-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, iso, Gauge32, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Bits, ObjectIdentity, IpAddress, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "iso", "Gauge32", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Bits", "ObjectIdentity", "IpAddress", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzRFNoiseTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 22))
trpzRFNoiseTc.setRevisions(('2011-01-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzRFNoiseTc.setRevisionsDescriptions(('v1.0.0: initial version, for 7.5 release',))
if mibBuilder.loadTexts: trpzRFNoiseTc.setLastUpdated('201101100000Z')
if mibBuilder.loadTexts: trpzRFNoiseTc.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzRFNoiseTc.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzRFNoiseTc.setDescription("Textual Conventions used by Trapeze Networks wireless switches. Copyright 2011 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzRFNoiseSourceID(TextualConvention, OctetString):
    description = 'RF Noise Source ID.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class TrpzRFNoiseSourceType(TextualConvention, Integer32):
    description = 'RF Noise Source Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 16, 33, 49, 50, 64, 65, 66))
    namedValues = NamedValues(("nsUnknown", 0), ("nsContinuousWave", 1), ("nsVideo", 16), ("nsMicrowaveOven", 33), ("nsPhoneDECT", 49), ("nsPhoneFHSS", 50), ("nsBluetoothAny", 64), ("nsBluetoothHeadset", 65), ("nsBluetoothHandsfree", 66))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-RF-NOISE-TC-MIB", trpzRFNoiseTc=trpzRFNoiseTc, TrpzRFNoiseSourceType=TrpzRFNoiseSourceType, PYSNMP_MODULE_ID=trpzRFNoiseTc, TrpzRFNoiseSourceID=TrpzRFNoiseSourceID)
