#
# PySNMP MIB module LANOPTICS-BRIDGE-OPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANOPTICS-BRIDGE-OPTION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:55:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, NotificationType, Gauge32, ModuleIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter64, iso, Counter32, IpAddress, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "Gauge32", "ModuleIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter64", "iso", "Counter32", "IpAddress", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lanOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 224))
lanOpticsBridgeProxyAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 6))
lanOpticsLMGRAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 6, 8))
lanOpticsLMGRLinkID = MibScalar((1, 3, 6, 1, 4, 1, 224, 6, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanOpticsLMGRLinkID.setStatus('mandatory')
lanOpticsLMGRCaptCntrlLink = MibScalar((1, 3, 6, 1, 4, 1, 224, 6, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanOpticsLMGRCaptCntrlLink.setStatus('mandatory')
mibBuilder.exportSymbols("LANOPTICS-BRIDGE-OPTION-MIB", lanOpticsLMGRAgent=lanOpticsLMGRAgent, lanOptics=lanOptics, lanOpticsBridgeProxyAgent=lanOpticsBridgeProxyAgent, lanOpticsLMGRCaptCntrlLink=lanOpticsLMGRCaptCntrlLink, lanOpticsLMGRLinkID=lanOpticsLMGRLinkID)
