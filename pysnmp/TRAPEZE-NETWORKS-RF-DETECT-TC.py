#
# PySNMP MIB module TRAPEZE-NETWORKS-RF-DETECT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-RF-DETECT-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, MibIdentifier, Counter64, Integer32, NotificationType, ObjectIdentity, iso, Bits, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "MibIdentifier", "Counter64", "Integer32", "NotificationType", "ObjectIdentity", "iso", "Bits", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzRFDetectTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 11))
trpzRFDetectTc.setRevisions(('2011-07-27 00:11', '2009-08-13 00:10', '2007-04-18 00:02', '2007-03-28 00:01',))
if mibBuilder.loadTexts: trpzRFDetectTc.setLastUpdated('201107270011Z')
if mibBuilder.loadTexts: trpzRFDetectTc.setOrganization('Trapeze Networks')
class TrpzRFDetectClassificationReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("default-classification", 2), ("rogue-list", 3), ("ap-in-modo", 4), ("neighbor-list", 5), ("ssid-masquerade", 6), ("seen-in-network", 7), ("ad-hoc", 8), ("ssid-list", 9), ("pass-fingerprint", 10), ("fail-fingerprint", 11))

class TrpzRFDetectClassification(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("not-classified", 2), ("member", 3), ("neighbor", 4), ("suspect", 5), ("rogue", 6), ("tag", 7))

class TrpzRFDetectNetworkingMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ad-hoc", 1), ("infrastructure", 2))

class TrpzRFDetectDot11ModulationStandard(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("dot11Unknown", 1), ("dot11Other", 2), ("dot11A", 3), ("dot11B", 4), ("dot11G", 5), ("dot11NA", 6), ("dot11NG", 7))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-RF-DETECT-TC", TrpzRFDetectClassification=TrpzRFDetectClassification, TrpzRFDetectClassificationReason=TrpzRFDetectClassificationReason, TrpzRFDetectNetworkingMode=TrpzRFDetectNetworkingMode, TrpzRFDetectDot11ModulationStandard=TrpzRFDetectDot11ModulationStandard, PYSNMP_MODULE_ID=trpzRFDetectTc, trpzRFDetectTc=trpzRFDetectTc)
